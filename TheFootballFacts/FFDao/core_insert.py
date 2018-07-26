# -*- coding: utf-8 -*-
'''
Created on 24 de jul de 2018

@author: jeanm
'''
from FFDao import core
from FFDao.core import my_engine, players_table, stats_table

def insert_Player(p_name, p_name_completed, p_age, p_photo, p_nationality,p_position, p_club, p_city, p_heigth, p_foot, p_weight):

    conn = my_engine.connect()

    p_table = players_table.insert()
    
    new_player = p_table.values(p_name            = p_name,
                                p_name_completed  = p_name_completed,
                                p_age             = p_age,
                                p_photo           = p_photo,
                                p_nationality     = p_nationality,
                                p_position        = p_position,
                                p_club            = p_club,
                                p_city            = p_city,
                                p_heigth          = p_heigth,
                                p_foot            = p_foot,
                                p_weight          = p_weight
                                )
    
    conn.execute(new_player)

def insert_Stats(s_name, s_name_completed, s_club, s_year, s_matches_played, s_gols, s_assistence, s_yellow_card, s_red_card, s_sec_yellow_card, 
                  s_min_played, s_titular, s_substituido):

    conn = my_engine.connect()

    p_table = stats_table.insert()
    
    new_stats = p_table.values(s_name             = s_name,
                                s_name_completed  = s_name_completed,
                                s_club            = s_club,
                                s_year            = s_year,
                                s_matches_played  = s_matches_played,
                                s_gols            = s_gols,
                                s_assistence      = s_assistence,
                                s_yellow_card     = s_yellow_card,
                                s_red_card        = s_red_card,
                                s_sec_yellow_card = s_sec_yellow_card,
                                s_min_played      = s_min_played,
                                s_titular         = s_titular,
                                s_substituido     = s_substituido
                                )
    
    conn.execute(new_stats)