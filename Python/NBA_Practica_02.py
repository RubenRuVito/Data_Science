# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:32:25 2022

@author: 0016571
"""

# Importando librerias
import pandas as pd
import numpy as np
from sklearn import linear_model
import requests
from matplotlib import pyplot as plt
from nba_api.stats import endpoints
from nba_api.stats.static import teams


# %% Recuperando Datos (Json) y tranformandolos en DFrames con la NBA_API endpoints, teams, players

# Ejemplos
# # data = endpoints.leagueleaders.LeagueLeaders(season='2020-21') # (540filas) Si no  pones variables, tempRegular Actual
# data = endpoints.leagueleaders.LeagueLeaders() # Temp Regular Actual (605filas)
# df = data.league_leaders.get_data_frame()
# data2 = endpoints.teamgamelogs.TeamGameLogs() # GameLogs de la temporada 2016-17 (Temporada Regular)
# df2 = data2.team_game_logs.get_data_frame()

# DATOS DE TEAMS 1:
# from nba_api.stats.static import teams

# Equipos temporada Actual..
data = teams.get_teams() # Lista de Objetos Json, con los Equipos de la Temp Actual
df = pd.DataFrame(data) # Conviertes en Dframe el objeto data

print(df[["id","full_name","abbreviation"]])

# ESTADISTICAS GENERALES HISTORICAS Y PRESENTES TEAMS..
# Stadisticas Actuales e Historicas de los Teams 
data2 = endpoints.teamyearbyyearstats.TeamYearByYearStats('1610612762') # ID de Utha Jazz
df2 = data2.team_stats.get_data_frame() # Se utiliza uno de los metodos de la libreria xa convertirlo en DFrame..

# Reucuperar las estadisticas historicas de varios equipos a la vez..

df['id'][0:3] # los 3 primeros Ids

list_id = list(df['id'][0:3])
print(list_id)
tupla_ids = (list_id[0],list_id[1],list_id[2])
print(tupla_ids)

# Para recuperar los datos de varios equipos, habria q realizar un bucle que acumule los datos recuperados
# en un dataframe para cada Id de TEAM..
# data3 = endpoints.teamyearbyyearstats.TeamYearByYearStats(list_ids)
# data3 = endpoints.teamyearbyyearstats.TeamYearByYearStats(tupla_ids)
# data3 = endpoints.teamyearbyyearstats.TeamYearByYearStats(('1610612737','1610612738')) # Solo recupera los datos del 1er Id de la lista
#df3 = data3.team_stats.get_data_frame()

df3_full = pd.DataFrame()
for ind in list_id:
    print(ind)
    data3 = endpoints.teamyearbyyearstats.TeamYearByYearStats(ind)
    df3 = data3.team_stats.get_data_frame()
    df3_full = pd.concat([df3, df3_full], axis=0)

# ESTADISTICAS GENERALES DE CADA PARTIDO DE LA TEMPORADA INDICADA..
# GameLog Team en Temp Regular Actual..en campo "MATCHUP" "@"-Visitante "vs."-Local
data4 = endpoints.teamgamelog.TeamGameLog('1610612762') # creo q se puede indicar más de un id
df4 = data4.get_data_frames() # se convierte en lista de listas
df4 = pd.DataFrame(df4[0]) # conviertes en dataframe el elemeto [0]

# Estadisticas +COMPLETAS de los partidos de un team en la Temporada indicada, ***si no lo indicas, objeto vacio..
data4_1 = endpoints.teamgamelogs.TeamGameLogs(team_id_nullable='1610612762', season_nullable='2021-22').get_data_frames()
df4_1 = pd.DataFrame(data4_1[0])

# GameLogs de todos los partidos de la Temp Regular Actual (2021-22 => GAME_ID=22021)
data5 = endpoints.LeagueGameLog().get_data_frames() # Lista de listas
df5 = pd.DataFrame(data5[0]) # Transformar en DataFrame..

# Gamelogs temporada 2020-2021  ***Si es un año que no existe, te crea un objeto vacio..
data6 = endpoints.LeagueGameLog(season=2020).get_data_frames()
df6 = pd.DataFrame(data6[0])




# %% Visualizando datos
print(df)
df
