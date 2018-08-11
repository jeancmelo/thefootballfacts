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
from FFDao import core, core_insert, core_select_club, core_select_champ
from FFDao.Dao import Dao
from FFDao.core_select_club import Player_Goals_Year, Player_Yellow_Cards, \
    Player_Red_Cards, Player_Time_Played, Player_Titular_Games, \
    Player_Evolution_Goals_Year, Player_Club_Played, Player_Goals_Year_Career,\
    Player_Yellow_Cards_Career, Player_Red_Cards_Career,\
    Player_Time_Played_Career, Player_Titular_Games_Career


bd = Dao
core = core_select_club
champ = core_select_champ

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
   
    data = core.Scores_per_area(club_name)
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Score por Area'
    line_chart.add('Goleiro', data[0])
    line_chart.add('Defensor', data[1])
    line_chart.add('Meio', data[2])
    line_chart.add('Atacante', data[3])
    graph_data = line_chart.render_data_uri()
   
    
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
                           all_players          = core.Club_players(club_name),
                           top_scores           = core.Best_Score_Players(club_name),
                           wrost_scores         = core.Wrots_Score_Players(club_name), 
                           graph_data           = graph_data
                           ), 200

@app.route("/championship/<championship_name>")
def html_championship(championship_name):
    
    c = champ.select_club_by_champ(championship_name)
    
    ages = champ.champ_age_data()
    box_plot = pygal.Box()
    box_plot.title = 'Idade dos Jogadores'
    box_plot.add('Idade', ages)
    age_graph = box_plot.render_data_uri()
    
    goals = champ.champ_goals_data()
    box_goals = pygal.Box()
    box_goals.title = 'Idade dos Jogadores'
    box_goals.add('Idade', goals)
    goals_box = box_goals.render_data_uri()
    
    titular = champ.champ_titular_data()
    box_titular = pygal.Box()
    box_titular.title = 'Idade dos Jogadores'
    box_titular.add('Idade', titular)
    titular_box = box_titular.render_data_uri()    
    
    
    cor_age = champ.champ_corralation_age_goals()
    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = 'Idade vs Goals'
    xy_chart.add('2018', cor_age)
    cor_age_goals = xy_chart.render_data_uri()        
    
    cor_age = champ.champ_corralation_age_matched_played()
    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = 'Idades vs Partidas Jogadas'
    xy_chart.add('2018', cor_age)
    cor_age_match_played = xy_chart.render_data_uri()    

    win_per_club = champ.champ_in_out_victory()
    win_clubs = win_per_club.render_data_uri()    
    
    position = champ.champ_player_per_position()
    position_player = position.render_data_uri()
    
    position_club = champ.champ_player_per_position_club()
    position_player_club = position_club.render_data_uri()
    
    #RENDERIZAR A PAGINA COM AS INFORMACOES
    return render_template("championship.html", 
                           championship_name            = championship_name,
                           champ_clubs                  = c,
                           goal_done                    = champ.champ_goals(championship_name),
                           yellow_cards                 = champ.champ_yellow_card(championship_name),
                           red_cards                    = champ.champ_red_card(championship_name),
                           age_graph                    = age_graph,
                           cor_age_match_played         = cor_age_match_played,
                           cor_age_goals                = cor_age_goals,
                           more_violent                 = champ.champ_most_violent(),
                           best_goals                   = champ.champ_best_goals(),
                           more_played                  = champ.champ_most_played(),
                           win_clubs                    = win_clubs,
                           position_player              = position_player,
                           position_player_club         = position_player_club,
                           goals_box                    = goals_box,
                           titular_box                  = titular_box                           
                           ), 200

@app.route("/player/all-players")
def html_all_players():
    
    p = core.select_players()
    
    return render_template("all-players.html", player = p)
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)






