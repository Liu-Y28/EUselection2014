# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:29:27 2019

@author: yliu11
"""
# downloded the 2 datasets from https://www.insee.fr/fr/information/3363419#titre-bloc-26
# cus the text files are seperated in spaces, we open it with excel, keep the cols we need, then import in python
#read in datasets##################################################
# dataset conations the codes of regions and departments
###################################################################
read1 = pd.ExcelFile(r'C:\Users\yliu11\Desktop\an_internship\region_depar.xlsx')
region_depar = read1.parse(read1.sheet_names[1], header=0) #use the second sheet and our own col nales

# dataset conations the codes and names of regions
read2 = pd.ExcelFile(r'C:\Users\yliu11\Desktop\an_internship\region_name.xlsx')
region_name = read2.parse(read2.sheet_names[0], header=0)

#recall the election result by department(conatins the codes and names of department)
depar_result = pd.read_csv(r'C:\Users\yliu11\Desktop\an_internship\data\deparesult.csv')

###################################################################
connec = sqlite3.connect("ff.db")#creat a final database
cur = connec.cursor()

#pd.io.sql.to_sql(region_name, region_name,con3, if_exists='replace', index=False)

# use name= would make the code work
region_name.to_sql(name='region_name', con=connec, index=False, if_exists='replace')
region_depar.to_sql(name='region_depar', con=connec, index=False, if_exists='replace')
depar_result.to_sql(name='depar_result', con=connec, index=False, if_exists='replace')

final = pd.read_sql('''select rn.REGION, rn.NCC, dr.Liste, sum(dr.total_vote) as vote\
                   from region_depar rd, region_name rn, depar_result dr\
                   where rd.REGION = rn.REGION and rd.NCC = dr.depar and dr.Liste != 0\
                   group by rn.REGION, dr.Liste''', connec)
           
#export the result as excel
final.to_excel(r'C:\Users\yliu11\Desktop\an_internship\result_by_region.xlsx')


