from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="teste_nivelamento",  # Nome do seu banco de dados
        user="postgres",           # Substitua pelo seu usuário PostgreSQL
        password="casamento121209"          # Substitua pela sua senha
    )

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    query_text = request.args.get('q', '')
    if not query_text:
        return jsonify({"error": "Você precisa fornecer um termo de busca"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        query = """
        SELECT registro_ans, nome_fantasia, cnpj
        FROM operadoras
        WHERE nome_fantasia ILIKE %s OR cnpj ILIKE %s
        LIMIT 10;
        """
        cur.execute(query, (f"%{query_text}%", f"%{query_text}%"))
        rows = cur.fetchall()
        cur.close()
        conn.close()

        results = [{"registro_ans": row[0], "nome_fantasia": row[1], "cnpj": row[2]} for row in rows]
        return jsonify(results)

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"error": "Erro ao acessar o banco de dados"}), 500

if __name__ == '__main__':
    app.run(debug=True)