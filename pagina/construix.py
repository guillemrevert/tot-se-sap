#!/usr/bin/env python3
"""Genera `pagina/tot-se-sap.html` incrustant el contingut dins de la plantilla.

    python pagina/construix.py

La pàgina és un **port** del joc a JavaScript, no una segona font de veritat: el
contingut ix sempre de `content/`, o siga que els números de la pàgina i els del
joc de Python no poden desquadrar-se. La lògica sí que està escrita dos vegades
(veure `plantilla.html`), i això és el preu conegut.

`proves/prova_pagina.py` falla si el fitxer generat no està al dia.
"""

import json
import pathlib
import sys

ARREL = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ARREL))

from motor import carrega  # noqa: E402

MARCADOR = "/*__DADES__*/null"
PLANTILLA = ARREL / "pagina" / "plantilla.html"
EIXIDA = ARREL / "pagina" / "tot-se-sap.html"

# Estat viu que penja `carrega`: la pàgina se'l fa ella, ací sobra.
VIU = ("desgast", "màxims", "tancat")


def dades():
    """El contingut dels YAML, sense l'estat de partida."""
    mon = carrega.mon_nou()
    fora = {clau: mon[clau] for clau in ("fets", "npcs", "intencions", "regles")}
    for npc in fora["npcs"].values():
        for camp in VIU:
            npc.pop(camp, None)
    return json.dumps(fora, ensure_ascii=False, separators=(",", ":"))


def construix():
    plantilla = PLANTILLA.read_text(encoding="utf-8")
    if MARCADOR not in plantilla:
        raise SystemExit(f"{PLANTILLA.name} no té el marcador {MARCADOR}")
    return plantilla.replace(MARCADOR, dades(), 1)


if __name__ == "__main__":
    pagina = construix()
    EIXIDA.write_text(pagina, encoding="utf-8", newline="\n")
    print(f"{EIXIDA.relative_to(ARREL)} · {len(pagina):,} bytes")
