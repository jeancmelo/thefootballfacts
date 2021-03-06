# -*- coding: utf-8 -*-
'''
Created on 6 de ago de 2018

@author: jeanm
'''
import pygal

from sqlalchemy import select, and_
from FFDao.core import players_table, stats_table
from pygal.style import Style

 #CUSTOMIZAÇÃO DA COR DO GRÁFICO DE SCORE POR ÁREA
custom_style = Style(
    background='transparent',
    plot_background='#FFF',
    foreground='#676767',
    value_font_size = 20.0,
    label_font_size=20.0,
    legend_font_size=20.0,
    major_label_font_size=20.0,
    guide_stroke_dasharray='#fbfbfb',
    major_guide_stroke_dasharray='#fbfbfb',
    foreground_strong='#676767',
    foreground_subtle='#676767',
    opacity='.8',
    opacity_hover='.9',
    transition='200ms ease-in',
    colors=('#5283a0', '#84b3d0', '#98bbd0', '#1b4b68', '#25586b', '#313186', '#218359', '#BF8230'))    
    
#REDE DE ÁREA DE SKILLS
def player_network_skills(p_name):
    


    retorno       = []
    ataque        = 0
    violencia     = 0
    regularidade  = 0
    performance   = 0

    a = select([stats_table.c.s_matches_played, stats_table.c.s_gols,stats_table.c.s_yellow_card, stats_table.c.s_red_card, stats_table.c.s_substituido]).where(
             and_(
                    stats_table.c.s_name == p_name,
    ) )
           
    for row in a.execute():
        retorno.append(row)
    
    for i, val in enumerate(retorno):
        regularidade = regularidade + retorno[i][0]
        ataque       = ataque + retorno[i][1]
        violencia    = violencia + retorno[i][2] + retorno[i][3]
        performance  = performance + retorno[i][4]
            
    radar_chart = pygal.Radar(style=custom_style)
    radar_chart.x_labels = ['Ataque', 'Violência', 'Regularidade', 'Performance']
    radar_chart.add('Performance', [ataque, violencia, (regularidade/30), performance])
    
    return radar_chart

#GRÁFICO DE ROSCA PARA VEZES TITULAR VS JOGOS
def player_titular_vs_non(p_name):
    
  

    retorno       = []
    substitutido       = []
    titular       = []


    a = select([stats_table.c.s_substituido, stats_table.c.s_titular]).where(
             and_(
                    stats_table.c.s_name == p_name,
    ) )
           
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
        substitutido.append(retorno[i][0])
        titular.append(retorno[i][1])

    pie_chart = pygal.Pie(style=custom_style)
    pie_chart.add('Substituido', sum(substitutido))
    pie_chart.add('Titular', sum(titular))
    
    return pie_chart


#REDE DE ÁREA DE SKILLS
def player_goals_per_year(p_name):

    #GR�FICO DE DESEMPENHO DE GOLS
    retorno = []
    years = []
    data  = []

    f_year  = []
    f_goals = []
    
    a = select([stats_table.c.s_gols, stats_table.c.s_year]).where(
             and_(
                    stats_table.c.s_name == p_name,
    ) )
           
    for row in a.execute():
        retorno.append(row)


    for i, val in enumerate(retorno):
        data.append(retorno[i][0])
        years.append(retorno[i][1])


    valores = [{"ano": c, "gols": y} for c, y in zip(years, data)]

    mysorted = sorted(valores, key=lambda x : x['ano'], reverse=True)
    ano_final  = int(mysorted[0]['ano'])
        
    mysorted = sorted(mysorted, key=lambda x : x['ano'], reverse=False)
    
    if len(mysorted[0]['ano']) < 3:
        ano_comeco = int(mysorted[0]['ano'])
    else:
        aux = mysorted[0]['ano']
        ano_comeco = int(aux[0:4])

    while ano_comeco < ano_final:
        aux = 0
        for i, val in enumerate(mysorted):
            try: 
                if int(mysorted[i]['ano']) == ano_comeco:
                    aux = aux + int(mysorted[i]['gols'])
            except ValueError:
                pass
        f_year.append(ano_comeco)
        f_goals.append(aux)   
        ano_comeco = ano_comeco + 1    

     
    
    date_chart = pygal.Line(x_label_rotation=20, style=custom_style)
    date_chart.x_labels = f_year
    date_chart.add('Gols', f_goals)
    
    return date_chart

#REDE DE ÁREA DE SKILLS
def player_time_per_year(p_name):


    
    
    
    #GR�FICO DE DESEMPENHO DE GOLS
    retorno = []
    years = []
    data  = []

    f_year  = []
    f_min_played = []
    
    a = select([stats_table.c.s_min_played, stats_table.c.s_year]).where(
             and_(
                    stats_table.c.s_name == p_name,
    ) )
           
    for row in a.execute():
        retorno.append(row)


    for i, val in enumerate(retorno):
        data.append(retorno[i][0])
        years.append(retorno[i][1])


    valores = [{"ano": c, "gols": y} for c, y in zip(years, data)]

    mysorted = sorted(valores, key=lambda x : x['ano'], reverse=True)
    ano_final  = int(mysorted[0]['ano'])
        
    mysorted = sorted(mysorted, key=lambda x : x['ano'], reverse=False)
    
    if len(mysorted[0]['ano']) < 3:
        ano_comeco = int(mysorted[0]['ano'])
    else:
        aux = mysorted[0]['ano']
        ano_comeco = int(aux[0:4])


    #print(mysorted)
    while ano_comeco < ano_final:
        aux = 0
        for i, val in enumerate(mysorted):
            try: 
                if int(mysorted[i]['ano']) == ano_comeco:
                    aux = aux + int(mysorted[i]['gols'])
            except ValueError:
                pass
        f_year.append(ano_comeco)
        f_min_played.append(aux)   
        ano_comeco = ano_comeco + 1    

    line_chart = pygal.Bar(style=custom_style)
    line_chart.x_labels = f_year
    line_chart.add('Tempo Jogado', f_min_played)

    return line_chart

#REDE DE ÁREA DE SKILLS
def player_cor_age_vs_time_played(p_name):

    
    #GR�FICO DE DESEMPENHO DE GOLS
    retorno = []
    years = []
    data  = []

    f_year  = []
    f_min_played = []
    
    a = select([stats_table.c.s_min_played, stats_table.c.s_year]).where(
             and_(
                    stats_table.c.s_name == p_name,
    ) )
           
    for row in a.execute():
        retorno.append(row)

    for i, val in enumerate(retorno):
        data.append(retorno[i][0])
        years.append(retorno[i][1])


    valores = [{"ano": c, "gols": y} for c, y in zip(years, data)]

    mysorted = sorted(valores, key=lambda x : x['ano'], reverse=True)
    ano_final  = int(mysorted[0]['ano'])
        
    mysorted = sorted(mysorted, key=lambda x : x['ano'], reverse=False)
    
    if len(mysorted[0]['ano']) < 3:
        ano_comeco = int(mysorted[0]['ano'])
    else:
        aux = mysorted[0]['ano']
        ano_comeco = int(aux[0:4])


    #print(mysorted)
    while ano_comeco < ano_final:
        aux = 0
        for i, val in enumerate(mysorted):
            try: 
                if int(mysorted[i]['ano']) == ano_comeco:
                    aux = aux + int(mysorted[i]['gols'])
            except ValueError:
                pass
        f_year.append(ano_comeco)
        f_min_played.append(aux)   
        ano_comeco = ano_comeco + 1    


    f_year = list(map(int, f_year))   
    f_min_played = list(map(int, f_min_played))   

    data = [(y, c) for c, y in zip(f_year, f_min_played)]
    

    xy_chart = pygal.XY(stroke=False, style=custom_style)
    xy_chart.add('A', data)
    xy_chart.render()

    return xy_chart

def testeData(club):
    
    retorno = []
    
    a = select([players_table]).where(
             and_(
                    players_table.c.p_name == "Cassiano",
    ) )
           
    for row in a.execute():
        retorno.append(row)
        
    print(retorno)
            

if __name__ == '__main__':
    testeData('Bahia')