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
