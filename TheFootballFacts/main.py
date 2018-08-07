# -*- coding: utf-8 -*-
'''
Created on 12 de jun de 2018

@author: jeanm
'''

from datetime import datetime, timedelta

from flask import Flask
from flask import render_template
import pygal

from FFClass.Club import Club
from FFClass.Player import Player
from FFDao import core, core_insert, core_select
from FFDao.Dao import Dao
from FFDao.core_select import Player_Goals_Year, Player_Yellow_Cards, \
    Player_Red_Cards, Player_Time_Played, Player_Titular_Games, \
    Player_Evolution_Goals_Year, Player_Club_Played, Player_Goals_Year_Career,\
    Player_Yellow_Cards_Career, Player_Red_Cards_Career,\
    Player_Time_Played_Career, Player_Titular_Games_Career
from FFutils.UtilClub import UtilClub
from FFutils.UtilPlayer import UtilPlayer


bd = Dao
core = core_select

#FLASK IMPORT
app = Flask(__name__)

@app.route('/')
def html_home():
    return render_template("index.html")

@app.route("/player/<player_name>")
def html_player(player_name):
    
    #RECONSTRUINDO O OBJETO
    p  = core.select_player_by_name(player_name)
    ps = core.selec_stats_by_name(player_name) 
    pe = Player_Evolution_Goals_Year(player_name);
    club_played = Player_Club_Played(player_name)
       

    #GR�FICO DE DESEMPENHO DE GOLS
    years = []
    data  = []
    for i, val in enumerate(pe):
        years.append(pe[i][1])
        data.append(pe[i][0])
    
    
    date_chart = pygal.Line(x_label_rotation=20)
    date_chart.x_labels = years
    date_chart.add('Gols', data)
    graph_data = date_chart.render_data_uri()
  
    return render_template("player.html",
                            player_name           = p[0][1],
                            player_age            = p[0][3],
                            p_photo               = p[0][4],
                            player_nacionality    = p[0][9],
                            player_position       = p[0][10],
                            foot                  = p[0][7],
                            club_atual            = p[0][4],
                            player_goal                = Player_Goals_Year(player_name, "2018"),
                            player_yellow_card         = Player_Yellow_Cards(player_name, "2018"),
                            player_red_card            = Player_Red_Cards(player_name, "2018"),
                            player_time_played         = Player_Time_Played(player_name, "2018"),
                            player_titular_year        = Player_Titular_Games(player_name, "2018"),
                            player_goal_career         = Player_Goals_Year_Career(player_name),
                            player_yellow_card_career  = Player_Yellow_Cards(player_name, "2018"),
                            player_red_card_career     = Player_Red_Cards(player_name, "2018"),
                            player_time_played_career  = Player_Time_Played_Career(player_name),
                            player_titular_year_career = Player_Titular_Games_Career(player_name),                            
                            graph_data                 = graph_data,
                            club_played                = club_played,
                            score_player               = 10                            
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
                           best_score           = core.Club_Best_Goals(club_name),
                           more_played          = core.Club_Most_Played(club_name),
                           more_violent         = core.CLub_Most_Violent(club_name),
                           goal_done            = core.Club_goals(club_name),
                           yellow_cards         = core.Club_yellow_card(club_name),
                           red_cards            = core.Club_red_card(club_name),
                           player_per_poisition = core.Club_get_number_per_position(club_name),
                           all_players          = core.Club_players(club_name)
                           ), 200

@app.route("/player/all-players")
def html_all_players():
    
    p = core.select_players()
    
    return render_template("all-players.html", player = p)
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)






