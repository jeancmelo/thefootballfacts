# -*- coding: utf-8 -*-

'''
Created on 8 de ago de 2018

@author: jeanm
'''
from sqlalchemy import select, and_
from pygal.style import Style

from FFDao.core import players_table, stats_table, club_table, champ_table
from numpy import integer
from _operator import contains
import json
from FFutils import UtilPlayer
from audioop import reverse
import pygal

def select_club_by_champ(c_champ):
    
    retorno = []
    club_name = []
    club_logo = []
    club_score = []
    
    a = select([club_table.c.c_name, club_table.c.c_emblem])
    
    for row in a.execute():
        retorno.append(row)
    
    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        club_name.append(retorno[i][0])
        club_logo.append(retorno[i][1])


    data = [{"club_name": c, "club_logo": y} for c, y in zip(club_name, club_logo)]
    
    mysorted = sorted(data, key=lambda x : x['club_name'], reverse=False)
        
    return mysorted

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_goals(c_champ):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_gols]).where(
                and_(
                    stats_table.c.s_champ == c_champ,
                    stats_table.c.s_year == "2018"
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
         valor_retorno = valor_retorno + retorno[i][0]
                
    return valor_retorno

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_data():
    
    retorno = []
    valor_retorno = 0
    
    a = select([champ_table])
    
    for row in a.execute():
        retorno.append(row)

    return valor_retorno

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_yellow_card(c_champ):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_yellow_card]).where(
                and_(
                    stats_table.c.s_champ == c_champ,
                    stats_table.c.s_year == "2018"
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
         valor_retorno = valor_retorno + retorno[i][0]
                
    return valor_retorno

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_red_card(c_champ):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_red_card]).where(
                and_(
                    stats_table.c.s_champ == c_champ,
                    stats_table.c.s_year == "2018"
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
         valor_retorno = valor_retorno + retorno[i][0]
                
    return valor_retorno

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_age_data():
    
    retorno = []
    idades =  []
    
    a = select([players_table.c.p_age])
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        aux = retorno[i][0]
        idades.append(aux[12:14])
   
    idades = list(map(int, idades))          

    return idades

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_goals_data():
    
    retorno = []
    idades =  []
    
    a = select([stats_table.c.s_gols])
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        idades.append(retorno)
   
    print(idades)          

    return idades

def win_and_defeat():

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

    win     = 0
    defeat  = 0
    tie     = 0
    score   = []
    
    a = select([club_table.c.c_n_win, club_table.c.c_n_defeat, club_table.c.c_n_tie])
    
    for row in a.execute():
        win = win + row[0]
        defeat =  defeat + row[1]
        tie = tie + row[2]
    
    pie_chart = pygal.Pie(style=custom_style)
    pie_chart.add('Vitórias', win)
    pie_chart.add('Derrotas', defeat)
    pie_chart.add('Empates', tie)
    
    return pie_chart

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_titular_data():
    
    retorno = []
    idades =  []
    
    a = select([stats_table.c.s_titular])
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        idades.append(retorno[i][0])
   
    idades = list(map(int, idades))          

    return idades

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_corralation_age_goals():
    
    retorno = []
    idades =  []
    nome   =  []
    matches_played = []
    
    a = select([players_table.c.p_age, players_table.c.p_name ])
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        aux = retorno[i][0]
        idades.append(aux[12:14])
        a = select([stats_table.c.s_gols]).where(
                    and_(
                        stats_table.c.s_name == retorno[i][1],
                        stats_table.c.s_year == "2018"
                    ) )        
        for row in a.execute():
            matches_played.append(row[0])


    idades = list(map(int, idades))   

    data = [(y, c) for c, y in zip(idades, matches_played)]
   
    return data

#RETORNA NÚMERO DE GOLS DO CLUB
def champ_corralation_age_matched_played():
    
    retorno = []
    idades =  []
    nome   =  []
    matches_played = []
    
    a = select([players_table.c.p_age, players_table.c.p_name ])
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        aux = retorno[i][0]
        idades.append(aux[12:14])
        a = select([stats_table.c.s_titular]).where(
                    and_(
                        stats_table.c.s_name == retorno[i][1],
                        stats_table.c.s_year == "2018"
                    ) )        
        for row in a.execute():
            matches_played.append(row[0])


    idades = list(map(int, idades))   

    data = [(y, c) for c, y in zip(idades, matches_played)]
   
    return data

#RETORNA MAIS VIOLENTOS DO TIME
def champ_most_violent():
    
    retorno = []

    a = select([stats_table.c.s_name, stats_table.c.s_yellow_card, stats_table.c.s_red_card, stats_table.c.s_club]).where(
                and_(
                    stats_table.c.s_year == "2018",
                    stats_table.c.s_champ == "Brasileirão Série A",
                ) )

    for row in a.execute():
        retorno.append(row)

    player = []
    gols = []
    position = []
    data = {}
    club = []
    photo = []

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        gols.append(retorno[i][1]+retorno[i][2])
        club.append(retorno[i][3])
        a = select([players_table.c.p_position, players_table.c.p_photo]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                ) )
        for row in a.execute():
             position.append(row[0])
             photo.append(row[1])         
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "club": m, "photo": f} for c, y, p, m, f in zip(player, gols, position, club, photo)]    
   
   #FAZ A CLASSIFICAO
    mysorted = sorted(data, key=lambda x : x['goals'], reverse=True)
   
    return mysorted[0:5]

#RETORNA ARTILHHEIROS DO TIME
def champ_best_goals():
    
    retorno = []

    a = select([stats_table.c.s_name, stats_table.c.s_gols, stats_table.c.s_club]).where(
                and_(
                    stats_table.c.s_year == "2018",
                    stats_table.c.s_champ == "Brasileirão Série A",
                ) )
    for row in a.execute():
        retorno.append(row)


    player = []
    gols = []
    position = []
    data = {}
    club = []
    photo = []
    
    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
         player.append(retorno[i][0])
         gols.append(retorno[i][1])
         club.append(retorno[i][2])
         a = select([players_table.c.p_position, players_table.c.p_photo]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                ) )
         for row in a.execute():
             position.append(row[0])
             photo.append(row[1])
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "club": m, "photo": f} for c, y, p, m, f in zip(player, gols, position, club, photo)]        
    
   #FAZ A CLASSIFICAO
    mysorted = sorted(data, key=lambda x : x['goals'], reverse=True)

    return mysorted[0:5]

#RETORNA ARTILHHEIROS DO TIME
def champ_most_played():
    
    retorno = []

    a = select([stats_table.c.s_name, stats_table.c.s_matches_played, stats_table.c.s_club]).where(
                and_(
                    stats_table.c.s_year == "2018",
                    stats_table.c.s_champ == "Brasileirão Série A",
                ) )
    for row in a.execute():
        retorno.append(row)

    player = []
    gols = []
    position = []
    data = {}
    club = []
    photo = []

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        gols.append(retorno[i][1])
        club.append(retorno[i][2])
        a = select([stats_table.c.s_matches_played, stats_table.c.s_gols]).where(
             and_(
                    stats_table.c.s_name == retorno[i][0],
                ) )
           
        for row in a.execute():
             position.append(row[0])
             photo.append(row[1])
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "club": m, "photo": f} for c, y, p, m, f in zip(player, gols, position, club, photo)]        
   
   #FAZ A CLASSIFICAO
    mysorted = sorted(data, key=lambda x : x['goals'], reverse=True)
   
    return mysorted[0:5]


#RETORNA ARTILHHEIROS DO TIME
def champ_in_out_victory():
    
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
    transition='200ms ease-in')    
    
    retorno = []

    a = select([club_table.c.c_n_win, club_table.c.c_name])
    
    for row in a.execute():
        retorno.append(row)

    line_chart = pygal.HorizontalBar(style=custom_style)
    
    print(retorno)
    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        line_chart.add(retorno[i][1], retorno[i][0])
        

 
   
    return line_chart

#RETORNA ARTILHHEIROS DO TIME
def champ_player_per_position():


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
    
    retorno = []
    goleiros   = 0
    defensores = 0 
    meias      = 0
    atacantes  = 0

    a = select([players_table.c.p_position])
               
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
        if retorno[i][0] == "Goalkeeper":
             goleiros = goleiros + 1
        elif retorno[i][0] == "Defender":
            defensores = defensores + 1
        elif retorno[i][0] == "Midfielder":   
            meias = meias + 1
        elif retorno[i][0] == "Attacker":  
            atacantes = atacantes + 1
            
    radar_chart = pygal.Radar(style=custom_style)
    radar_chart.x_labels = ['Goalkeeper', 'Defender', 'Midfielder', 'Attacker']
    radar_chart.add('Brasileirão 2018', [goleiros, defensores, meias, atacantes])
    
    return radar_chart

#RETORNA ARTILHHEIROS DO TIME
def champ_player_per_position_club():
    
    retorno = []
    retorno2 = []

    radar_chart = pygal.Radar()
    radar_chart.title = 'V8 benchmark results'
    radar_chart.x_labels = ['Goalkeeper', 'Defender', 'Midfielder', 'Attacker']
    
    a = select([players_table.c.p_club])
               
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
        b = select([players_table.c.p_position]).where(players_table.c.p_club == retorno[i][0])
                   
             
        for r in b.execute():
            retorno2.append(r)

        goleiros   = 0
        defensores = 0 
        meias      = 0
        atacantes  = 0
                    
        for j, val in enumerate(retorno2):
           
            if retorno2[j][0] == "Goalkeeper":
                 goleiros = goleiros + 1
            elif retorno2[j][0] == "Defender":
                defensores = defensores + 1
            elif retorno2[j][0] == "Midfielder":   
                meias = meias + 1
            elif retorno2[j][0] == "Attacker":  
                atacantes = atacantes + 1
                
        radar_chart.add(retorno[i][0], [goleiros, defensores, meias, atacantes])
       


    
    
    return radar_chart

if __name__ == '__main__':
    champ_data()   
