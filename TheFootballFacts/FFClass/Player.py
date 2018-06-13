class Player(object):
	"""docstring for Player"""

	#ATRIBUTOS DO JOGADOR
	player_name        = "vazio"
	player_age         = "vazio"
	player_photo       = "vazio"
	player_nationality = "vazio"
	player_position    = "vazio"

	#ATRIBUTOS ESPECÍFICOS JOGADOR
	player_n_gols         = 0
	player_n_disarm       = 0
	player_n_right_passes = 0
	player_n_wrong_passes = 0
	player_n_kick         = 0

	#STATUS DO JOGADOR (1 = Ok | 2 = Cartão Amarelo | 3 - Expulso | 4 - Contundido)
	player_status         = 1

	#ATRIBUTO DE MACHINE LEARNING
	score_player          = 0
	
	def __init__(self):

		self.player_name = player_name
		