#!/usr/bin/env python
# coding: utf-8

# # Texas Cosmetologist Violations
# 
# Texas has a system for [searching for license violations](https://www.tdlr.texas.gov/cimsfo/fosearch.asp). You're going to search for cosmetologists!

# ## Setup: Import what you'll need to scrape the page
# 
# We'll be using Selenium for this, *not* BeautifulSoup and requests.

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()


# ## Starting your search
# 
# Starting from [here](https://www.tdlr.texas.gov/cimsfo/fosearch.asp), search for **cosmetologist violations** for people with the last name **Nguyen**.

# In[2]:


driver.get("https://www.tdlr.texas.gov/cimsfo/fosearch.asp")


# In[3]:


driver.find_element_by_id("pht_status").send_keys("Cosmetologists")
driver.find_element_by_id("pht_lnm").send_keys("Nguyen")
button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[18]/td/input[1]")
button.click()


# In[ ]:





# In[ ]:





# In[ ]:





# ## Scraping
# 
# Once you are on the results page, do this.

# ### Loop through each result and print the entire row
# 
# Okay wait, that's a heck of a lot. Use `[:10]` to only do the first ten (`listname[:10]` gives you the first ten).

# In[4]:


table_rows = driver.find_elements_by_tag_name("tr")
for row in table_rows[:10]:
    print(row.text.strip())
    print("----------")


# ### Loop through each result and print each person's name
# 
# You'll get an error because the first one doesn't have a name. How do you make that not happen?! If you want to ignore an error, you use code like this:
# 
# ```python
# try:
#    # try to do something
# except:
#    # Instead of stopping on an error, it'll jump down here instead
#    print("It didn't work')
# ```
# 
# It should help you out. If you don't want to print anything, you can type `pass` instead of the `print` statement. Most people use `pass`, but it's also nice to print out debug statements so you know when/where it's running into errors.
# 
# **Why doesn't the first one have a name?**

# In[5]:


table_cells = driver.find_elements_by_tag_name("td")
table_cells[5].text.strip()


# In[6]:


for row in table_rows:
    try:
        print(row.find_element_by_class_name("results_text").text.strip())
    except:
        print("Did not work")
#     for cell in table_cells[:10]:
        


# In[ ]:





# In[ ]:





# In[ ]:





# ## Loop through each result, printing each violation description ("Basis for order")
# 
# > - *Tip: You'll get an error even if you're ALMOST right - which row is causing the problem?*
# > - *Tip: You can get the HTML of something by doing `.get_attribute('innerHTML')` - it might help you diagnose your issue.*
# > - *Tip: Or I guess you could just skip the one with the problem...*

# In[24]:


for row in table_rows:
    try:
        print(row.find_elements_by_tag_name("td")[2].text.strip())
    except:
        print("Did not work")
    print("--------")


# ## Loop through each result, printing the complaint number
# 
# - TIP: Think about the order of the elements

# In[31]:


for row in table_rows:
    print("Complaint #:")
    try:
        print(row.find_elements_by_tag_name("span")[10].text.strip())
    except:
        print("Did not work")
    print("--------")


# ## Saving the results
# 
# ### Loop through each result to create a list of dictionaries
# 
# Each dictionary must contain
# 
# - Person's name
# - Violation description
# - Violation number
# - License Numbers
# - Zip Code
# - County
# - City
# 
# Create a new dictionary for each result (except the header).
# 
# > *Tip: If you want to ask for the "next sibling," you can't use `find_next_sibling` in Selenium, you need to use `element.find_element_by_xpath("following-sibling::div")` to find the next div, or `element.find_element_by_xpath("following-sibling::*")` to find the next anything.

# In[32]:


results = []
for row in table_rows:
    try:
        name = row.find_element_by_class_name("results_text").text.strip()
        v_description = row.find_elements_by_tag_name("td")[2].text.strip()
        v_number = row.find_elements_by_tag_name("span")[10].text.strip()
        lic_number = row.find_elements_by_tag_name("span")[8].text.strip()
        zip_code = row.find_elements_by_tag_name("span")[6].text.strip()
        county = row.find_elements_by_tag_name("span")[4].text.strip()
        city = row.find_elements_by_tag_name("span")[2].text.strip()
        result = {
            'name': name,
            'v_description': v_description,
            'v_number': v_number,
            'lic_number': lic_number,
            'zip_code': zip_code,
            'county': county,
            'city': city,
        }
        results.append(result)
    except:
        pass
results


# ### Save that to a CSV
# 
# - Tip: Use `pd.DataFrame` to create a dataframe, and then save it to a CSV.

# In[33]:


import pandas as pd
df = pd.DataFrame(results)
df.head()


# In[34]:


df.to_csv("texas_cosmet.csv", index=False)


# ### Open the CSV file and examine the first few. Make sure you didn't save an extra weird unnamed column.

# In[35]:


df1 = pd.read_csv("texas_cosmet.csv")
df1.head()


# ## Let's do this an easier way
# 
# Use Selenium and `pd.read_html` to get the table as a dataframe.

# In[37]:


import lxml
from bs4 import BeautifulSoup


# In[42]:


table = pd.read_html(driver.page_source)
table[0]


# In[ ]:




