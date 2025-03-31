# Variáveis, Conexões e Sensores Para Extração e Movimentação de Dados com Airflow

import sqlite3

db_path = "sensors.db"

# Conecte ao banco de dados (se não existir, ele será criado)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    weather TEXT,
    temperature REAL,
    humidity INTEGER
)
""")

# Commit e fechar a conexão
conn.commit()
conn.close()

print(f"\nBanco de dados criado e tabela 'weather_data' está pronta em {db_path}")

