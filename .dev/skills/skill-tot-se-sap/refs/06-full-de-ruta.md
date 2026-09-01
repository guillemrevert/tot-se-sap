# 06 — Full de ruta

Qui mana ací és `CLAUDE.md` («si dubtes si una cosa entra al v0: **no entra**») i
`docs/v0.md` §3. Este ref només diu **on estem**.

---

## v0 — validar si el bucle de conversa és divertit

Terminal pura. 3 NPCs, un cas de mentida, 8 fets. Text lleig a posta.

| | Estat |
|---|---|
| Esquema YAML + carregador | ✅ fet |
| Motor `(intenció, palanca)` → estat | ✅ fet |
| Postura per fet → quin eix l'obri | ✅ fet |
| Degradació de palanques per NPC | ✅ fet |
| `llindar_ruptura`: l'NPC es tanca | ✅ fet |
| Les 6 intencions, una plantilla cadascuna | ✅ fet |
| CLI: palanca → intenció, calibratge | ✅ fet |
| 3 NPCs amb postura distinta sobre el mateix fet | ✅ fet |
| 6-8 fets encadenats, cada fet premi i clau | ✅ fet (8) |
| **`alarma`** com a multiplicador de resistència | ❌ **no existix** |
| **Estat visible**: que el jugador sàpiga quin llindar li falta | ⚠️ només en mode calibratge |
| **Validador de resolubilitat** (§15) | ❌ **no existix** — `docs/v0.md` §5 el posava al pas 3, no al final |
| Provar-ho jugant mitja hora | ❌ pendent |

**Fora del v0, explícitament:** propagació (§16.5 — amb 3 NPCs tothom s'entera de tot),
reputació (és de campanya, §14.3), la confessió com a final (§13.2), gràfics, minijocs,
filtre d'estil, text lliure, múltiples variants de plantilla.

> El v0 contesta *«funciona el mecanisme?»*. **No** contesta *«és divertit?»* — això
> necessita el cas de veres (`docs/v0.md` §2).

---

## Després del v0 — per ordre de dependència, no de ganes

1. **Escriure el cas de veres** (§16.1). És el bloquejador roig: hi ha ~20 KB de sistema
   i zero cas. El que mata projectes així no és el codi.
2. **Fiabilitat variable segons la via** (§2.2). El ganxo ja hi és (`obtinguts[f]["via"]`).
   És el punt 2 del que este projecte té de propi (§12) i no costa quasi res.
3. **`sostre` per NPC** — hi ha gent que **mai** confiarà en tu. Tanca portes de veres,
   i és el que el validador de §15 ha de comprovar. Sense `sostre`, §15 no té què validar.
4. **Filtre d'estil procedural** (§4 capa 3) + `traços` per NPC.
5. **Variants de plantilla** — només les que canten després de jugar-hi (§6.3).
6. **La confessió com a final** (§13.2): `CONFRONTAR` amb `f_autoria` contra l'NPC més dur.
   No cal cap intenció nova. Amb porta explícita: *«estàs segur? açò tanca el cas»* (§13.3).
7. **Propagació** (§10.3) — necessita 5+ NPCs per dir res.
8. **Reputació entre capítols** (§14.3-14.6). Toca `resistència`, **mai** `sostre`.
9. **Text lliure per classificació** (§7), si algun dia. **Mai per generació.**

## Fora per sempre

- ❌ **Forçar panys** i minijocs en general: no generen palanques. Si cal entrar en un
  lloc, el problema ha de ser **social**.
- ❌ **Puntuar paraules soltes** del text lliure (§7): inverteix els incentius del jugador.
- ❌ **Retry / resetejar els NPCs** (§14.2): la partida 2 seria una guia.
- ❌ **Detindre ningú** (§13.1): si tens autoritat, les palanques són decoració.
