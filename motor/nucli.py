"""(intenció, palanca) -> estat nou.

Ací dins no entra ni ix ni una línia de diàleg. Si algun dia este fitxer
necessita mirar una cadena de text, alguna cosa s'ha dissenyat malament.
"""

EIXOS = ("intimidació", "confiança", "temptació")


def eix_del_fet(mon, npc_id, fet_id):
    """Quin eix obri este fet en este NPC. Ho decidix la postura (§2.3)."""
    postura = mon["npcs"][npc_id]["sap"][fet_id]
    return mon["regles"]["postura_eix"][postura]


def llindar(mon, npc_id, fet_id):
    postura = mon["npcs"][npc_id]["sap"][fet_id]
    mult = mon["regles"]["dificultat_postura"][postura]
    return round(mon["fets"][fet_id]["dificultat"] * mult)


def pes(mon, npc_id, fet_id):
    """Quant val esta carta contra este NPC ara mateix."""
    npc = mon["npcs"][npc_id]
    r = mon["regles"]
    base = r["pes_vulnerable"] if fet_id in npc["vulnerable_a"] else r["pes_normal"]
    escala = r["degradació"]
    return base * escala[min(npc["desgast"].get(fet_id, 0), len(escala) - 1)]


def palanques(mon, npc_id):
    """Les cartes que tens, amb el que valen contra este NPC."""
    npc = mon["npcs"][npc_id]
    return [(f, pes(mon, npc_id, f), npc["desgast"].get(f, 0)) for f in mon["obtinguts"]]


def previsió(mon, npc_id, intencio_id, palanca_id):
    """Els deltes que faria esta jugada, sense aplicar-los."""
    p = pes(mon, npc_id, palanca_id) if palanca_id else 0.0
    return {e: round(v * p) for e, v in mon["intencions"][intencio_id]["deltes"].items()}


def pendents(mon, npc_id):
    """Què li falta per soltar el que amaga. NOMÉS per a calibrar.

    El jugador no ha de veure això: se n'ha d'assabentar pel que li conteste.
    """
    npc = mon["npcs"][npc_id]
    fora = []
    for fet_id in npc["sap"]:
        if fet_id in mon["obtinguts"]:
            continue
        eix = eix_del_fet(mon, npc_id, fet_id)
        fora.append((fet_id, eix, npc["estat"][eix], llindar(mon, npc_id, fet_id)))
    return sorted(fora, key=lambda t: t[3])


def _obri(mon, npc_id):
    """Fets d'este NPC que ara compleixen el llindar."""
    npc = mon["npcs"][npc_id]
    nous = []
    for fet_id in npc["sap"]:
        if fet_id in mon["obtinguts"]:
            continue
        eix = eix_del_fet(mon, npc_id, fet_id)
        if npc["estat"][eix] >= llindar(mon, npc_id, fet_id):
            mon["obtinguts"][fet_id] = {"de": npc_id, "via": eix}
            nous.append(fet_id)
    return nous


def _refreda(mon):
    """Passa un torn per a tothom. La por es passa; la confiança no.

    No és el món movent-se sol: la causa és que has deixat de pressionar.
    I no torna a zero, perquè recorda qui eres.
    """
    r = mon["regles"]
    for npc in mon["npcs"].values():
        for eix, quant in r["refredament"].items():
            if quant <= 0:
                continue
            terra = round(npc["màxims"][eix] * r["terra_refredament"])
            npc["estat"][eix] = max(terra, npc["estat"][eix] - quant)


def aplica(mon, npc_id, intencio_id, palanca_id):
    """L'única porta d'entrada del motor. Muta `mon` i torna què ha passat."""
    npc = mon["npcs"][npc_id]
    if npc["tancat"]:
        return {"deltes": {}, "oberts": [], "ruptura": False, "tancat": True}

    deltes = previsió(mon, npc_id, intencio_id, palanca_id)
    for eix, v in deltes.items():
        npc["estat"][eix] = max(0, min(100, npc["estat"][eix] + v))
        npc["màxims"][eix] = max(npc["màxims"][eix], npc["estat"][eix])

    if palanca_id:
        npc["desgast"][palanca_id] = npc["desgast"].get(palanca_id, 0) + 1
    mon["torns"] += 1

    if npc["estat"]["intimidació"] >= npc["ruptura"]:
        npc["tancat"] = True
        return {"deltes": deltes, "oberts": [], "ruptura": True, "tancat": False}

    oberts = _obri(mon, npc_id)
    _refreda(mon)
    return {"deltes": deltes, "oberts": oberts, "ruptura": False, "tancat": False}
