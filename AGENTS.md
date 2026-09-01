# AGENTS.md — porta d'entrada

Qualsevol que entre ací (Claude, Codex, Augment o un humà) comença per este fitxer.
Si només llegixes una cosa, que siga esta pàgina.

---

## Què és açò

**Tot se sap** — joc de detectius de terminal. Ets un **detectiu privat** en un poble de
muntanya de ~200 habitants. No portes placa: l'única moneda que tens és **la informació**.
El que li arranques a un NPC és la munició per arrancar-li informació al següent.

**Estat: v0 — prototip de terminal jugable.** 3 NPCs, 8 fets, un cas de mentida (`cas_prova`).
~460 línies de Python. L'objectiu del v0 no és el joc: és saber si el bucle de conversa és divertit.

---

## L'invariant

> **El motor només opera sobre el parell `(intenció, palanca)`. Mai toca text.**

- `intenció` = què li fas (`AMENAÇAR`, `OFERIR`, `EMPATITZAR`, `CONFRONTAR`, `INSINUAR`, `PREGUNTAR`)
- `palanca` = amb què — un `fet_id` que ja has arrancat a algú

Si `motor/` necessita mirar una cadena de text, alguna cosa s'ha dissenyat malament.
Detall: [`refs/03-motor.md`](.dev/skills/skill-tot-se-sap/refs/03-motor.md).

---

## On està la veritat

| Vols saber… | Mira |
|---|---|
| **per què** el joc és així | [`docs/disseny.md`](docs/disseny.md) — document mestre (§1-16). No es resumix enlloc més. |
| què entra al v0 i què no | [`docs/v0.md`](docs/v0.md) |
| decisions i límits durs | [`CLAUDE.md`](CLAUDE.md) |
| **què hi ha** construït ara | [`.dev/skills/skill-tot-se-sap/SKILL.md`](.dev/skills/skill-tot-se-sap/SKILL.md) → `refs/` |
| què s'està fent i per què | [`.dev/plans/`](.dev/plans/) |
| què va passar en una sessió | [`.dev/memories-log/`](.dev/memories-log/) |

> **Regla d'or de la documentació:** `docs/` diu **per què**; `refs/` diu **què hi ha**.
> No es dupliquen mai — es creuen amb enllaços. Si et trobes copiant disseny a un ref,
> pares i poses un enllaç.

---

## Arrancar

Cada dia: doble clic a `jugar.bat`, o bé

```bash
.venv/Scripts/python.exe cli.py
```

Muntar l'entorn la primera vegada (i per què `python` a seques no val en esta màquina):
[`.dev/plans/2026-09-01-entorn.md`](.dev/plans/2026-09-01-entorn.md) F2.

Dependències: `pyyaml` i prou, declarada a `requirements.txt`. Provat amb Python 3.13.

Dins del joc: `n` canviar d'interlocutor · `f` el que ja saps · `c` **calibratge** (números
crus, llindars pendents) · `q` eixir. El mode calibratge és l'única finestra al motor que hi ha.

---

## Protocol de treball

1. **Abans de tocar res** — llig el ref que toque. No comences a llegir codi a cegues.
2. **Si hi ha més d'una manera raonable d'afrontar un canvi: pregunta abans de tocar codi.**
   És la regla del `CLAUDE.md` i és la que més es trenca.
3. **Feina de més d'una sessió** → un pla a `.dev/plans/AAAA-MM-DD-nom.md` **abans** de començar.
4. **Canvi de disseny** → `docs/disseny.md`. **Canvi d'abast** → `docs/v0.md`.
   Mai un canvi de disseny que només visca al codi.
5. **Canvi de contingut** (`content/*.yaml`) → tornar a passar el validador de resolubilitat.
   ⚠️ Encara no existix: [`refs/08-qualitat-i-proves.md`](.dev/skills/skill-tot-se-sap/refs/08-qualitat-i-proves.md).
6. **En tancar sessió** → una entrada a `.dev/memories-log/`. Curta. Què s'ha decidit i què queda obert.

---

## Frontera de canvi

- `motor/` — lògica pura. Zero text, zero `print`, zero `input`.
- `sortida/` — l'única capa que toca cadenes.
- `content/` — de qui escriu. **El codi no conté ni una línia de diàleg.**
- `cli.py` — bucle de terminal. Provisional per definició.
- Un canvi = una cosa. Si toques motor i contingut alhora, són dos canvis.

És un repo git, branca `main`. **Un canvi = un commit**: si toques motor i contingut alhora,
són dos commits. Missatge d'una línia, imperatiu, en valencià.

⚠️ Encara **no hi ha remot, ni llicència, ni CI** — F4 i F5 de
[`.dev/plans/2026-09-01-entorn.md`](.dev/plans/2026-09-01-entorn.md). Fins llavors açò és
un repo local i prou.

---

## Les 8 regles que el codi ha de respectar

Viuen al [`CLAUDE.md`](CLAUDE.md) i no es copien ací a posta. Resum d'una línia perquè
no se't passe cap: els eixos entren en conflicte · el cost va a la palanca · degradació
mai crema total · fiabilitat variable segons la via · alarma inversa · el món no es mou
sol · propagació màxima 2 salts · l'estat és moneda i el jugador l'ha de poder llegir.
