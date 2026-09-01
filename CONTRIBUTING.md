# Contribuir

Gràcies per mirar-t'ho. Este document és curt a posta: el projecte també ho és.

## Abans de res

Llig [`AGENTS.md`](AGENTS.md). És la porta d'entrada i explica com està construït açò ara
mateix, on viu cada cosa i què queda obert. Cinc minuts que n'estalvien moltes.

## Muntar l'entorn

```bash
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt   # Linux/macOS: .venv/bin/python
.venv/Scripts/python.exe cli.py
```

Passar les proves:

```bash
.venv/Scripts/python.exe -m unittest discover -s proves -t . -p "prova_*.py"
```

El `-p` no és opcional: els fitxers es diuen `prova_*.py` i el patró per defecte
d'`unittest` és `test*.py`. Sense ell trobaria zero proves i et diria `OK`.

`pyyaml` és l'única dependència i així ha de continuar. Si un canvi en necessita una altra,
eixa és la conversa abans que el codi.

Detall complet, i per què `python` a seques pot no funcionar en Windows:
[`.dev/plans/2026-09-01-entorn.md`](.dev/plans/2026-09-01-entorn.md) F2.

## Com entra un canvi

**El disseny no es discutix dins d'un PR.** Es discutix a
[`docs/disseny.md`](docs/disseny.md), i quan hi ha acord, s'escriu allí. Un PR que canvia
com funciona el joc sense que el document ho reflectisca no entra, encara que el codi siga bo.

**Si hi ha més d'una manera raonable d'afrontar un canvi, pregunta abans de tocar codi.**
És la regla de la casa i és la que més es trenca.

**Un canvi = una cosa.** Si toques el motor i el contingut alhora, són dos canvis.

**Un canvi a `content/` ha de passar el validador de resolubilitat**, que comprova que el
cas encara es puga acabar. ⚠️ El validador **encara no existix**: espec a
[`.dev/skills/skill-tot-se-sap/refs/08-qualitat-i-proves.md`](.dev/skills/skill-tot-se-sap/refs/08-qualitat-i-proves.md).
Mentre no hi siga, digues al PR com has comprovat que el cas seguix sent resoluble.

**Si un canvi deixa fals un document, arreglar-lo és part del canvi**, no feina a banda.

## Estil

Directe, curt, sense cerimònia. Funcions planes, res de jerarquies de classes per a coses
que són dades. No abstraure fins que hi haja **tres** casos reals que ho demanen. Tot està
a [`CLAUDE.md`](CLAUDE.md).

Els noms del domini van en valencià (`fet`, `palanca`, `postura`, `eix`, `desgast`). No és
un caprici: és el vocabulari amb què està pensat el joc. La infraestructura, en el que faça
falta.

## Llengua

El projecte és en valencià i els documents interns també. Si no el parles, escriu en anglés
i ja ho passarem: preferim la teua aportació a la teua gramàtica.

## Llicències

Són dues i cobrixen coses distintes — [AGPL-3.0](LICENSE) per al codi,
[CC BY-NC-SA 4.0](LICENSE-CONTINGUT) per al contingut. Contribuint acceptes que el que
aportes vaja sota la que li toque.

⚠️ **Si el que aportes és contingut** (un cas, un capítol, diàlegs), a més li concedixes al
manteniment del projecte permís per a usar-lo també sota altres condicions, inclosa la
comercial. Sense eixe permís, la clàusula «no comercial» blocaria el projecte sencer i no
es podria publicar mai una recopilació de pagament. Conserves l'autoria sempre.

El nom «Tot se sap» no el cobrix cap de les dues: [`TRADEMARK.md`](TRADEMARK.md).
