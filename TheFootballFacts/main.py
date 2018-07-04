'''
Created on 12 de jun de 2018

@author: jeanm
'''

from _hashlib import new
from builtins import str

from flask import Flask
from flask import render_template
from flask.globals import request
from flask_bootstrap  import  Bootstrap

from FFClass.Player import Player
from FFutils.UtilPlayer import UtilPlayer


#FLASK IMPORT
app = Flask(__name__)

@app.route('/')
def html_home():
    return render_template("index.html")

@app.route("/player/<nome>")
def html_player(nome):
    
    p = Player("Jean Melo", "24", "http://s2.glbimg.com/FEOzbUht1L9IAr98ARmMvw722dQ=/top/s.glbimg.com/jo/eg/f/original/2014/04/25/adriano.png", "Brasileira", "Meio Campo",
               20, 5, 10, 20, 100)
    
    util = UtilPlayer(p)
    score_area = util.score_player_meia(p)

    return render_template("player.html",
                            nome=p.player_name,
                            age=p.player_age,
                            image=p.player_photo,
                            nacionality=p.player_nationality,
                            position=p.player_position,
                            score_player=score_area
                            )
    
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






