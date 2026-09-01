"""L'invariant central, convertit en una cosa que falla sola.

> El motor només opera sobre el parell (intenció, palanca). Mai toca text.

Si esta prova falla no és un detall d'estil: és que el motor ha començat a saber
què és una lletra, i llavors la capa de sortida ja no es pot tirar i tornar a
escriure. Que és tot el que compra la separació.
"""

import pathlib
import unittest

ARREL = pathlib.Path(__file__).resolve().parent.parent
MOTOR = sorted((ARREL / "motor").glob("*.py"))
SORTIDA = sorted((ARREL / "sortida").glob("*.py"))


class ProvaInvariant(unittest.TestCase):
    # El missatge nostre substituix el d'unittest, que bolcaria el fitxer sencer.
    longMessage = False

    def test_hi_ha_fitxers_a_mirar(self):
        """Si un dia es reanomena una carpeta, que no passe la prova en buit."""
        self.assertTrue(MOTOR, "no s'ha trobat cap .py a motor/")
        self.assertTrue(SORTIDA, "no s'ha trobat cap .py a sortida/")

    def test_el_motor_no_coneix_la_sortida(self):
        for f in MOTOR:
            codi = f.read_text(encoding="utf-8")
            for prohibit in ("import sortida", "from sortida", "import cli", "from cli"):
                self.assertNotIn(prohibit, codi, f"motor/{f.name}: «{prohibit}»")

    def test_el_motor_no_parla_ni_escolta(self):
        for f in MOTOR:
            codi = f.read_text(encoding="utf-8")
            self.assertNotIn("print(", codi, f"motor/{f.name} escriu per pantalla")
            self.assertNotIn("input(", codi, f"motor/{f.name} llig del teclat")

    def test_la_sortida_no_calcula(self):
        """L'altra direcció: `sortida` rep l'estat ja resolt, no se'l fa."""
        for f in SORTIDA:
            codi = f.read_text(encoding="utf-8")
            for prohibit in ("import motor", "from motor"):
                self.assertNotIn(prohibit, codi, f"sortida/{f.name}: «{prohibit}»")


if __name__ == "__main__":
    unittest.main()
