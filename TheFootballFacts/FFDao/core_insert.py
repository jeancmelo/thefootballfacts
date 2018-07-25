'''
Created on 24 de jul de 2018

@author: jeanm
'''
from FFDao import core
from FFDao.core import my_engine, players_table




def insert_Player(p_name, p_name_completed, p_age, p_photo, p_nationality,p_position, p_club, p_matches_played, p_gols, p_assistence, p_yellow_card, p_red_card, p_sec_yellow_card, 
                  p_min_played, p_titular, p_substituido):

    conn = my_engine.connect()

    p_table = players_table.insert()
    
    new_player = p_table.values(p_name            = p_name,
                                p_name_completed  = p_name_completed,
                                p_age             = p_age,
                                p_photo           = p_photo,
                                p_nationality     = p_nationality,
                                p_position        = p_position,
                                p_club            = p_club,
                                p_matches_played  = p_matches_played,
                                p_gols            = p_gols,
                                p_assistence      = p_assistence,
                                p_yellow_card     = p_yellow_card,
                                p_red_card        = p_red_card,
                                p_sec_yellow_card = p_sec_yellow_card,
                                p_min_played      = p_min_played,
                                p_titular         = p_titular,
                                p_substituido     = p_substituido,
                                )
    
    conn.execute(new_player)
