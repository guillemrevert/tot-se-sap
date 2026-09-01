# 10 — Glossari

El domini va en català. Ací està el mapa cap al codi perquè ningú s'invente sinònims.

| Terme | Què és | Al codi |
|---|---|---|
| **fet** | una peça d'informació. Alhora **premi** (l'has guanyada) i **clau** (obri la següent) | `mon["fets"][fet_id]`, ids `f_…` |
| **palanca** | un fet que ja tens, usat per pressionar algú. **Fet i palanca són la mateixa cosa** en moments distints | `palanca_id` |
| **intenció** | què li fas: `AMENAÇAR` `OFERIR` `EMPATITZAR` `CONFRONTAR` `INSINUAR` `PREGUNTAR`. Llista **tancada** | `mon["intencions"]` |
| **eix** | `intimidació` · `confiança` · `temptació`. L'estat de l'NPC cap a tu | `nucli.EIXOS` |
| **postura** | **per què** este NPC calla este fet: `PROTEGEIX` `POR` `PROFIT` `INDIFERENT`. Decidix quin eix l'obri | `npc["sap"][fet_id]` |
| **llindar** (*gate*) | quant eix cal per a que solte el fet | `nucli.llindar()` |
| **dificultat** | el número cru del fet, abans del multiplicador de postura | `fets[f]["dificultat"]` |
| **pes** | quant val una carta contra este NPC ara: vulnerabilitat × degradació | `nucli.pes()` |
| **desgast** | quantes vegades has usat una carta **contra este NPC** | `npc["desgast"]` |
| **degradació** | que una carta valga menys cada vegada. Mai zero | `regles["degradació"]` |
| **ruptura** | l'NPC es tanca per sempre. Estat terminal, per intimidació | `npc["ruptura"]`, `npc["tancat"]` |
| **refredament** | que els eixos baixen sols cada torn, amb terra | `regles["refredament"]` |
| **via** | per quin eix vas traure un fet. Determinarà si és **cert** (§2.2) | `obtinguts[f]["via"]` |
| **to** | registre de la resposta: `sec` `obert` `interessat` `pressionat` | `text.to()` |
| **forma** | forma gramatical del fet: `nu` `subordinada` `nominal` | `intencions[i]["forma"]` |
| **calibratge** | mode de depuració del CLI (tecla `c`): números crus i llindars pendents | `cli.calibratge` |
| **alarma** | com d'implicat es creu l'NPC. Multiplica resistència, **no** és un quart eix | ❌ no existix encara |
| **sostre** | màxim que un eix pot arribar en un NPC. Tanca portes de veres | ❌ no existix encara |

## Anglés que sí que s'usa

`gate` només com a sinònim de `llindar` en conversa. Al codi, `llindar`.
Infraestructura (`main`, `path`, `yaml`) en anglés sense complexos. Coherència per damunt de puresa.
