<h1 align='center'>Bank-Project</h1>
<p align='center'>A short description for my bank project.</p>
<p align='center'><b>Apache2 | Flask API | PostgresqlDB </b></p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=flask,postgres&theme=dark">
</p>

---
<br>

### <h1 align="center">How To Run?</h1>
**First step is edit your default `.env` file configuration.**

``` .env
# SQL server

database_name=FinanceDatabase
database_host=localhost
database_port=5432
database_password=financePassword
database_username=financeUser

# API

api_host=0.0.0.0
api_port=8080
api_origin=*

# Website Apache.

website_port=80
```

If you have docker installed:
``` bash
# Clona o repositorio
git clone https://github.com/DevMaycon/bank-project/

# Entra no repositorio
cd bank-project

# Deploy dos containers
docker compose up -d # Running in background.
```

If you don't have docker installed, feel free to install in [Docker Installation guide.](https://www.docker.com/get-started/)

---
