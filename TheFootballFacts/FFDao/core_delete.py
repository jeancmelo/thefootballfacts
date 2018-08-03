'''
Created on 24 de jul de 2018

@author: jeanm
'''
from sqlalchemy import delete, select
from core import my_engine
from FFDao.core import players_table, stats_table, club_table
import re

conn = my_engine.connect()

def limparBanco():
    retorno = []
    deletar = []
    a = select([stats_table])
        
    for row in a.execute():
        retorno.append(row)
    
    for i, val in enumerate(retorno):
        if len(retorno[i][5]) < 4:
            deletar.append(retorno[i][0])  
        elif re.search(r'[A-z]', retorno[i][5]):
            #print(retorno[i][5])
            deletar.append(retorno[i][0])    
        else:
            #print(retorno[i][5])
            pass
            #deletar.append(retorno[i][0])
    
    for d in deletar:
        a = delete(stats_table).where(stats_table.c.id == d)
        result = conn.execute(a)
        print("deletado:", d )


if __name__ == '__main__':
    limparBanco()