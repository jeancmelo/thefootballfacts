# -*- coding: utf-8 -*-
'''
Created on 12 de jun de 2018

@author: jeanm
'''

from flask import Flask
from flask import render_template
import pygal
from pygal.style import Style

from FFDao import core_select_club, core_select_champ, core_select_player
from FFDao.core_select_club import Player_Goals_Year, Player_Yellow_Cards, \
    Player_Red_Cards, Player_Time_Played, Player_Titular_Games, \
    Player_Club_Played, Player_Goals_Year_Career,\
    Player_Time_Played_Career, Player_Titular_Games_Career

core = core_select_club
champ = core_select_champ
player_select = core_select_player

#FLASK IMPORT
app = Flask(__name__)

@app.route('/')
def html_home():
    
    c = champ.select_club_by_champ("Brasileirão%20Série%20A")
    d = champ.Best_Score_Players(12)
        
    return render_template("index.html",
                            champ_clubs           = c,
                            best_players          = d
                           ), 200

@app.route("/player/<player_name>")
def html_player(player_name):
    
    p  = core.select_player_by_name(player_name)
    club_played = Player_Club_Played(player_name)

    player_radar = player_select.player_network_skills(player_name)
    radar_player = player_radar.render_data_uri()
    
    data_graph  = player_select.player_goals_per_year(player_name)
    graph_data = data_graph.render_data_uri()
    
    chart_pie = player_select.player_titular_vs_non(player_name)
    pie_chart = chart_pie.render_data_uri()
  
    chart_line = player_select.player_time_per_year(player_name)
    line_chart = chart_line.render_data_uri()
    
    chart_xy   = player_select.player_cor_age_vs_time_played(player_name)
    xy_chart   = chart_xy.render_data_uri()
    
    try:
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
                                radar_player               = radar_player,
                                pie_chart                  = pie_chart,
                                line_chart                 = line_chart,
                                xy_chart                   = xy_chart,
                                score_player               = 10                            
                                )
    except Exception as e:
        return render_template("404.html"), 404
    
@app.route("/club/<club_name>")
def html_club(club_name):
    
    #CUSTOMIZAÇÃO DA COR DO GRÁFICO DE SCORE POR ÁREA
    custom_style = Style(
    background='transparent',
    plot_background='#FFF',
    foreground='#676767',
    value_font_size = 20.0,
    label_font_size=20.0,
    legend_font_size=20.0,
    major_label_font_size=20.0,
    guide_stroke_dasharray='#fbfbfb',
    major_guide_stroke_dasharray='#fbfbfb',
    foreground_strong='#676767',
    foreground_subtle='#676767',
    opacity='.8',
    opacity_hover='.9',
    transition='200ms ease-in',
    colors=('#5da052', '#8ed084', '#9fd098', '#25681b'))    
    
    data = core.Scores_per_area(club_name)
    line_chart = pygal.HorizontalBar(style=custom_style)
    line_chart.add('Goleiro', data[0])
    line_chart.add('Defensor', data[1])
    line_chart.add('Meio', data[2])
    line_chart.add('Atacante', data[3])
    graph_data = line_chart.render_data_uri()
   
    best_form = core.club_best_formation(club_name)

    club_stat = core.select_club_by_name(club_name)
    vt = int(club_stat[0]['club_n_win'])
    dr = int(club_stat[0]['club_n_defeat'])
    en = int(club_stat[0]['club_n_tie'])
    
    pie_chart = pygal.Pie(style=custom_style)
    pie_chart.add('Vitórias', vt)
    pie_chart.add('Derrotas', dr)
    pie_chart.add('Empates', en)
    chart_pie = pie_chart.render_data_uri()
    
    try:
        return render_template("club.html", 
                               club_stats           = core.select_club_by_name(club_name),
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
                               graph_data           = graph_data,
                               best_formation       = best_form[0],
                               player_formation     = best_form[1],
                               club_last_games      = core.club_last_games(club_name),
                               club_next_games      = core.club_next_games(club_name),
                               chart_pie            = chart_pie,
                               ), 200
    except Exception as e:
        return render_template("404.html"), 404
   
    
@app.route("/championship/<championship_name>")
def html_championship(championship_name):
    
    c = champ.select_club_by_champ(championship_name)

    #CUSTOMIZAÇÃO DA COR DO GRÁFICO DE SCORE POR ÁREA
    custom_style = Style(
    background='transparent',
    plot_background='#FFF',
    foreground='#676767',
    value_font_size = 20.0,
    label_font_size=20.0,
    legend_font_size=20.0,
    major_label_font_size=20.0,
    guide_stroke_dasharray='#fbfbfb',
    major_guide_stroke_dasharray='#fbfbfb',
    foreground_strong='#676767',
    foreground_subtle='#676767',
    opacity='.8',
    opacity_hover='.9',
    transition='200ms ease-in',
    colors=('#A09E52', '#78774C', '#68661B', '#4D6219', '#657148', '#82974D', '#7C3F67', '#5D3B51'))    
    

    ages = champ.champ_age_data()
    box_plot = pygal.Box(style=custom_style)
    box_plot.title = 'Idade dos Jogadores'
    box_plot.add('Idade', ages)
    age_graph = box_plot.render_data_uri()
    
    goals = champ.win_and_defeat()
    goals_box = goals.render_data_uri()
    
    titular = champ.champ_titular_data()
    box_titular = pygal.Box(style=custom_style)
    box_titular.title = 'Idade dos Jogadores'
    box_titular.add('Idade', titular)
    titular_box = box_titular.render_data_uri()    
    
    cor_age = champ.champ_corralation_age_goals()
    xy_chart = pygal.XY(stroke=False, style=custom_style)
    xy_chart.title = 'Idade vs Goals'
    xy_chart.add('2018', cor_age)
    cor_age_goals = xy_chart.render_data_uri()        
    
    cor_age = champ.champ_corralation_age_matched_played()
    xy_chart = pygal.XY(stroke=False, style=custom_style)
    xy_chart.title = 'Idades vs Partidas Jogadas'
    xy_chart.add('2018', cor_age)
    cor_age_match_played = xy_chart.render_data_uri()    

    win_per_club = champ.champ_in_out_victory()
    win_clubs = win_per_club.render_data_uri()    
    
    position = champ.champ_player_per_position()
    position_player = position.render_data_uri()

    try:
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
                               goals_box                    = goals_box,
                               titular_box                  = titular_box                           
                           ), 200
    except Exception as e:
        return render_template("404.html"), 404                       

@app.route('/player')
def html_players():
    
    d = champ.Best_Score_Players(0)
        
    return render_template("players.html",
                            best_players          = d
                           ), 200

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route("/perguntas-frequentes")
def html_faq():
    return render_template('perguntas-frequentes.html'), 200



    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)






