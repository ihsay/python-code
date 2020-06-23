#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import json
import requests

#import data
response = requests.get("https://api.covid19india.org/v3/data.json")
data = json.loads(response.text)    

#extract the subset of the required data
data_MH = data['MH']['districts']    #get the data for Maharashtra districts
total_cases = {}
for city,c_type in data_MH.items():
    total_cases.update({city : c_type['total']})
#total_cases dictionary is in the format {district: {'confirmed': x, 'deceased': y, 'recovered': z}}


#plot the graph
df = pd.DataFrame(total_cases)
df = df.transpose()
df.plot(kind='bar',y='confirmed', title='Covid-19 confirmed cases in Maharashtra',color='blue')
df.plot(kind='bar',y='deceased', title='Covid-19 deceased cases in Maharashtra',color='red')
df.plot(kind='bar',y='recovered', title='Covid-19 recovered cases in Maharashtra',color='green')
df.plot(kind='bar',y='migrated', title='Covid-19 migrated cases in Maharashtra',color='yellow')



# In[ ]:





# In[5]:





# In[ ]:




