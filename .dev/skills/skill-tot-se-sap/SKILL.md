---
name: skill-tot-se-sap
description: Coneixement de treball del projecte «Tot se sap» — com està construït el joc ara mateix. Llig-lo abans de tocar motor, contingut o sortida.
---

# Tot se sap — coneixement de treball

**Açò descriu QUÈ hi ha construït.** El **per què** viu a [`docs/disseny.md`](../../../docs/disseny.md)
i no es duplica ací: quan un ref necessita justificar una decisió, enllaça `§N` d'allí.

Si véns de zero: [`AGENTS.md`](../../../AGENTS.md) primer, este índex després.

---

## Refs

| Ref | Què hi trobaràs | Quan el necessites |
|---|---|---|
| [`01-arquitectura.md`](refs/01-arquitectura.md) | Mòduls, flux d'un torn, per què la línia motor/sortida | Abans de moure res de lloc |
| [`02-model-de-dades.md`](refs/02-model-de-dades.md) | Esquema real dels 4 YAML + l'estat viu que penja el carregador | Abans de tocar `content/` o afegir un camp |
| [`03-motor.md`](refs/03-motor.md) | L'algorisme del torn, en ordre. Els números i què fa cadascú | Abans de tocar `motor/nucli.py` |
| [`04-sortida-i-text.md`](refs/04-sortida-i-text.md) | Plantilles, formes gramaticals, to, cua anti-repetició | Abans de tocar `sortida/` o escriure plantilles |
| [`05-contingut.md`](refs/05-contingut.md) | El `cas_prova` sencer: la veritat, el graf de fets, qui sap què | Abans d'escriure un fet o un NPC |
| [`06-full-de-ruta.md`](refs/06-full-de-ruta.md) | v0 / v1 / v2 i el que està explícitament fora | Quan dubtes si una cosa entra ara |
| [`07-decisions-obertes.md`](refs/07-decisions-obertes.md) | Els forks vius, amb estat i qui els bloqueja | **Abans de proposar arquitectura** |
| [`08-qualitat-i-proves.md`](refs/08-qualitat-i-proves.md) | Política de proves i l'espec del validador de resolubilitat (§15) | Abans de canviar números o contingut |
| [`09-auditoria-codi-vs-disseny.md`](refs/09-auditoria-codi-vs-disseny.md) | Auditoria 31-08-2026: on el codi i el disseny no diuen el mateix | Per saber què està trencat ara |
| [`10-glossari.md`](refs/10-glossari.md) | Vocabulari del domini ↔ identificadors del codi | Quan no saps si dir `gate` o `llindar` |

---

## Regles d'este coneixement

1. **Un ref descriu el present.** Si una cosa és un pla, va a `.dev/plans/`. Si és un
   desig, va a `docs/`.
2. **Zero duplicació.** El disseny s'enllaça, no es resumix. La duplicació és el que fa
   que la documentació quede vella sense que ningú se n'adone.
3. **Un ref que menta un número l'ha de citar del fitxer on viu** (`content/regles.yaml`),
   no repetir-lo. Els números es toquen sovint.
4. **Si canvies codi i el ref queda fals, el ref és part del canvi.** No és feina extra:
   és el canvi.
