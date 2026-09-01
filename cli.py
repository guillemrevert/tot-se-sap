#!/usr/bin/env python3
"""Tot se sap — v0. Una conversa, sempre dins.

  python cli.py

Tecles: [n] canviar d'interlocutor · [f] el que ja saps · [c] calibratge · [q] eixir
"""

import sys

from motor import carrega, nucli
from sortida import text

sys.stdout.reconfigure(encoding="utf-8")

AMPLE = 66
OBJECTIU = "f_autoria"


def barra(v):
    plens = round(v / 10)
    return "█" * plens + "░" * (10 - plens)


def marca(usos):
    """Quant li queda a la carta. Mai baixa de ●○○: degradació, no crema."""
    n = 3 - min(usos, 2)
    return "●" * n + "○" * (3 - n)


def capçalera(mon, npc_id, calibratge):
    npc = mon["npcs"][npc_id]
    print("\n" + "─" * AMPLE)
    print(f"  {npc['nom'].upper()} · {npc['ofici']}")
    print(f"  {npc['presentació']}")
    print()
    for eix in nucli.EIXOS:
        v = npc["estat"][eix]
        print(f"  {eix:<12} {barra(v)}" + (f"  {v:>3}" if calibratge else ""))
    if calibratge:
        print()
        for fet_id, eix, ara, cal in nucli.pendents(mon, npc_id):
            print(f"    · {fet_id:<20} {eix} {ara}/{cal}")
        print(f"    torn {mon['torns']}")
    if npc["tancat"]:
        print("\n  [tancat. Ja no et parlarà.]")
    print("─" * AMPLE)


def tria(pregunta, opcions, extres=""):
    """Torna un índex, o una lletra d'`extres`, o None si no val."""
    resp = input(f"\n  {pregunta} > ").strip().lower()
    if resp in extres:
        return resp
    if resp.isdigit() and 0 <= int(resp) < len(opcions):
        return int(resp)
    return None


def menu_palanca(mon, npc_id, calibratge):
    ps = nucli.palanques(mon, npc_id)
    print("\n  De què li parles?\n")
    for i, (fet_id, p, usos) in enumerate(ps, 1):
        cua = f"   ×{p:.2f}" if calibratge else ""
        print(f"   [{i}] {mon['fets'][fet_id]['nu']}")
        print(f"       {marca(usos)}{cua}")
    print("   [0] de res concret")
    print("\n   [n] canviar  [f] el que saps  [c] calibratge  [q] eixir")
    t = tria("de què", [None] + ps, "nfcq")
    if isinstance(t, str):
        return t
    if t is None:
        return None
    return None if t == 0 else ps[t - 1][0]


def menu_intenció(mon, npc_id, palanca_id, calibratge):
    if palanca_id is None:
        return "PREGUNTAR"
    noms = list(mon["intencions"])
    print("\n  Com li ho dius?\n")
    for i, nom in enumerate(noms, 1):
        d = nucli.previsió(mon, npc_id, nom, palanca_id)
        cua = f"   {d}" if calibratge else ""
        print(f"   [{i}] {nom:<12} {text.direcció(mon['intencions'][nom]['deltes'])}{cua}")
    print("   [0] tornar")
    t = tria("com", [None] + noms)
    if t is None or t == 0:
        return None
    return noms[t - 1]


def mostra_fets(mon):
    print("\n  El que saps:\n")
    if not mon["obtinguts"]:
        print("   (res)")
    for fet_id, com in mon["obtinguts"].items():
        print(f"   · {mon['fets'][fet_id]['nu']}")
        print(f"     de {mon['npcs'][com['de']]['nom']}, per {com['via']}")


def canvia(mon, actual):
    ids = list(mon["npcs"])
    print("\n  Amb qui parles?\n")
    for i, npc_id in enumerate(ids, 1):
        npc = mon["npcs"][npc_id]
        estat = " (tancat)" if npc["tancat"] else ""
        print(f"   [{i}] {npc['nom']}, {npc['ofici']} — {npc['lloc']}{estat}")
    t = tria("amb qui", [None] + ids)
    return actual if t is None or t == 0 else ids[t - 1]


def main():
    mon = carrega.mon_nou()
    actual = list(mon["npcs"])[0]
    calibratge = False

    print("\n  TOT SE SAP — v0")
    print("  Han robat la caixa de la cooperativa. Tu no portes placa.")
    print("  L'única cosa que tens és el que et diguen.")

    while True:
        capçalera(mon, actual, calibratge)

        if mon["npcs"][actual]["tancat"]:
            actual = canvia(mon, actual)
            continue

        p = menu_palanca(mon, actual, calibratge)
        if p == "q":
            break
        if p == "n":
            actual = canvia(mon, actual)
            continue
        if p == "f":
            mostra_fets(mon)
            continue
        if p == "c":
            calibratge = not calibratge
            continue

        intenció = menu_intenció(mon, actual, p, calibratge)
        if intenció is None:
            continue

        res = nucli.aplica(mon, actual, intenció, p)

        print(f"\n  TU  — «{text.frase_jugador(mon, intenció, p)}»")
        print(f"\n  {mon['npcs'][actual]['nom'].upper()} — «{text.resposta(mon, actual, res)}»")
        for fet_id in res["oberts"]:
            print(f"       ▸ {mon['fets'][fet_id]['nu']}")
            print(f"         [tret per {mon['obtinguts'][fet_id]['via']}]")

        if OBJECTIU in mon["obtinguts"]:
            print(f"\n  Ho tens. {mon['torns']} torns.")
            break
        if all(n["tancat"] for n in mon["npcs"].values()):
            print("\n  Els has cremat tots. No queda ningú amb qui parlar.")
            break

    print()


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\n")
