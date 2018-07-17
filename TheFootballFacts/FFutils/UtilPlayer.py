from FFClass.Player import Player
from FFDao import Dao

bd = Dao

class UtilPlayer(object):
	
	"""docstring for UtilPlayer"""
	def __init__(self, Player):
		pass
	
	#DEFINIR SCORE DO GOLEIRO
	def score_player_keeper(self, Player):
		pass
		
	#DEFINIR SCORE DO ZAGUEIRO
	def score_player_zagueiro(self, Player):
		pass
	
	#DEFINIR SCORE DO MEIA
	def score_player_meia(self, Player):
		score_player = Player.player_n_right_passes / Player.player_n_wrong_passes
	
		return score_player
		
	#DEFINIR SCORE DO LATERAL
	def score_player_lateral(self, Player):
		pass
	
	#DEFINIR SCORE DO ATACANTE
	def score_player_forward(self, Player):
		
		return 10


	def best_5_players(self, Arr_Players):
		
		uP = UtilPlayer 
		best_players = []
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[11], player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12]) 
			
			#VERIFICANDO O POSICIONAMENTO
			if (p.player_position == "Forward"):
				uP.score_player_forward("", p)
				
				
				best_players.append(p.player_name)

			elif(p.player_position == "Midfielder"):
				pass
			elif(p.player_position == "Defender"):
				pass
			elif(p.player_position == "Goalkeeper"):
				pass
			
			#ADICIONA OS MELHORES 5 (BobbleSort)
			
			
		return best_players
			
