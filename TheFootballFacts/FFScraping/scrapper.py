import requests
from unicodedata import normalize 
from bs4 import BeautifulSoup
from FFDao.Dao import Dao
from nt import stat

bd = Dao

#global url_player2 

def scrapperPlayers():
	i = 1	
	url = 'https://footystats.org/brazil/serie-a'
	url2 = 'https://footystats.org'
		
	url_player = []
	url_player2 = []
	
	r = requests.get(url)
	soup =  BeautifulSoup(r.text, 'lxml')
	
	lista_nome = soup.find_all('td', class_='team borderRightContent')
	for lista_url in lista_nome:
		if lista_url.next_element.name == 'a':
			url_player.append('{0}{1}'.format(url2, lista_url.next_element.get('href')))
	
	for url_time in url_player:
		url_player2 = []
		r = requests.get(url_time)
		soup =  BeautifulSoup(r.text, 'lxml')
		
		#PEGA A URL DOS JOGADORES DOS TIMES		
		lista_player = soup.find_all('p', class_='col-lg-6 ellipses')

		for lista_url in lista_player:
			url_player2.append('{0}{1}'.format(url2, lista_url.next_element.get('href')))
			#print(('{0}{1}'.format(url2, lista_url.next_element.get('href'))))
		
		for url_player2 in url_player2:
				r = requests.get(url_player2)
				soup =  BeautifulSoup(r.text, 'lxml')
			
				#PEGAR INFO DO JOGADOR
				info_p = []
				#player_info = soup.find_all('div', class_='row cf lightGrayBorderBottom ')
				player_info = soup.find_all('p', class_='col-lg-7 lh14e')
				for p_info in player_info:
					info_p.append(p_info.text) 
		
				#TRATAR O NOME
				p_name = info_p[0]			
			
				#TRATAR PARA USAR O NOME COMO URL
				p_url = p_name.lower() 
				p_url = p_url.replace(" ","-")
				p_url = normalize('NFKD', p_url).encode('ASCII', 'ignore').decode('ASCII')			
				
				#PAIS DE ORIGEM
				p_origem = info_p[1]
				
				#POSICAO DO JOGADOR
				p_position = info_p[2]		
	
				#IDADE DO JOGADOR
				p_age = info_p[3]	
				
				player_club = soup.find('span', class_='fa-adjust-h3')
				p_club = player_club.text
				p_club = p_club[0:len(p_club)-6]
				
				stats_p = []
				#RETIRA AS STATS DO JOGADOR
				player_stats = soup.find('div', class_='w100 cf player_season_row')
				player_stats = player_stats.find_all('p', class_='mild-small')
				for p_stats in player_stats:
					stats_p.append(p_stats)
	
				p_matches_played = stats_p[0].text 
				p_gols           = stats_p[1].text
				p_assistence     = stats_p[2].text
				p_yellow_card    = stats_p[3].text
				p_red_card		 = stats_p[4].text
				p_penaulti       = stats_p[5].text
				p_played_time    = stats_p[6].text.replace("'","")
		
				#GRAVA JOGADOR NO BANCO
				bd.add_Player("", p_name, p_club, p_position, p_origem, p_matches_played,  p_gols, p_assistence, p_yellow_card, p_red_card, p_penaulti, p_played_time)
				print(i,"Adicionado ", p_name, " com Sucesso no time:", p_club)
				i = i+1


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
		aux = soup.find('h1', class_='teamName')
		aux = aux.text.split("-")
		aux2 = aux[0].lower()
		valor = len(aux2)
		aux2 = aux2[0:valor -1]
		club_name = aux2[1:len(aux2)]		
		
				
		#PEGANDO NUMERO DE VITORIAS DENTRO E FORA
		aux = soup.find_all('td', class_='w')
		i = 0;
		for vitorias in aux:
			if (i == 0):
				club_n_win    = vitorias.text
				i = i+1
			elif (i == 1):
				club_n_win_in = vitorias.text

		
		#PEGANDO NUMERO DE DERROTAS DENTRO E FORA
		aux = soup.find_all('td', class_='d')
		i = 0;
		for derrotas in aux:
			if (i == 0):
				club_n_defeat    = derrotas.text
				i = i+1
			elif (i == 1):
				club_n_defeat_in = derrotas.text		
	
		#PEGANDO NUMERO DE EMPATES DENTRO E FORA
		aux = soup.find_all('td', class_='l')
		i = 0;
		for empates in aux:
			if (i == 0):
				club_n_tie    = empates.text
				i = i+1
			elif (i == 1):
				club_n_tie_in = empates.text			
		#print(club_n_win, club_n_defeat, club_n_tie)
		
		#CRIAR A URL COM O EMBLEMA DO CLUBE
		nome = club_name.replace(" ","-")
		nome = normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
		nome = nome[0:len(nome)]
		club_emblem = "/static/emblem/" + nome + ".png"
		#print(club_emblem)
		
		#VARIAVEL DE NACIONLIDADE DO CLUBE
		club_country = "Brasil"
		
		#ADICIONA NO BANCO DE DADOS O CLUBE
		bd.add_club("", club_name, club_n_win, club_n_defeat, club_n_tie, club_emblem, club_country, club_n_win_in, club_n_defeat_in, club_n_tie_in)
		print("Adicionado ", club_name, " Vitorias: ", club_n_win, " Derrotas: ",  club_n_defeat, " Empates: ", club_n_tie, " Emblema: ",club_emblem, " Pais: ",club_country, "Vitoria Dentro :",  club_n_win_in)


if __name__ == '__main__':
    #scrapperPlayers()
    #scrapperClub()
	#print(bd.consultar_all_Club(""))
	print(bd.consultar_all_Players(""))
