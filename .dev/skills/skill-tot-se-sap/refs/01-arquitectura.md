# 01 — Arquitectura

Estat: **v0 jugable**. ~360 línies de Python, 4 YAML, zero dependències excepte `pyyaml`.

---

## Mòduls

```
content/*.yaml   dades. Fets, NPCs, intencions, números. Zero codi.
motor/carrega.py llig els YAML i els penja l'estat viu de la partida
motor/nucli.py   (intenció, palanca) -> estat nou.  ← el cor. Zero text.
sortida/text.py  estat -> cadenes. L'única capa que sap què és una lletra.
cli.py           bucle de terminal, menús, pintat. Provisional per definició.
pagina/          PORT a JavaScript: una pàgina jugable, autònoma. Veure més avall.
```

Dependència en una direcció i prou:

```
content ──► carrega ──► nucli ──► (resultat) ──► text ──► cli
                          ▲                                 │
                          └──────── cli crida aplica() ──────┘
```

`nucli.py` no importa `sortida`. `sortida` no importa `nucli`: rep el `mon` i el `res`
que li passa `cli`. Si algun dia `nucli` importa `sortida`, l'invariant s'ha trencat.

---

## `pagina/` — el port, i el que costa

`pagina/plantilla.html` és el joc reescrit en JavaScript dins d'un sol fitxer, i
`pagina/construix.py` li incrusta el contingut i escriu `pagina/tot-se-sap.html`.

```bash
python pagina/construix.py
```

Dues coses que han de quedar clares:

- ✅ **El contingut no es duplica.** Ix sempre de `content/`, i `proves/prova_pagina.py`
  **falla** si algú toca un YAML i no torna a generar. La promesa de «no poden
  desquadrar-se» la sosté eixa prova, no la bona voluntat.
- ⚠️ **La lògica sí que està escrita dos vegades.** El motor viu en Python i en
  JavaScript, i **la separació motor/sortida ahí dins no està forçada per res**: és un
  fitxer amb dues seccions retolades. Verificat el 01-09-2026 que els dos motors donen
  el mateix resultat jugada a jugada, però és una foto, no una garantia.
- ⚠️ **`Math.round` de JavaScript no és `round()` de Python** (l'un puja a l'alça i
  l'altre arredonix a parell). La pàgina porta la seua pròpia funció `arrod()` per això.
  Si algú la lleva, els números deixen de ser els del joc.

El port és **tirable**: si la plataforma acaba sent Python, se'n va sencer i el contingut
es queda. Si acaba sent web, ja està mig fet.

## La línia motor / sortida

> El motor només opera sobre el parell `(intenció, palanca)`. Mai toca text. (§3)

No és purisme. És el que permet que el dia de demà l'entrada siga text lliure classificat
(§7) o botons o veu, **sense tocar ni una línia del motor**. La capa de sortida es pot
tirar i tornar a escriure; el motor no.

Prova de foc: `grep` de cometes a `motor/nucli.py` només ha de trobar docstrings i claus
de diccionari (`"intimidació"`, `"estat"`…). Cap frase.

---

## Flux d'un torn

1. `cli` pinta la capçalera de l'NPC (`nucli.EIXOS`, i amb `c` també `nucli.pendents`).
2. `cli` demana **palanca primer, intenció després** (§3.4).
   Amb `[0] de res concret` → palanca `None` → intenció forçada `PREGUNTAR`.
3. `cli` pot demanar `nucli.previsió(...)` per ensenyar cap on va la jugada (mai la magnitud).
4. `cli` crida **`nucli.aplica(mon, npc_id, intenció, palanca)`** — l'única porta d'entrada.
5. `aplica` torna `{deltes, oberts, ruptura, tancat}`. Ordre intern exacte a [`03-motor.md`](03-motor.md).
6. `cli` passa això a `sortida.text` per a la frase del jugador i la resposta de l'NPC.
7. Si `f_autoria` ha caigut → final. Si tots els NPCs estan tancats → final sec.

---

## Estil

Funcions curtes i planes. Cap classe. NPCs, fets i intencions són **dades** (dicts eixits
del YAML), no objectes amb comportament. Els noms del domini van en català
(`fet`, `palanca`, `postura`, `desgast`, `ruptura`); la infraestructura, en el que faça falta.

Els accents als identificadors de Python (`previsió`, `intenció`) són vàlids i intencionats.
⚠️ Trampa: des de fora no els pots agafar amb `getattr(nucli, "previsió")` escrit en ASCII.

---

## Arrancar

```bash
.venv/Scripts/python.exe cli.py
```

`jugar.bat` fixa la consola en UTF-8 (`chcp 65001`) i tria el `python.exe` del `.venv` si
existix, i `py -3` si no. `cli.py` fa `sys.stdout.reconfigure(encoding="utf-8")` pel mateix
motiu de la consola.

⚠️ **`python` a seques no funciona en esta màquina**: el del PATH és l'àlies de la Microsoft
Store. El llançador `py` està instal·lat però tampoc és al PATH. Per això tot passa pel
`.venv`. Muntar-lo: [`plans/2026-09-01-entorn.md`](../../../plans/2026-09-01-entorn.md) F2.

Dependències: `pyyaml`, declarada a `requirements.txt`.
