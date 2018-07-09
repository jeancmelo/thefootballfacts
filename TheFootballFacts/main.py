'''
Created on 12 de jun de 2018

@author: jeanm
'''

from builtins import str

from flask import Flask
from flask import render_template
from flask.globals import request

from FFDao.Dao import Dao
from FFutils.UtilPlayer import UtilPlayer
from FFClass.Club import Club
from FFClass.Player import Player


bd = Dao

#FLASK IMPORT
app = Flask(__name__)

@app.route('/')
def html_home():
    return render_template("index.html")

@app.route("/player/<player_name>")
def html_player(player_name):
    
    #Fazer Consulta no Banco pelo Nome
    aux = bd.consultar_Players("", player_name)

    
    #RECONSTRUINDO O OBJETO
    p = Player(aux[0][1],aux[0][2],aux[0][3],aux[0][4],aux[0][5],aux[0][6])   
 
    #if(p.player.name == ""):
    #    return render_template("notfound.html",player_name-p.player_name)
            
    #util = UtilPlayer(p)
    #score_area = util.score_player_meia(p)

    return render_template("player.html",
                            nome=p.player_name,
                            age=p.player_age,
                            image=p.player_photo,
                            nacionality=p.player_nationality,
                            position=p.player_position,
                            score_player=10
                            )
    
@app.route("/club/<club_name>")
def html_club(club_name):
    
    #RECONSTRUINDO O OBJETO
    aux = bd.consultar_Club("", club_name)
    c = Club(aux[0][1],aux[0][2],aux[0][3],aux[0][4],aux[0][5], aux[0][6], aux[0][7], aux[0][8])

    #RETORNA OS JOGADOES DAQUELE TIME
    arr_club_players = bd.consultar_Players_by_Club("",club_name)
    
    #RENDERIZAR A PAGINA COM AS INFORMACOES
    return render_template("club.html", 
                           club_name            = c.club_name,
                           club_fundation_Date  = c.club_fundation_Date,
                           club_country         = c.club_country,
                           club_emblem          = c.club_emblem,
                           club_n_win           = c.club_n_win,
                           club_n_defeat        = c.club_n_defeat,
                           club_n_tie           = c.club_n_tie,
                           players              = arr_club_players
                           ), 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)






