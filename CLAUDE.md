# Tot se sap

Joc de detectius. Ets un **detectiu privat** en un poble de muntanya de ~200 habitants. No portes placa, o siga que l'única moneda que tens és **la informació**: el que li arranques a un NPC és la munició per arrancar-li informació al següent.

📖 **El disseny complet està a `docs/disseny.md`. Llegeix-lo abans de proposar arquitectura.**
🚪 **Com està construït ara mateix i què queda obert: `AGENTS.md`.**

---

## Invariant central — no el trenques mai

> **El motor només opera sobre el parell `(intenció, palanca)`. Mai toca text.**

- `intenció` = què li fas a l'NPC (`AMENAÇAR`, `OFERIR`, `EMPATITZAR`, `CONFRONTAR`, `INSINUAR`, `PREGUNTAR`)
- `palanca` = amb què (un `fet_id` que ja has obtingut)

Gates, deltes d'eixos, fets que s'obrin, accions d'NPC: tot es resol sobre eixe parell. La generació de text és una **capa de sortida separada** que rep l'estat resultant.

Si en algun moment la lògica de joc necessita mirar una cadena de text, alguna cosa s'ha dissenyat malament.

---

## Estat del projecte: v0 — prototip de terminal

**Objectiu:** validar si el bucle de conversa és divertit. Res més.

**Abast del v0:**
- Terminal pura (`input()` / `print()`). Zero UI.
- 3 NPCs, un cas, ~15 fets.
- Una sola variant de plantilla per intenció. Text lleig a posta.
- Navegació per **nodes clicables** (llista de llocs), no món caminable.

**NO construir encara** — encara que semble fàcil:
- ❌ Gràfics, cenital, assets
- ❌ Minijocs (forçar panys està descartat del tot)
- ❌ Filtre d'estil procedural (quequeig, etc.) — v1
- ❌ Text lliure / classificador — v2
- ❌ Múltiples variants de plantilla — només quan el joc s'haja jugat i se sàpiga quines canten

Si dubtes si una cosa entra al v0: **no entra**.

---

## Contingut fora del codi

Fets, NPCs, plantilles i xarxa social viuen en **YAML** dins de `content/`. El codi Python no conté ni una línia de diàleg.

Motiu: l'escriptura no ha de dependre de tocar codi, i el dia que es porte a un altre llenguatge el contingut se'n va intacte.

---

## Estil de codi

Escriu com escriuria John Carmack: **directe, curt, sense cerimònia**.

- Funcions curtes i planes. Res de jerarquies de classes per a coses que són dades.
- Els NPCs, fets i intencions són **dades**, no objectes amb comportament. Un dict o un dataclass simple.
- Zero frameworks, zero dependències que no facen falta. `pyyaml` i prou.
- No abstraure fins que hi haja **tres** casos reals que ho demanen. Amb dos, es duplica.
- Noms en català per al domini (`fet`, `palanca`, `intenció`, `postura`), anglès per a la infraestructura si convé. Coherència per damunt de puresa.

**Si hi ha diverses maneres d'afrontar un canvi, pregunta abans de tocar codi.**

Als refactors: canvi curt i funcional, que toque el mínim i seguisca l'estil que ja hi ha.

---

## Regles de disseny que el codi ha de respectar

1. **Els eixos entren en conflicte.** Intimidar puja `intimidació` i **fon** `confiança`. Si hi ha una estratègia dominant, el disseny està trencat.
2. **El cost va a la palanca, no a la intenció.** Les palanques es **degraden** per NPC (100% → 50% → 25%). Les intencions són gratis i il·limitades. Una sola decisió que faça mal per torn.
3. **Degradació, mai crema total.** Que el jugador perda l'efecte sorpresa, no la partida.
4. **Fiabilitat variable:** informació treta per intimidació pot ser **falsa** (et diu el que vols sentir); per confiança és certa; per temptació és certa però amb preu.
5. **Alarma inversa:** qui es creu irrellevant parla molt però és inintimidable. Preguntar té un cost — cada pregunta li diu al tio què busques.
6. **El món no es mou tot sol.** Tota acció d'NPC ha de tindre una causa **traçable fins a una acció del jugador**. Excepció única i guionitzada: el culpable actua si t'acostes massa.
7. **Propagació màxima de 2 salts.** Prou per sentir que corre la veu, prou poc per depurar-ho.
8. **L'estat és moneda, no només feedback.** El jugador ha de poder saber quin llindar li falta. Si falla i no entén per què, el disseny ha fallat.

---

## Estructura

```
AGENTS.md         # porta d'entrada: estat, protocol, on és cada cosa
content/          # YAML — fets, NPCs, intencions, números
  fets.yaml
  npcs.yaml
  intencions.yaml
  regles.yaml     # tots els números del motor, per tocar-los sense tocar codi
motor/            # lògica pura: (intenció, palanca) → estat nou
sortida/          # generació de text a partir de l'estat
cli.py            # bucle de terminal
docs/disseny.md   # document de disseny complet
docs/v0.md        # abast del v0
.dev/             # coordinació: plans, memòria de sessions, refs
                  #   xarxa.yaml arribarà amb la propagació. Fora del v0.
```
