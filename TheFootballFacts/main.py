'''
Created on 12 de jun de 2018

@author: jeanm
'''

from builtins import str

#FLASK IMPORT
from flask import Flask
from flask import render_template
from flask.globals import request
from flask_bootstrap  import  Bootstrap


app = Flask(__name__)

@app.route('/')
def html_home():
    return render_template("index.html")

@app.route("/player/<nome>")
def html_player(nome):
    return render_template("player.html", nome=nome)

@app.route("/club/<nome>")
def html_club(nome):
    
    #FAZER A CHAMADA PARA O BANCO

    
    arr_club_info = ["Coritiba Foot Ball Club", "12/10/1909", "Curitiba - Parana - BR", "Campeao Brasileiro 1985", "#14", "#100"]
    arr_club_stats = [10, 20, 15, 5, 5]
    arr_club_players = ["Wilson Rodrigues", "Abner", "Alecsandro", "Allison Farias", "Raphael Lucas"]
    
    return render_template('club.html', 
                           nome=arr_club_info[0], 
                           datafundacao=arr_club_info[1],
                           paiscidade=arr_club_info[2],
                           tituloprincipal=arr_club_info[3],
                           rankfifa=arr_club_info[4],
                           score=arr_club_info[5],
                           players=arr_club_players), 200



@app.route("/add/<int:n1>/<int:n2>")
def echo_cal_add(n1, n2):
    return str(n1+n2), 200

@app.route("/nome")
def echo_cal_param():
    cpf = request.args.get("cpf")    
           
    return cpf, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)






