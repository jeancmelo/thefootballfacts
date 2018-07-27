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
                    Column('p_name_completed', String(200), ForeignKey("stats_player.s_name_completed")),
                    Column('p_age', Integer, nullable=False),
                    Column('p_photo', String),
                    Column('p_city', String),
                    Column('p_heigth', String),     
                    Column('p_foot', String),     
                    Column('p_weight', String),                                                                        
                    Column('p_nationality', String),
                    Column('p_position', String),
                    Column('p_club', String, ForeignKey("club.c_name"), nullable=False),
                    Column('criado_em', DateTime, default=datetime.now),
                    Column('atualizado_em',
                           DateTime,
                           default=datetime.now,
                           onupdate=datetime.now))

stats_table = Table('stats_player', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('s_name', String(100), index=True),
                    Column('s_name_completed', String(200)),
                    Column('s_champ', String),  
                    Column('s_club', String),  
                    Column('s_year', String),                  
                    Column('s_matches_played', Integer),
                    Column('s_gols', Integer),
                    Column('s_assistence', Integer),
                    Column('s_yellow_card', Integer),   
                    Column('s_red_card', Integer),
                    Column('s_sec_yellow_card', Integer),   
                    Column('s_min_played', Integer),   
                    Column('s_titular', Integer),
                    Column('s_substituido', Integer),
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


def insert_Player(p_name, p_name_completed, p_age, p_photo, p_nationality,p_position, p_club):

    conn = my_engine.connect()

    p_table = players_table.insert()
    
    new_player = p_table.values(p_name            = p_name,
                                p_name_completed  = p_name_completed,
                                p_age             = p_age,
                                p_photo           = p_photo,
                                p_nationality     = p_nationality,
                                p_position        = p_position,
                                p_club            = p_club,
                                )
    
    conn.execute(new_player)
