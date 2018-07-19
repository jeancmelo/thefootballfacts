from FFClass.Player import Player
from FFDao import Dao

bd = Dao

class UtilPlayer(object):
	
	"""docstring for UtilPlayer"""
	def __init__(self, player):
		pass
	
	#DEFINIR SCORE DO GOLEIRO
	def score_player_keeper(self, player):
		pass
		
	#DEFINIR SCORE DO ZAGUEIRO
	def score_player_defender(self, player):
		score = 0
		
		#ETAPA DE AGREGAÇAO
		score = score + (player.p_gols*5)
		score = score + (player.p_assistence*4)
		score = score + (player.p_matches_played*1)
		
		#ETAPA DE DOWGRADE
		score = score - (player.p_red_card*5)
		score = score - (player.p_yellow_card*3)
		score = score - (player.p_matches_played*1)
		
		#ADICIONA O SCORE AO PLAYER (NAO GRAVA NO BANCO)
		player.player_score = score
		
		return player
	
	#DEFINIR SCORE DO MEIA
	def score_player_midfielder(self, player):
		score = 0
		
		#ETAPA DE AGREGAÇAO
		score = score + (player.p_gols*5)
		score = score + (player.p_assistence*4)
		score = score + (player.p_matches_played*1)
		
		#ETAPA DE DOWGRADE
		score = score - (player.p_red_card*5)
		score = score - (player.p_yellow_card*3)
		score = score - (player.p_matches_played*1)
		
		#ADICIONA O SCORE AO PLAYER (NAO GRAVA NO BANCO)
		player.player_score = score
		
		return player
		
	
	#DEFINIR SCORE DO ATACANTE
	def score_player_forward(self, player):
		
		score = 0
		
		#ETAPA DE AGREGACAO
		score = score + (player.p_gols*5)
		score = score + (player.p_assistence*4)
		score = score + (player.p_matches_played*1)
		
		#ETAPA DE DOWGRADE
		score = score - (player.p_red_card*5)
		score = score - (player.p_yellow_card*3)
		score = score - (player.p_matches_played*1)
		
		#ADICIONA O SCORE AO PLAYER (NAO GRAVA NO BANCO)
		player.player_score = score
		
		return player


	def best_5_players(self, Arr_Players):
		
		up = UtilPlayer 
		best_scores = []
		name_best_player = []
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12], player_name[13]) 
			
			#VERIFICANDO O POSICIONAMENTO
			if (p.player_position == "Forward"):
				p = up.score_player_forward("", p)
				#best_scores.append(p)
			elif(p.player_position == "Midfielder"):
				p = up.score_player_midfielder("", p)
				#best_scores.append(p)
				pass
			elif(p.player_position == "Defender"):
				p = up.score_player_defender("", p)
				#best_scores.append(p)
				pass
			elif(p.player_position == "Goalkeeper"):
				pass
			
			#ADICIONA OS MELHORES 5 (BobbleSort)
			if len(best_scores) < 5:
				best_scores.append(p)
			else:
				if p.player_score > best_scores[0].player_score:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = best_scores[1]
					best_scores[1] = best_scores[0]
					best_scores[0] = p
				elif p.player_score > best_scores[1].player_score:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = best_scores[1]
					best_scores[1] = p													
				elif p.player_score > best_scores[2].player_score:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = p
				elif p.player_score > best_scores[3].player_score:
					best_scores[4] = best_scores[3]
					best_scores[3] = p
				elif p.player_score > best_scores[4].player_score:
					best_scores[4] = p
				
																	
				#ORDENA O ARRAY Bubble Sort
				for bp in range(len(best_scores)-1,0,-1):
					for i in range(bp):
						if best_scores[i].player_score>best_scores[i+1].player_score:
							temp = best_scores[i]
							best_scores[i] = best_scores[i+1]
							best_scores[i+1] = temp
			
							
		for bp in best_scores:
			name_best_player.append(bp.player_name)	
			
		return name_best_player
			
	def worst_5_players(self, Arr_Players):
		
		up = UtilPlayer 
		worst_players = []
		name_worst_player = []
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12], player_name[13]) 
			
			#VERIFICANDO O POSICIONAMENTO
			if (p.player_position == "Forward"):
				p = up.score_player_forward("", p)
				#worst_players.append(p)
			elif(p.player_position == "Midfielder"):
				p = up.score_player_midfielder("", p)
				#worst_players.append(p)
				pass
			elif(p.player_position == "Defender"):
				p = up.score_player_defender("", p)
				#worst_players.append(p)
				pass
			elif(p.player_position == "Goalkeeper"):
				pass
			
			#ADICIONA OS MELHORES 5 (BobbleSort)
			if len(worst_players) < 5:
				worst_players.append(p)
			else:
				if p.player_score < worst_players[0].player_score:
					worst_players[4] = worst_players[3]
					worst_players[3] = worst_players[2]
					worst_players[2] = worst_players[1]
					worst_players[1] = worst_players[0]
					worst_players[0] = p
				elif p.player_score < worst_players[1].player_score:
					worst_players[4] = worst_players[3]
					worst_players[3] = worst_players[2]
					worst_players[2] = worst_players[1]
					worst_players[1] = p													
				elif p.player_score < worst_players[2].player_score:
					worst_players[4] = worst_players[3]
					worst_players[3] = worst_players[2]
					worst_players[2] = p
				elif p.player_score < worst_players[3].player_score:
					worst_players[4] = worst_players[3]
					worst_players[3] = p
				elif p.player_score < worst_players[4].player_score:
					worst_players[4] = p
				
																	
				#ORDENA O ARRAY Bubble Sort
				for bp in range(len(worst_players)-1,0,-1):
					for i in range(bp):
						if worst_players[i].player_score<worst_players[i+1].player_score:
							temp = worst_players[i]
							worst_players[i] = worst_players[i+1]
							worst_players[i+1] = temp
			
							
		for bp in worst_players:
			name_worst_player.append(bp.player_name)	
			
		return name_worst_player
	
	def best_scores(self, Arr_Players):
		
		best_scores = []
		name_best_player = []
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12], player_name[13]) 
			
			#ADICIONA OS MELHORES 5 (BobbleSort)
			if len(best_scores) < 5:
				best_scores.append(p)
			else:
				if p.p_gols > best_scores[0].p_gols:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = best_scores[1]
					best_scores[1] = best_scores[0]
					best_scores[0] = p
				elif p.p_gols > best_scores[1].p_gols:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = best_scores[1]
					best_scores[1] = p													
				elif p.p_gols > best_scores[2].p_gols:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = p
				elif p.p_gols > best_scores[3].p_gols:
					best_scores[4] = best_scores[3]
					best_scores[3] = p
				elif p.p_gols > best_scores[4].p_gols:
					best_scores[4] = p
							
		for bp in best_scores:
			name_best_player.append(bp.player_name)	
			
		return name_best_player
	
	def best_assistence(self, Arr_Players):
		
		best_scores = []
		name_best_player = []
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12], player_name[13]) 
			
			#ADICIONA OS MELHORES 5 (BobbleSort)
			if len(best_scores) < 5:
				best_scores.append(p)
			else:
				if p.p_assistence > best_scores[0].p_assistence:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = best_scores[1]
					best_scores[1] = best_scores[0]
					best_scores[0] = p
				elif p.p_assistence > best_scores[1].p_assistence:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = best_scores[1]
					best_scores[1] = p													
				elif p.p_assistence > best_scores[2].p_assistence:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = p
				elif p.p_assistence > best_scores[3].p_assistence:
					best_scores[4] = best_scores[3]
					best_scores[3] = p
				elif p.p_assistence > best_scores[4].p_assistence:
					best_scores[4] = p
							
		for bp in best_scores:
			name_best_player.append(bp.player_name)	
			
		return name_best_player	
	
	def more_played(self, Arr_Players):
		
		best_scores = []
		name_best_player = []
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12], player_name[13]) 
			
			#ADICIONA OS MELHORES 5 (BobbleSort)
			if len(best_scores) < 5:
				best_scores.append(p)
			else:
				if p.p_played_time > best_scores[0].p_played_time:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = best_scores[1]
					best_scores[1] = best_scores[0]
					best_scores[0] = p
				elif p.p_played_time > best_scores[1].p_played_time:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = best_scores[1]
					best_scores[1] = p													
				elif p.p_played_time > best_scores[2].p_played_time:
					best_scores[4] = best_scores[3]
					best_scores[3] = best_scores[2]
					best_scores[2] = p
				elif p.p_played_time > best_scores[3].p_played_time:
					best_scores[4] = best_scores[3]
					best_scores[3] = p
				elif p.p_played_time > best_scores[4].p_played_time:
					best_scores[4] = p
							
		for bp in best_scores:
			name_best_player.append(bp.player_name)	
			
		return name_best_player		
	
	
		