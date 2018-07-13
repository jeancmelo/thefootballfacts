class Player(object):
	"""docstring for Player"""

	def __init__(self, player_name, player_club, player_position, player_age, player_nationality, p_matches_played, p_gols, p_assistence,
		              p_yellow_card, p_red_card, p_penaulti, p_played_time, player_photo=""):


		#ATRIBUTOS DO JOGADOR
		self.player_name           = player_name
		self.player_age            = player_age
		self.player_photo          = player_photo
		self.player_nationality    = player_nationality
		self.player_position       = player_position
		self.player_club 	 	   = player_club
	
		#ATRIBUTOS ESPECÃ�FICOS JOGADOR
		self.p_matches_played      = p_matches_played
		self.p_gols                = p_gols
		self.p_assistence          = p_assistence
		self.p_yellow_card         = p_yellow_card
		self.p_red_card            = p_penaulti
		self.p_played_time         = p_played_time										

	
		#STATUS DO JOGADOR (1 = Ok | 2 = CartÃ£o Amarelo | 3 - Expulso | 4 - Contundido)
		#player_status         = 1
	
		#ATRIBUTO DE MACHINE LEARNING
		#score_player          = 0
		
