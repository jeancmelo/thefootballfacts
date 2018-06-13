class Club(object):
	"""docstring for Club"""

	#ATRIBUTOS DO CLUBE
	club_name           = "vazio"
	club_fundation_Date = "vazio"
	club_country        = "vazio"
	club_city           = "vazio"
	club_logo           = "vazio"

	#ATRIBUTOS DE PERFORMANCE GERAIS DO CLUBE
	club_n_win = 0
	club_n_defeat  = 0
	club_n_tie     = 0
	
	#ATRIBUTOS DE PERFORMANCE ESPECÍFICAS DO CLUBE
	club_g_win_in   = 0
	club_g_win_out  = 0

	#JOGADORES DO CLUB
	club_players = []


	def __init__(self, club_name, club_country, club_players):

		self.club_name = club_name
		self.club_country = club_country
		self.club_players = club_players
		