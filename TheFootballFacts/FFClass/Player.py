class Player(object):
	"""docstring for Player"""

	def __init__(self, player_name, player_club, player_position, player_age, player_nationality, p_heigth, p_foot, p_weight, p_matches_played, p_gols, p_assistence,
		              p_yellow_card, p_red_card, p_penaulti, p_played_time, player_photo="", player_score=0):


		#ATRIBUTOS DO JOGADOR
		self.player_name           = player_name
		self.player_age            = player_age
		self.player_photo          = player_photo
		self.player_nationality    = player_nationality
		self.player_position       = player_position
		self.player_club 	 	   = player_club
		self.Player_height         = p_heigth
		self.p_foot                = p_foot
		self.p_heigth              = p_heigth
		self.p_weight              = p_weight
		
		#ATRIBUTOS ESPECÃ�FICOS JOGADOR
		self.p_matches_played      = p_matches_played
		self.p_gols                = p_gols
		self.p_assistence          = p_assistence
		self.p_yellow_card         = p_yellow_card
		self.p_red_card            = p_red_card
		self.p_played_time         = p_played_time			
		self.p_penaulti            = p_penaulti					

		#ATRIBUTO DE MACHINE LEARNING
		self.player_score               = player_score

	
		#STATUS DO JOGADOR (1 = Ok | 2 = CartÃ£o Amarelo | 3 - Expulso | 4 - Contundido)
		#player_status         = 1
	
		
