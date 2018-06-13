class Championship(object):
	"""docstring for Championship"""

	#ATRIBUTOS DO CAMPEONATO
	champ_name = "vazio"
	champ_type = "vazio"
	champ_game = "vazio"
	champ_table = []
	champ_club = []
		
	def __init__(self, champ_name, champ_type, champ_game, champ_table, champ_club):
	
		self.champ_name = champ_name
		self.champ_type = champ_type			
		self.champ_game = champ_game			
		self.champ_table = champ_table
		self.champ_club = champ_club			

	def oi(self):
		print(self.c_name)