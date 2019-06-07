# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:47:07 2019

@author: yliu11
"""
output02.head()
#seperate the table to 31 tables
r0 = pd.read_sql('select commu, Liste, sum(Voix) as total_vote from output02 group by 1,2', connection)
r1 = pd.read_sql('select commu, Liste1 as Liste, sum(Voix1) as total_vote from output02 group by 1,2', connection)
r2 = pd.read_sql('select commu, Liste2 as Liste,sum(Voix2) as total_vote from output02 group by 1,2', connection)
r3 = pd.read_sql('select commu, Liste3 as Liste,sum(Voix3) as total_vote from output02 group by 1,2', connection)
r4 = pd.read_sql('select commu, Liste4 as Liste,sum(Voix4) as total_vote from output02 group by 1,2', connection)
r5 = pd.read_sql('select commu, Liste5 as Liste, sum(Voix5) as total_vote from output02 group by 1,2', connection)
r6 = pd.read_sql('select commu, Liste6 as Liste, sum(Voix6) as total_vote from output02 group by 1,2', connection)
r7 = pd.read_sql('select commu, Liste7 as Liste, sum(Voix7) as total_vote from output02 group by 1,2', connection)
r8 = pd.read_sql('select commu, Liste8 as Liste, sum(Voix8) as total_vote from output02 group by 1,2', connection)
r9 = pd.read_sql('select commu, Liste9 as Liste, sum(Voix9) as total_vote from output02 group by 1,2', connection)
r10 = pd.read_sql('select commu, Liste10 as Liste,sum(Voix10) as total_vote from output02 group by 1,2', connection)
r11 = pd.read_sql('select commu, Liste11 as Liste, sum(Voix11) as total_vote from output02 group by 1,2', connection)
r12 = pd.read_sql('select commu, Liste12 as Liste, sum(Voix12) as total_vote from output02 group by 1,2', connection)
r13 = pd.read_sql('select commu, Liste13 as Liste, sum(Voix13) as total_vote from output02 group by 1,2', connection)
r14 = pd.read_sql('select commu, Liste14 as Liste, sum(Voix14) as total_vote from output02 group by 1,2', connection)
r15 = pd.read_sql('select commu, Liste15 as Liste, sum(Voix15) as total_vote from output02 group by 1,2', connection)
r16 = pd.read_sql('select commu, Liste16 as Liste, sum(Voix16) as total_vote from output02 group by 1,2', connection)
r17 = pd.read_sql('select commu, Liste17 as Liste, sum(Voix17) as total_vote from output02 group by 1,2', connection)
r18 = pd.read_sql('select commu, Liste18 as Liste, sum(Voix18) as total_vote from output02 group by 1,2', connection)
r19 = pd.read_sql('select commu, Liste19 as Liste, sum(Voix19) as total_vote from output02 group by 1,2', connection)
r20= pd.read_sql('select commu, Liste20 as Liste, sum(Voix20) as total_vote from output02 group by 1,2', connection)
r21= pd.read_sql('select commu, Liste21 as Liste,sum(Voix21) as total_vote from output02 group by 1,2', connection)
r22 = pd.read_sql('select commu,Liste22 as Liste, sum(Voix22) as total_vote from output02 group by 1,2', connection)
r24 = pd.read_sql('select commu, Liste23 as Liste, sum(Voix23) as total_vote from output02 group by 1,2', connection)
r25= pd.read_sql('select commu, Liste24 as Liste, sum(Voix24) as total_vote from output02 group by 1,2', connection)
r23 = pd.read_sql('select commu, Liste25 as Liste, sum(Voix25) as total_vote from output02 group by 1,2', connection)
r26 = pd.read_sql('select commu, Liste26 as Liste, sum(Voix26) as total_vote from output02 group by 1,2', connection)
r27= pd.read_sql('select commu, Liste27 as Liste, sum(Voix27) as total_vote from output02 group by 1,2', connection)
r28= pd.read_sql('select commu, Liste28 as Liste, sum(Voix28) as total_vote from output02 group by 1,2', connection)
r29 = pd.read_sql('select commu, Liste29 as Liste, sum(Voix29) as total_vote from output02 group by 1,2', connection)
r30 = pd.read_sql('select commu, Liste30 as Liste, sum(Voix30) as total_vote from output02 group by 1,2', connection)

commur = r0.append(r1).append(r3).append(r4).append(r5).append(r6).\
        append(r7).append(r8).append(r9).append(r10).append(r11).\
        append(r12).append(r13).append(r14).append(r15).append(r16).\
        append(r17).append(r18).append(r19).append(r20).append(r21).\
        append(r22).append(r23).append(r24).append(r25).append(r26).\
        append(r27).append(r28).append(r29).append(r30)

commur.to_csv(os.path.join(path,r'commur.csv'))# keep a csv file incase of any other use

#cus there r some databaseerror in the cols, here we create new database for basetables
# we create the database "commune"
con2 = sqlite3.connect("commune.db")
#write the dataframe "commur" into the db
commur.to_sql('commune', con2, if_exists='replace', index=False) #connect the dataframe with the database
#do the query using db (not the dataframe!!)
commur2 = pd.read_sql('select commu, Liste, sum(total_vote) as vote_commune from commune group by 1,2 having commu != "0" and Liste != "0"', con2)

#export the result as excel
commur2.to_excel(r'C:\Users\yliu11\Desktop\an_internship\result_by_commune.xlsx')

