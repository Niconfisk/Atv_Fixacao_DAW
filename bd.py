import sqlite3


def criar():
    conn = sqlite3.connect('futebol.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS futebol(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            posicao VARCHAR(3) NOT NULL,
            altura REAL NOT NULL);
    """)

    conn.close()


def novo_jogador(nome, posicao, altura):
    conn = sqlite3.connect('futebol.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO futebol(nome, posicao, altura)
        VALUES(?, ?, ?);
    """, (nome, posicao, altura))
    conn.commit()
    conn.close()


def listar_jogador():
    conn = sqlite3.connect('futebol.db')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM futebol")
    resultado = []
    for row in values:
        resultado.append({
            'id': row[0],
            'nome': row[1],
            'posicao': row[2],
            'altura': row[3],
        })
    conn.close()
    return resultado


def atualiza_jogador(id, nome, posicao, altura):
    conn = sqlite3.connect('futebol.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE futebol
        SET nome=?, posicao=?, altura=?
        WHERE id=?;
        """,
        (nome, posicao, altura, id)
    )
    conn.commit()
    conn.close()


def remove_jogador(id):
    conn = sqlite3.connect('futebol.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM futebol
        WHERE id=?;
        """,
        (id,)
    )
    conn.commit()
    conn.close()



def detalha_jogador(id):
    conn = sqlite3.connect('futebol.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM futebol
        WHERE id=?;
        """,
        (id,)
    )
    item = cursor.fetchone()
    conn.close()
    if item is None:
        return None
    return {
        'id': item[0],
        'nome': item[1],
        'posicao': item[2],
        'altura': item[3],
    }


if __name__=='__main__':
    criar()