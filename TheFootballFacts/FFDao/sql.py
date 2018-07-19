import sqlite3
conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
 
c = conn.cursor()

# criando a tabela (schema)
c.execute("""
CREATE TABLE player (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        player_name varchar(250) NOT NULL,
        player_age INTEGER NOT NULL,
        player_photo varchar(300) NOT NULL,
        player_nationality varchar(100) NOT NULL,
        player_position varchar(50) NOT NULL,
        player_club varchar(50) NOT NULL,
        p_matches_played INTEGER,
        p_gols INTEGER,
        p_assistence INTEGER,
        p_yellow_card INTEGER,
        p_red_card INTEGER,
        p_penaulti INTEGER,
        p_played_time INTEGER                                 
        );
        """)

c.execute("""
CREATE TABLE club (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        club_name varchar(250) NOT NULL,
        club_fundation_Date DATE,
        club_country varchar(300),
        club_city varchar(100) ,
        club_emblem varchar(50),
        club_n_win INTEGER,
        club_n_defeat INTEGER,
        club_n_tie INTEGER,
        club_n_win_in INTEGER,
        club_n_defeat_in INTEGER,
        club_n_tie_in INTEGER        
        );
        """)

c.execute("""
CREATE TABLE championship (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome varchar(250) NOT NULL,
        clubs varchar(250) NOT NULL                          
        );
        """)

conn.commit()
conn.close()
