import sqlite3

conn = sqlite3.connect("rbmc.db")
cursor = conn.cursor()

total = 0

with open("sourcetable.txt", "r", encoding="utf-8") as f:

    for linha in f:

        linha = linha.strip()

        if not linha.startswith("STR;"):
            continue

        campos = linha.split(";")

        if len(campos) < 19:
            print("Linha ignorada:", campos[0:3])
            continue

        try:

            cursor.execute("""
            INSERT OR REPLACE INTO estacoes (
                mountpoint,
                nome,
                formato_rtcm,
                mensagens_rtcm,
                taxa_atualizacao,
                constelacoes,
                rede,
                pais,
                latitude,
                longitude,
                necessita_nmea,
                solucao,
                receptor,
                compressao,
                autenticacao,
                taxa_cobranca,
                bitrate,
                descricao
            )
            VALUES (
                ?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?,?,?,?
            )
            """, (

                campos[1],
                campos[2],
                campos[3],
                campos[4],
                campos[5],
                campos[6],
                campos[7],
                campos[8],
                campos[9],
                campos[10],
                campos[11],
                campos[12],
                campos[13],
                campos[14],
                campos[15],
                campos[16],
                campos[17],
                campos[18]
            ))

            total += 1

        except Exception as e:

            print("Erro:", campos[1])
            print(e)

conn.commit()
conn.close()

print()
print(f"Importadas: {total} estações")