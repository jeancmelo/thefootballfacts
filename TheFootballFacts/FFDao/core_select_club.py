# -*- coding: utf-8 -*-

'''
Created on 24 de jul de 2018

@author: jeanm
'''
import re

from sqlalchemy import select, and_

from FFDao.core import players_table, stats_table, club_table
from numpy import integer
from _operator import contains
import json
from FFutils import UtilPlayer
from audioop import reverse



def select_player_by_name(p_name):
    c_player = []
    a = select([players_table]).where(players_table.c.p_name == p_name)
    for row in a.execute():
        c_player.append(row)
        
    return c_player

def selec_stats_by_name(p_name):
    retorno = []
    a = select([stats_table]).where(
                and_(
                    stats_table.c.s_name == p_name,
                    stats_table.c.s_year == '2018'
                ) )
    for row in a.execute():
        retorno.append(row)
        
    return retorno   

def select_players():
    retorno = []
    a = select([players_table.c.p_name])
    
    for row in a.execute():
        retorno.append(row)
        
       
    return retorno   

def select_club_by_name(c_name):
    retorno = []
    a = select([club_table]).where(club_table.c.c_name == c_name)
    for row in a.execute():
        retorno.append(row)
        
    return retorno       

def select_top_players(c_name):
    retorno = []
    a = select([stats_table.c.s_matches_played, stats_table.c.s_name] ).where(
                and_(
                    stats_table.c.s_club == 'Flamengo',
                    stats_table.c.s_year == '2018',
                    stats_table.c.s_champ == 'Brasileirão Série A'
                ) )
    for row in a.execute():
        retorno.append(row)
    
    return retorno       

#RETORNA NÚMERO DE GOLS NAQUELE ANO
def Player_Goals_Year(p_name, p_year):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_gols]).where(
                and_(
                    stats_table.c.s_name == p_name,
                    stats_table.c.s_year == p_year
                ) )
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0] 
        
        
    return valor_retorno

#RETORNA NÚMERO DE TEMPO JOGADO
def Player_Time_Played(p_name, p_year):
    
    retorno = []
    valor_retorno = 0 
    
    a = select([stats_table.c.s_min_played]).where(
                and_(
                    stats_table.c.s_name == p_name,
                    stats_table.c.s_year == p_year
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0]         
        
    return valor_retorno

#RETORNA NÚMERO DE CARTÕES VERMELHOS        
def Player_Red_Cards(p_name, p_year):
    
    retorno = []
    valor_retorno = 0
     
    a = select([stats_table.c.s_red_card]).where(
                and_(
                    stats_table.c.s_name == p_name,
                    stats_table.c.s_year == p_year
                ) )
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0]         
        
    return valor_retorno

#RETORNA NÚMERO DE CARTÕES AMARELOS
def Player_Yellow_Cards(p_name, p_year):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_yellow_card]).where(
                and_(
                    stats_table.c.s_name == p_name,
                    stats_table.c.s_year == p_year
                ) )
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0]         
        
    return valor_retorno

#RETORNA NÚMERO DE JOGOS COMO TITULAR
def Player_Titular_Games(p_name, p_year):
    
    retorno = []
    valor_retorno = 0
        
    a = select([stats_table.c.s_titular]).where(
                and_(
                    stats_table.c.s_name == p_name,
                    stats_table.c.s_year == p_year
                ) )
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0]         
        
    return valor_retorno

#RETORNA GOLS POR ANO
def Player_Evolution_Goals_Year(p_name):
    
    retorno = []
    a = select([stats_table.c.s_gols, stats_table.c.s_year]).where(
                and_(
                    stats_table.c.s_name == p_name
                ) )
    for row in a.execute():
        retorno.append(row)
        
    return retorno   

#RETORNA TIMES QUE JÁ JOGOU
def Player_Club_Played(p_name):
    
    retorno = []
    a = select([stats_table.c.s_club, stats_table.c.s_year]).where(
                and_(
                    stats_table.c.s_name == p_name
                ) )
    for row in a.execute():
        retorno.append(row)
            
    clubs = []
    year = []
    data = {}

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        if retorno[i][0] in clubs:
            pass
        else:
            if len(clubs) >= 5:
                pass
            else:
                clubs.append(retorno[i][0])
                year.append(retorno[i][1])

    data = [{"club": c, "year": y} for c, y in zip(clubs, year)]

    return data

#RETORNA NÚMERO DE GOLS NAQUELE ANO
def Player_Goals_Year_Career(p_name):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_gols]).where(
                and_(
                    stats_table.c.s_name == p_name
                ) )
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0] 
        
        
    return valor_retorno

#RETORNA NÚMERO DE TEMPO JOGADO
def Player_Time_Played_Career(p_name):
    
    retorno = []
    valor_retorno = 0 
    
    a = select([stats_table.c.s_min_played]).where(
                and_(
                    stats_table.c.s_name == p_name
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0]         
        
    return valor_retorno

#RETORNA NÚMERO DE CARTÕES VERMELHOS        
def Player_Red_Cards_Career(p_name):
    
    retorno = []
    valor_retorno = 0
     
    a = select([stats_table.c.s_red_card]).where(
                and_(
                    stats_table.c.s_name == p_name
                ) )
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0]         
        
    return valor_retorno

#RETORNA NÚMERO DE CARTÕES AMARELOS
def Player_Yellow_Cards_Career(p_name):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_yellow_card]).where(
                and_(
                    stats_table.c.s_name == p_name
                ) )
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        if retorno[i][0].find("/") != -1:
            valor_retorno = valor_retorno + retorno[i][0]
        else:
            print(retorno[i][0])
            pass
            
    return valor_retorno

#RETORNA NÚMERO DE JOGOS COMO TITULAR
def Player_Titular_Games_Career(p_name):
    
    retorno = []
    valor_retorno = 0
        
    a = select([stats_table.c.s_titular]).where(
                and_(
                    stats_table.c.s_name == p_name
                ) )
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        valor_retorno = valor_retorno + retorno[i][0]         
        
    return valor_retorno

#RETORNA ARTILHHEIROS DO TIME
def Club_Best_Goals(c_club):
    
    retorno = []

    a = select([stats_table.c.s_name, stats_table.c.s_gols]).where(
                and_(
                    stats_table.c.s_club == c_club.capitalize(),
                    stats_table.c.s_year == "2018",
                ) )
    for row in a.execute():
        retorno.append(row)

    player = []
    gols = []
    position = []
    data = {}
    
    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
         player.append(retorno[i][0])
         gols.append(retorno[i][1])
         a = select([players_table.c.p_position]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                    players_table.c.p_club == c_club.capitalize()
                ) )
         for row in a.execute():
             position.append(row[0])
         
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p} for c, y, p in zip(player, gols, position)]        
    
   #FAZ A CLASSIFICAO
    mysorted = sorted(data, key=lambda x : x['goals'], reverse=True)

    return mysorted[0:5]

#RETORNA ARTILHHEIROS DO TIME
def Club_Most_Played(c_club):
    
    retorno = []

    a = select([stats_table.c.s_name, stats_table.c.s_matches_played]).where(
                and_(
                    stats_table.c.s_club == c_club.capitalize(),
                    stats_table.c.s_year == "2018"
                ) )
    for row in a.execute():
        retorno.append(row)

    player = []
    gols = []
    position = []
    data = {}

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        gols.append(retorno[i][1])
        a = select([players_table.c.p_position]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                    players_table.c.p_club == c_club.capitalize()
                ) )
           
        for row in a.execute():
             position.append(row[0])
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p} for c, y, p in zip(player, gols, position)]  
   
   #FAZ A CLASSIFICAO
    mysorted = sorted(data, key=lambda x : x['goals'], reverse=True)
   
    return mysorted[0:5]

#RETORNA MAIS VIOLENTOS DO TIME
def CLub_Most_Violent(c_club):
    
    retorno = []

    a = select([stats_table.c.s_name, stats_table.c.s_yellow_card, stats_table.c.s_red_card]).where(
                and_(
                    stats_table.c.s_club == c_club.capitalize(),
                    stats_table.c.s_year == "2018"
                ) )
    for row in a.execute():
        retorno.append(row)

    player = []
    gols = []
    position = []
    data = {}

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        gols.append(retorno[i][1]+retorno[i][2])
        a = select([players_table.c.p_position]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                    players_table.c.p_club == c_club.capitalize()
                ) )
        for row in a.execute():
             position.append(row[0])         
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p} for c, y, p in zip(player, gols, position)]    
   
   #FAZ A CLASSIFICAO
    mysorted = sorted(data, key=lambda x : x['goals'], reverse=True)
   
    return mysorted[0:5]

#RETORNA NÚMERO DE GOLS DO CLUB
def Club_goals(c_club):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_gols]).where(
                and_(
                    stats_table.c.s_club == c_club.capitalize(),
                    stats_table.c.s_year == "2018"
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
         valor_retorno = valor_retorno + retorno[i][0]
                
    return valor_retorno

#RETORNA NÚMERO DE GOLS DO CLUB
def Club_yellow_card(c_club):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_yellow_card]).where(
                and_(
                    stats_table.c.s_club == c_club.capitalize(),
                    stats_table.c.s_year == "2018"
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
         valor_retorno = valor_retorno + retorno[i][0]
                
    return valor_retorno

#RETORNA NÚMERO DE GOLS DO CLUB
def Club_red_card(c_club):
    
    retorno = []
    valor_retorno = 0
    
    a = select([stats_table.c.s_red_card]).where(
                and_(
                    stats_table.c.s_club == c_club.capitalize(),
                    stats_table.c.s_year == "2018"
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
         valor_retorno = valor_retorno + retorno[i][0]
                
    return valor_retorno

#RETORNA Nº DE JOGADORES POR POSICAO
def Club_get_number_per_position(c_club):
    
    goleiros   = 0
    defensores = 0 
    meias      = 0
    atacantes  = 0
    
    retorno   = []
    
    valor_retorno = 0
    
    a = select([players_table.c.p_position]).where(
                and_(
                    players_table.c.p_club == c_club.capitalize(),
                ) )
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
            
    #TRANSFORMA EM JSON     
    data = [{"goleiros": goleiros, "defensores": defensores, "meias": meias, "atacantes": atacantes}]
           
    return data

#RETORNA OS JOGADORES DO TIME
def Club_players(c_club):
    
    retorno = []
    
    a = select([stats_table.c.s_name]).where(
                and_(
                    stats_table.c.s_club == c_club.capitalize(),
                    stats_table.c.s_year == "2018",
                    stats_table.c.s_champ == "Brasileirão Série A"
                ) )
    for row in a.execute():
        retorno.append(row)

    player   = []
    position = []
    data = {}

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        a = select([players_table.c.p_position]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                    players_table.c.p_club == c_club.capitalize()
                ) )        
        for row in a.execute():
             position.append(row[0])         
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "position": p} for c, p in zip(player, position)]   
        
    return(data)

def Best_Score_Players(c_club):

    retorno = []
    player  = []
    score   = []
    
    up = UtilPlayer
    
    a = select([players_table.c.p_name, players_table.c.p_position]).where(
                and_(
                    players_table.c.p_club == c_club.capitalize(),
                ) )
    for row in a.execute():
        retorno.append(row)

    print(retorno[1][1])   
    for i, val in enumerate(retorno):
        if retorno[i][1] == "Goalkeeper":
             score.append(up.score_player_keeper(retorno[i][0], c_club))
        elif retorno[i][1] == "Defender":
             score.append(up.score_player_defender(retorno[i][0], c_club))
        elif retorno[i][1] == "Midfielder":   
             score.append(up.score_player_midfielder(retorno[i][0], c_club))
        elif retorno[i][1] == "Attacker":  
             score.append(up.score_player_forward(retorno[i][0], c_club))
        player.append(retorno[i][0])
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "score": s} for c, s in zip(player, score)]   

   #FAZ A CLASSIFICAO
    #mysorted = sorted(data, key=lambda x : x['score'], reverse=True)
   
    return data[0:5]        
        

def Wrots_Score_Players(c_club):

    retorno = []
    player  = []
    score   = []
    
    up = UtilPlayer
    
    a = select([players_table.c.p_name, players_table.c.p_position]).where(
                and_(
                    players_table.c.p_club == c_club.capitalize(),
                ) )
    for row in a.execute():
        retorno.append(row)

    print(retorno[1][1])   
    for i, val in enumerate(retorno):
        if retorno[i][1] == "Goalkeeper":
             score.append(up.score_player_keeper(retorno[i][0], c_club))
        elif retorno[i][1] == "Defender":
             score.append(up.score_player_defender(retorno[i][0], c_club))
        elif retorno[i][1] == "Midfielder":   
             score.append(up.score_player_midfielder(retorno[i][0], c_club))
        elif retorno[i][1] == "Attacker":  
             score.append(up.score_player_forward(retorno[i][0], c_club))
        player.append(retorno[i][0])
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "score":s} for c, s in zip(player, score)]   

   #FAZ A CLASSIFICAO
   # mysorted = sorted(data, key=lambda x : x['score'], reverse=True)
    #mysorted.sort(reverse=True)
       
    return data[0:5]        

        
if __name__ == '__main__':
    print(selec_stats_by_name("Réver"))   
    


        