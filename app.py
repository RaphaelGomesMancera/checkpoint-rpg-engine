import os
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv
import oracledb

load_dotenv()

app = Flask(__name__)
app.secret_key = "segredo-simples-para-mensagens"

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DSN = os.getenv("DB_DSN")


def get_connection():
    return oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_DSN
    )


def listar_herois():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_heroi, nome, classe, hp_atual, hp_max, status
        FROM TB_HEROIS
        ORDER BY id_heroi
    """)

    colunas = [col[0].lower() for col in cursor.description]
    dados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return dados


@app.route("/")
def index():
    try:
        herois = listar_herois()
        return render_template("index.html", herois=herois)
    except Exception as e:
        return f"Erro ao carregar heróis: {str(e)}", 500


@app.route("/processar", methods=["POST"])
def processar_turno():
    bloco_plsql = """
    DECLARE
        v_dano_nevoa NUMBER := 15;
        v_novo_hp NUMBER;

        CURSOR c_herois IS
            SELECT id_heroi, hp_atual
            FROM TB_HEROIS
            WHERE status = 'ATIVO'
            FOR UPDATE;
    BEGIN
        FOR r_herois IN c_herois LOOP
            v_novo_hp := r_herois.hp_atual - v_dano_nevoa;

            IF v_novo_hp <= 0 THEN
                UPDATE TB_HEROIS
                SET hp_atual = 0,
                    status = 'CAÍDO'
                WHERE CURRENT OF c_herois;
            ELSE
                UPDATE TB_HEROIS
                SET hp_atual = v_novo_hp
                WHERE CURRENT OF c_herois;
            END IF;
        END LOOP;

        COMMIT;
    END;
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(bloco_plsql)
        cursor.close()
        conn.close()

        flash("Próximo turno processado com sucesso!")
    except Exception as e:
        flash(f"Erro ao processar turno: {str(e)}")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)