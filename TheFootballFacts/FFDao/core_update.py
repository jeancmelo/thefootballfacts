'''
Created on 24 de jul de 2018

@author: jeanm
'''
from sqlalchemy import update
from FFDao.core import players_table, engine

# datetime.datetime(2017, 7, 3, 20, 20, 17, 134448)
# datetime.datetime(2017, 7, 3, 20, 22, 8, 267343)
conn = engine.connect()

u = update(players_table).where(players_table.c.nome == 'Juacy')

# u = u.values(nome='Juacy')
u = u.values(idade=(players_table.c.idade + 1))

result = conn.execute(u)

print(result.rowcount)

conn.close()