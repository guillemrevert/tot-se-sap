# Plans

Un fitxer per feina que no cap en una sessió. `AAAA-MM-DD-nom-curt.md`.

**Es fa el pla ABANS de començar**, no com a acta del que ja s'ha fet. El valor és
que algú puga dir «això no» quan encara val zero desfer-ho.

Un pla no s'esborra mai: es marca `completed` / `abandonat` i es queda. Un pla abandonat
amb el motiu escrit val més que un pla esborrat.

## Plantilla

```markdown
# Pla — <títol>

Data: AAAA-MM-DD
Responsable: <qui>
Estat: proposta | en marxa | completat | abandonat

## Objectiu
Una frase. Què ha de ser cert quan açò s'acabe.

## Context
Què hi ha ara i per què no basta. Enllaços als refs i a docs/disseny.md.

## Abast
Inclòs: …
Exclòs: …          ← esta línia val més que l'anterior

## Decisions
Confirmades amb <qui>, data. Numerades, perquè després es puguen citar.

## Fases
1. …

## Riscos
Què pot eixir malament i què es fa si passa.

## Verificació
Com se sabrà que està fet. Comprovable, no opinable.
```
