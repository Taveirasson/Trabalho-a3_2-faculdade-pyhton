#importação das bibliotecas
from flask import Flask, request, render_template, send_file
import mysql.connector
import pandas as pd
from io import BytesIO


from class_graficos import Graficos

#inicia o flask
app = Flask(__name__)

# Conecta com mysql
conexao = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='root',
    database = 'atividade' )


@app.route('/')
def index():
    return render_template('index.html')

# Rota do registro doenca
@app.route('/registro_doenca', methods=['POST','GET'])
def registro_doenca():
    if request.method == 'POST':
        diagnostico = request.form['diagnostico']
        eritrocitos = request.form['eritrocitos']
        hemoglobina = request.form['hemoglobina']
        dematocrito = request.form['dematocrito']
        hcm = request.form['hcm']
        vgm = request.form['vgm']
        chgm = request.form['chgm']
        metarrubricitos = request.form['metarrubricitos']
        proteina_plasmatica = request.form['proteina_plasmatica']
        leucocitos = request.form['leucocitos']
        leucograma = request.form['leucograma']
        segmentados = request.form['segmentados']
        bastonetes = request.form['bastonetes']
        blastos = request.form['blastos']
        metamielocitos = request.form['metamielocitos']
        mielocitos = request.form['mielocitos']
        linfocitos = request.form['linfocitos']
        monocitos = request.form['monocitos']
        eosinofilos = request.form['eosinofilos']
        basofilos = request.form['basofilos']
        plaquetas = request.form['plaquetas']

        cursor = conexao.cursor()

        comando_insert = f"INSERT INTO formulario (diagnostico, eritrocitos, hemoglobina, dematocrito, hcm, vgm, chgm, metarrubricitos, proteina_plasmatica, leucocitos, leucograma, segmentados, bastonetes, blastos, metamielocitos, mielocitos, linfocitos, monocitos, eosinofilos, basofilos, plaquetas)VALUES ('{diagnostico}', '{eritrocitos}', '{hemoglobina}', '{dematocrito}', '{hcm}', '{vgm}', '{chgm}', '{metarrubricitos}', '{proteina_plasmatica}', '{leucocitos}', '{leucograma}', '{segmentados}', '{bastonetes}', '{blastos}', '{metamielocitos}', '{mielocitos}', '{linfocitos}', '{monocitos}', '{eosinofilos}', '{basofilos}', '{plaquetas}');"

        cursor.execute(comando_insert)
        conexao.commit()
        cursor.close()

    return render_template('registro_doenca.html')


def fetch_data():
    # Consultar dados do MySQL
    query = "SELECT * FROM formulario;"
    df = pd.read_sql(query, conexao)
    return df

@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    if request.method == 'POST':
        # Obter escolhas do usuário do formulário
        tipo_grafico = request.form['grafico']
        dado1 = request.form['dado1']
        dado2 = request.form['dado2']

        # Obter gráfico com base nas escolhas do usuário
        df = fetch_data()  # Certifique-se de ter a função fetch_data() definida
        gf = Graficos(df)

        dado1 = None if dado1 == 'null' else dado1
        dado2 = None if dado2 == 'null' else dado2

        graph = gf.gerar_grafico(tipo_grafico, dado1, dado2)

        return render_template('dashboard.html', graph=graph)

    return render_template('dashboard.html')

@app.route('/download_excel')
def download_excel():
    # Obter dados do banco de dados
    df = fetch_data()

    # Criar um arquivo Excel em memória
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)

        # Adiciona uma planilha vazia para garantir que haja pelo menos uma planilha visível
        writer.book.create_sheet()

    output.seek(0)

    # Enviar o arquivo Excel como uma resposta de download
    return send_file(output, download_name='dados_excel.xlsx', as_attachment=True)

#executa o aplicativo flask
if __name__ == '__main__':
    app.run(debug=True)