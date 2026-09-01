"""La pàgina jugable no pot desquadrar-se del contingut.

Si algú toca `content/` o `pagina/plantilla.html` i no torna a generar la pàgina,
esta prova falla. És l'única cosa que sosté la promesa de «no poden desquadrar-se»:
sense ella, la pàgina és una còpia que envellix a soles.

    python pagina/construix.py

per a arreglar-ho.
"""

import json
import pathlib
import re
import unittest

ARREL = pathlib.Path(__file__).resolve().parent.parent

from pagina import construix  # noqa: E402


class ProvaPagina(unittest.TestCase):
    longMessage = False

    def test_la_pagina_esta_al_dia(self):
        generada = construix.construix()
        al_disc = construix.EIXIDA.read_text(encoding="utf-8")
        self.assertEqual(
            generada,
            al_disc,
            "pagina/tot-se-sap.html no correspon al contingut actual — "
            "passa `python pagina/construix.py`",
        )

    def test_les_dades_incrustades_son_les_del_contingut(self):
        """Que el que hi ha dins de la pàgina siga el YAML, no una còpia a mà."""
        dins = json.loads(construix.dades())
        del_disc = re.search(r"const DADES = (\{.*?\});\n", construix.EIXIDA.read_text(encoding="utf-8"), re.S)
        self.assertIsNotNone(del_disc, "no trobe el bloc de dades dins de la pàgina generada")
        self.assertEqual(json.loads(del_disc.group(1)), dins, "les dades de la pàgina no són les del contingut")

    def test_la_pagina_no_demana_res_de_fora(self):
        """Ha de ser autònoma: un fitxer que òbris i ja. Excepció: les lletres."""
        html = construix.EIXIDA.read_text(encoding="utf-8")
        for url in re.findall(r'(?:src|href)="(https?://[^"]+)"', html):
            self.assertTrue(
                url.startswith(("https://fonts.googleapis.com", "https://fonts.gstatic.com")),
                f"la pàgina depén de {url}",
            )


if __name__ == "__main__":
    unittest.main()
