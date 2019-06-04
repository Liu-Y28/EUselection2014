# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:11:49 2019

@author: yliu11
"""
# Working in Python, based on the official data published in the EU and French government official website, 
# this project tries to find the result of the 2014 EU selection 
# by municipality, by department and by regions.

import urllib, json
from urllib.request import urlopen
import pandas as pd
import numpy as np
import sqlite3
#################################### 1. overview
surl01 = "http://www.europarl.europa.eu/website/election-results/data/turnout/year/2014.json"
data01 = urllib.request.urlopen(surl01).read()
output01 = json.loads(data01)

# after checked the dataset we only keep 'results' for analysis
turnout = pd.DataFrame(output01["results"])
turnout.head()
#check the turnout of each country from high to low
top = turnout.sort_values(by = "percent", ascending = False)
top.head(15) 
       
#################################### 2. by municipality
# dataset could be found in https://www.data.gouv.fr/en/datasets/elections-europeennes-2014-resultats-par-communes/
surl02 = "https://www.data.gouv.fr/en/datasets/r/d6817473-7c6b-4a41-955c-b620c86e7fd7"
data02 = urllib.request.urlopen(surl02)
output = pd.ExcelFile(data02)
output02 = output.parse(output.sheet_names[0], header=0) #use the 1st sheet

# turn nan to 0, because it means no one vote for this party
output02 = output02.fillna(0)
# only keep cols we need
list(output02) #check the colnames
output02 = output02[['Code du département','Libellé du département','Code de la commune','Libellé de la commune','Exprimés',
                     'Nuance Liste','Voix','Nuance Liste.1','Voix.1','Nuance Liste.2','Voix.2','Nuance Liste.3','Voix.3','Nuance Liste.4','Voix.4',
                     'Nuance Liste.5','Voix.5','Nuance Liste.6','Voix.6','Nuance Liste.7','Voix.7','Nuance Liste.8','Voix.8','Nuance Liste.9','Voix.9','Nuance Liste.10','Voix.10',
                     'Nuance Liste.11','Voix.11','Nuance Liste.12','Voix.12','Nuance Liste.13','Voix.13','Nuance Liste.14','Voix.14','Nuance Liste.15','Voix.15',
                    'Nuance Liste.16','Voix.16','Nuance Liste.17','Voix.17','Nuance Liste.18','Voix.18','Nuance Liste.19','Voix.19','Nuance Liste.20','Voix.20',
                    'Nuance Liste.21','Voix.21','Nuance Liste.22','Voix.22','Nuance Liste.23','Voix.23','Nuance Liste.24','Voix.24','Nuance Liste.25','Voix.25',
                    'Nuance Liste.26','Voix.26','Nuance Liste.27','Voix.27','Nuance Liste.28','Voix.28','Nuance Liste.29','Voix.29','Nuance Liste.30','Voix.30']]
output02.rename(columns={'Code du département': 'Code_du_depar', 'Libellé du département': 'depar',
                         'Code de la commune': 'Code_de_la_commu', 'Libellé de la commune': 'commu',
                         'Nuance Liste': 'Liste', 'Nuance Liste.1': 'Liste1',
                         'Voix.1': 'Voix1',
                         'Nuance Liste.2': 'Liste2', 'Voix.3': 'Voix3',
                         'Nuance Liste.3': 'Liste3', 'Voix.2': 'Voix2',
                         'Nuance Liste.4': 'Liste4', 'Voix.4': 'Voix4',
                         'Nuance Liste.5': 'Liste5', 'Voix.5': 'Voix5',
                         'Nuance Liste.6': 'Liste6', 'Voix.6': 'Voix6',
                         'Nuance Liste.7': 'Liste7', 'Voix.7': 'Voix7',
                         'Nuance Liste.8': 'Liste8', 'Voix.8': 'Voix8',
                         'Nuance Liste.9': 'Liste9', 'Voix.9': 'Voix9',
                         'Nuance Liste.10': 'Liste10', 'Voix.10': 'Voix10',
                         'Nuance Liste.11': 'Liste11', 'Voix.11': 'Voix11',
                         'Nuance Liste.12': 'Liste12', 'Voix.12': 'Voix12',
                         'Nuance Liste.13': 'Liste13', 'Voix.13': 'Voix13',
                         'Nuance Liste.14': 'Liste14', 'Voix.14': 'Voix14',
                         'Nuance Liste.15': 'Liste15', 'Voix.15': 'Voix15',
                         'Nuance Liste.16': 'Liste16', 'Voix.16': 'Voix16',
                         'Nuance Liste.17': 'Liste17', 'Voix.17': 'Voix17',
                         'Nuance Liste.18': 'Liste18', 'Voix.18': 'Voix18',
                         'Nuance Liste.19': 'Liste19', 'Voix.19': 'Voix19',
                         'Nuance Liste.20': 'Liste20', 'Voix.20': 'Voix20',
                         'Nuance Liste.21': 'Liste21', 'Voix.21': 'Voix21',
                         'Nuance Liste.22': 'Liste22', 'Voix.22': 'Voix22',
                         'Nuance Liste.23': 'Liste23', 'Voix.23': 'Voix23',
                         'Nuance Liste.24': 'Liste24', 'Voix.24': 'Voix24',
                         'Nuance Liste.25': 'Liste25', 'Voix.25': 'Voix25',
                         'Nuance Liste.26': 'Liste26', 'Voix.26': 'Voix26',
                         'Nuance Liste.27': 'Liste27', 'Voix.27': 'Voix27',
                         'Nuance Liste.28': 'Liste28', 'Voix.28': 'Voix28',
                         'Nuance Liste.29': 'Liste29', 'Voix.29': 'Voix29',
                         'Nuance Liste.30': 'Liste30', 'Voix.30': 'Voix30',
                         'Nuance Liste.31': 'Liste31', 'Voix.31': 'Voix31'
                         }, inplace=True)
list(output02) #check the cols
 
output02.to_csv('output02.csv') #save the file

#store dataframe into the database
connection = sqlite3.connect("output02.db")#create the database
output02.to_sql('output02', connection, if_exists='replace', index=False) #connect the dataframe with the database

#by department
result_depar_ = pd.read_sql('select Liste, depar, sum(Voix) as total_vote from output02 where (Code_du_depar,Liste) = (1,"LEXG")', connection)
result_depar_.head()




























