#!/usr/bin/env python
# coding: utf-8

# ## Logging on
# 
# Use Selenium to visit https://webapps1.chicago.gov/buildingrecords/ and accept the agreement.
# 
# > Think about when you use `.find_element_...` and when you use `.find_elementSSS_...`

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import lxml
from bs4 import BeautifulSoup
driver = webdriver.Chrome()


# In[4]:


driver.get("https://webapps1.chicago.gov/buildingrecords/")


# In[6]:


driver.find_element_by_id("rbnAgreement1").click()
driver.find_element_by_id("submit").click()


# In[ ]:





# In[ ]:





# ## Searching
# 
# Search for **400 E 41ST ST**.

# In[7]:


driver.find_element_by_id("fullAddress").send_keys("400 E 41ST ST")


# In[8]:


driver.find_element_by_id("submit").click()


# ## Saving tables with pandas
# 
# Use pandas to save a CSV of all **permits** to `Permits - 400 E 41ST ST.csv`. Note that there are **different sections of the page**, not just one long permits table.

# In[15]:


tables = pd.read_html(driver.page_source)
tables[0]


# In[17]:


# The scraped table has all dates as NaN which is becaue the date has a span tag with "disply:None".


# ## Saving tables the long way
# 
# Save a CSV of all DOB inspections to `Inspections - 400 E 41ST ST.csv`, but **you also need to save the URL to the inspection**. As a result, you won't be able to use pandas, you'll need to use a loop and create a list of dictionaries.
# 
# You can use Selenium (my recommendation) or you can feed the source to BeautifulSoup. You should have approximately 157 rows.
# 
# You'll probably need to find the table first, then the rows inside, then the cells inside of each row. You'll probably use lots of list indexing. I might recommend XPath for finding the table.
# 
# *Tip: If you get a "list index out of range" error, it's probably due to an issue involving `thead` vs `tbody` elements. What are they? What are they for? What's in them? There are a few ways to troubleshoot it.*

# In[28]:


inspection_table = driver.find_element_by_id("resultstable_inspections")
rows = inspection_table.find_elements_by_tag_name("tr")


# In[ ]:





# In[48]:


results = []
for row in rows:
    try:
        INSP = row.find_elements_by_tag_name('td')[0].text.strip()
        INSP_url = row.find_elements_by_tag_name('td')[0].find_element_by_tag_name('a').get_attribute('href')
        inspection_date = row.find_elements_by_tag_name('td')[1].text.strip()
        status = row.find_elements_by_tag_name('td')[2].text.strip()
        type_description = row.find_elements_by_tag_name('td')[3].text.strip()
        result = {
            'INSP': INSP,
            'INSP_url': INSP_url,
            'inspection_date': inspection_date,
            'status': status,
            'type_description': type_description
        }
        results.append(result)
    except:
        pass
results


# In[49]:


df = pd.DataFrame(results)
df.to_csv("inspections-new.csv", index=False)


# In[52]:


df1 = pd.read_csv("inspections-new.csv")
df1.head()


# ### Loopity loops
# 
# > If you used Selenium for the last question, copy the code and use it as a starting point for what we're about to do!
# 
# If you click the inspection number, it'll open up a new window that shows you details of the violations from that visit. Count the number of violations for each visit and save it in a new column called **num_violations**.
# 
# Save this file as `Inspections - 400 E 41ST ST - with counts.csv`.
# 
# Since it opens in a new window, we have to say "Hey Selenium, pay attention to that new window!" We do that with `driver.switch_to.window(driver.window_handles[-1])` (each window gets a `window_handle`, and we're just asking the driver to switch to the last one.). A rough sketch of what your code will look like is here:
# 
# ```python
# # Click the link that opens the new window
# 
# # Switch to the new window/tab
# driver.switch_to.window(driver.window_handles[-1])
# 
# # Do your scraping in here
# 
# # Close the new window/tab
# driver.close()
# 
# # Switch back to the original window/tab
# driver.switch_to.window(driver.window_handles[0])
# ```
# 
# You'll want to play around with them individually before you try it with the whole set - the ones that pass are very different pages than the ones with violations! There are a few ways to get the number of violations, some easier than others.

# In[ ]:


# Ran out of time with this one.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




