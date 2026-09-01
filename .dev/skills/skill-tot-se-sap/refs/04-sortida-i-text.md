# 04 — Sortida i text

`sortida/text.py`, 57 línies. **El motor no sap que este fitxer existix.**
Rep el `mon` i el `res` que li dona `cli` i torna cadenes.

---

## La frase del jugador

```
plantilla_de_la_intenció.format( forma_demanada = fet[forma_demanada] )  ->  concorda()
```

Cada intenció declara `forma: subordinada | nominal` i la plantilla usa eixa clau.
Sis intencions × N fets amb una plantilla escrita cadascuna: el contingut creix **lineal**.

**El text del jugador no canvia segons l'NPC** (§5). El detectiu parla igual davant d'un
xiquet i d'un sicari; el que canvia és **si li funciona**. Si algun dia veus una plantilla
amb un `if npc`, això s'ha trencat.

### `concorda(s)`

Apedaç de concordança, no un motor morfològic: contraccions (`de el → del`,
`a els → als`, `per el → pel`…) i apostrofació davant de vocal (`de a… → d'a…`).

Viu **ací i no al motor**, i té frontera clara: el que no arregle `concorda` s'arregla
**escrivint millor la forma al fet**, no afegint-hi regles. §4 ja avisa que la concordança
és fàcil si es pensa des del principi i dolorosa si no.

## La resposta de l'NPC

```
to(npc):  intimidació ≥ 60 -> "pressionat"
          temptació   ≥ 50 -> "interessat"
          confiança   ≥ 50 -> "obert"
          si no             -> "sec"
```

Es tria en eixe ordre: **la pressió tapa la resta**. Un NPC intimidat i alhora temptat
sona a intimidat.

`respostes[to]` és una llista i es recorre en cua circular per `(npc_id, to)` — la
repetició immediata és el que fa que un sistema procedural es note com un sistema (§5).
La cua viu en un dict de mòdul (`_cua`), o siga **global i no es reinicia**: si algun dia
hi ha partida nova sense reiniciar el procés, s'ha de netejar.

`ruptura` és una cadena i no una llista: es diu una vegada i s'acabà.

## `direcció(deltes)`

Torna `"puja intimidació · fon confiança"`. **Direcció, mai magnitud.** El jugador ha de
saber cap on empeny, no fer comptes. Els números crus només ixen amb la tecla `c`.

---

## El que NO hi ha

- ❌ **El filtre d'estil de §4/capa 3** — quequeig, pauses, frases tallades generades
  proceduralment sobre qualsevol frase. `to()` és un esbós de tres línies del que ha de
  ser eixa capa. És v1.
- ❌ **Traços per NPC** (registre, verbositat, mania). Ara mateix la veu de cada NPC viu
  sencera en les seues línies escrites a mà — que és exactament l'explosió combinatòria
  que §5 vol evitar quan hi haja 15 NPCs.
- ❌ **Variants de plantilla per rang d'estat.** Una sola variant per intenció (§6.2):
  amenaçar a `intimidació 10` i a `70` diuen literalment el mateix. Es notarà jugant, i
  eixe és el moment d'escriure variants — no abans.
