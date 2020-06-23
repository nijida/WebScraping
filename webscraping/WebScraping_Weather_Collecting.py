#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import libraries
import numpy as np
import pandas as pd
import urllib.request 
from bs4 import BeautifulSoup
import requests as req
from bs4 import Tag
from datetime import datetime, timedelta


# In[ ]:


#URL Parameters
quote_page = 'https://www.tmd.go.th/climate/climate.php?FileID=1' 


# In[ ]:


url_page = urllib.request.urlopen(quote_page) 


# In[ ]:


html_script  = BeautifulSoup(url_page, 'html.parser')


# In[ ]:


html_script


# In[ ]:


province = []
temperature_high = []
temperature_low =[]
wind_direction = []
wind_speed = []
weather_time = []
rain = []
rain_accumulation = []

# Loop ('tr', { 'class':  ['RADS','RDS']}) to extract td element within
for tr_element in html_script.find_all('tr', { 'class':  ['RADS','RDS']}): 
    td_element=tr_element.find_all("td")   
    
    all_temp = []
    
    for i in range(len(td_element)):
        # <td colspan=x> means x number of Null values   
        if td_element[i].get('colspan'):
            empty = [np.nan] * (int(td_element[i].get('colspan'))) # Assign x number of Null
            all_temp = all_temp + empty
        else:
            element = [td_element[i].text]
            all_temp = all_temp + element
    
    # Append each element to each attribute
    province.append(all_temp[0])
    temperature_high.append(all_temp[1])
    temperature_low.append(all_temp[2])
    wind_direction.append(all_temp[3])
    wind_speed.append(all_temp[4])
    weather_time.append(all_temp[5])
    rain.append(all_temp[6])
    rain_accumulation.append(all_temp[7])


# In[ ]:


# Combine attributes to a dataframe
yesterday_weather = pd.DataFrame({'province':province,'temperature_high':temperature_high,'temperature_low':temperature_low,'wind_direction':wind_direction,'wind_speed':wind_speed,'weather_time':weather_time,'rain':rain,'rain_accumulation':rain_accumulation})    


# In[ ]:


yesterday_weather


# In[ ]:




