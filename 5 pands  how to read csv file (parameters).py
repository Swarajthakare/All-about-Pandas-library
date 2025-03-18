#!/usr/bin/env python
# coding: utf-8

# # how to read csv file part 2

# ## header / prefix / names

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv')
df


# #### changing heading

# In[4]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',header = 1)
df


# In[5]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv', header = None)
df


# ### prefix = work with header, giving string headers

# In[6]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',header = None, prefix = 'Columns')
df


# ## names

# In[7]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',names = ['A','B','c','D','E','F','G'])
df


# In[9]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',names = ['ID','Name','Industry','Inception','Revenue','Expenses','Profit','Growth'])
df


# In[ ]:




