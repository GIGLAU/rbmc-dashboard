DROP TABLE IF EXISTS estacoes;

CREATE TABLE estacoes (
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
);