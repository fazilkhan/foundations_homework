#!/usr/bin/env python
# coding: utf-8

# # Rock and Mineral Clubs
# 
# Scrape all of the rock and mineral clubs listed at https://rocktumbler.com/blog/rock-and-mineral-clubs/ (but don't just cut and paste!)
# 
# Save a CSV called `rock-clubs.csv` with the name of the club, their URL, and the city they're located in.
# 
# **Bonus**: Add a column for the state. There are a few ways to do this, but knowing that `element.parent` goes 'up' one element might be helpful.
# 
# * _**Hint:** The name of the club and the city are both inside of td elements, and they aren't distinguishable by class. Instead you'll just want to ask for all of the tds and then just ask for the text from the first or second one._
# * _**Hint:** If you use BeautifulSoup, you can select elements by attributes other than class or id - instead of `doc.find_all({'class': 'cat'})` you can do things like `doc.find_all({'other_attribute': 'blah'})` (sorry for the awful example)._
# * _**Hint:** If you love `pd.read_html` you might also be interested in `pd.concat` and potentially `list()`. But you'll have to clean a little more!_

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import numpy as np
import lxml
from bs4 import BeautifulSoup
import requests
import re
driver = webdriver.Chrome()


# In[2]:


driver.get("https://rocktumbler.com/blog/rock-and-mineral-clubs/")


# In[3]:


rows = driver.find_elements_by_tag_name('tr')


# In[49]:


club_list = []
for row in rows:
    try:
        state = row.find_elements_by_tag_name('h3')[0].text.strip()
    except:
        pass
        try:
    #         print(row.find_elements_by_tag_name('h3')[0].text.strip())
            name_club = row.find_element_by_tag_name('a').text.strip()
            url = row.find_element_by_tag_name('a').get_attribute('href')
            place = row.find_elements_by_tag_name('td')[1].text.strip()
    #         print("-----")
        except:
            pass
        club = {
            'state': state,
            'name_club': name_club,
            'url': url,
            'place': place
        }
        club_list.append(club)


# In[51]:


# Honestly, I have no idea why I had to put the first line for the state in a separate tray loop.
# But when I had all that in one single loop it just didn't work. In fact, the code for state worked but I keep 
# getting erros on the remaining variables that they were not defined. Interestingly, each time I 'print(ed)' them
# but when I tried to save them to a variable and save them to a list, the loop brooke. This is just a random
# solution found with a lot of trial and error. Also, the Selenium window closed on its own after running this loop
# but I got what I wanted so I am not complaining.


# In[52]:


df = pd.DataFrame(club_list)
df.head(20)


# In[53]:


df.to_csv("rock-clubs.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




