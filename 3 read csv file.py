#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


help(pd.read_csv)


# In[10]:


df1 = pd.read_csv('B:\\Worked dataset\\tips.csv')
df1


# In[11]:


df1 = pd.read_csv(r'B:\Worked dataset\tips.csv')
df1


# In[12]:


import os


# In[13]:


print(os.getcwd())


# In[14]:


#cwd = current working directory


# In[ ]:




