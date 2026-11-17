import sqlite3

conn = sqlite3.connect("rbmc.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estacoes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    mountpoint TEXT UNIQUE,

    nome TEXT,

    formato_rtcm TEXT,

    mensagens_rtcm TEXT,

    taxa_atualizacao INTEGER,

    constelacoes TEXT,

    rede TEXT,

    pais TEXT,

    latitude REAL,

    longitude REAL,

    necessita_nmea INTEGER,

    solucao INTEGER,

    receptor TEXT,

    compressao TEXT,

    autenticacao TEXT,

    taxa_cobranca TEXT,

    bitrate INTEGER,

    descricao TEXT

)
""")

conn.commit()

conn.close()

print("Tabela criada com sucesso.")