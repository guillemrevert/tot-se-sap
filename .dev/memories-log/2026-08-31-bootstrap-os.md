# 2026-08-31 — Muntar la capa de coordinació

## Què s'ha fet

Sessió de documentació. **Zero canvis a codi o contingut.**

- `AGENTS.md` — porta d'entrada única.
- `.dev/` — `plans/`, `memories-log/`, `archive/`, i `skills/skill-tot-se-sap/` amb 10 refs.
- Auditoria del codi contra el disseny → `refs/09`.
- `CLAUDE.md` — dos fets falsos corregits + pas per `AGENTS.md`.
- `.gitignore` i esborrat dels `__pycache__/`.
- L'arxiu penjat (pla de CritKeep) → `.dev/archive/`, marcat com a plantilla d'un altre projecte.

## Decisions preses

Les cinc estan al pla: [`../plans/2026-08-31-bootstrap-os.md`](../plans/2026-08-31-bootstrap-os.md).
La que més condiciona la resta: **`docs/` diu per què, `refs/` diu què hi ha.** El disseny
no es mou ni es resumix; s'enllaça.

## Què queda obert

Vuit decisions a [`../skills/skill-tot-se-sap/refs/07-decisions-obertes.md`](../skills/skill-tot-se-sap/refs/07-decisions-obertes.md).
Les que bloquegen de veres:

- **D5 — entorn.** No hi ha repo git, ni dependències declarades, ni com s'executa fora
  d'esta màquina. És el següent tema de conversa.
- **D1 — les tres de `v0.md` §1.** El document diu que el motor no es pot escriure sense
  elles. El motor està escrit. `alarma` no existix.
- **D7 — la finestra de `f_autoria`.**

## Trampes trobades

- **El cas es guanya per 0 punts de marge.** `f_autoria` demana 85, Roc trenca a 90, i el
  camí verificat cau **exactament en 85**. La jugada natural (sempre la carta més forta)
  topa en 84 i no arriba mai. Detall a `refs/09` A1.
- **`round()` de Python arredonix a parell.** `round(12.5) == 12` però `round(7.5) == 8`.
  Els deltes reals del joc no són els que ix fent el compte de cap: `CONFRONTAR` amb carta
  vulnerable fresca fa **22**, no 23.
- **Una jugada que moga menys de 5 d'intimidació no avança**, perquè el refredament se la
  menja el mateix torn. Els incrementets no són «poc a poc»: són zero.
- **`python` del PATH és l'àlies de la Microsoft Store i no arranca.** Cal
  `%LOCALAPPDATA%\Programs\Python\Python313\python.exe`, que és el que fa `jugar.bat`.
- Els identificadors amb accent (`nucli.previsió`) no es poden agafar amb `getattr` escrit
  en ASCII des d'un script de fora.
