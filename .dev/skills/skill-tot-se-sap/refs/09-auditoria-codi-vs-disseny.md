# 09 — Auditoria: codi contra disseny

Data: **31-08-2026**. Abast: tot el codi i tot el contingut contra `docs/disseny.md`,
`docs/v0.md` i `CLAUDE.md`. **No s'ha tocat ni una línia de codi ni de contingut** per a
fer-la.

Mètode: lectura + dues sondes d'usar i tirar sobre el motor de veres (punt fix de
resolubilitat i cerca exhaustiva sobre l'eix d'intimidació de Roc). Les sondes no s'han
guardat al projecte: el seu lloc és el validador de §15, que encara no existix
([`08`](08-qualitat-i-proves.md)).

---

## 🔴 A1 — El cas és guanyable, però no jugant a l'obvi

`f_autoria` demana `intimidació 85` en Roc. Roc trenca a `90`. **Finestra de cinc punts**,
i `aplica()` comprova la ruptura **abans** d'obrir fets: passar-se de 90 tanca Roc encara
que la mateixa jugada haguera passat el llindar.

Mesurat:

- **Hi ha camí.** Tres jugades, amb les cartes que pots portar de Silvestre i Neus:
  `AMENAÇAR f_roc_va_pagar` (+38) → refreda a 33 → **la mateixa carta ja gastada**
  (+19) → refreda a 47 → `AMENAÇAR f_clau_penjada` (+38) = **85 clavat**.
- **La jugada natural no arriba.** Una política voraç —sempre la carta més forta que no
  trenque— topa en **84** i no puja d'ahí: crema les cartes fortes massa prompte i després
  cada jugada que li queda mou menys que el refredament de 5 per torn.

O siga que la manera d'arribar-hi és **gastar la mateixa carta dues vegades a posta** i
guardar-se'n una de forta per al final. És bon disseny en potència —§3.3 vol exactament
eixa decisió— però ara mateix:

1. El joc **no dona cap senyal** de per què 84 no basta (regla 8, i el fallo d'*Interrogation* de §3.5).
2. El camí que funciona és contraintuïtiu i **cau exactament al llindar**: qualsevol
   número que es toque el pot trencar en qualsevol direcció.
3. Si t'has passat de 90, el cas és **inguanyable i el joc no t'ho diu** (veure A2).

⚠️ Enumerar tota la finestra `[85, 90)` no va acabar en temps raonable amb una cerca
exhaustiva senzilla. El que està verificat és el d'ací dalt, no que 85 siga l'únic valor
tocable. → decisió **D7** de [`07`](07-decisions-obertes.md).

## 🔴 A2 — Es pot arribar a un estat inguanyable sense avís

Si Roc es tanca, `f_autoria` no s'obri mai més: és l'únic que el sap. Però `cli.py` només
declara final quan **tots tres** estan tancats. Amb Roc cremat i els altres dos vius, el
jugador seguix jugant una partida que ja no es pot guanyar.

## 🔴 A3 — `alarma` no existix

Zero aparicions a `motor/`, `sortida/`, `cli.py` i `content/`. És una de les tres decisions
que `docs/v0.md` §1 declara bloquejants (*«el motor no es pot escriure sense elles»*), i
és la peça 5 del que este projecte té de propi (§12: *alarma inversa*). El motor s'ha
escrit igual. → **D1**.

## 🟡 A4 — Del model de §11 falta més del que sembla

No implementats: `sostre`, `resistència`, `reactivitat`, `traços`, `ha_sentit_de_tu`,
`accions_disponibles`, `fiabilitat_per_via`, `intencions_vàlides`, xarxa, reputació.

Els majoritaris són v1 i està bé. **Dos són d'ara:**

- **`sostre`** — sense ell, el validador de §15 no té la meitat del que ha de comprovar
  (el seu punt 1 parla literalment del sostre), i la ruptura acaba fent-li de suplent.
- **`fiabilitat_per_via`** — el ganxo ja existix (`obtinguts[f]["via"]` guarda per quin eix
  vas traure cada fet) i **no l'usa ningú**. És el punt 2 del que fa este projecte distint
  de tot el que hi ha (§12), i costa poc.

També falta `intencions_vàlides` per fet: §3.4 diu que el menú ha de mostrar *«només les
3-4 intencions que tenen sentit»* amb eixa palanca, i el CLI ensenya sempre les sis.

## 🟡 A5 — El validador de §15 no existix

`docs/v0.md` §5 el posa al pas 3 de 4 i escriu *«ja — no al final»*. És el que permet
tocar números sense por, i A1 és exactament el tipus de cosa que hauria caçat el primer dia.
→ [`08`](08-qualitat-i-proves.md).

## 🟡 A6 — Zero proves

Cap fitxer de test, cap marc. → **D8**.

## 🟡 A7 — Decisions preses al codi que no estan escrites enlloc

Ni són errors ni són dolentes; el problema és que ningú les ha ratificat i **es descobrixen
llegint codi**:

| Què | On |
|---|---|
| Les 4 decisions del fork d'esquema de `v0.md` §6 | **D2** |
| §16.2 (INSINUAR gratis) resolt per desgast de palanca, no per alarma | **D1** |
| §16.3 (arrancada en fred) resolt perquè els fets `INDIFERENT` cauen sols al torn 1 | **D1** |
| El refredament mou **tots** els NPCs cada torn | **D4** |
| `PREGUNTAR` amb palanca la gasta i no mou res (intencionat, §3.2, però sembla un bug) | — |

## 🟡 A8 — `CLAUDE.md` desactualitzat en dos punts concrets

1. L'arbre d'`Estructura` llista `content/xarxa.yaml`, **que no existix** (correcte: la
   propagació està fora del v0), i **no llista `content/regles.yaml`**, que és on viuen
   tots els números del motor.
2. La regla 2 diu que les palanques es degraden *«100% → 50% → 0»*. El codi fa
   `[1.0, 0.5, 0.25]`, i `content/regles.yaml` explica per què al comentari: terra a 0.25
   *«perds l'efecte sorpresa, no la partida»* — que és la regla 3 del mateix fitxer.
   **El codi té raó i el document no.**

## 🟡 A9 — Entorn sense muntar

Sense repo git, sense `pyyaml` declarat, sense versió mínima de Python escrita, i amb un
`jugar.bat` que depén d'una ruta absoluta d'esta màquina. → **D5**.

## 🟢 A10 — El que sí que està bé

- L'invariant es respecta: `motor/nucli.py` no conté ni una frase, i `sortida/` és l'única
  capa que toca cadenes. La línia es pot verificar a ull en 30 segons.
- El desgast és **per NPC**, com mana §3.3. És el detall que més fàcil hauria sigut fer malament.
- El terra de degradació a 0.25 respecta *degradació, mai crema total*, i la UI ho reforça
  no pintant mai `○○○`.
- Tots els números viuen a `content/regles.yaml` amb comentaris que expliquen **per què**,
  no què. És exactament el que demana «el contingut fora del codi».
- El triangle de §2.3 està muntat de veres: `f_clau_penjada` el saben tres NPCs amb tres
  postures distintes i s'obri per tres eixos distints. La pregunta que el v0 havia de
  contestar **es pot contestar jugant**.
