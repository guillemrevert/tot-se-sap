# 07 — Decisions obertes

**Llig açò abans de proposar arquitectura.** Una decisió que no està ací és que ja està
presa (a `CLAUDE.md` o a `docs/disseny.md`) i no s'ha de tornar a obrir.

Actualitzat: 01-09-2026.

| # | Decisió | Estat | Bloqueja |
|---|---|---|---|
| D1 | Les tres de `docs/v0.md` §1 | 🔴 obertes, i el codi ja s'ha escrit sense elles | el motor sencer |
| D2 | Esquema de dades (`docs/v0.md` §6) | 🟡 resolt **de facto** al codi, sense ratificar | tocar `content/` |
| D3 | Quant estat veu el jugador | 🔴 contradicció viva | UX, i la regla 8 |
| D4 | El refredament global | 🟡 decidit al codi, no al disseny | la regla 6 |
| D5 | ~~Entorn: git, dependències, com s'executa~~ | 🟢 **tancada** 01-09-2026 | — |
| D6 | Llengua de la capa `.dev/` | 🟢 català (assumit, no confirmat) | res urgent |
| D7 | La finestra de `f_autoria` | 🔴 el cas **no és guanyable jugant a l'obvi** | jugar-hi |
| D8 | ~~Marc de proves~~ | 🟢 **tancada** 01-09-2026: `unittest` | — |

---

## D1 — Les tres de `docs/v0.md` §1 🔴

`docs/v0.md` diu *«cap de les tres està confirmada»* i *«el motor no es pot escriure sense
elles»*. **El motor s'ha escrit.** Estat real de cadascuna:

| Qüestió | Proposta de §16 | Què fa el codi |
|---|---|---|
| **INSINUAR costa algo?** | sí: costa `alarma` | Costa **desgast de palanca**, com qualsevol altra intenció (`aplica` degrada sempre). §16.2 queda tapat, però per una via distinta de la proposada. |
| **Arrancada en fred** | PREGUNTAR puja `alarma` i te'l fa intimidable | Els fets `INDIFERENT` tenen el llindar per davall de la confiança inicial i **cauen sols** al primer torn. Funciona, però és una propietat del contingut, no una mecànica. |
| **Què és `alarma`** | multiplicador sobre `resistència` | **No existix.** Zero aparicions al codi i al contingut. |

**A decidir:** ratificar el que fa el codi i tancar §16.2/§16.3, o implementar `alarma` de
veres. Si s'implementa, cal `resistència` primer, que tampoc existix.

## D2 — L'esquema de dades 🟡

Les quatre decisions del fork de §6 es van prendre escrivint el codi. Estan marcades ⚑ a
[`02-model-de-dades.md`](02-model-de-dades.md):

1. **Formes gramaticals** → tres cadenes fixes per fet (`nu`/`subordinada`/`nominal`).
2. **Els gates viuen al fet** (`dificultat`) + multiplicador per postura. No hi ha matriu fet×NPC.
3. **`postura_per_fet` només per als fets que l'NPC té** — `sap` diu alhora *què sap* i *per què calla*.
4. **No hi ha `modificadors_per_postura` per intenció.** La postura tria l'eix i escala la
   dificultat; no toca els deltes.

Funcionen. **Però no s'han discutit**, i §6 deia explícitament que no s'havien de triar
sense parlar-ho. Cal un sí o un no, no un altre disseny.

## D3 — Quant estat veu el jugador 🔴

- Regla 8 del `CLAUDE.md`: *«el jugador ha de poder saber quin llindar li falta»*.
- `nucli.pendents()` al docstring: *«el jugador no ha de veure això: se n'ha d'assabentar
  pel que li conteste»*.

Les dues no poden ser certes. Ara mateix guanya la segona (els llindars només ixen amb la
tecla `c`, que és depuració), i eixe és **exactament l'error d'*Interrogation*** que §3.5
assenyala com el risc principal del projecte. El terme mitjà evident —que la resposta de
l'NPC comunique la distància— **encara no està dissenyat**.

## D4 — El refredament global 🟡

`_refreda()` mou els eixos de **tots** els NPCs cada torn. El docstring ho defensa: la
causa traçable és que has deixat de pressionar. És defensable, però és una lectura de la
regla 6 i **no està escrita a `docs/disseny.md`**. O s'escriu allí, o el refredament passa
a ser només de l'NPC amb qui parles.

## D5 — Entorn 🟢 tancada

Guia sencera: [`plans/2026-09-01-entorn.md`](../../../plans/2026-09-01-entorn.md).

**Fet l'01-09-2026 (F1 i F2):**

- Repo git en `main`, amb `.gitattributes` (finals de línia) i `.gitignore`.
- `.venv` + `requirements.txt`. `pyyaml` ja no depén de la instal·lació global.
- `jugar.bat` ja no porta cap ruta d'esta màquina: tria el `.venv` o `py -3`.
- Decidit: **aplicació, no llibreria** — res d'empaquetat, `requirements.txt` i prou.

**Fet l'01-09-2026 (F4):**

- **AGPL-3.0** per al codi, **CC BY-NC-SA 4.0** per a `content/` i `docs/`, i `TRADEMARK.md`
  per al nom. El patró ix de CritKeep (AGPL + política de marca), no del que proposava la
  guia, que deia MIT. Motiu: coherència entre projectes i copyleft fort sobre el motor.
- README amb captura real del bucle, i CONTRIBUTING amb la cessió de drets per a contingut.

**Fet l'01-09-2026 (F3):**

- 14 proves amb `unittest` en `proves/`. Tanca **D8**.

**Fet l'01-09-2026 (F5):**

- `.github/workflows/proves.yml`: passa les proves en Python 3.11 i 3.13, i té el pas del
  validador escrit i comentat, per a descomentar-lo el dia de F6.

L'entorn està muntat: es clona, s'arranca amb dues ordres i té proves. **Publicar-lo és un
acte a banda, no una decisió**, i és l'únic que queda:

- ⏳ **Remot.** El repo és local. Fins que no es publique, la CI **no s'ha executat mai** i
  el README té un `<aquest-repo>` de marcador. Verificat fins on es pot sense GitHub: el
  YAML es llig, l'ordre coincidix amb la documentada, i tot el codi passa un `ast.parse`
  amb `feature_version=(3, 11)` — sintaxi, no execució.
- Versió mínima de Python: es declararà al README (3.11) i l'ha de verificar la CI.
- ⚠️ El llançador `py` està instal·lat però **no és al PATH**, i el `python` del PATH és
  l'àlies de la Microsoft Store. Res del projecte ho necessita ja, però qualsevol ordre
  escrita com a `python …` fallarà en esta màquina.

## D6 — Llengua de `.dev/` 🟢

Tot el projecte està en valencià i el pla d'on ix esta estructura estava en anglés
**perquè aquell repo era codi obert amb col·laboradors de fora**. Ací no és el cas, o siga
que `.dev/` va en valencià. **Es canvia el dia que entre algú que no el parle**, no abans.

## D7 — La finestra de `f_autoria` 🔴

`f_autoria` demana `intimidació 85`; Roc trenca a `90`. Mesurat (veure
[`09`](09-auditoria-codi-vs-disseny.md)): **hi ha camí, però el joc «obvi» —tirar sempre
la carta més forta— topa a 84 i no arriba mai**, i el joc no dona cap senyal de per què.

Tres eixides, i són de disseny, no de números:

- **A — tocar números.** Baixar el gate o pujar la ruptura. Barat, i deixa el problema viu
  per al pròxim cas.
- **B — `sostre` de veres** (§11): que l'eix tinga un màxim per NPC i que la ruptura no siga
  l'única manera de tancar una porta.
- **C — que la ruptura no siga instantània.** Un avís abans (§11 `reactivitat: S_ENFADA`).

Es decidix quan el validador de §15 existisca i es puga veure què passa amb cada opció.

## D8 — Proves 🟢 tancada

`unittest` de la biblioteca estàndard, en `proves/`, amb 14 proves que passen. El detall i
els dos paranys de `discover`, a [`08`](08-qualitat-i-proves.md).

El que **no** cobrixen és el contracte del motor, i és a posta: D1 i D2 encara el poden
canviar.

---

## Ja decidides (no reobrir)

- **`docs/` es queda on està.** El disseny **no** es mou dins de `refs/`: `docs/` diu per
  què, `refs/` diu què hi ha. (31-08-2026)
- **Un sol punt d'entrada: `AGENTS.md`.** `CLAUDE.md` es queda com el que ja era —
  decisions i límits durs—, no es duplica. (31-08-2026)
