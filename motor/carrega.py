import pathlib

import yaml

CONTENT = pathlib.Path(__file__).resolve().parent.parent / "content"


def _llig(nom):
    with open(CONTENT / nom, encoding="utf-8") as f:
        return yaml.safe_load(f)


def mon_nou():
    """Carrega el contingut i li penja l'estat viu."""
    mon = {
        "fets": _llig("fets.yaml"),
        "npcs": _llig("npcs.yaml"),
        "intencions": _llig("intencions.yaml"),
        "regles": _llig("regles.yaml"),
        "obtinguts": {},   # fet_id -> {de, via}
        "torns": 0,
    }
    for npc in mon["npcs"].values():
        npc["desgast"] = {}                    # fet_id -> usos contra ELL (§3.3)
        npc["màxims"] = dict(npc["estat"])     # fins on l'has portat mai
        npc["tancat"] = False
    return mon
