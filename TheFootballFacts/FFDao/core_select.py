'''
Created on 24 de jul de 2018

@author: jeanm
'''
from sqlalchemy import select, and_
from FFDao.core import players_table, stats_table

s = select([stats_table])
a = select([stats_table]).where(
                and_(
                    stats_table.c.s_club == 'Flamengo',
                    stats_table.c.s_year == '2018'
                ) )

b = select([stats_table]).where( stats_table.c.s_club == 'Flamengo')

for row in a.execute():
    print(row)