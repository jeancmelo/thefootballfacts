import requests
from bs4 import BeautifulSoup

url = 'http://www.soccerstats.com/team.asp?league=brazil&stats=15-atletico-pr'

r = requests.get(url)
#print(r.text.encode("utf-8"))

soup =  BeautifulSoup(r.text, 'lxml')

lista_nome = soup.find_all('h1')

for lista_nome in lista_nome:
		print(lista_nome.next_element)

