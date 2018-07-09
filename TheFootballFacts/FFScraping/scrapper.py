from _operator import concat
from _sqlite3 import sqlite_version
import sqlite3
from unicodedata import normalize 

from bs4 import BeautifulSoup
import requests

from FFDao.Dao import Dao


bd = Dao
	


def scrapperPlayers():
	url = 'https://www.scoreboard.com/br/equipe/flamengo/WjxY29qB/'
	r = requests.get(url)
	soup =  BeautifulSoup(r.text, 'lxml')
	lista_nome = soup.find_all('span', class_='flag fl_39')
	url2 = 'https://www.scoreboard.com'
	url_player = []
	for lista_url in lista_nome:
		if lista_url.next_element.name == 'a':
			url_player.append('{0}{1}'.format(url2, lista_url.next_element.get('href')))

	
	for url_player in url_player:
		validador = url_player.find("jogador")
		if(validador > 0):
			r = requests.get(url_player)
			soup =  BeautifulSoup(r.text, 'lxml')
			
			player_name = soup.find('div', class_='team-name')
			
			#LIMPA AS INFORMACOES
			aux = player_name.text
			aux = aux.split("(")
				
			#PEGA O NOME DO JOGADOR
			aux2 = aux[0].lower()
			valor = len(aux2)
			aux2 = aux2[0:valor -1]
			player_name = aux2
			
			#PEGA O TIME DO JOGADOR
			aux2 = aux[1].lower()
			valor = len(aux2)
			aux2 = aux2[0:valor -1]
			player_club = aux2
	
			
			#PEGA A IDADE DO JOGADOR
			
			#PEGA A POSICAO DO JOGADOR
			player_position = soup.find('div', class_='player-type-name')
			player_position = player_position.text
				
			#GRAVA JOGADOR NO BANCO
			bd.add_Player("", player_name, player_club, player_position)
			print("Adicionado ", player_name, " com Sucesso no time:", player_club)



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
    scrapperClub()
	#print(bd.consultar_all_Club(""))
	#print(bd.consultar_all_Players(""))
