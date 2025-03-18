#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',na_values = 'not available')
df2


# In[3]:


df2.isnull()


# In[4]:


df2.isnull().sum()


# In[6]:


df2.isnull().sum().sum()


# In[7]:


df2.notnull()


# In[8]:


df2.notnull().sum()


# In[10]:


df2.notnull().sum().sum()


# In[14]:


import numpy as np


# In[16]:


#series
sr = pd.Series([1,2,3,np.nan,4,np.NAN])
sr


# In[17]:


sr.isnull()


# In[ ]:




