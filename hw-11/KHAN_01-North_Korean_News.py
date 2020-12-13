#!/usr/bin/env python
# coding: utf-8

# # North Korean News
# 
# Scrape the North Korean news agency http://kcna.kp
# 
# Save a CSV called `nk-news.csv`. This file should include:
# 
# * The **article headline**
# * The value of **`onclick`** (they don't have normal links)
# * The **article ID** (for example, the article ID for `fn_showArticle("AR0125885", "", "NT00", "L")` is `AR0125885`
# 
# The last part is easiest using pandas. Be sure you don't save the index!
# 
# * _**Tip:** If you're using requests+BeautifulSoup, you can always look at response.text to see if the page looks like what you think it looks like_
# * _**Tip:** Check your URL to make sure it is what you think it should be!_
# * _**Tip:** Does it look different if you scrape with BeautifulSoup compared to if you scrape it with Selenium?_
# * _**Tip:** For the last part, how do you pull out part of a string from a longer string?_
# * _**Tip:** `expand=False` is helpful if you want to assign a single new column when extracting_
# * _**Tip:** `(` and `)` mean something special in regular expressions, so you have to say "no really seriously I mean `(`" by using `\(` instead_
# * _**Tip:** if your `.*` is taking up too much stuff, you can try `.*?` instead, which instead of "take as much as possible" it means "take only as much as needed"_

# In[2]:


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


# In[3]:


driver = webdriver.Chrome()


# In[4]:


driver.get('http://kcna.kp')


# In[5]:


driver.find_element_by_link_text("English").click()


# In[6]:


news_list = []
a_tags = driver.find_elements_by_tag_name("a")
for oclick in a_tags:
    try:
        head = oclick.text.strip()
#         print(head)
        art_ID = oclick.get_attribute('onclick')
        if head == "":
            try:
                head = oclick.find_element_by_tag_name('img').get_attribute('title')
#                 print(oclick.find_element_by_tag_name('img').get_attribute('title'))
            except:
                pass
#         print("------")
    except:
        pass
    art_dict = {
        'header': head,
        'art_ID': art_ID
    }
    news_list.append(art_dict)


# In[7]:


df = pd.DataFrame(news_list)


# In[8]:


df.to_csv("nkn", index=False)


# In[9]:


df1 = pd.read_csv("nkn")


# In[10]:


df1 = df1.dropna()


# In[11]:


df1 = df1[~df1.art_ID.str.contains("(^fn_convert\w.+?)")]


# In[12]:


df1 = df1[df1.art_ID.str.contains("^fn_showArticle")]


# In[20]:


df1 = df1[~df1.art_ID.str.contains("^fn_showArticle\('',")]


# In[37]:


df1 = df1[df1.header.str.contains("^\w.+?\s")]


# In[41]:


df1 = df1[~df1.header.str.contains("News of 80-day Campaign")]


# In[72]:


#for some reason regex stopped working for articles with no ID.


# In[71]:


df1 = df1[~df1.header.str.contains("Education & Public Health")]


# In[75]:


df1 = df1[~df1.header.str.contains("Top News")]


# In[76]:


df1 = df1[~df1.header.str.contains("Science & Technology")]


# In[77]:


df1 = df1[~df1.header.str.contains("Supreme Leader's Activities")]


# In[78]:


df1 = df1[~df1.header.str.contains("Latest News")]


# In[82]:


df1 = df1[~df1.header.str.contains("International Relations")]


# In[97]:


df1['article_ID'] = df1.art_ID.str.extract("(\w\w\d\d\d\d\d\d\d)", expand=False)


# In[99]:


df1.to_csv("nk-news.csv", index=False)


# In[ ]:


#-Ends-

