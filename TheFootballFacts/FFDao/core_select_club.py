# -*- coding: utf-8 -*-

'''
Created on 24 de jul de 2018

@author: jeanm
'''
import re

from sqlalchemy import select, and_, or_

from FFDao.core import players_table, stats_table, club_table, champ_table
from numpy import integer
from _operator import contains
import json
from FFutils import UtilPlayer, UtilArea
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
    
    retorno           = []
    club_n_win_out    = 0
    club_n_defeat_out = 0
    rate_win          = 0
    rate_defeat       = 0
    rate_tie          = 0
    disputed_matches  = 0
    
    a = select([club_table]).where(club_table.c.c_name == c_name)
    for row in a.execute():
        retorno.append(row)

    try:
        club_n_win_out       = (retorno[0][7] - retorno[0][4])*-1
        club_n_defeat_out    = (retorno[0][8] - retorno[0][5])*-1
        rate_win             = round(retorno[0][7]/(retorno[0][7] - retorno[0][4])*-1, 2)
        rate_defeat          = round(retorno[0][8]/(retorno[0][8] - retorno[0][5])*-1, 2)
        rate_tie             = round(retorno[0][9]/(retorno[0][9] - retorno[0][6])*-1, 2)    
        disputed_matches     = retorno[0][4] + retorno[0][5] + retorno[0][6]
    except:
        pass

    #TRANSFORMA EM JSON     
    data = [{"club_name": retorno[0][1], "club_country": "Brasil", "club_fundation_Date": retorno[0][2],"club_emblem": retorno[0][3],"club_n_win": retorno[0][4],
             "club_n_defeat": retorno[0][5], "club_n_tie": retorno[0][6], "club_n_win_in": retorno[0][7],"club_n_defeat_in": retorno[0][8],
             "club_n_tie_in": retorno[0][9],"club_n_win_out": club_n_win_out, "club_n_defeat_out": club_n_defeat_out, "rate_win": rate_win, "rate_defeat": rate_defeat, 
             "rate_tie": rate_tie, "disputed_matches": disputed_matches}]
    
    return data       

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
    photo    = []
    data = {}
    
    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
         player.append(retorno[i][0])
         gols.append(retorno[i][1])
         a = select([players_table.c.p_position, players_table.c.p_photo]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                    players_table.c.p_club == c_club.capitalize()
                ) )
         for row in a.execute():
             position.append(row[0])
             photo.append(row[1])
         
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "photo": f} for c, y, p, f in zip(player, gols, position, photo)]        
    
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
    photo    = []
    data = {}

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        gols.append(retorno[i][1])
        a = select([players_table.c.p_position, players_table.c.p_photo]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                    players_table.c.p_club == c_club.capitalize()
                ) )
           
        for row in a.execute():
             position.append(row[0])
             photo.append(row[1])
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "photo": f} for c, y, p, f in zip(player, gols, position, photo)]  
   
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
    photo    = []
    data = {}

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        gols.append(retorno[i][1]+retorno[i][2])
        a = select([players_table.c.p_position, players_table.c.p_photo]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                    players_table.c.p_club == c_club.capitalize()
                ) )
        for row in a.execute():
             position.append(row[0])         
             photo.append(row[1])
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "goals": y, "position": p, "photo": f} for c, y, p, f in zip(player, gols, position, photo)]    
   
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
    photo    = []
    position = []
    data = {}

    #LISTA DE CLUBES QUE JA ATUOU
    i  = 0
    for i, val in enumerate(retorno):
        player.append(retorno[i][0])
        a = select([players_table.c.p_position, players_table.c.p_photo]).where(
             and_(
                    players_table.c.p_name == retorno[i][0],
                    players_table.c.p_club == c_club.capitalize()
                ) )        
        for row in a.execute():
             position.append(row[0])
             photo.append(row[1])         
    
    #TRANSFORMA EM JSON     
    data = [{"player": c, "position": p, "photo" : f} for c, p, f in zip(player, position, photo)]   
        
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
    mysorted = sorted(data, key=lambda x : x['score'], reverse=True)
   
    return mysorted[0:6]        
        

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
    mysorted = sorted(data, key=lambda x : x['score'], reverse=False)
    #mysorted.sort(reverse=True)
       
    return mysorted[0:5]        


def Scores_per_area(c_club):

    retorno = []
    player  = []
    goalkeepr   = 0
    defensor    = 0
    midle       = 0
    attacant    = 0
    data = []
    
    up = UtilPlayer
    
    a = select([players_table.c.p_name, players_table.c.p_position]).where(
                and_(
                    players_table.c.p_club == c_club.capitalize(),
                ) )
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
        if retorno[i][1] == "Goalkeeper":
             goalkeepr = goalkeepr + up.score_player_keeper(retorno[i][0], c_club)
        elif retorno[i][1] == "Defender":
             defensor = defensor + up.score_player_defender(retorno[i][0], c_club)
        elif retorno[i][1] == "Midfielder":   
             midle = midle + up.score_player_midfielder(retorno[i][0], c_club)
        elif retorno[i][1] == "Attacker":  
             attacant = attacant + up.score_player_forward(retorno[i][0], c_club)

    data.append(goalkeepr)
    data.append(defensor)
    data.append(midle)
    data.append(attacant)
    
       
    return data        

def club_best_formation(c_club):

    retorno = []
    
    goalkeeper = []
    defender   = []
    midfielder = []
    forward    = []
    
    goalkeeper_name = []
    defender_name   = []
    midfielder_name = []
    forward_name    = []
    
    goalkeeper_position = []
    defender_position   = []
    midfielder_position = []
    forward_position    = []
    
    goalkeeper_photo = []
    defender_photo  = []
    midfielder_photo = []
    forward_photo    = []    


    up = UtilPlayer
    
    a = select([players_table.c.p_name, players_table.c.p_position, players_table.c.p_photo]).where(
                and_(
                    players_table.c.p_club == c_club.capitalize(),
                ) )
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        if retorno[i][1] == "Goalkeeper":
             goalkeeper.append(up.score_player_keeper(retorno[i][0], c_club))
             goalkeeper_name.append(retorno[i][0])
             goalkeeper_position.append(retorno[i][1])
             goalkeeper_photo.append(retorno[i][2])
        elif retorno[i][1] == "Defender":
             defender.append(up.score_player_defender(retorno[i][0], c_club))
             defender_name.append(retorno[i][0])
             defender_position.append(retorno[i][1])
             defender_photo.append(retorno[i][2])
        elif retorno[i][1] == "Midfielder":   
             midfielder.append(up.score_player_midfielder(retorno[i][0], c_club))
             midfielder_name.append(retorno[i][0])
             midfielder_position.append(retorno[i][1])
             midfielder_photo.append(retorno[i][2])             
        elif retorno[i][1] == "Attacker":  
             forward.append(up.score_player_forward(retorno[i][0], c_club))
             forward_name.append(retorno[i][0])
             forward_position.append(retorno[i][1])
             forward_photo.append(retorno[i][2])
    
    
    #TRANSFORMA EM JSON     
    goalkeeper_data = [{"player": c, "score":s, "position": p, "photo": f} for c, s, p, f in zip(goalkeeper_name, goalkeeper, goalkeeper_position, goalkeeper_photo)]
    
    #adicao
    #TRANSFORMA EM JSON     
    defender_data = [{"player": c, "score":s, "position": p, "photo": f} for c, s, p, f in zip(defender_name, defender, defender_position, defender_photo)]   
    
    #TRANSFORMA EM JSON     
    midfielder_data = [{"player": c, "score":s, "position": p, "photo": f} for c, s, p, f in zip(midfielder_name, midfielder, midfielder_position, midfielder_photo)]   
    
    #TRANSFORMA EM JSON     
    forward_data = [{"player": c, "score":s, "position": p, "photo": f} for c, s, p, f in zip(forward_name, forward, forward_position, forward_photo)]                  
    
    #FAZ A CLASSIFICAO
    goalkeeper_data = sorted(goalkeeper_data, key=lambda x : x['score'], reverse=True)
    defender_data   = sorted(defender_data, key=lambda x : x['score'], reverse=True)
    midfielder_data = sorted(midfielder_data, key=lambda x : x['score'], reverse=True)
    forward_data    = sorted(forward_data, key=lambda x : x['score'], reverse=True)            
    
    #ABRE A CHAMADA PARA FUNÇÃO QUE FAZ A ESCOLHE DA MELHOR FORMAÇÃO
    ua = UtilArea
    
    best_form = ua.best_formation_test(goalkeeper_data, defender_data, midfielder_data, forward_data)

    return best_form
    
def club_last_games(c_club):

    retorno    = []
    home   = []
    away   = []
    placar = []
    data   = []
    
    a = select([champ_table]).where(
                or_(
                    champ_table.c.c_home == c_club.capitalize(),
                    champ_table.c.c_away == c_club.capitalize(),
                ) )
    
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        if retorno[i][3] != " vs":
            home.append(retorno[i][1])
            away.append(retorno[i][2])
            placar.append(retorno[i][3])
            data.append(retorno[i][4])
            #last_games.append(retorno[i]) 
            
    
    #TRANSFORMA EM JSON     
    last_games = [{"data": c, "home":s, "placar": p, "away": f} for c, s, p, f in zip(data, home, placar, away)]                  
    
    return last_games[0:5]
    

def club_next_games(c_club):

    retorno    = []
    home   = []
    away   = []
    placar = []
    data   = []
    
    a = select([champ_table]).where(
                or_(
                    champ_table.c.c_home == c_club.capitalize(),
                    champ_table.c.c_away == c_club.capitalize(),
                ) )
    
    
    for row in a.execute():
        retorno.append(row)
        
    for i, val in enumerate(retorno):
        if retorno[i][3] == " vs":
            home.append(retorno[i][1])
            away.append(retorno[i][2])
            placar.append(retorno[i][3])
            data.append(retorno[i][4])
            #last_games.append(retorno[i]) 
            
    
    #TRANSFORMA EM JSON     
    next_games = [{"data": c, "home":s, "placar": p, "away": f} for c, s, p, f in zip(data, home, placar, away)]                  
    
    return next_games[0:5]    
    
        
if __name__ == '__main__':
    select_club_by_name("bahia")   
    


        