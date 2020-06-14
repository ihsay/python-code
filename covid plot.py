#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import json
import requests
import matplotlib.pyplot as plt 

#import data
#https://api.covid19india.org/raw_data6.json
response = requests.get("https://api.covid19india.org/v3/data.json")
data = json.loads(response.text)    
#print(type(data))

#extract the subset of the required data
x = data['MH']['districts']
#print(x)
districts_list = list(x.keys())
#print(districts_list)
total_cases = {}
#print(type(total_cases))
for city,c_type in x.items():
    #print(c_type['total'])
    total_cases.update({city : c_type['total']})
print(total_cases)

#plot the graph


# In[4]:





# In[5]:


pip install requests


# In[ ]:




