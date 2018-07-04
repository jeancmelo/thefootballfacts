class Player(object):
	"""docstring for Player"""

	def __init__(self, player_name, player_age, player_photo, player_nationality, player_position, player_n_gols, player_n_disarm, player_n_right_passes,player_n_wrong_passes, player_n_kick):

		#ATRIBUTOS DO JOGADOR
		self.player_name        = player_name
		self.player_age         = player_age
		self.player_photo       = player_photo
		self.player_nationality = player_nationality
		self.player_position    = player_nationality
	
		#ATRIBUTOS ESPECÃ�FICOS JOGADOR
		self.player_n_gols         = player_n_gols
		self.player_n_disarm       = player_n_disarm
		self.player_n_right_passes = player_n_right_passes
		self.player_n_wrong_passes = player_n_wrong_passes
		self.player_n_kick         = player_n_kick
	
		#STATUS DO JOGADOR (1 = Ok | 2 = CartÃ£o Amarelo | 3 - Expulso | 4 - Contundido)
		#player_status         = 1
	
		#ATRIBUTO DE MACHINE LEARNING
		#score_player          = 0
		
