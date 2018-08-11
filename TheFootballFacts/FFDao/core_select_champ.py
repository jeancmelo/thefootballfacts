# -*- coding: utf-8 -*-

'''
Created on 8 de ago de 2018

@author: jeanm
'''
from sqlalchemy import select, and_

from FFDao.core import players_table, stats_table, club_table
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
        idades.append(retorno[i][0])
   
    idades = list(map(int, idades))          

    return idades

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

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        gols.append(retorno[i][1]+retorno[i][2])
        club.append(retorno[i][3])
        a = select([players_table.c.p_position]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                ) )
        for row in a.execute():
             position.append(row[0])         
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "club": m} for c, y, p, m in zip(player, gols, position, club)]    
   
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
    
    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
         player.append(retorno[i][0])
         gols.append(retorno[i][1])
         club.append(retorno[i][2])
         a = select([players_table.c.p_position]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                ) )
         for row in a.execute():
             position.append(row[0])
         
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "club": m} for c, y, p, m in zip(player, gols, position, club)]        
    
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

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        gols.append(retorno[i][1])
        club.append(retorno[i][2])
        a = select([players_table.c.p_position]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                ) )
           
        for row in a.execute():
             position.append(row[0])
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "club": m} for c, y, p, m in zip(player, gols, position, club)]        
   
   #FAZ A CLASSIFICAO
    mysorted = sorted(data, key=lambda x : x['goals'], reverse=True)
   
    return mysorted[0:5]


#RETORNA ARTILHHEIROS DO TIME
def champ_in_out_victory():
    
    retorno = []

    a = select([club_table.c.c_n_win, club_table.c.c_name])
    
    for row in a.execute():
        retorno.append(row)

    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Goals Por Time'
    
    print(retorno)
    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        line_chart.add(retorno[i][1], retorno[i][0])
        

 
   
    return line_chart

#RETORNA ARTILHHEIROS DO TIME
def champ_player_per_position():
    
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
            
    radar_chart = pygal.Radar()
    radar_chart.title = 'V8 benchmark results'
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


