# -*- coding: utf-8 -*-
from FFClass.Player import Player
from FFDao import Dao


from sqlalchemy import select, and_
from FFDao.core import players_table, stats_table, club_table


#DEFINIR SCORE DO GOLEIRO
def score_player_keeper(player, c_club):
	
	c_player = []
	a = select([stats_table]).where(
                and_(
					stats_table.c.s_name == player,
					stats_table.c.s_club == c_club.capitalize(),
					stats_table.c.s_champ == "Brasileirão Série A",
					stats_table.c.s_year  == "2018"
				) )
	
	for row in a.execute():
		c_player.append(row)
    
	gols         = c_player[0][6]
	#jogos         = c_player[0][5]
	penaulti     = c_player[0][7]
	titular	     = c_player[0][12]
	min_jogados  = c_player[0][11]	
	
	amarelo     = c_player[0][8]
	seg_amarelo	 = c_player[0][9]
	vermelho     = c_player[0][10]

	    
	score = 0
	
	#ETAPA DE AGREGAÇAO
	score = score + (gols*5)
	#score = score + (jogos*1)
	score = score + (penaulti*1)
	score = score + (titular*1)
	score = score + (min_jogados*1)	
	
	#ETAPA DE DOWGRADE
	score = score - (vermelho*5)
	score = score - (amarelo*3)
	score = score - (seg_amarelo*1)

		
	return score
	
#DEFINIR SCORE DO ZAGUEIRO
def score_player_defender(player, c_club):
	
	c_player = []
	a = select([stats_table]).where(
                and_(
					stats_table.c.s_name == player,
					stats_table.c.s_club == c_club.capitalize(),
					stats_table.c.s_champ == "Brasileirão Série A",
					stats_table.c.s_year  == "2018"
				) )
	
	for row in a.execute():
		c_player.append(row)
    
	gols         = c_player[0][6]
	jogos         = c_player[0][5]
	penaulti     = c_player[0][7]
	titular	     = c_player[0][12]
	min_jogados  = c_player[0][11]	
	
	amarelo     = c_player[0][8]
	seg_amarelo	 = c_player[0][9]
	vermelho     = c_player[0][10]
	
	    
	score = 0
	
	#ETAPA DE AGREGAÇAO
	score = score + (gols*5)
	#score = score + (jogos*1)
	score = score + (penaulti*1)
	score = score + (titular*1)
	score = score + (min_jogados*1)	
	
	#ETAPA DE DOWGRADE
	score = score - (vermelho*5)
	score = score - (amarelo*3)
	score = score - (seg_amarelo*1)

		
	return score

#DEFINIR SCORE DO MEIA
def score_player_midfielder(player, c_club):
	
	c_player = []
	a = select([stats_table]).where(
                and_(
					stats_table.c.s_name == player,
					stats_table.c.s_club == c_club.capitalize(),
					stats_table.c.s_champ == "Brasileirão Série A",
					stats_table.c.s_year  == "2018"
				) )
	
	for row in a.execute():
		c_player.append(row)
    
	gols         = c_player[0][6]
	jogos        = c_player[0][5]
	penaulti     = c_player[0][7]
	titular	     = c_player[0][12]
	min_jogados  = c_player[0][11]	
	
	amarelo      = c_player[0][8]
	seg_amarelo	 = c_player[0][9]
	vermelho     = c_player[0][10]
	
	    
	score = 0
	
	#ETAPA DE AGREGAÇAO
	score = score + (gols*5)
	#score = score + (jogos*1)
	score = score + (penaulti*1)
	score = score + (titular*1)
	score = score + (min_jogados*1)	
	
	#ETAPA DE DOWGRADE
	score = score - (vermelho*5)
	score = score - (amarelo*3)
	score = score - (seg_amarelo*1)
	
		
	return score
	

#DEFINIR SCORE DO ATACANTE
def score_player_forward(player, c_club):
	
	c_player = []
	a = select([stats_table]).where(
                and_(
					stats_table.c.s_name == player,
					stats_table.c.s_club == c_club.capitalize(),
					stats_table.c.s_champ == "Brasileirão Série A",
					stats_table.c.s_year  == "2018"
				) )
	
	for row in a.execute():
		c_player.append(row)
    
	gols         = c_player[0][6]
	jogos         = c_player[0][5]
	penaulti     = c_player[0][7]
	titular	     = c_player[0][12]
	min_jogados  = c_player[0][11]	
	
	amarelo     = c_player[0][8]
	seg_amarelo	 = c_player[0][9]
	vermelho     = c_player[0][10]
	
	    
	score = 0
	
	#ETAPA DE AGREGAÇAO
	score = score + (gols*5)
	#score = score + (jogos*1)
	score = score + (penaulti*1)
	score = score + (titular*1)
	score = score + (min_jogados*1)	
	
	#ETAPA DE DOWGRADE
	score = score - (vermelho*5)
	score = score - (amarelo*3)
	score = score - (seg_amarelo*1)

		
	return score



