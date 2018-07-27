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
from FFDao import core, core_insert, core_select


bd = Dao
core = core_select

#FLASK IMPORT
app = Flask(__name__)

@app.route('/')
def html_home():
    return render_template("index.html")

@app.route("/player/<player_name>")
def html_player(player_name):
    
    #CONSULTA NO BANCO PELO NOME
    #aux = bd.consultar_Players("", player_name)
    
    #RECONSTRUINDO O OBJETO
    p  = core.select_player_by_name(player_name)
    ps = core.selec_stats_by_name(player_name) 

    #p = Player(aux[0][1],aux[0][2],aux[0][3],aux[0][4],aux[0][5],aux[0][6], aux[0][7],aux[0][8],aux[0][9],aux[0][10],aux[0][11],aux[0][12])   
 
    return render_template("player.html",
                            player_name           = p[0][1],
                            player_age            = p[0][3],
                            p_photo               = p[0][4],
                            player_nacionality    = p[0][9],
                            player_position       = p[0][10],
                            player_goal           = ps[0][6],
                            player_yellow_card    = ps[0][8],
                            player_red_card       = ps[0][10],
                            score_player          = 10                            
                            )
    
@app.route("/club/<club_name>")
def html_club(club_name):
    
    #RECONSTRUINDO O OBJETO
    c = core.select_club_by_name(club_name)
    

   
    
    #RENDERIZAR A PAGINA COM AS INFORMACOES
    return render_template("club.html", 
                           club_name            = c[0][1],
                           club_fundation_Date  = c[0][2],
                           club_country         = "Brasil",
                           club_emblem          = c[0][3],
                           club_n_win           = c[0][4],
                           club_n_defeat        = c[0][5],
                           club_n_tie           = c[0][6],
                           club_n_win_in        = c[0][7],
                           club_n_win_out       = (c[0][7] - c[0][4])*-1,
                           club_n_defeat_in     = c[0][8],
                           club_n_defeat_out    = (c[0][8] - c[0][5])*-1,
                           club_n_tie_in        = c[0][9],
                           rate_win             = c[0][7]/(c[0][7] - c[0][4])*-1,
                           rate_defeat          = c[0][8]/(c[0][8] - c[0][5])*-1,
                           rate_tie             = c[0][9]/(c[0][9] - c[0][6])*-1,
                           ), 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)






