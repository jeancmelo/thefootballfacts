'''
Created on 12 de jun de 2018

@author: jeanm
'''

from flask import Flask
from flask import render_template

from FFDao.Dao import Dao
from FFClass.Club import Club
from FFClass.Player import Player
from FFutils.UtilPlayer import UtilPlayer
from FFutils.UtilClub import UtilClub

bd = Dao

#FLASK IMPORT
app = Flask(__name__)

@app.route('/')
def html_home():
    return render_template("index.html")

@app.route("/player/<player_name>")
def html_player(player_name):
    
    #CONSULTA NO BANCO PELO NOME
    aux = bd.consultar_Players("", player_name)
    
    #RECONSTRUINDO O OBJETO
    p = Player(aux[0][1],aux[0][2],aux[0][3],aux[0][4],aux[0][5],aux[0][6])   
 
    #if(p.player.name == ""):
    #    return render_template("notfound.html",player_name-p.player_name)
            
    #util = UtilPlayer(p)
    #score_area = util.score_player_meia(p)

    return render_template("player.html",
                            nome                = p.player_name,
                            age                 = p.player_age,
                            image               = p.player_photo,
                            nacionality         = p.player_nationality,
                            position            = p.player_position,
                            score_player        = 10
                            )
    
@app.route("/club/<club_name>")
def html_club(club_name):
    
    #CONSULTA NO BANCO PELO NOME
    aux = bd.consultar_Club("", club_name)
    
    #RECONSTRUINDO O OBJETO
    c = Club(aux[0][1],aux[0][2],aux[0][3],aux[0][4],aux[0][5], aux[0][6], aux[0][7], aux[0][8], aux[0][8])
    
    #RETORNA OS JOGADOES DAQUELE TIME
    arr_club_players = bd.consultar_Players_by_Club("", club_name)
    
    #CHAMA A METODO DE SCORE DOS PLAYERS
    up = UtilPlayer
    uc = UtilClub
    
    #UTILIZACAO DAS UTIL DE PLAYER
    best_players    = up.best_5_players("", arr_club_players)
    worst_players   = up.worst_5_players("", arr_club_players)
    best_scores     = up.best_scores("", arr_club_players)
    best_assistence = up.best_assistence("", arr_club_players)
    
    #UTILIZACAO DAS UTIL DE CLUB
    goal_done      = uc.goal_done("", arr_club_players)
    yellow_cards   = uc.yellow_cards("", arr_club_players)
    red_cards      = uc.red_cards("", arr_club_players)
    
    #RENDERIZAR A PAGINA COM AS INFORMACOES
    return render_template("club.html", 
                           club_name            = c.club_name,
                           club_fundation_Date  = c.club_fundation_Date,
                           club_country         = c.club_country,
                           club_emblem          = c.club_emblem,
                           club_n_win           = c.club_n_win,
                           club_n_defeat        = c.club_n_defeat,
                           club_n_tie           = c.club_n_tie,
                           players              = arr_club_players,
                           club_n_win_in        = c.club_n_win_in,
                           club_n_win_out       = (c.club_n_win_in - c.club_n_win)*-1,
                           club_n_defeat_in     = c.club_n_defeat_in,
                           club_n_defeat_out    = (c.club_n_defeat_in - c.club_n_defeat)*-1,
                           club_n_tie_in        = c.club_n_tie_in,
                           best_players         = best_players,
                           worst_players        = worst_players,
                           goal_done            = goal_done,
                           yellow_cards         = yellow_cards,
                           red_cards            = red_cards,
                           best_scores          = best_scores,
                           best_assistence      = best_assistence
                           ), 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)






