#!/usr/bin/env python
# coding: utf-8

#  ### na_values / keep_default_na / na_filter

# In[1]:


import pandas as pd


# In[2]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',true_values = ['Health'])
df2


# In[3]:


# nan


# ### na_values = for making string values as nan

# In[5]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',na_values = 'not available')
df2


# In[6]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',na_values = ['no values','not available'])
df2


# #### making nan to spesific value of perticular columne
# 

# In[7]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',na_values = {'companies':'no values'})
df2


# ### keep_default_na = 
# 
# ## True = consider Nan
# ## False = not Consider Nan

# In[8]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',keep_default_na = True)
df2


# ## Data parsing = processing of  analysing a string of symboles.
# ### because of it boost performance
# 

# In[ ]:




