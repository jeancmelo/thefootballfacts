'''
Created on 24 de jul de 2018

@author: jeanm
'''
from sqlalchemy import select
from FFDao.core import players_table

s = select([players_table])

for row in s.execute():
    print(row.c.p_name)