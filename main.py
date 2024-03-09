from flask import *
from bd import listar_jogador, remove_jogador, novo_jogador, detalha_jogador, atualiza_jogador

app = Flask(__name__)


@app.route('/')
def list_boardgames():
    jogadors = listar_jogador()
    return render_template("futebol.html", jogadors=jogadors)

@app.route("/remover/<int:chave>")
def apagar(chave):
    remove_jogador(chave)
    return redirect('/')

@app.route("/novo", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.form.to_dict()
        novo_jogador(dados.get('nome'), dados.get('posicao'), dados.get('altura'))
        return redirect('/')
    return render_template('form_futebol.html', jogador=None, title='Novo Jogador')

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        atualiza_jogador(chave, dados.get('nome'), dados.get('posicao'), dados.get('altura'))
        return redirect('/')
    jogador = detalha_jogador(chave)
    return render_template('form_futebol.html', jogador=jogador, title='Editar Jogador')



if __name__ == '__main__':
    # Execução do servidor flask
  
    app.run()