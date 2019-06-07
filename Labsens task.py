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
c = connection.cursor()
output02.to_sql('output02', connection, if_exists='replace', index=False) #connect the dataframe with the database

#seperate the table to 31 tables
result0 = pd.read_sql('select Code_du_depar, depar, Liste, sum(Voix) as total_vote from output02 group by 1,2', connection)
result1 = pd.read_sql('select Code_du_depar, depar, Liste1 as Liste, sum(Voix1) as total_vote from output02 group by 1,2', connection)
result2 = pd.read_sql('select Code_du_depar, depar, Liste2 as Liste,sum(Voix2) as total_vote from output02 group by 1,2', connection)
result3 = pd.read_sql('select Code_du_depar, depar, Liste3 as Liste,sum(Voix3) as total_vote from output02 group by 1,2', connection)
result4 = pd.read_sql('select Code_du_depar, depar, Liste4 as Liste,sum(Voix4) as total_vote from output02 group by 1,2', connection)
result5 = pd.read_sql('select Code_du_depar, depar, Liste5 as Liste, sum(Voix5) as total_vote from output02 group by 1,2', connection)
result6 = pd.read_sql('select Code_du_depar, depar, Liste6 as Liste, sum(Voix6) as total_vote from output02 group by 1,2', connection)
result7 = pd.read_sql('select Code_du_depar, depar, Liste7 as Liste, sum(Voix7) as total_vote from output02 group by 1,2', connection)
result8 = pd.read_sql('select Code_du_depar, depar, Liste8 as Liste, sum(Voix8) as total_vote from output02 group by 1,2', connection)
result9 = pd.read_sql('select Code_du_depar, depar, Liste9 as Liste, sum(Voix9) as total_vote from output02 group by 1,2', connection)
result10 = pd.read_sql('select Code_du_depar, depar, Liste10 as Liste,sum(Voix10) as total_vote from output02 group by 1,2', connection)
result11 = pd.read_sql('select Code_du_depar, depar, Liste11 as Liste, sum(Voix11) as total_vote from output02 group by 1,2', connection)
result12 = pd.read_sql('select Code_du_depar, depar, Liste12 as Liste, sum(Voix12) as total_vote from output02 group by 1,2', connection)
result13 = pd.read_sql('select Code_du_depar, depar, Liste13 as Liste, sum(Voix13) as total_vote from output02 group by 1,2', connection)
result14 = pd.read_sql('select Code_du_depar, depar, Liste14 as Liste, sum(Voix14) as total_vote from output02 group by 1,2', connection)
result15 = pd.read_sql('select Code_du_depar, depar, Liste15 as Liste, sum(Voix15) as total_vote from output02 group by 1,2', connection)
result16 = pd.read_sql('select Code_du_depar, depar, Liste16 as Liste, sum(Voix16) as total_vote from output02 group by 1,2', connection)
result17 = pd.read_sql('select Code_du_depar, depar, Liste17 as Liste, sum(Voix17) as total_vote from output02 group by 1,2', connection)
result18 = pd.read_sql('select Code_du_depar, depar, Liste18 as Liste, sum(Voix18) as total_vote from output02 group by 1,2', connection)
result19 = pd.read_sql('select Code_du_depar, depar, Liste19 as Liste, sum(Voix19) as total_vote from output02 group by 1,2', connection)
result20= pd.read_sql('select Code_du_depar, depar, Liste20 as Liste, sum(Voix20) as total_vote from output02 group by 1,2', connection)
result21= pd.read_sql('select Code_du_depar, depar, Liste21 as Liste,sum(Voix21) as total_vote from output02 group by 1,2', connection)
result22 = pd.read_sql('select Code_du_depar, depar,Liste22 as Liste, sum(Voix22) as total_vote from output02 group by 1,2', connection)
result24 = pd.read_sql('select Code_du_depar, depar, Liste23 as Liste, sum(Voix23) as total_vote from output02 group by 1,2', connection)
result25= pd.read_sql('select Code_du_depar, depar, Liste24 as Liste, sum(Voix24) as total_vote from output02 group by 1,2', connection)
result23 = pd.read_sql('select Code_du_depar, depar, Liste25 as Liste, sum(Voix25) as total_vote from output02 group by 1,2', connection)
result26 = pd.read_sql('select Code_du_depar, depar, Liste26 as Liste, sum(Voix26) as total_vote from output02 group by 1,2', connection)
result27= pd.read_sql('select Code_du_depar, depar, Liste27 as Liste, sum(Voix27) as total_vote from output02 group by 1,2', connection)
result28= pd.read_sql('select Code_du_depar, depar, Liste28 as Liste, sum(Voix28) as total_vote from output02 group by 1,2', connection)
result29 = pd.read_sql('select Code_du_depar, depar, Liste29 as Liste, sum(Voix29) as total_vote from output02 group by 1,2', connection)
result30 = pd.read_sql('select Code_du_depar, depar, Liste30 as Liste, sum(Voix30) as total_vote from output02 group by 1,2', connection)

#make a big basetable for finding the result by department
deparesult = result0.append(result1).append(result3).append(result4).append(result5).append(result6).\
        append(result7).append(result8).append(result9).append(result10).append(result11).\
        append(result12).append(result13).append(result14).append(result15).append(result16).\
        append(result17).append(result18).append(result19).append(result20).append(result21).\
        append(result22).append(result23).append(result24).append(result25).append(result26).\
        append(result27).append(result28).append(result29).append(result30)

deparesult.to_csv(os.path.join(path,r'deparesult.csv'))# keep a csv file incase of any other use

#cus there r some databaseerror in the col total_vote, so here we create new database for basetables
con = sqlite3.connect("deparesult.db")
deparesult.to_sql('deparesult', connection, if_exists='replace', index=False) #connect the dataframe with the database
deparesult2 = pd.read_sql('select depar, Liste, sum(total_vote) as vote_depar from deparesult group by 1,2 having depar != 0 and Liste != 0', connection)

#at last export the result as excel
deparesult2.to_excel(r'C:\Users\yliu11\Desktop\an_internship\result_by_departement.xlsx')


























