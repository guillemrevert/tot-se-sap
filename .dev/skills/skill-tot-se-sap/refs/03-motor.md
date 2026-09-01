# 03 — El motor

`motor/nucli.py`. **L'única porta d'entrada és `aplica()`.** Tota la resta són consultes
sense efectes secundaris que `cli` usa per pintar.

```python
aplica(mon, npc_id, intencio_id, palanca_id) -> {deltes, oberts, ruptura, tancat}
```

---

## L'ordre importa

`aplica` fa exactament açò, en este ordre:

1. **NPC tancat?** → torna `{tancat: True}` i no passa res més. Un NPC tancat no gasta torn.
2. **Calcula deltes** = `previsió()` = `delta_de_la_intenció × pes_de_la_palanca`, arredonit.
3. **Aplica** els deltes als eixos, limitats a `[0, 100]`. Actualitza `màxims`.
4. **Degrada la palanca** contra este NPC (`desgast[fet] += 1`). Passe torn.
5. **Ruptura?** `intimidació >= npc["ruptura"]` → tancat per sempre i **torna ja**.
6. **Obri fets** — tots els de `sap` que ara complixen el llindar.
7. **Refreda** tots els NPCs.

⚠️ **Els passos 5 i 6 estan en este ordre i això té conseqüències.** Si una jugada et
posa per damunt de la ruptura, l'NPC es tanca **encara que la mateixa jugada haguera
passat el llindar d'un fet**. Passar-se't no és «arribes tard»: és que no arribes.
Conseqüència mesurada a [`09`](09-auditoria-codi-vs-disseny.md).

---

## Com es resol un fet

```
eix    = regles.postura_eix[ npc.sap[fet] ]                     # QUIN eix l'obri
llindar = round( fets[fet].dificultat × regles.dificultat_postura[postura] )
obert   ⟺ npc.estat[eix] >= llindar
```

La **postura** és tota la peça: el mateix fet, amb la mateixa `dificultat`, s'obri per
eixos distints segons per què calla cadascú (§2.3).

| Postura | Eix que l'obri | Lectura |
|---|---|---|
| `PROTEGEIX` | `confiança` | calla per protegir algú → no el pots forçar |
| `POR` | `intimidació` | calla per por → només cedix a pressió |
| `PROFIT` | `temptació` | calla perquè en trau → només pagant |
| `INDIFERENT` | `confiança` | no calla: és que li dona igual (§9.3) |

`INDIFERENT` porta a més `dificultat_postura: 0.4`. Això és el que fa que un fet de
dificultat 15 li caiga a Silvestre amb 6 de confiança — i com que comença amb 15, **cau
sol al primer torn**. Eixa és, de facto, la resposta a l'arrancada en fred de §16.3, i
no està escrita enlloc més ([`07`](07-decisions-obertes.md)).

## Quant val una carta

```
pes = (1.5 si el fet és de vulnerable_a, si no 1.0) × degradació[min(usos, 2)]
```

`degradació: [1.0, 0.5, 0.25]` — la tercera vegada encara val **un quart**, no zero.
És la regla 3: *degradació, mai crema total*. La UI ho pinta `●●● / ●●○ / ●○○` i mai
`○○○`, a posta.

⚠️ **El desgast és per NPC.** La mateixa carta val 100% contra el següent.

## Refredament

```
terra = round( màxims[eix] × terra_refredament )      # 0.4
estat[eix] = max( terra, estat[eix] − refredament[eix] )
```

`intimidació −5`, `temptació −3`, `confiança 0` per torn. La por es passa i una oferta
damunt la taula es refreda; la confiança guanyada no s'evapora sola.

Dues coses que se'n deriven i que no són òbvies:

- **Una jugada que moga menys de 5 d'intimidació no avança**: el refredament se la menja
  el mateix torn. Els incrementets menuts (una carta cremada, un `INSINUAR` fluix) són
  **neutres o negatius**, no «poc a poc».
- El terra recorda: si l'has portat a 80, ja no baixarà de 32 encara que passen 20 torns.

⚠️ `_refreda()` mou **tots** els NPCs cada torn, no només aquell amb qui parles. El
docstring ho defensa (*la causa és que has deixat de pressionar*), però és una lectura de
la regla 6 que no està al `docs/disseny.md`. Veure [`07`](07-decisions-obertes.md).

---

## Consultes (sense efectes)

| Funció | Per a què |
|---|---|
| `previsió(mon, npc, intenció, palanca)` | els deltes que faria la jugada. `cli` en pinta la **direcció**, mai la magnitud |
| `palanques(mon, npc)` | les cartes que tens amb el que valen contra este NPC |
| `pendents(mon, npc)` | què li falta a cada fet seu. **Només calibratge** (tecla `c`) |
| `eix_del_fet` / `llindar` / `pes` | les tres fórmules de dalt, soltes |

⚠️ `pendents()` diu al docstring *«el jugador no ha de veure això»*, però la regla 8 del
`CLAUDE.md` diu *«el jugador ha de poder saber quin llindar li falta»*. Contradicció viva:
[`07`](07-decisions-obertes.md).

---

## Trampes

- **`round()` de Python arredonix a parell** (*banker's rounding*): `round(12.5) == 12`
  i `round(7.5) == 8`. Els deltes reals no són els que et diu el cap: `CONFRONTAR` amb
  una carta vulnerable fresca fa **22**, no 23. Si algun dia els números canten, comença per ací.
- **`PREGUNTAR` amb palanca gasta la carta i no mou res.** És intencionat (§3.2:
  *«res — la gasta debades»*), però des de fora sembla un bug.
- **Un NPC tancat no consumix torn** ni refreda: `aplica` ix per la porta 1.
