import socket
import sqlite3

HOST = "170.84.40.52"
PORT = 2101

DB = "rbmc.db"


def baixar_sourcetable():

    requisicao = (
        "GET / HTTP/1.0\r\n"
        "User-Agent: NTRIP RBMC\r\n"
        "\r\n"
    )

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(30)

    s.connect((HOST, PORT))

    s.send(requisicao.encode())

    resposta = b""

    while True:

        dados = s.recv(4096)

        if not dados:
            break

        resposta += dados

    s.close()

    return resposta.decode(
        errors="ignore"
    )


def atualizar_banco(texto):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM estacoes")

    total = 0

    for linha in texto.splitlines():

        linha = linha.strip()

        if not linha.startswith("STR;"):
            continue

        campos = linha.split(";")

        if len(campos) < 19:
            continue

        cursor.execute("""

        INSERT INTO estacoes (

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

        """,

        (

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

    conn.commit()
    conn.close()

    return total


def main():

    print("Baixando Source Table...")

    texto = baixar_sourcetable()

    with open(
        "sourcetable_atual.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(texto)

    total = atualizar_banco(texto)

    print(
        f"Atualizadas {total} estações."
    )


if __name__ == "__main__":
    main()