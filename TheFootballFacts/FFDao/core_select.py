# -*- coding: utf-8 -*-

'''
Created on 24 de jul de 2018

@author: jeanm
'''
import re

from sqlalchemy import select, and_

from FFDao.core import players_table, stats_table, club_table

retorno = []
a = select([stats_table.c.s_min_played, stats_table.c.s_name] ).where(
                and_(
                    stats_table.c.s_club == 'Flamengo',
                    stats_table.c.s_year == '2018',
                    stats_table.c.s_champ == 'Brasileirão Série A'
                ) )
for row in a.execute():
    retorno.append(row)
    
print(retorno)       

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

        