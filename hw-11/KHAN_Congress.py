#!/usr/bin/env python
# coding: utf-8

# # Scraping one page per row
# 
# Let's say we're interested in our members of Congress, because who isn't? Read in `congress.csv`.

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


# In[4]:


df = pd.read_csv("congress.csv")
df.head()


# # Let's scrape one
# 
# The `slug` is the part of the URL that's particular to that member of Congress. So `/james-abdnor/A000009` really means `https://www.congress.gov/member/james-abdnor/A000009`.
# 
# Scrape his name, birthdaye, party, whether he's currently in congress, and his bill count (don't worry if the bill count is dirty, you can clean it up later).

# In[14]:


driver = webdriver.Chrome()


# In[100]:


# for row in df.head(2).iterrows():
#     driver.get(f"https://www.congress.gov/member/{row[1]['slug']}")
#     print(driver.find_element_by_class_name('legDetail').text.strip())
#     print(driver.find_element_by_tag_name('tr').text.strip())
#     print(driver.find_element_by_class_name('results-number').text.strip())
    
    
    


# # Build a function
# 
# Write a function called `scrape_page` that makes a URL out of the the `slug`, like we're going to use `.apply`.

# In[ ]:





# In[99]:


# def scrape_page(row):
#     driver.get(f"https://www.congress.gov/member/james{row['slug']}")
#     data = {}
#     data['name'] = driver.find_element_by_tag_name("h1").text.strip()
#     data['party'] = driver.find_element_by_tag_name("tr").text.strip()
#     data['bills'] = driver.find_element_by_class_name("results-number").text.strip()
#     print(data)


# In[44]:


def scrape_page(row):
    try:
        driver.get(f"https://www.congress.gov/member/james{row['slug']}")
        data = {}
        data['name'] = driver.find_element_by_tag_name("h1").text.strip()
        data['party'] = driver.find_element_by_tag_name("tr").text.strip()
        data['bills'] = driver.find_element_by_class_name("results-number").text.strip()
    except:
        pass
    return pd.Series(data)


# In[46]:


scraped_df = df.apply(scrape_page, axis=1)


# In[47]:


scraped_df.head()


# In[56]:


scraped_df.bills = scraped_df.bills.str.replace(",", "")


# In[59]:


scraped_df.bills = scraped_df.bills.str.extract("1-100 of (\d.+)", expand=False)


# In[62]:


scraped_df['name_new'] = scraped_df.name.str.extract("(\w.*) \(")


# In[64]:


scraped_df['birth_year'] = scraped_df.name.str.extract("\w.* \((\d.+?) ")


# In[67]:


scraped_df['tenure'] = scraped_df.name.str.extract("(In Congress \w.*)")


# In[73]:


scraped_df = scraped_df.dropna(subset=['tenure'])


# In[83]:


scraped_df['currently_in_congress'] = scraped_df.name.str.extract("In Congress \d.+? - (Present)")


# In[86]:


scraped_df['currently_in_congress'] = scraped_df['currently_in_congress'].fillna("No")


# In[88]:


scraped_df['currently_in_congress'] = scraped_df['currently_in_congress'].str.replace("Present", "Yes")


# In[91]:


scraped_df['party'] = scraped_df['party'].str.extract("Party (\w.+)")


# In[97]:


df_new = df.merge(scraped_df, how='outer', left_index=True, right_index=True)


# In[98]:


df_new.to_csv("congress-plus-scraped.csv", index=False)


# In[ ]:





# # Do the scraping
# 
# Rewrite `scrape_page` to actually scrape the URL. You can use your scraping code from up above. Start by testing with just one row (I put a sample call below) and then expand to your whole dataframe.
# 
# Save the results as `scraped_df`.
# 
# * **Hint:** Be sure to use `return`!
# * **Hint:** Make sure you return a `pd.Series`

# In[ ]:





# In[ ]:


# Test with this
scrape_page({'slug': 'neil-abercrombie/A000014'})


# In[ ]:





# ## Join with your original dataframe
# 
# Join your new data with your original data, adding the `_scraped` suffix on the new columns. You can use either `.join` or `.merge`, but be sure to read the docs to know the difference!

# In[ ]:





# ## Save it
# 
# Save your combined results to `congress-plus-scraped.csv`.

# In[ ]:





# In[ ]:




