"""Integritat referencial del contingut.

No prova el motor —el seu contracte encara pot canviar (D1, D2)— sinó que el que
està escrit als YAML es referix a coses que existixen.

És el precursor del validador de resolubilitat (§15): açò diu si el contingut és
*coherent*, i el validador dirà si a més és *jugable*.
"""

import unittest

from motor import carrega, nucli

FORMES = ("nu", "subordinada", "nominal")
TONS = ("sec", "obert", "interessat", "pressionat")   # els que torna sortida.text.to()


class ProvaContingut(unittest.TestCase):
    # El missatge nostre substituix el d'unittest, que bolcaria el fitxer sencer.
    longMessage = False

    @classmethod
    def setUpClass(cls):
        cls.mon = carrega.mon_nou()

    # --- fets ---

    def test_els_fets_estan_sencers(self):
        for fet_id, fet in self.mon["fets"].items():
            for forma in FORMES:
                text = fet.get(forma)
                self.assertIsInstance(text, str, f"{fet_id}: falta la forma «{forma}»")
                self.assertTrue(text.strip(), f"{fet_id}: la forma «{forma}» està buida")
            self.assertIsInstance(
                fet.get("dificultat"), int, f"{fet_id}: la dificultat no és un número"
            )

    def test_cada_fet_el_sap_algu(self):
        """Un fet que no sap ningú és contingut mort: no es pot traure mai."""
        sabuts = {f for npc in self.mon["npcs"].values() for f in npc["sap"]}
        orfes = sorted(set(self.mon["fets"]) - sabuts)
        self.assertFalse(orfes, f"fets que no sap ningú: {orfes}")

    # --- NPCs ---

    def test_el_que_saben_els_npcs_existix(self):
        regles = self.mon["regles"]
        for npc_id, npc in self.mon["npcs"].items():
            for fet_id, postura in npc["sap"].items():
                self.assertIn(fet_id, self.mon["fets"], f"{npc_id} sap «{fet_id}», que no existix")
                self.assertIn(
                    postura, regles["postura_eix"], f"{npc_id}/{fet_id}: postura «{postura}» desconeguda"
                )
                self.assertIn(
                    postura,
                    regles["dificultat_postura"],
                    f"{npc_id}/{fet_id}: la postura «{postura}» no té multiplicador",
                )

    def test_les_vulnerabilitats_existixen(self):
        for npc_id, npc in self.mon["npcs"].items():
            for fet_id in npc["vulnerable_a"]:
                self.assertIn(
                    fet_id, self.mon["fets"], f"{npc_id} és vulnerable a «{fet_id}», que no existix"
                )

    def test_els_npcs_estan_sencers(self):
        for npc_id, npc in self.mon["npcs"].items():
            for eix in nucli.EIXOS:
                self.assertIn(eix, npc["estat"], f"{npc_id}: li falta l'eix «{eix}»")
            self.assertIsInstance(npc.get("ruptura"), int, f"{npc_id}: ruptura no és un número")
            for to in TONS:
                self.assertTrue(npc["respostes"].get(to), f"{npc_id}: no té respostes de «{to}»")
            self.assertTrue(npc["respostes"].get("ruptura"), f"{npc_id}: no té línia de ruptura")

    # --- intencions ---

    def test_les_intencions_encaixen_amb_els_fets(self):
        for nom, intencio in self.mon["intencions"].items():
            forma = intencio["forma"]
            self.assertIn(forma, FORMES, f"{nom} demana la forma «{forma}», que no existix")
            self.assertIn(
                "{" + forma + "}",
                intencio["plantilla"],
                f"{nom} declara la forma «{forma}» però la plantilla no la gasta",
            )
            for eix in intencio["deltes"]:
                self.assertIn(eix, nucli.EIXOS, f"{nom} mou «{eix}», que no és un eix")

    def test_hi_ha_frase_per_a_l_arrancada_en_fred(self):
        """Amb zero palanques, l'única jugada possible és PREGUNTAR sense res."""
        self.assertIn("PREGUNTAR", self.mon["intencions"])
        self.assertTrue(
            self.mon["intencions"]["PREGUNTAR"].get("obertura"),
            "PREGUNTAR no té «obertura»: el primer torn de la partida es queda en «...»",
        )

    # --- regles ---

    def test_les_postures_obrin_eixos_de_veres(self):
        for postura, eix in self.mon["regles"]["postura_eix"].items():
            self.assertIn(eix, nucli.EIXOS, f"la postura {postura} obri «{eix}», que no és un eix")

    def test_el_refredament_es_sobre_eixos(self):
        for eix in self.mon["regles"]["refredament"]:
            self.assertIn(eix, nucli.EIXOS, f"es refreda «{eix}», que no és un eix")

    def test_la_degradacio_mai_crema_del_tot(self):
        """Regla 3: que el jugador perda l'efecte sorpresa, no la partida."""
        escala = self.mon["regles"]["degradació"]
        self.assertTrue(escala, "l'escala de degradació està buida")
        self.assertGreater(
            escala[-1], 0, "l'últim escaló de degradació és 0: una carta gastada deixa de servir"
        )


if __name__ == "__main__":
    unittest.main()
