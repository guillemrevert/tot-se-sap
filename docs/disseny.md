# Joc d'interrogatoris — notes de disseny

Vista cenital, estil súper antic. El nucli del joc no és el moviment: és **arrancar informació als NPCs**.

---

## 1. Idea central

El jugador vol un fet que un NPC té. L'NPC no el diu de gratis. Cada fet està tancat darrere d'un llindar sobre un o més eixos d'estat, i el jugador els mou amb el que diu.

**Eixos inicials:** `intimidació`, `confiança`, `temptació`.

Cada NPC té el seu propi vector d'estat, que evoluciona durant la conversa.

---

## 2. Regles de disseny que sostenen tot

### 2.1 Els eixos han d'entrar en conflicte

Si insistir sempre puja intimidació, el camí òptim és espamejar el mateix botó i no hi ha joc.

- Intimidar puja `intimidació` però **fon** `confiança`.
- Hi ha fets que només s'obrin amb `confiança` alta → no els pots aconseguir per la força.
- Passar-se de rosca (intimidació molt alta) → l'NPC es tanca, fuig o crida els guàrdies. **Estat terminal.**

La tensió entre eixos és el que converteix això en un joc i no en una màquina expenedora.

### 2.2 La informació té fiabilitat variable segons com l'has obtinguda

| Via | Què obtens |
|---|---|
| Intimidació alta | Et diu **el que vols sentir**. Pot ser fals. |
| Confiança alta | Et diu **la veritat**. |
| Temptació alta | Et diu la veritat, però **et demana algo a canvi**. |

Un mateix fet, tres valors de veritat. Rejugabilitat i profunditat narrativa sense escriure més contingut.

### 2.3 Cada NPC té una POSTURA sobre cada fet

No tots callen pel mateix motiu: un **protegeix** algú, un altre té **por**, un altre en **trau profit**, un altre simplement **no li importes**.

La postura determina quin eix funciona amb ell. Sense això, tots els NPCs són el mateix mur amb noms distints. **És la peça que dona joc real al sistema d'eixos.**

---

## 3. Arquitectura del diàleg: INTENCIÓ + PALANCA

Tota frase que el jugador puga dir es descompon en dues coses:

- **Intenció** — què li fas a l'NPC (`AMENAÇAR`, `OFERIR`, `EMPATITZAR`, `CONFRONTAR`, `INSINUAR`, `PREGUNTAR`). Determina **quins eixos mous i en quina direcció**.
- **Palanca** — amb què. El contingut concret (la filla, el deute del taverner, el magatzem els dimarts). Determina **quant** mous, i si dispara reaccions especials.

> **El motor només treballa amb el parell `(intenció, palanca)`. Mai toca text.**
> Gates, deltes, fets que s'obrin: tot opera sobre el parell.

### 3.1 Les palanques SÓN els fets ja extrets

No pots amenaçar amb la filla fins que algú t'ha dit que en té una.

**La informació que arranques a un NPC és la munició per arrancar-li informació a un altre.** El recurs que busques és el mateix que gastes. Això tanca el bucle del joc sobre si mateix — i en un joc que va d'extraure informació, és exactament el centre.

Referents que fan això bé: *The Case of the Golden Idol*, *Return of the Obra Dinn*.

### 3.2 Exemple — una palanca, sis usos

Palanca: `fet_magatzem_dimarts` ("entres al magatzem els dimarts a la nit")

| Intenció | Frase generada | Efecte |
|---|---|---|
| AMENAÇAR | "Al teu cap li interessaria saber què fas al magatzem els dimarts." | `intim +25 · conf −15` |
| OFERIR | "Jo no he vist res del magatzem. La meua memòria millora si tu m'ajudes." | `temp +20 · intim +5` |
| EMPATITZAR | "Sé el del magatzem. També sé que amb el que et paguen no arribes a fi de mes." | `conf +20 · intim +5` |
| CONFRONTAR | "Dius que els dimarts estàs a casa. Jo et vaig veure entrar al magatzem." | `conf −10 · intim +15` + obri fets |
| INSINUAR | "Els dimarts són dies estranys per als magatzems, no trobes?" | `intim +8` — barat, sonda sense cremar la carta |
| PREGUNTAR | "Què fas al magatzem els dimarts?" | res — la gasta debades |

INSINUAR vs CONFRONTAR és una decisió real: **confrontar en fals** (sense la prova) et fa quedar com un idiota i et penalitza confiança per a la resta de la partida.

### 3.3 Economia de decisió: el cost va a la PALANCA, no a la intenció

> **Regla: una sola decisió que faça mal per torn.**

- **La palanca és escassa.** Es degrada amb l'ús *contra aquell NPC concret*: primera vegada val 100%, segona 50%, tercera ja res. La decisió de pes és **quina carta gastes ací i quina et guardes per al que serà més dur**.
- **La intenció NO costa res.** Pots amenaçar les vegades que vulgues. Només decideix quin eix mous. Triar-la és ràpid i intuïtiu ("a aquest li falta confiança → EMPATITZAR"), sense càlcul.

Resultat: **un clic pensat + un clic ràpid.** El ritme s'aguanta.

⚠️ Si les intencions **també** foren limitades (X usos d'intimidació per cas), tindries dos recursos escassos gastant-se en la mateixa acció i el jugador no pot raonar bé sobre cap dels dos. *Interrogation* fa això i és la queixa recurrent dels jugadors.

⚠️ **Degradació, no crema total.** Si la palanca desapareix del tot, el jugador pot quedar-se encallat sense sortida. Que perda l'efecte sorpresa, no la partida.

### 3.4 Ordre d'entrada a la UI: palanca → intenció

Si el jugador ha de considerar 6 intencions × 12 palanques abans de cada línia, la conversa deixa de ser una conversa i passa a ser un full de càlcul. **El ritme és fràgil** — i el referent més pròxim (*Interrogation*) va ràpid precisament perquè cada torn és un sol clic.

Solució: **primer la palanca** (ja saps de què vols parlar), i llavors apareixen **només les 3-4 intencions que tenen sentit amb ella**. No tota palanca admet tota intenció — no pots empatitzar amb una cosa que no li fa mal. Espai de decisió llegible sense perdre la sensació d'autoria.

### 3.5 L'estat és MONEDA, no només feedback

Diferència clau amb els referents: allí els indicadors són **feedback** (veus l'NPC posar-se nerviós i infereixes si vas bé). Ací els eixos són una **moneda que gastes per obrir panys**.

És més interessant, però **més exigent d'UX**: has de deixar claríssim quin llindar li falta al jugador. Si no, li passa el d'*Interrogation* — falla i no entén per què.

---

## 4. Generació de text: 3 capes independents

Cada capa s'escriu **una sola vegada** i es multipliquen entre elles. Això és el que fa el projecte acabable.

```
FET (text nu)  →  PLANTILLA D'INTENCIÓ  →  FILTRE D'ESTIL  →  sortida
```

### Capa 1 — Fets

Text nu, escrit una vegada: `"entres al magatzem els dimarts"`.

### Capa 2 — Plantilles per intenció

```
AMENAÇAR   → "Al teu cap li interessaria saber que {X}."
EMPATITZAR → "Sé que {X}. També sé que no et paguen prou."
CONFRONTAR → "Dius que no. Jo sé que {X}."
```

6 intencions × 40 palanques = **240 frases escrivint-ne 46**.

⚠️ **Concordança gramatical** — en català/castellà no és trivial. `"parlem de" + "entres al magatzem"` → *"parlem de entres al magatzem"*. Solució: guardar cada palanca en **2-3 formes** (subordinada, nominal, ...) i que la plantilla demane la que necessita. Fàcil si es pensa des del principi, dolorós si no.

### Capa 3 — Filtre d'estil (procedural)

Transforma la resposta de l'NPC segons el seu estat: quequeig, pauses, frases tallades, desesperació si la intimidació és alta; respostes més llargues i obertes si hi ha confiança.

**El quequeig es genera proceduralment sobre qualsevol frase** — no s'escriu a mà per cada línia.

---

## 5. Variants de plantilla

Cada intenció acaba sent una **llista** de variants, no una cadena. Però la selecció no és aleatòria:

- **Per estat** — amenaçar a `intimidació 10` no és el mateix que a `70`. La primera és una insinuació educada, la segona és brutal. Etiquetar cada variant amb el rang on encaixa. Això **comunica al jugador que la situació ha escalat**.
- **Per personatge (PJ)** — les 6 maneres d'amenaçar defineixen la veu del protagonista. Si són intercanviables, el personatge no existeix.
- **Cua anti-repetició** — la repetició immediata és el que fa que un sistema procedural es note com un sistema.

### El text del JUGADOR no canvia segons l'NPC

Si el PJ parla diferent davant de cadascú, no és un personatge: és un camaleó.

**El que canvia és si li funciona.** Amenaçar un xiquet i amenaçar un sicari és la mateixa frase amb resultats oposats. Més interessant que canviar-li el text.

### El text de l'NPC sí que ha de sonar a ell

Però **no escrivint variants per personatge** (torna l'explosió combinatòria). Donar-li **2-3 traços** i que el filtre d'estil els aplique: registre (culte/vulgar), verbositat, potser una mania verbal.

---

## 6. Ordre de treball

1. **Prototip en text pur.** Terminal, sense gràfics, sense joc. 3 NPCs, un misteri xicotet, ~15 fets.
   - Si això és divertit en text lleig → hi ha joc de veres.
   - Si no ho és → els gràfics cenitals no ho salvaran, i t'has estalviat mesos.
2. **Una sola variant per intenció** al principi. Muntar el motor sencer i jugar-hi.
3. Després de mitja hora de joc real ja se sap quines frases canten → **escriure variants només on fan falta**. Escriure variació abans de saber què es repeteix és feina llançada, i et menja les ganes just quan encara no tens res jugable.

---

## 7. Text lliure (v2, opcional)

El banc de paraules composable ja dona el ~90% de la sensació d'autoria.

Si algun dia es vol text lliure de veres, **la via NO és generar amb un LLM** (car) sinó **classificar-hi l'entrada**:

> *"Seria una llàstima que el teu cap s'assabentara del que passa al magatzem els dimarts."*
> → `intenció: AMENAÇAR` + `palanca: fet_magatzem_dimarts`

Exactament el mateix parell que hauria produït clicant al banc de paraules. **El motor no canvia ni una línia.** Classificar val una fracció de generar.

### Per què NO puntuar paraules soltes

Inverteix els incentius del jugador:
- *"si no em dius on és, el teu xiquet dormirà al riu"* → brutal, però cap paraula de la llista → **neutre**.
- *"et mataré"* → `+30` perquè conté "matar".
- Negacions: *"no et vull fer mal"* conté "fer mal".

El jugador aprén als cinc minuts que **escriure bé el castiga**. Descartat.

---

## 8. Riscos reals

- ⚠️ **El coll d'ampolla no és el codi, és el contingut.** Els indies no moren per problemes tècnics, moren perquè algú es cansa d'escriure el fet número 200. Tota l'arquitectura d'ací va orientada a que el contingut cresca **lineal i no exponencial**.
- ⚠️ **La complexitat d'un joc així no és estructural, és de disseny.** Que el jugador entenga *per què* l'NPC s'ha tancat. Que sàpiga que li han mentit. Que el conjunt de fets forme un **puzle resoluble**. Això no es resol amb bona arquitectura: es resol iterant i fent que gent el jugue.

---

## 9. Premissa i món

### 9.1 Ets un DETECTIU PRIVAT (decisió tancada)

No és ambientació, és **el que justifica tot el sistema**.

Un policia intimida perquè porta placa: la pressió li ve de fora. Un detectiu privat **no té res excepte el que sap**. Això converteix la informació en l'única moneda que hi ha, i el bucle de palanques deixa de ser una mecànica enganxada per ser la conseqüència lògica de qui eres.

Efecte secundari: **ningú es fia de tu**. Fins i tot arrancar informació bàsica al més innocent costa. Perfecte.

### 9.2 Poble de muntanya, ~200 habitants

Triar poble **és triar el sistema de propagació** (§10). No se'n pot fugir: si intimides el taverner i mitja hora després la seua cunyada et rep com si res, el jugador nota que el món és fals. La proximitat és tota la gràcia de l'escenari i també la seua exigència.

### 9.3 ALARMA: qui es creu irrellevant és inintimidable

**Una de les millors mecàniques del disseny.** No és un tret fix, és un **estat que canvia mentre parles**:

- NPC relaxat → **parla molt**, però no el pots pressionar (li dona igual, no es creu implicat).
- NPC alarmat → **es tanca**, però ara sí que el pots pressionar.

Implicació forta: **preguntar té un cost.** Cada cosa que preguntes li diu al tio què estàs buscant. No hi ha exploració gratuïta.

### 9.4 Abast: què entra i què no

**Entra** (alimenta el nucli o el ritme):
- Registrar habitacions → **genera palanques**
- Oficina amb missatges que arriben
- Informe forense **amb retard** → et força a seguir movent-te mentre esperes

**Fora:**
- ❌ **Forçar panys.** El minijoc més fet de la història i no toca el nucli: no genera palanques. Si cal entrar en un lloc, que el problema siga **social** — aconseguir que algú et done la clau.
- ❌ **Món caminable lliure (de moment).** Un poble amb navegació lliure són desenes d'hores d'art i col·lisions per una cosa que et dona un **mapa de nodes clicables**: 90% de la sensació pel 5% del treball. Si funciona amb nodes, ja caminaràs després.

---

## 10. Accions d'NPC i propagació

### 10.1 Els NPC no només parlen: ACTUEN

Avisar algú, amagar una prova, marxar del poble, mentir-li a un altre sobre tu.

Amb això deixes de tindre una porta que s'obri o no i passes a tindre **algú que juga contra tu**. I resol el problema del punt 3.5: quan et passes de rosca no veus un número roig — **arribes a sa casa i ja no hi és**. La conseqüència es fa visible sense explicar-la.

### 10.2 Regla d'or: el món NO es mou tot sol

> **Tota acció d'NPC ha de tindre una causa traçable fins a una acció del jugador.**

Si t'enxampes escrivint un NPC que fa alguna cosa "perquè sí", has trencat la regla. Això no és una limitació tècnica: és el que permet al jugador **raonar** sobre el que passa, perquè tot el que passa porta la seua empremta.

### 10.3 Propagació: 1-2 salts i s'acaba

Si l'NPC només reacciona quan li parles **a ell**, no hi ha xarxa — cada NPC segueix sent una sala aïllada amb decorat de muntanya.

El que fa que el poble existisca és que **la cunyada reaccione en assabentar-se'n**, encara que tu no li hages dit res. Segueix complint §10.2: la cadena arranca en tu, només que amb un salt més.

- Xarxa xicoteta de **qui parla amb qui** + retard. La cunyada del taverner s'assabenta; el pastor apartat, no.
- Valor de **reputació** al poble que es mou amb el que fas.
- **Límit dur: 1-2 salts.** Prou per sentir que corre la veu, prou poc per poder-ho depurar.

⚠️ La propagació **és** una acció d'NPC, no un sistema a banda. Un tio espantat no és que "s'ho guarde": és que **corre a avisar** algú.

### 10.4 Excepció: el culpable

Si literalment ningú es mou sense tu, el culpable és un moble esperant que el trobes.

Se li dona **una sola acció**: si t'acostes massa, actua — destrueix la prova, fa marxar algú, prepara una coartada.

**No és un sistema, és un guió.** Però eixa única acció converteix el cas en una cursa i et dona el final.

---

## 11. Esquelet de dades (esbós, a concretar)

```
Fet:
  id
  formes: { subordinada, nominal, ... }   # concordança
  gates: { intimidació: N, confiança: N, temptació: N }
  fiabilitat_per_via: { intim: fals|distorsionat, conf: cert, temp: cert+preu }
  intencions_vàlides: [ ... ]             # no tota palanca admet tota intenció

NPC:
  # --- capa 1: TRETS FIXOS (defineixen la persona) ---
  resistència: { eix → quant costa moure'l }
  sostre:      { eix → màxim assolible }   # ⚠️ hi ha gent que MAI confiarà en tu,
                                           # facen el que facen. Més interessant que
                                           # la resistència: tanca portes de veres.
  reactivitat: AGUANTA | S_ENFADA | MENT   # ← el tercer és el bo
  vulnerabilitat: tema_id                  # què li fa mal
  traços: { registre, verbositat, mania }  # per al filtre d'estil

  # --- capa 2: ESTAT VIU (canvia durant la partida) ---
  estat: { intimidació, confiança, temptació }
  alarma                                   # com d'implicat es creu (§9.3)
  ha_sentit_de_tu: [ ... ]                 # el que li ha arribat per la xarxa

  # --- capa 3: PER FET ---
  postura_per_fet: { fet_id → PROTEGEIX | POR | PROFIT | INDIFERENT }
  desgast_palanques: { fet_id → n_usos }   # ⚠️ la degradació és PER NPC, no global

  llindar_ruptura                          # es tanca / fuig / avisa algú
  accions_disponibles: [ AVISAR(qui) | AMAGAR_PROVA | MARXAR | MENTIR_SOBRE_TU ]

Intenció:
  deltes_base: { eix → valor }
  plantilles: [ { text, rang_estat, forma_requerida } ]
  modificadors_per_postura

Xarxa social:
  arestes: { npc_a → [npc_b, ...] }        # qui parla amb qui
  retard_per_aresta
  max_salts: 2                             # límit dur (§10.3)

Món:
  reputació_poble
  cues: [ { esdeveniment, torns_restants } ]  # forense, missatges a l'oficina
```

---

## 12. Estat de l'art — què existeix ja i què no

Les peces existeixen per separat. **Cap referent uneix les tres.**

| Joc | Què té | Què li falta |
|---|---|---|
| ***Interrogation: You Will Be Deceived*** (Critique Gaming, 2019) | Eixos (ritme cardíac = por, monitor de confiança). Empatia / intimidació / engany segons la persona. La informació d'un sospitós desbloqueja opcions amb un altre (text en groc). | Opcions **fixes**: el *què* i el *com* venen soldats en un sol clic. No compons res. |
| ***We Should Talk*** (2020) | Frase modular: cicles per fragments per construir-la. Matisos reals de to. | Cap sistema d'estat ni economia d'informació. |
| ***Golden Idol*** / ***Obra Dinn*** | Banc de paraules que **guanyes** com a prova. | No és conversa: és deducció final. |

### El que queda nostre

1. **Composar la frase amb els fets robats** i que això moga eixos → ningú ho fa junt.
2. **Fiabilitat variable segons l'eix** usat per obtindre-la.
3. **Capa d'estil procedural** sobre la resposta de l'NPC.
4. **Detectiu privat sense placa** → la informació és l'única moneda (§9.1).
5. **Alarma inversa**: qui es creu irrellevant parla però és inintimidable (§9.3).
6. **NPCs que actuen i es passen la veu**, no sales aïllades (§10).

### Deures abans de programar

**Jugar-se *Interrogation*** (5-6 h, sovint en oferta forta a Steam). No per copiar-lo: per veure on falla. La crítica recurrent és que **quan falles no saps per què** — i això és exactament el risc de disseny del punt 3.5. Tens l'error documentat de gratis en un joc de 2019.

---
---

# Part II — decisions de sessió (31-08-2026)

Les seccions 1-12 són les notes originals i no s'han tocat. El que ve ara són decisions preses charrant sobre elles. **El que encara és proposta i no decisió està marcat com a tal.**

---

## 13. Final del capítol

### 13.1 Tu no detens ningú

§9.1 diu que no portes placa. Si pots detindre, tens autoritat, i tot el sistema de palanques passa a ser decoració.

El que sí que pots fer és **convèncer algú que ho faça** — el caporal, el jutge de pau. Això és bo perquè converteix el final en *una interrogació més*: el de la placa tampoc et creu de gratis, també té resistència, sostre i postura. La moneda no canvia, només l'interlocutor.

**Fora del v0.** És un NPC i un cas d'ús més.

### 13.2 El final és la CONFESSIÓ

Descartat com a mecànica del v0: acusar presentant proves (seleccionar sospitós + conjunt de fets + validar-los contra una solució). És un **segon sistema**, de deducció, enganxat al motor de conversa.

La confessió no és res nou: és **la conversa més difícil de la partida**, contra l'NPC amb més resistència i els sostres més baixos. Tot el joc passa a ser entrenament per a eixa porta.

> **L'acusació no necessita una intenció nova.** És `CONFRONTAR` amb el fet de l'autoria. La llista de sis intencions es queda tancada.

### 13.3 No saps si has encertat fins que s'acaba

*Obra Dinn* i *Golden Idol* et confirmen quan encertes. Ací **no es confirma res** fins que es tanca el capítol. Això és el que manté viva la pregunta que sosté tot §2.2 — *i si m'han mentit?*.

⚠️ Com que no hi ha marxa arrere, l'acusació ha de tindre una **porta explícita**: *"estàs segur? això tanca el cas"*. No per amabilitat — perquè el jugador ha de sentir que ha **triat** el final, no que ha punxat on no tocava.

### 13.4 Veredicte binari, tenyit per la via

El resultat és `completat` / `no completat`. El que el tenyix és **com** hi has arribat, i això ix de §2.2 sense escriure sistema:

| Via | Resultat |
|---|---|
| Home correcte, per **confiança** | Net. |
| Home correcte, per **intimidació** | El tens, però la confessió no val res. Formalment completat, i saps que has fet una porqueria. |
| Home correcte, per **temptació** | El tens perquè li has pagat algo. |
| Home equivocat | No completat. I el de veres continua al poble. |

Quatre línies d'epíleg, no un sistema.

### 13.5 Acusar en fals ha de fer mal

Sense penalització, l'estratègia òptima és provar totes les palanques contra tots fins que algú s'esfondre. §3.2 ja té el precedent (*confrontar en fals et penalitza per a la resta de la partida*): acusar qui no toca tanca eixe NPC per sempre i la xarxa ho propaga.

### 13.6 D'on ix `fet_autoria` — opció A al v0

- **A — algú el sap.** En un poble de 200 sempre hi ha un testimoni acollonit. L'autoria és un fet normal amb un gate molt alt. El motor no canvia gens. ✅ **v0**
- **B — no el té ningú, es composa** de dos o tres fets que junts només apunten a un lloc. És deducció de veres, però necessita un sistema per combinar fets.

A i B no són arquitectures distintes: en els dos casos `fet_autoria` és un fet com qualsevol altre i l'única diferència és **què l'obri**. Si algun dia cal B, és afegir `requereix: [fet_ids]` a la fitxa del fet. No és un rewrite.

El testimoni acollonit de l'opció A és, a més, el candidat perfecte per a l'alarma inversa de §9.3: parla molt mentre es creu irrellevant, i es tanca just quan t'acostes.

---

## 14. Estructura de campanya

### 14.1 Antologia — el prota canvia de localització

Cada capítol: poble nou, gent nova, fets nous. Resol el problema de contingut de §8 — no mantens una teranyina de 200 persones que creix per sempre, sinó que en tanques una de ~15 fets i la cremes.

### 14.2 No hi ha retry

Descartat: conservar els fets i resetejar els NPCs. Si els NPCs obliden, comences la segona volta amb totes les palanques al 100% contra gent amb confiança neutra, alarma a zero i el desgast per NPC esborrat — i la decisió de "quina carta creme ací" (§3.3) desapareix. La partida 2 és una guia.

I un NPC que no recorda que ahir el vas amenaçar és exactament *"la cunyada que et rep com si res"* que §9.2 assenyala com la cosa que fa que el món se sent fals.

Com que te'n vas del poble, **no pots tornar a arreglar-ho**. L'home equivocat es queda tancat. No cal cap sistema de retry perquè no hi ha retry: hi ha una cicatriu que et segueix tres pobles més enllà.

### 14.3 Els fets moren amb el poble; la reputació viatja

> **Fets: per capítol. Reputació: per campanya.**

Els fets moren amb el poble perquè **la gent mor amb el poble** — un fet és una palanca contra algú concret, i eixe algú ja no hi és.

La reputació no, perquè **el que viatja eres tu**. Encaixa amb §9.1 millor que res: un detectiu sense placa no té res excepte el que sap i **el que han sentit d'ell**. La reputació *és* la placa que no tens. Arribes al poble següent i algú et diu *"tu eres el que va acusar el forner d'Ares, no?"* — i eixa frase és tot el sistema de continuïtat que cal.

Un grapat de flags creuant capítols, no un graf de fets.

⚠️ Els ids dels fets són **globals** igual (`c1_magatzem_dimarts`). No per arrossegar-los entre capítols, sinó perquè costa zero i estalvia confusions al depurar i als guardats.

### 14.4 La reputació NO pot ser determinant

> **La reputació toca `resistència`, mai `sostre`.**

Que et coste més obrir la gent, sí. Que tanque portes de veres, no. El `sostre` és el que fa una cosa impossible, i una cosa impossible per una decisió presa fa tres hores — quan encara no podies saber què implicava — és el tipus de càstig que fa que la gent tanque el joc.

Segona barrera, automàtica: **cada capítol ha de ser resoluble amb la pitjor reputació possible** (§15).

La reputació ha de ser una cosa que **notes**, no una cosa contra la qual lluites. Algú que et rep més sec, un que et diu a la cara el que ha sentit, qui s'obri primer i qui l'últim. Textura i memòria, no un mur.

### 14.5 La reputació ha de ser llegible a l'arribada

Si al poble 3 tothom està tancat i no saps per què, és el fallo d'*Interrogation* de §3.5 una altra vegada. Que algú t'ho diga a la cara el primer minut: la fallada del capítol 1 s'ha de poder **veure**.

### 14.6 💡 Proposta (v1) — la reputació no és un número

Dos reputacions distintes amb efectes oposats:

- **"Va acusar un innocent"** → no et creuen. Costa més obrir res.
- **"Trau confessions a base de por"** → et **tenen por**. I per §2.2, qui et té por **et diu el que vols sentir**.

O siga: anar a base d'hòsties al capítol 1 fa que al capítol 3 tot el que t'arribe estiga enverinat *abans de començar*. La brutalitat no et penalitza amb un modificador: et degrada la **qualitat de la informació** durant tota la campanya.

Ix sola d'una regla que ja hi ha escrita. **No tocar al v0.**

---

## 15. Validador de resolubilitat

Script que, des de l'estat buit, verifica que el capítol es pot acabar. Es fa **abans del primer NPC**, no després: amb ~15 fets la cerca és trivial i et deixa tocar números sense por.

Ha de comprovar:

1. **Cada fet és assolible.** El `sostre` (§11) pot tancar un fet per sempre: si demana `confiança 60` i l'únic NPC que el té té sostre 40, no s'obri mai — i el jugador ho descobrirà després de gastar mitja hora. La degradació de palanques ho agreuja.
2. **El final és assolible**, i per quines vies. Si el culpable té el sostre de confiança per davall del gate de la confessió i només queda la intimidació, el jugador **només pot arribar al final fals** (§13.4). Això ha de ser una decisió, no un accident dels números.
3. **Es resol amb la pitjor reputació possible** (§14.4).

---

## 16. Qüestions obertes

### 16.1 🔴 La història — bloqueja la resta

Hi ha ~20 KB de sistema i zero cas. §8 ja avisa que el que mata projectes així no és el codi: escriure el cas **és** la feina, no la preparació per a la feina.

Però ací el cas no s'escriu com un misteri normal, perquè el disseny li imposa una forma:

> **Cada fet ha de ser alhora premi i clau.**

Un fet que només és premi és un cul-de-sac. Un fet que només és clau te l'has de regalar. Amb ~15 fets no estàs escrivint una trama: estàs escrivint un **graf** on cada node obri el següent, i la trama és el que el justifica. Un misteri de novel·la no compleix això per defecte — allí la informació apareix perquè el detectiu pregunta.

Mètode: escriu primer **la veritat** (què va passar, qui, per què), i després pregunta't **qui podia veure cada tros**. L'A/B de §13.6 ix sol.

### 16.2 INSINUAR gratis es menja l'economia de §3.3

§3.2 diu literalment *"barat, sonda sense cremar la carta"*. Si INSINUAR no degrada la palanca, l'estratègia òptima és **insinuar-ho tot contra tots per escanejar l'espai**, llegir les reaccions i només després comprometre's. El jugador arriba a cada decisió amb informació perfecta i gratuïta, i adéu a "una sola decisió que faça mal per torn".

💡 **Proposta:** sondar costa **alarma** (§9.3). Queda un model de tres costos:

| | Cost |
|---|---|
| **Palanca** | Material — es degrada, per NPC |
| **Alarma** | Informacional — li dius què busques |
| **Intenció** | Gratis |

### 16.3 L'arrancada en fred

Torn 1: zero fets, o siga zero palanques. L'única cosa possible és PREGUNTAR, que a §3.2 val *"res, la gasta debades"*. Com obtens el primer fet no està escrit enlloc — i són els primers cinc minuts de joc, que és on la gent abandona.

💡 **Proposta:** ix sol creuant-ho amb §9.3. Preguntes → puges alarma → l'NPC es tanca **però ara és intimidable**. La pressió te la fabriques tu preguntant.

### 16.4 `alarma` és un multiplicador, no un eix

A §11 va fora del vector d'estat, correcte, però no diu què és. No és una moneda que gastes per obrir panys: és un **guany que modula la resistència dels altres tres**. Si no queda escrit abans de programar, s'implementarà com un quart eix amb gates i duplica l'espai de disseny per res.

### 16.5 La propagació no és testable amb 3 NPCs

Amb 3 NPCs i màxim 2 salts, tothom s'entera de tot: no hi ha xarxa que observar. La regla 7 del `CLAUDE.md` la posa com a invariant, però al v0 no dirà res.

💡 **Proposta:** deixar-la **fora del v0** explícitament, o pujar a 5 NPCs — però llavors ja no és el prototip xicotet.

### 16.6 El cost de contingut per fet és més gran del que diu §4

*"240 frases escrivint-ne 46"* és optimista. Per fet real s'escriu: text + 2-3 formes gramaticals + gates + fiabilitat per via + intencions vàlides + postura per NPC. Segueix sent **lineal**, que és el que importa, però la constant és bastant més gran que "una cadena". Millor saber-ho abans del fet 200.
