from FFClass.Player import Player
from FFutils.UtilPlayer import UtilPlayer

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

	def assistence(self, Arr_Players):

		assistence = 0
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[11], player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12]) 
			
			assistence = assistence + p.p_assistence
		
			return assistence		

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
		
	def score_per_area(self, Arr_Players):
		
		
		up = UtilPlayer
		
		score_per_area  = []
		score_forward    = 0
		score_midfielder = 0
		score_defender   = 0
		score_goalkeeper = 0 
				
		
		for player_name in Arr_Players:
			
			#RECONSTRUINDO O OBJETO
			p = Player(player_name[1],player_name[6],player_name[5],player_name[3],player_name[2],player_name[7], player_name[8], player_name[9], player_name[10], player_name[11], player_name[12], player_name[13]) 
			
			#VERIFICANDO O POSICIONAMENTO
			if (p.player_position == "Forward"):
				p = up.score_player_forward("", p)
				score_forward = score_forward + p.player_score
			elif(p.player_position == "Midfielder"):
				p = up.score_player_midfielder("", p)
				score_midfielder = score_midfielder + p.player_score
				pass
			elif(p.player_position == "Defender"):
				p = up.score_player_defender("", p)
				score_defender = score_defender + p.player_score
				pass
			elif(p.player_position == "Goalkeeper"):
				pass
					
		
		score_per_area.append(score_forward)
		score_per_area.append(score_midfielder)
		score_per_area.append(score_defender)
		score_per_area.append(score_goalkeeper)	
		
		return score_per_area
				