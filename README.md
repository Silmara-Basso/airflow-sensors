# airflow-sensors
Fluxo    completo    de    extração,    processamento    e armazenamento  de  dados  usando Airflow em especial explorando uso de sensores.

# Para instalar e executar o Apache Airflow siga os passos abaixo:

Execute o comando abaixo para criar as imagens Docker do Airflow e inicializar o banco de dados:

`docker compose up airflow-init`

`docker compose up`

Abra o navegador e efetue login. 

http://localhost:8080/login

User: airflow
Senha: airflow

Obs: Se você tiver o PostgreSQL instalado na sua máquina rodando na porta 5432 desligue-o ou haverá conflito de portas impedindo a inicialização do Airflow.

# Busque pelo arquivo do docker compose mais recente no link abaixo:

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

