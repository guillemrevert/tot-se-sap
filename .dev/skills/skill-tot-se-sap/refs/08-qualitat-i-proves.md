# 08 — Qualitat i proves

**Estat actual: zero proves.** Cap fitxer de test, cap marc triat, cap comprovació
automàtica. El que s'ha verificat s'ha verificat a mà o amb scripts d'usar i tirar.

Açò no és un descuit menor: `docs/v0.md` §5 posa el validador de resolubilitat al **pas 3
de quatre**, i diu explícitament *«ja — no al final»*. Es va saltar.

---

## El validador de resolubilitat (§15) — espec

La peça que falta. Des de l'estat buit, verifica que el capítol **es pot acabar**. Amb 8
fets la cerca és trivial i el que dona a canvi és poder **tocar números sense por**.

Ha de comprovar tres coses:

1. **Cada fet és assolible.** El `sostre` d'un NPC pot tancar un fet per sempre: si demana
   `confiança 60` i l'únic que el sap té sostre 40, no s'obri mai — i el jugador ho
   descobrirà després de gastar mitja hora. La degradació de palanques ho agreuja.
   ⚠️ Ara mateix `sostre` no existix ([`07`](07-decisions-obertes.md) D1), o siga que
   este punt es comprova contra la **ruptura**, que fa de sostre de facto.
2. **El final és assolible, i per quines vies.** Si al culpable només se li pot arribar per
   intimidació, el jugador **només pot arribar al final fals** (§13.4). Això ha de ser una
   decisió, no un accident dels números.
3. **Es resol amb la pitjor reputació possible** (§14.4). Fora d'abast fins que hi haja
   reputació.

### Requisits que l'implementació ha de complir

- **Sobre el motor de veres**, cridant `nucli.aplica()`. Un validador que reimplemente les
  fórmules valida el validador, no el joc.
- **Punt fix per rondes**: amb les cartes que tens ara, quins fets nous cauen; repetir fins
  que no en caiga cap. Un fet obri palanques que obrin fets.
- **Optimista a posta**: cada fet s'avalua des de l'estat inicial de l'NPC amb totes les
  cartes disponibles. Si ni així s'arriba, segur que no s'arriba.
- ⚠️ **Una cerca voraç no basta.** Mesurat: tirar sempre la carta més forta topa a
  `intimidació 84` en Roc i no arriba mai a 85, tot i que **hi ha camí**
  ([`09`](09-auditoria-codi-vs-disseny.md)). Cal cerca exhaustiva amb dedupe sobre
  `(eix, màxim, desgast)`, i té estats de sobra per a fer-ho: ~6.500 en el pitjor cas.
- Ha de dir **quant li falta** quan una cosa no arriba, no només que no arriba.

### On va

Fitxer nou, executable a soles (`python validador.py`), fora de `motor/` — no és part del
joc. Que la seua eixida siga llegible a l'ull: és una eina d'ajust, no un test de CI.

---

## Política

1. **Tot canvi a `content/*.yaml` o a `content/regles.yaml` passa el validador.** Els
   números són contingut i es toquen sovint: eixe és exactament el motiu pel qual viuen fora
   del codi, i el motiu pel qual cal una xarxa.
2. **Tot canvi a `motor/nucli.py`** hauria de tindre una comprovació que falle abans i passe
   després. Encara no hi ha on posar-la.
3. **`sortida/` i `cli.py` es proven jugant.** No paga la pena automatitzar text que està
   lleig a posta i que es tirarà.

## Què no fer

- ❌ Muntar CI, cobertura o un marc de proves gran. El projecte té 460 línies.
- ❌ Provar `sortida/text.py` cadena a cadena: eixe text és provisional per definició.
- ❌ Escriure proves del motor **abans** de tancar D1 i D2 de [`07`](07-decisions-obertes.md).
  Provar un contracte que encara no s'ha ratificat és feina que es llança.

## Decidir: quin marc

`unittest` (a la biblioteca estàndard, zero dependències, encaixa amb *«zero dependències
que no facen falta»*) contra `pytest` (millors assercions, una dependència més). No està
decidit. Amb 460 línies, `unittest` sembla el que toca — però és una decisió, no un fet.
