# 05 — Contingut: el `cas_prova`

> ⚠️ **Açò és bastida i es tira.** El cas de veres (§16.1) no s'escriu ací. Este contingut
> existix per a provar el **mecanisme**, no per a ser divertit: una cosa robada, no un mort.
> Està marcat `cas_prova` als YAML perquè d'ací dos mesos no es confonga amb el bo.

---

## La veritat

Roc, el taverner, deu diners fora del poble. Neus, que porta els comptes de la
cooperativa, es deixa la clau penjada darrere de la barra quan baixa a fer el vermut.
Roc va agafar la caixa. Neus ho sospita i calla **perquè li deu un favor**. Silvestre,
el pastor, va veure llum aquella nit i **no li dona cap importància**.

Es va escriure en l'ordre que mana §16.1: primer la veritat, després *qui podia veure
cada tros*.

## El triangle

La peça que el `cas_prova` ha de provar és §2.3: **el mateix fet, tres motius distints per
callar**. `f_clau_penjada` el saben els tres —

| Qui | Postura | Eix que l'obri |
|---|---|---|
| Silvestre | `PROFIT` — en vol traure algo | `temptació` |
| Neus | `PROTEGEIX` — tapa Roc | `confiança` |
| Roc | `POR` — l'assenyala a ell | `intimidació` |

Si jugant no es nota que són tres murs diferents, els eixos són decoració i el disseny
està trencat. **És l'única pregunta que este contingut ha de contestar.**

## El graf

Llindar = `dificultat × multiplicador de postura` (`INDIFERENT` × 0.4). Els números
concrets els mana `content/regles.yaml`; ací està la forma.

| Fet | Dif. | Silvestre (rupt. 70) | Neus (rupt. 85) | Roc (rupt. 90) |
|---|---|---|---|---|
| `f_caixa_no_forcada` | 10 | — | INDIF · conf **4** | — |
| `f_llum_cooperativa` | 15 | INDIF · conf **6** | — | — |
| `f_roc_va_pagar` | 20 | INDIF · conf **8** | — | — |
| `f_neus_te_clau` | 30 | — | POR · intim **30** | — |
| `f_roc_deu_diners` | 40 | — | — | POR · intim **40** |
| `f_clau_penjada` | 50 | PROFIT · temp **50** | PROTEG · conf **50** | POR · intim **50** |
| `f_neus_deu_favor` | 55 | — | PROTEG · conf **55** | PROFIT · temp **55** |
| `f_autoria` | 85 | — | — | POR · intim **85** |

Estat inicial: Silvestre `conf 15`, Neus `conf 20`, Roc `conf 5`. Tots els altres eixos a 0.

**Arrancada en fred:** els tres fets `INDIFERENT` tenen el llindar per davall de la
confiança inicial, o siga que **cauen sols a la primera jugada** amb eixe NPC. Això
desencalla el torn 1 de §16.3 sense cap mecanisme nou… i sense que ningú ho haja decidit
per escrit ([`07`](07-decisions-obertes.md)).

**Cartes que fan mal** (`vulnerable_a`, pes ×1.5): Silvestre **cap** · Neus tres · Roc quatre.
Que Silvestre no en tinga cap el fa un mur pla: contra ell totes les cartes valen igual.

⚠️ `f_autoria` demana `intimidació 85` i Roc trenca a `90`. **Finestra de cinc punts.**
Conseqüències mesurades a [`09`](09-auditoria-codi-vs-disseny.md) — és la troballa gran.

---

## Escriure un fet

Cada fet ha de ser **premi i clau** (§16.1). Un fet que només és premi és un cul-de-sac;
un que només és clau te l'has de regalar. Amb 8 fets no escrius una trama: escrius un
**graf** on cada node obri el següent, i la trama és el que el justifica.

Per fet real s'escriu: `nu` + `subordinada` + `nominal` + `dificultat` + una entrada a
`sap` per cada NPC que el sàpiga (amb postura) + possiblement `vulnerable_a`. §4 diu
*«240 frases escrivint-ne 46»*; és optimista, però **el creixement seguix sent lineal**,
que és l'únic que importa (§8).

## Escriure un NPC

Les quatre llistes de `respostes` (`sec` / `obert` / `interessat` / `pressionat`) més la
de `ruptura`. Dues línies per to basten al v0 — només serveixen per a que la cua
anti-repetició tinga on triar.

Un NPC nou obliga a decidir la seua postura sobre **cada fet que sàpiga**. Eixe és el cost
real d'afegir gent, no les línies de diàleg.
