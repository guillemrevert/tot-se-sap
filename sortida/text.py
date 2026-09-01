"""Capa de sortida: rep l'estat que ha deixat el motor i el torna text.

El motor no sap que este fitxer existix.
"""

import re

_cua = {}   # (npc_id, to) -> índex, per no repetir la mateixa línia seguida

# Apedaç de concordança (§4). Ha de viure ací: el motor no toca text.
_CONTRACCIONS = {"de el": "del", "de els": "dels", "a el": "al",
                 "a els": "als", "per el": "pel", "per els": "pels"}


def concorda(s):
    for k, v in _CONTRACCIONS.items():
        s = re.sub(rf"\b{k}\b", v, s)
    return re.sub(r"\bde ([aeiouàèéíòóú])", r"d'\1", s)


def frase_jugador(mon, intencio_id, palanca_id):
    intencio = mon["intencions"][intencio_id]
    if palanca_id is None:
        return intencio.get("obertura", "...")
    forma = intencio["forma"]
    plena = intencio["plantilla"].format(**{forma: mon["fets"][palanca_id][forma]})
    return concorda(plena)


def direcció(deltes):
    """Què mou esta jugada. Direcció, mai magnitud: el jugador no fa comptes."""
    if not deltes:
        return "no li fa res"
    return " · ".join(("puja " if v > 0 else "fon ") + eix for eix, v in deltes.items())


def to(npc):
    """Quin registre li toca. Encara no és el filtre d'estil de §4 (v1)."""
    e = npc["estat"]
    if e["intimidació"] >= 60:
        return "pressionat"
    if e["temptació"] >= 50:
        return "interessat"
    if e["confiança"] >= 50:
        return "obert"
    return "sec"


def resposta(mon, npc_id, res):
    npc = mon["npcs"][npc_id]
    if res["ruptura"]:
        return npc["respostes"]["ruptura"]
    clau = (npc_id, to(npc))
    línies = npc["respostes"][clau[1]]
    i = _cua.get(clau, 0)
    _cua[clau] = (i + 1) % len(línies)
    return línies[i]
