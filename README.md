# gameslist
Projeto criado durante a pós graduação em Desenvolvimento Web Full Stack. Esse repositório possui o backend utilizando o framework flask rest x.

Para a execução correta do sistema, instale as dependencias necessárias com os comandos:

```
python -m venv venv
pip install -r requirements.txt
```

Configure a aplicação através do arquivo .env com as variáveis de ambiente necessárias:

```
ATLAS_URI=mongodb+srv://<usuario>:<senha>@<url>
DB_NAME=<nomeDoBanco>
```

Após isso rode o sistema com o comando:

```
python app.py
```