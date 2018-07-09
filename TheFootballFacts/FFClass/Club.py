class Club(object):
	"""docstring for Club"""
	
	def __init__(self, club_name, club_fundation_Date = "", club_country = "", club_city = "", club_emblem = "", club_n_win=0, club_n_defeat = 0, club_n_tie=0, club_n_win_in=0, club_n_defeat_in=0, club_n_tie_in=0 ):

		#ATRIBUTOS DO CLUBE
		self.club_name        		= club_name
		self.club_fundation_Date    = club_fundation_Date
		self.club_country        	= club_country
		self.club_city              = club_city
		self.club_emblem            = club_emblem
		
		#ATRIBUTOS DE PERFORMANCE GERAIS DO CLUBE
		self.club_n_win 			= club_n_win
		self.club_n_defeat  		= club_n_defeat
		self.club_n_tie			    = club_n_tie
		
		#ATRIBUTOS DE PERFORMANCE ESPECÃ�FICAS DO CLUBE
		self.club_n_win_in          = club_n_win_in
		self.club_n_defeat_in  		= club_n_defeat_in
		self.club_n_tie_in  		= club_n_tie_in
	


