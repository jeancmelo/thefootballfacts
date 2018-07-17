'''
Created on 15 de jun de 2018

@author: jeanm
'''
import sqlite3

#conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_minhaAgenda.db')
class Dao():

    def __init__(self, params):
        '''
        Constructor
        '''
    def consultar_Players(self, player_name):  
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        cursor = conn.execute("select * from player WHERE player_name LIKE ?", (player_name,))
        rows = cursor.fetchall()
        
        return rows
    
    def consultar_Players_by_Club(self, player_club):  
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        cursor = conn.execute("select * from player WHERE player_club LIKE ?", (player_club,))
        rows = cursor.fetchall()
        
        return rows

    def consultar_Players_by_Position(self, player_position, player_club):  
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        cursor = conn.execute("select * from player WHERE player_position LIKE ? AND player_club LIKE?", (player_position, player_club,))
        rows = cursor.fetchall()
        
        return rows
        
    def consultar_Club(self, club_name):  
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        cursor = conn.execute("select * from club WHERE club_name LIKE ?", (club_name,))
        rows = cursor.fetchall()
        
        return rows
    
    def consultar_all_Club(self):  
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        cursor = conn.execute("select * from club")
        rows = cursor.fetchall()
        
        return rows

    
    def consultar_Championship(self, nome):  
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        cursor = conn.execute("select * from championship WHERE nome LIKE ?", (nome,))
        rows = cursor.fetchall()
        
        return rows
    
    def add_club(self, club_name, club_n_win, club_n_defeat, club_n_tie, club_emblem, club_country, club_n_win_in, club_n_defeat_in, 
                 club_n_tie_in, club_fundation_Date="00/00/0000",  club_city="none"):
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        #VERIFICAR SE JA EXISTE E CASO NAO, ADICIONAR
        cursor = conn.execute("select club_name from club WHERE club_name LIKE ?", (club_name,))
        rows = cursor.fetchall()
        if not rows:
            conn.execute("""
            INSERT INTO club (club_name, club_fundation_Date, club_country, club_city, club_emblem, club_n_win, club_n_defeat, club_n_tie, club_n_win_in, club_n_defeat_in, club_n_tie_in )
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
           """, (club_name, club_fundation_Date, club_country, club_city, club_emblem, club_n_win, club_n_defeat, club_n_tie, club_n_win_in, club_n_defeat_in, club_n_tie_in))
            conn.commit()           
        else:
            pass
    
    
    def update_club(self, club_name, club_emblem, club_n_win, club_n_defeat, club_n_tie):
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        conn.execute('''UPDATE club SET club_emblem = ?, club_n_win = ?, club_n_defeat = ?, club_n_tie = ?  WHERE nome = ?''', (club_emblem, club_n_win, club_n_defeat, club_n_tie, club_name))

        conn.commit()
        
        
    def add_Player(self, player_name, player_club, player_position, player_age, p_matches_played, p_gols, p_assistence, p_yellow_card, p_red_card, p_penaulti, p_played_time, player_photo="", player_nationality="none"):
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        #VERIFICAR SE JA EXISTE E CASO NAO, ADICIONAR
        cursor = conn.execute("select * from player WHERE player_name LIKE ?", (player_name,))
        rows = cursor.fetchall()
        if not rows:
            conn.execute("""
            INSERT INTO player (player_name, player_age, player_photo, player_nationality, player_position, player_club, p_matches_played, p_gols, p_assistence, p_yellow_card, p_red_card, p_penaulti, p_played_time)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
           """, (player_name, player_age, player_photo, player_nationality, player_position, player_club, p_matches_played, p_gols, p_assistence, p_yellow_card, p_red_card, p_penaulti, p_played_time,))
            conn.commit()           
        else:
            pass
        
    def consultar_all_Players(self):  
        conn = sqlite3.connect('C:/Users/jeanm/Desktop/banco/sql_thefootbalfact.db')
        
        cursor = conn.execute("select * from player")
        rows = cursor.fetchall()
        
        return rows
    