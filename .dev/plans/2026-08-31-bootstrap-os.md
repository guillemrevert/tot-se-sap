# Pla — Capa de coordinació (Project OS)

Data: 2026-08-31
Responsable: Claude (amb Guillem)
Estat: **completat**

## Objectiu

Que qualsevol agent o persona que òbriga este projecte puga entendre en què està, què
s'ha decidit i què queda obert **sense llegir el codi ni l'historial de xat**, i que la
pròxima sessió no torne a obrir discussions ja tancades.

## Context

Punt de partida: `CLAUDE.md` + `docs/disseny.md` (512 línies, el document mestre) +
`docs/v0.md` + ~360 línies de Python jugables. Tot correcte i tot **desconnectat**: no hi
havia porta d'entrada, ni registre de decisions, ni cap lloc on visquera *què hi ha
construït ara* — només *per què ha de ser així*.

L'espurna és `2026-05-27-project-os-bootstrap.md`, un pla del projecte **CritKeep**
(Claude amb Iban) per adaptar aquell repo a un «Project Operating System». Es va portar
ací com a plantilla.

⚠️ **Falta la peça d'origen.** Aquell pla adapta un document, `project-operating-system-bootstrap.md`,
**que no s'ha aportat**. O siga que l'estructura d'ací està **reconstruïda a partir de les
pistes del pla** (una porta d'entrada, `plans/`, `memories-log/`, `refs/` numerats, un sol
punt d'entrada per als agents, frontera de commit), no copiada. Si eixe document apareix,
el primer que s'ha de fer és contrastar-lo amb açò.

## Abast

**Inclòs:** `AGENTS.md`, `.dev/` sencer (plans, memòria, arxiu, skill amb 10 refs),
auditoria del codi contra el disseny, correccions factuals a `CLAUDE.md`, `.gitignore`.

**Exclòs — i açò val més que la llista de dalt:**
- ❌ **Cap canvi a `motor/`, `sortida/`, `cli.py` ni `content/`.** Ni un byte.
- ❌ Cap decisió de disseny nova. El que s'ha trobat obert s'ha **documentat com a obert**,
  no resolt pel meu compte (`CLAUDE.md`: *si hi ha diverses maneres, pregunta*).
- ❌ El validador de §15, tot i que falta i fa falta: és codi i té forks de disseny dins.
- ❌ `git init`. És una decisió d'entorn i toca parlar-la.

## Decisions preses

1. **`docs/` no es mou.** El pla de CritKeep migrava la documentació dins de `refs/`; ací
   no, perquè `docs/disseny.md` és el document mestre i `CLAUDE.md` hi apunta. Queda:
   **`docs/` diu per què, `refs/` diu què hi ha**, i s'enllacen. Una casa canònica per cosa.
2. **Refs numerats però adaptats a este projecte**, no a la numeració canònica 01..11 de
   CritKeep (`03-api-contracts`, `05-frontend-patterns`… no volen dir res ací).
3. **Tot en valencià.** L'anglés d'aquell pla es justificava perquè era codi obert amb
   col·laboradors de fora. Ací no. Es revisarà el dia que entre algú que no el parle.
4. **`CLAUDE.md` no es reescriu**, només se li corregixen dos fets falsos i se li afig el
   pas per `AGENTS.md`. Ja era el que havia de ser: decisions i límits durs.
5. **L'arxiu penjat va a `.dev/archive/`**, no s'esborra, amb un README que diu clarament
   que és d'un altre projecte i que no és font de veritat.

## Fases

1. ✅ Llegir-ho tot i sondar el motor de veres per saber en quin estat està.
2. ✅ Esquelet `.dev/` + arxivar l'arxiu penjat + `.gitignore`.
3. ✅ `AGENTS.md` i `SKILL.md`.
4. ✅ Refs 01-06 i 10: què hi ha construït.
5. ✅ Ref 09: auditoria codi contra disseny, amb sondes sobre el motor.
6. ✅ Refs 07 i 08: decisions obertes i política de proves.
7. ✅ Correccions a `CLAUDE.md` + registre de memòria.

## Riscos

- **Cerimònia.** `CLAUDE.md` diu *zero frameworks, no abstraure fins que hi haja tres
  casos*. Deu fitxers de documentació per a 360 línies de codi ho podrien contradir.
  Mitigació: el pes real d'este projecte és el **disseny** (>30 KB), no el codi, i cada
  ref conté informació que abans només vivia dins del cap d'algú o dins del codi.
- **Documentació que envellix.** El pitjor resultat possible és un ref que menta. Mitigació:
  regla escrita al `SKILL.md` — els refs no repetixen números, els citen del fitxer on viuen;
  i si un canvi deixa un ref fals, arreglar-lo **és part del canvi**.
- **Duplicar el disseny.** Mitigació: la regla `docs/` per què ↔ `refs/` què hi ha, escrita
  a `AGENTS.md`, al `SKILL.md` i ací.

## Verificació

- ✅ `AGENTS.md` porta a tota la resta en un salt.
- ✅ Cap ref repetix una secció de `docs/disseny.md`: totes les referències són `§N` + enllaç.
- ✅ `git status` no mostraria cap canvi a `motor/`, `sortida/`, `cli.py` ni `content/`
  (no hi ha repo; comprovat a mà: no s'han obert per a escriure).
- ✅ Les tres decisions bloquejants de `docs/v0.md` §1 apareixen com a **obertes** a
  `refs/07`, amb el que fa el codi al costat.
- ✅ L'auditoria conté almenys una troballa **mesurada**, no opinada (A1).
