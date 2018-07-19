from FFClass.Player import Player

class UtilClub(object):
	"""docstring for UtilClub"""
	def __init__(self, arg):
		super(UtilClub, self).__init__()
		self.arg = arg
		
	def goal_done(self, Arr_Players):

		goal_done = 0
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[11], player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12]) 
			
			goal_done = goal_done + p.p_gols
		
			return goal_done

	def yellow_cards(self, Arr_Players):
		
		yellow_cards = 0
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[11], player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12]) 
			
			yellow_cards = yellow_cards + p.p_yellow_card
		
			return yellow_cards

	def red_cards(self, Arr_Players):
		
		red_cards = 0
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[11], player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12]) 
			
			red_cards = red_cards + p.p_red_card
		
			return red_cards
		
		