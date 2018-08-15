# -*- coding: utf-8 -*-
'''

Created on 14 de ago de 2018

@author: jeanm

'''
import json

def best_formation_test(goalkeeper_data, defender_data, midfielder_data, forward_data):
	
	possible_formations = ('4-4-2', '3-5-2', '4-3-3', '5-3-2', '4-5-1', '5-2-3')
	score_formations    = []
	players_formation   = []
	retorno = []
	
	for i in possible_formations:
		#score_formation(goalkeeper_data, defender_data, midfielder_data, forward_data,i)
		print("Testando Formação: " + i)
		
		area = i.split('-')
		
		defensor = int(area[0])
		meio     = int(area[1])
		atacante = int(area[2])
		
		score = 0
		players  = []
		posiiton = []
		photo    = []

		#score = score + (goalkeeper_data[0]['score'])
		#players.append(goalkeeper_data[0]['player'])
					
		for i, val in enumerate(defender_data[0:defensor]):
			score = score + (defender_data[i]['score'])
			players.append(defender_data[i]['player'])
		
		for i, val in enumerate(midfielder_data[0:meio]):
			score = score + (midfielder_data[i]['score'])
			players.append(midfielder_data[i]['player'])
			
		for i, val in enumerate(forward_data[0:atacante]):
			score = score + (forward_data[i]['score'])
			players.append(forward_data[i]['player'])
			
		score_formations.append(score)
		
		#TRANSFORMA EM JSON	 
		retorno = [{"formacao": c, "score":s} for c, s in zip(possible_formations, score_formations)]
	
		#FAZ A CLASSIFICAO
		retorno = sorted(retorno, key=lambda x : x['score'], reverse=True)
	
	r = retorno[0]['formacao'].split('-')
	
	defensor = int(r[0])
	meio     = int(r[1])
	atacante = int(r[2])
	
	for i, val in enumerate(defender_data[0:defensor]):
		players.append(defender_data[i]['player'])
		posiiton.append(defender_data[i]['position'])
		photo.append(defender_data[i]['photo'])		
	
	for i, val in enumerate(midfielder_data[0:meio]):
		players.append(midfielder_data[i]['player'])
		posiiton.append(midfielder_data[i]['position'])
		photo.append(midfielder_data[i]['photo'])		
		
	for i, val in enumerate(forward_data[0:atacante]):
		players.append(forward_data[i]['player'])	
		posiiton.append(forward_data[i]['position'])
		photo.append(forward_data[i]['photo'])			
	
	
	players_formation = [{"player": c, "position":s, "photo": f} for c, s, f in zip(players, posiiton, photo)]
	
	return (retorno[0]['formacao'], players_formation)

	
def retorna_players(goalkeeper_data, defender_data, midfielder_data, forward_data, formation):
		area = formation.split('-')
		
		defensor = int(area[0])
		meio     = int(area[1])
		atacante = int(area[2])
		
		score   = []
		players = []

					
		for i, val in enumerate(defender_data[0:defensor]):
			players.append(defender_data[i]['player'])
		
		for i, val in enumerate(midfielder_data[0:meio]):
			players.append(midfielder_data[i]['player'])
			
		for i, val in enumerate(forward_data[0:atacante]):
			score = score + (forward_data[i]['score'])
			players.append(forward_data[i]['player'])


		return players

