from FFClass.Player import Player

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
	def score_player_atacante(self, Player):
		pass


