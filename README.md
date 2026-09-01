# Tot se sap

<p>
  <img src="https://img.shields.io/badge/codi-AGPL--3.0-blue.svg" alt="Llicència del codi" />
  <img src="https://img.shields.io/badge/contingut-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="Llicència del contingut" />
  <img src="https://img.shields.io/badge/estat-prototip-orange.svg" alt="Estat" />
  <img src="https://img.shields.io/badge/python-3.11%2B-yellow.svg" alt="Python" />
</p>

Eres un **detectiu privat** en un poble de muntanya de dos-cents habitants. No portes
placa, o siga que l'única moneda que tens és **la informació**.

El que li arranques a un NPC és la munició per a arrancar-li informació al següent. Cada
fet és alhora **premi i clau**: el guanyes i el gastes.

---

## El bucle

Tota frase que pots dir es descompon en dues coses: **una intenció** (què li fas) i **una
palanca** (amb què). La palanca és un fet que ja li has tret a algú.

```
──────────────────────────────────────────────────────────────────
  SILVESTRE · pastor
  Assegut a la pedra, amb el gaiato entre les cames. Content de veure algú.

  intimidació  ░░░░░░░░░░
  confiança    ██░░░░░░░░
  temptació    ░░░░░░░░░░
──────────────────────────────────────────────────────────────────

  De què li parles?

   [1] hi havia llum a la cooperativa a les tres de la matinada del diumenge
       ●●●
   [2] Roc va pagar un deute dilluns de matí, en efectiu
       ●●●
   [0] de res concret

  de què > 1

  Com li ho dius?

   [1] AMENAÇAR     puja intimidació · fon confiança
   [2] OFERIR       puja temptació · puja intimidació
   [3] EMPATITZAR   puja confiança · puja intimidació
   [4] CONFRONTAR   fon confiança · puja intimidació
   [5] INSINUAR     puja intimidació
   [6] PREGUNTAR    no li fa res

  com > 5

  TU  — «Curiós, això de la llum de la cooperativa a les tres de la matinada. No trobes?»

  SILVESTRE — «Home, coses se'n diuen, però jo no faig cas.»
```

**Els eixos entren en conflicte.** Intimidar puja `intimidació` i **fon** `confiança`. Hi ha
fets que només s'obrin amb confiança alta: eixos no els trauràs mai a base d'hòsties.

**Cada NPC calla per un motiu distint.** Un **protegix** algú, un altre té **por**, un altre
en **trau profit**. El motiu decidix quin eix li obri la boca. Tres NPCs poden saber el
mateix i ser tres murs diferents.

**El cost va a la palanca, no a la intenció.** Amenaçar és gratis i il·limitat. El que és
escàs és **quina carta gastes ací i quina et guardes** per al que serà més dur: cada
palanca es degrada contra l'NPC on l'uses. Mai fins a zero — perds l'efecte sorpresa, no
la partida.

**I t'han pogut mentir.** Un fet tret a base de por pot ser fals: t'ha dit el que volies
sentir. Tret per confiança, és cert. No ho sabràs fins al final.

---

## Provar-lo

```bash
git clone <aquest-repo> "tot-se-sap"
cd tot-se-sap
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt   # Linux/macOS: .venv/bin/python
.venv/Scripts/python.exe cli.py
```

A Windows, després del primer muntatge: doble clic a `jugar.bat`.

Dependències: `pyyaml` i prou. Python 3.11 o superior.

Dins del joc: `n` canviar d'interlocutor · `f` el que ja saps · `c` calibratge (ensenya els
números crus i els llindars que et falten) · `q` eixir.

---

## Estat: prototip

Açò **encara no és un joc**, és un banc de proves per a contestar una pregunta: *el bucle de
conversa és divertit?*

- 3 NPCs, 8 fets, una conversa. Terminal pura, zero interfície.
- Una sola variant de frase per intenció. **El text està lleig a posta.**
- El cas que ve dins es diu `cas_prova` i és **bastida: es tira.** Una cosa robada, no un
  mort, i escrit per a estressar el mecanisme. El cas de veres encara no està escrit.

El que **no** hi ha i no ho busques: gràfics, minijocs, món caminable, text lliure, i cap
sistema de propagació entre NPCs.

---

## El disseny

El pes d'este projecte no és el codi —són quatre-centes línies— sinó el disseny.

| | |
|---|---|
| [`docs/disseny.md`](docs/disseny.md) | El document mestre. **Per què** el joc és així, secció a secció. |
| [`docs/v0.md`](docs/v0.md) | Què entra en este prototip i què no. |
| [`AGENTS.md`](AGENTS.md) | Porta d'entrada: com està construït ara i què queda obert. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Com muntar l'entorn i com entra un canvi. |

L'invariant que no es trenca mai:

> **El motor només opera sobre el parell `(intenció, palanca)`. Mai toca text.**

La generació de text és una capa de sortida separada. Per això el contingut viu en YAML,
el codi no conté ni una línia de diàleg, i el dia que açò es porte a un altre llenguatge
el contingut se'n va intacte.

---

## Llicències

Són dues, i cobrixen coses distintes:

| Què | Llicència |
|---|---|
| **Codi** (`motor/`, `sortida/`, `cli.py`…) | [AGPL-3.0](LICENSE) |
| **Contingut** (`content/`, `docs/`) | [CC BY-NC-SA 4.0](LICENSE-CONTINGUT) |
| **El nom «Tot se sap»** i la identitat visual | [cap de les dues](TRADEMARK.md) |

En resum: clona el motor i fes el teu joc de detectius, amb el teu nom. Els casos els pots
jugar, adaptar i compartir, però no vendre.

---

## Sobre el projecte

Fet a València per [Guillem](https://github.com/guillemrevert), amb l'ajuda de
col·laboradors d'IA. El joc, les notes i el codi estan en valencià: el vocabulari del
domini (`fet`, `palanca`, `postura`, `eix`) és part del projecte, no un detall d'estil.

Referents que fan bé alguna de les peces, i cap les tres juntes: *Interrogation: You Will
Be Deceived*, *The Case of the Golden Idol*, *Return of the Obra Dinn*, *We Should Talk*.

---

## In English

**Tot se sap** ("everybody finds out") is a terminal detective game where you are a private
investigator with no badge, so information is the only currency you have. Every sentence
you can say decomposes into an **intent** and a **lever** — a fact you extracted from
somebody else. Facts are both the reward and the key.

The engine is a pure `(intent, lever) → new state` function that never touches text;
all writing lives in YAML. The game, the design notes and the domain vocabulary are in
Valencian, and that is deliberate. Code is AGPL-3.0, content is CC BY-NC-SA 4.0, and the
name is neither — see [TRADEMARK.md](TRADEMARK.md).

It is an early prototype: 3 NPCs, 8 facts, deliberately ugly prose, and a throwaway case.
