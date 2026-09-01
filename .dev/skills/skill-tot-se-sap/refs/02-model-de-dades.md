# 02 — Model de dades

L'esbós de `docs/disseny.md` §11 és un esbós. **Açò és el que hi ha de veres.**
Bona part del fork obert de `docs/v0.md` §6 s'ha resolt escrivint el codi; les decisions
que es van prendre així estan marcades ⚑ i encara no s'han ratificat ([`07`](07-decisions-obertes.md)).

---

## `content/fets.yaml`

```yaml
f_clau_penjada:
  nu:          "la clau es queda penjada darrere de la barra…"   # per a llistes i UI
  subordinada: "que la clau es queda penjada darrere de la barra…"
  nominal:     "la clau penjada darrere de la barra…"
  dificultat:  50
```

- **Tres formes gramaticals** per fet. La plantilla demana la que li fa falta i així
  s'evita *«parlem de entres al magatzem»* (§4). ⚑ Decisió: **formes fixes al fet**, no
  generació morfològica.
- `dificultat` és **un sol número**. ⚑ **El gate viu al fet, no al parell fet×NPC**:
  quin *eix* l'obri ho decidix la postura de l'NPC, i la postura també li aplica un
  multiplicador. Un número per fet + un multiplicador per postura, en compte d'una matriu.
- No hi ha `fiabilitat_per_via` ni `intencions_vàlides` ni `requereix`, tot i que §11 i
  §13.6 els contemplen. Veure [`09`](09-auditoria-codi-vs-disseny.md).

## `content/npcs.yaml`

```yaml
roc:
  nom: Roc
  ofici: taverner
  lloc: La taverna
  presentació: "Darrere de la barra, secant got rere got. No et mira."
  estat: { intimidació: 0, confiança: 5, temptació: 0 }
  ruptura: 90                      # intimidació >= açò -> es tanca per sempre
  vulnerable_a: [f_roc_va_pagar, …] # quines cartes li fan mal
  sap:                             # fet -> POSTURA
    f_autoria: POR
  respostes:                       # to -> llista de línies
    sec: [...]  obert: [...]  interessat: [...]  pressionat: [...]
    ruptura: "…"                   # una sola, no llista
```

- ⚑ **`postura_per_fet` només per als fets que l'NPC té.** `sap` fa dues coses alhora:
  diu **què sap** i **per què calla**. §11 el deixava obert; ací s'ha unificat.
- `vulnerable_a` és la `vulnerabilitat: tema_id` de §11, però **per fet i en llista**,
  no per tema.
- **No implementats de §11:** `resistència`, `sostre`, `reactivitat`, `traços`,
  `alarma`, `ha_sentit_de_tu`, `accions_disponibles`. `sostre` és el més greu: és
  justament el que el validador de §15 ha de comprovar.

## `content/intencions.yaml`

```yaml
AMENAÇAR:
  deltes: { intimidació: 25, confiança: -15 }
  forma: subordinada                       # quina forma del fet demana
  plantilla: "…saber {subordinada}."
PREGUNTAR:
  deltes: {}
  obertura: "Vinc pel de la caixa…"        # només PREGUNTAR: frase sense palanca
```

- ⚑ **Una plantilla per intenció, no una llista de variants.** Correcte per al v0 (§6.2).
- ⚑ **No hi ha `modificadors_per_postura`** (§11). La postura només tria l'eix i escala
  la dificultat; no toca els deltes.

## `content/regles.yaml`

Tots els números del motor, fora del codi a posta. Detall de què fa cadascú a
[`03-motor.md`](03-motor.md). Claus: `postura_eix`, `dificultat_postura`, `degradació`,
`pes_vulnerable`, `pes_normal`, `refredament`, `terra_refredament`.

---

## Estat viu (el penja `motor/carrega.py`, no està als YAML)

```python
mon = { "fets":…, "npcs":…, "intencions":…, "regles":…,
        "obtinguts": { fet_id: {"de": npc_id, "via": eix} },   # les teues cartes
        "torns": 0 }

npc["desgast"] = { fet_id: n_usos }   # PER NPC (§3.3). Mai global.
npc["màxims"]  = dict(npc["estat"])   # fins on l'has portat mai -> terra del refredament
npc["tancat"]  = False
```

`obtinguts[fet]["via"]` **ja guarda per quin eix el vas traure**. No l'usa ningú encara:
és el ganxo on ha d'anar la fiabilitat variable de §2.2, que és el punt 2 del que el
projecte té de propi (§12).

---

## Convencions

- `fet_id` amb prefix `f_`. §14.3 demana prefix de capítol (`c1_…`) quan n'hi haja més d'un.
- `npc_id` en minúscules, sense accents.
- Intencions en MAJÚSCULES. Postures en MAJÚSCULES.
- Eixos: `intimidació`, `confiança`, `temptació` — amb accent, i són claus de diccionari.
