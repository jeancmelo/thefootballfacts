# -*- coding: utf-8 -*-
from unicodedata import normalize 

from bs4 import BeautifulSoup
import requests
from FFDao.Dao import Dao
from FFDao import core, core_insert
from _datetime import datetime
import re
from time import sleep
from random import randint

core = core_insert

def scrapperClub():
	
	url_clubs = []
	url2 = "https://footystats.org"
	
	#CRIAR OS CLUBES NO
	#for arrayClub in arrayClub:
	#	bd.add_club("", arrayClub)

	url = "https://footystats.org/brazil/serie-a"
	r = requests.get(url)
	soup =  BeautifulSoup(r.text, 'lxml')
	
	#ENCONTRAR AS URLS DOS TIMES
	lista_nome =  soup.find_all('td', class_='team borderRightContent')
	for lista_url in lista_nome:
		if lista_url.next_element.name == 'a':
			url_clubs.append('{0}{1}'.format(url2, lista_url.next_element.get('href')))

	#PERCORRE AS URLS DOS CLUBES PARA PEGAR OS DADOS	
	for url_clubs in url_clubs:
		r = requests.get(url_clubs)
		soup =  BeautifulSoup(r.text, 'lxml')

		#PEGAR NOME DO CLUBE
		even = soup.find('h1', class_='teamName')
		even = even.text.split("-")
		even2 = even[0].lower()
		valor = len(even2)
		even2 = even2[0:valor -1]
		club_name = even2[1:len(even2)]		
		
				
		#PEGANDO NUMERO DE VITORIAS DENTRO E FORA
		even = soup.find_all('td', class_='w')
		i = 0;
		for vitorias in even:
			if (i == 0):
				club_n_win    = vitorias.text
				i = i+1
			elif (i == 1):
				club_n_win_in = vitorias.text

		
		#PEGANDO NUMERO DE DERROTAS DENTRO E FORA
		even = soup.find_all('td', class_='d')
		i = 0;
		for derrotas in even:
			if (i == 0):
				club_n_defeat    = derrotas.text
				i = i+1
			elif (i == 1):
				club_n_defeat_in = derrotas.text		
	
		#PEGANDO NUMERO DE EMPATES DENTRO E FORA
		even = soup.find_all('td', class_='l')
		i = 0;
		for empates in even:
			if (i == 0):
				club_n_tie    = empates.text
				i = i+1
			elif (i == 1):
				club_n_tie_in = empates.text			
		
		#PEGAR OS UTLIMOS JOGOS E OS PROXIMOS
		
		#***** VEERIFICAR GRAVACAO NO BANCO********"
		club_games = []
		
		time_in = soup.find_all('div', class_='homeTeamInfo')
		time_out = soup.find_all('div', class_='awayTeamInfo')
		date = soup.find_all('span', class_='monthAndDay')
				
		for i, val in enumerate(time_in):
			club_games.append(date[i].text)
			club_games.append(time_in[i].text)
			club_games.append(time_out[i].text)


		#CRIAR A URL COM O EMBLEMA DO CLUBE
		nome = club_name.replace(" ","-")
		nome = normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
		nome = nome[0:len(nome)]
		club_emblem = "/static/emblem/" + nome + ".png"
		#print(club_emblem)
		
		#VARIAVEL DE NACIONLIDADE DO CLUBE
		club_country = "Brasil"
		
		#ADICIONA NO BANCO DE DADOS O CLUBE
		core.insert_Club(club_name, "00/00/00", club_emblem, club_n_win, club_n_defeat,club_n_tie, club_n_win_in, club_n_defeat_in, club_n_tie_in)
		#bd.add_club("", club_name, club_n_win, club_n_defeat, club_n_tie, club_emblem, club_country, club_n_win_in, club_n_defeat_in, club_n_tie_in)
		print("Adicionado ", club_name, " Vitorias: ", club_n_win, " Derrotas: ",  club_n_defeat, " Empates: ", club_n_tie, " Emblema: ",club_emblem, " Pais: ",club_country, "Vitoria Dentro :",  club_n_win_in)

def scrapperJogos():
	
		url = "https://www.academiadasapostasbrasil.com/stats/competition/brasil-stats/26/15366/45710/0/"
		url2 = ""
		rodada  = 38;
		home    = []
		result  = []
		away    = []
		date    = []
		rodada_final = []
		i       = 0
		
		while rodada < 39:
			sleep(randint(3,10))
			clubs   = []
			horario = []
			
			if rodada <= 9:
				url2 = url + "0" + str(rodada)
			else:
				url2 = url + str(rodada)
			
			r = requests.get(url2)
			soup =  BeautifulSoup(r.text, 'lxml')
			jogos =  soup.find_all('tr', class_='even')
			
			
			for j in jogos:
				clubs.append(j.find_all('a'))		

			for j in jogos:
				horario.append(j.find_all('td', class_='nowrap'))
				
			
			while i <= 4:
				aux = horario[i][0].text.replace("\n        ", "")
				date.append(aux[0:19])
				home.append(clubs[i][0].text)
				aux = clubs[i][1].text.replace("\n        ", "")
				result.append(aux[0:3])
				away.append(clubs[i][2].text)
				rodada_final.append(rodada)
				i = i + 1


			#REFAZ PARA AS LINHAS FALTANTES
			clubs   = []
			horario = []
			
			jogos2 =  soup.find_all('tr', class_='odd')
			for j in jogos2:
				clubs.append(j.find_all('a'))		

			for j in jogos:
				horario.append(j.find_all('td', class_='nowrap'))
				
			i = 0
			while i <= 4:
				aux = horario[i][0].text.replace("\n        ", "")
				date.append(aux[0:19])
				home.append(clubs[i][0].text)
				aux = clubs[i][1].text.replace("\n        ", "")
				result.append(aux[0:3])
				away.append(clubs[i][2].text)
				rodada_final.append(rodada)
				i = i + 1
			print("Rodada " + str(rodada) + " Cadastrado")
			rodada =  rodada + 1

		for i, val in enumerate(date):
			core.insert_ChampGames(home[i], away[i], result[i], date[i], rodada_final[i])



def scrapperPlayersStats():
		requisicoes = 0
		aux = "https://www.academiadasapostasbrasil.com/stats/person/brasil/"
		jogadores = ["diego-alves/8905", "sidao/112354", "keiller/446980","lucas-franca/431776",  "fabio-santos/8968", "mayke/268729","marcelo-grohe/9187","corinthians/320",
					 "cassio/17304", "fernando-prass/16938","agenor/64369",  "gilberto/187555", "jefferson/4802", "douglas-pires/191016", "rafael-thyere/286196", "joao-paulo/317934",
					 "pedro-botelho/9116", "giovanni/115289","mansur/185489", "otavio/328063",  "tiago-alves/80072"]
		
		#ENCONTRA AS URLS DOS JOGADORES COM BASE EM UM DELES:
		for j in jogadores:

			
			url_player = []
			print("URL TIME:" + j)
			url = aux + j
			print("COMECANDO...")
			
			sleep(randint(3,10))
			
			requisicoes += 1
			print(requisicoes)
			r = requests.get(url)
			soup =  BeautifulSoup(r.text, 'lxml')
			
			#PEGA VALORES DA LINHA EVEN
			players =  soup.find_all('tr', class_='even')
			arr =  []
			arr2 = []
			for p in players:
				arr.append(p.find('a'))
	
			for i in arr:
				if i is None:
					pass
				else:
					arr2.append(i.get('href'))
				
			for j in arr2:
				if j.find('person') == -1:
				 	pass
				else:
				 	url_player.append(j)
			 	
			#PEGA VALORES DA LINHA ODD				
			players =  soup.find_all('tr', class_='odd')
			arr =  []
			arr2 = []	
			for p in players:
				arr.append(p.find('a'))
	
			for i in arr:
				if i is None:
					pass
				else:
					arr2.append(i.get('href'))
				
			for j in arr2:
				if j.find('person') == -1:
					pass
				else:
					url_player.append(j)
			
			print(url_player)
			for url in url_player:
				sleep(randint(2,7))
				print("URL JOGADOR:" + url)
				#PEGA DADOS DE JOGO DO JOGADORES:
				r = requests.get(url)
				soup =  BeautifulSoup(r.text, 'lxml')
				
				players =  soup.find_all('tr', class_='stats-player-odd')
					
				p_stats = []
				
				#PEGA VALORES DA LINHA EVEN
				players =  soup.find_all('tr', class_='even')		
				for i, val in enumerate(players):
					p = players[i].find_all('td')
					for row in p:
						if re.search(r'\d{4}-\d{2}-\d{2}', row.text.replace("\n", "").replace("  ", "").replace("\r", "")):
							i = len(players)
						elif row.text.replace("\n", "").replace("  ", "").replace("\r", "") == 'Transferência':
							i = len(players)
						else:
							p_stats.append(row.text.replace("\n", "").replace("  ", "").replace("\r", ""))
				
				#PEGA VALORES DA LINHA ODD
				players =  soup.find_all('tr', class_='odd')
				for i, val in enumerate(players):
					p = players[i].find_all('td')
					for row in p:
						if re.search(r'\d{4}-\d{2}-\d{2}', row.text.replace("\n", "").replace("  ", "").replace("\r", "")):
							i = len(players)
						elif row.text.replace("\n", "").replace("  ", "").replace("\r", "") == 'Transferência':
							i = len(players)							
						else:
							p_stats.append(row.text.replace("\n", "").replace("  ", "").replace("\r", ""))
						
				
				#PEGA NOME E ATRIBUTOS DO JOGADOR:
				name =  soup.find_all('h2', class_='boxed-header')
				p_name = name[0].text.replace("\n", "").replace("  ", "")
				
				
				#PEGA DADOS GERAIS
				info =  soup.find_all('tr', class_='stats-player-odd')
				p_info = []
				for i, val in enumerate(info):
					p = info[i].find_all('td')
					for row in p:
						p_info.append(row.text.replace("\n", "").replace("  ", ""))		
		
				info =  soup.find_all('tr', class_='stats-player-even')
				for i, val in enumerate(info):
					p = info[i].find_all('td')
					for row in p:
						p_info.append(row.text.replace("\n", "").replace("  ", ""))		
						

				#PEGA POSICAO DO JOGADOR:
				position = soup.find_all('img', class_='player_pos_img')
				p_position = position[0].get('title')
				
				photo = soup.find_all('img')
				p_photo = photo[3].get('src')
				

				if p_position != "coach":
					core.insert_Player(p_name, p_info[1], p_info[13], p_photo, p_info[11], p_position, p_stats[1], p_info[5], p_info[7], p_info[9], p_info[15])
					i = 0
					while i < len(p_stats) -14:
						core.insert_Stats(p_name, p_info[1], p_stats[i+2], p_stats[i+1], p_stats[i], p_stats[i+4], p_stats[i+9], 0, p_stats[i+11], p_stats[i+13], p_stats[i+12], 
									  p_stats[i+3], p_stats[i+5], p_stats[i+8])
						print(" - Jogador " + p_name + " adicionado dados da sua passagem pelo:" + p_stats[i+1])
						i = i+14


if __name__ == '__main__':
    #scrapperPlayers()
    #scrapperClub()
    #scrapperPlayersStats()
    #scrapperJogos()
	#search("Jose Henrique")
