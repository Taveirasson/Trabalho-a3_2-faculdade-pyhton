#importação das bibliotecas
from flask import Flask, request, render_template
import mysql.connector

#inicia o flask
app = Flask(__name__)


# Conecta com mysql
conexao = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='root',
    database = 'atividade' )

# Rota do index
@app.route('/')
def index():
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

    return render_template('index.html')


#executa o aplicativo flask
if __name__ == '__main__':
    app.run(debug=True)