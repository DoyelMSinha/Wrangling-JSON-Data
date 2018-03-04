## JSON exercise

#Using data in file 'data/world_bank_projects.json'  
#1. Find the 10 countries with most projects
#2. Find the top 10 major project themes (using column 'mjtheme_namecode')
#3. In 2. above you will notice that some entries have only the code and the name is missing. 
#Create a dataframe with the missing names filled in.

import pandas as pd
import json
import numpy as np
import re
from pandas.io.json import json_normalize

json_df = pd.read_json('data/world_bank_projects.json')
 
#print 10 countries with most projects
print (json_df.groupby(['countrycode'])[['project_name']].nunique().sort_values(by=['project_name'], ascending=False)[0:9])
 
with open('data/world_bank_projects.json') as json_file:  
    data = json.load(json_file)

#Find the top 10 major project themes
df_2 = json_normalize(data,'mjtheme_namecode')
print(df_2.name.value_counts(normalize=False, sort=True, ascending=False)[0:9])

#Create a dataframe with the missing names filled in
df_4=df_2.name.value_counts(normalize=False, sort=True, ascending=False)[0:9].to_frame()
list1=[]
list2=[]
df_5=pd.DataFrame()
for index, row in df_4.iterrows():
    if re.match(r'^\s*$', index):
        index = 'Missing'
    list1.append(index)
    list2.append(row['name'])
df_5 = pd.DataFrame({'name': list2}, index=list1)
print(df_5)
