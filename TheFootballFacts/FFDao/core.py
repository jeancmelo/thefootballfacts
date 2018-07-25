'''
Created on 24 de jul de 2018

@author: jeanm
'''
from datetime import datetime
from sqlalchemy import (create_engine, MetaData, Column,
                        Table, Integer, String, DateTime, ForeignKey)


my_engine = create_engine(r'sqlite:///C:\Users\jeanm\Desktop\banco\thefootball_teste.db')


metadata = MetaData(bind=my_engine)

players_table = Table('player', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('p_name', String(100), index=True),
                    Column('p_name_completed', String(200)),
                    Column('p_age', Integer, nullable=False),
                    Column('p_photo', String),
                    Column('p_nationality', String),
                    Column('p_position', String),
                    Column('p_club', String, ForeignKey("club.c_name"), nullable=False),
                    Column('p_matches_played', Integer),
                    Column('p_gols', Integer),
                    Column('p_assistence', Integer),
                    Column('p_yellow_card', Integer),   
                    Column('p_red_card', Integer),
                    Column('p_sec_yellow_card', Integer),   
                    Column('p_min_played', Integer),   
                    Column('p_titular', Integer),
                    Column('p_substituido', Integer),
                    Column('criado_em', DateTime, default=datetime.now),
                    Column('atualizado_em',
                           DateTime,
                           default=datetime.now,
                           onupdate=datetime.now))

club_table = Table('club', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('c_name', String(200), index=True),
                    Column('c_fundation', String(50)),
                    Column('c_emblem', String),
                    Column('c_n_win', Integer),
                    Column('c_n_defeat', Integer),
                    Column('c_n_tie', Integer),
                    Column('c_n_win_in', Integer),
                    Column('c_n_defeat_in', Integer),
                    Column('c_n_tie_in', Integer),
                    Column('criado_em', DateTime, default=datetime.now),
                    Column('atualizado_em',
                           DateTime,
                           default=datetime.now,
                           onupdate=datetime.now))

metadata.create_all()


def insert_Player(p_name, p_name_completed, p_age, p_photo, p_nationality,p_position, p_club, p_matches_played, p_gols, p_assistence, p_yellow_card, p_red_card, p_sec_yellow_card, 
                  p_min_played, p_titular, p_substituido):

    conn = my_engine.connect()

    p_table = players_table.insert()
    
    new_player = p_table.values(p_name            = p_name,
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
