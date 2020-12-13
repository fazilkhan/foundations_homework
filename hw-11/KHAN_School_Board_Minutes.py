#!/usr/bin/env python
# coding: utf-8

# # School Board Minutes
# 
# Scrape all of the school board minutes from http://www.mineral.k12.nv.us/pages/School_Board_Minutes
# 
# Save a CSV called `minutes.csv` with the date and the URL to the file. The date should be formatted as YYYY-MM-DD.
# 
# **Bonus:** Download the PDF files
# 
# **Bonus 2:** Use [PDF OCR X](https://solutions.weblite.ca/pdfocrx/index.php) on one of the PDF files and see if it can be converted into text successfully.
# 
# * **Hint:** If you're just looking for links, there are a lot of other links on that page! Can you look at the link to know whether it links or minutes or not? You'll want to use an "if" statement.
# * **Hint:** You could also filter out bad links later on using pandas instead of when scraping
# * **Hint:** If you get a weird error that you can't really figure out, you can always tell Python to just ignore it using `try` and `except`, like below. Python will try to do the stuff inside of 'try', but if it hits an error it will skip right out.
# * **Hint:** Remember the codes at http://strftime.org
# * **Hint:** If you have a date that you've parsed, you can use `.dt.strftime` to turn it into a specially-formatted string. You use the same codes (like %B etc) that you use for converting strings into dates.
# 
# ```python
# try:
#   blah blah your code
#   your code
#   your code
# except:
#   pass
# ```
# 
# * **Hint:** You can use `.apply` to download each pdf, or you can use one of a thousand other ways. It'd be good `.apply` practice though!

# In[44]:


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


# In[45]:


driver.get("http://www.mineral.k12.nv.us/pages/School_Board_Minutes")


# In[46]:


elements = driver.find_elements_by_tag_name('a')


# In[26]:


school_min = []
for element in elements[17:74]:
    date = element.text.strip()
    min_url = element.get_attribute('href')
    minutes = {
        'date': date,
        'min_url': min_url
    }
    school_min.append(minutes)
school_min


# In[34]:


df = pd.DataFrame(school_min)
df.head()


# In[42]:


df['date'] = pd.to_datetime(df['date'])


# In[81]:


df.tail()


# In[80]:


import urllib.request


# In[79]:


for row in df.iterrows():
    response = urllib.request.urlopen(row[1]['min_url'])
#     print(row)
    file = open(f"/Users/khanfazil/Documents/python_soma/homework/11-homework/school_min_pdfs/{row[1]['date']}.pdf", 'wb')
    file.write(response.read())
    file.close()


# In[ ]:


# Sorry for using a for loop with a dataframe, still don't understand how apply works. Please don't cut my fingers.

