#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# #what is pandas replace = values to the dataframe are replaced with other values dynamically.
# 
# #### parameters = to_replace

# In[3]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv')
df


# In[4]:


df.replace(to_replace = 'Health',value = 'Finance')


# In[5]:


#shortcut
df.replace('Health','Finance')


# In[6]:


df.replace(10,15)


# In[7]:


df.replace([1,2,3,4,5,6,7,8,9,10],0)


# In[8]:


df.replace([1,2,3,4,5,6,7,8,9,10],[11,22,33,44,55,66,77,88,99,100])


# In[9]:


df.replace({'Industry':'Health'},None)


# In[10]:


df.replace({'Industry':'Health','Profit':0},None)

#regex
#use to detect pattern 


# In[11]:


df


# In[12]:


df.replace('[A-Za-z]',0)


# In[13]:


df.replace('[A-Za-z]',0,regex = True)


# In[14]:


df.replace({'Industry':'[A-Za-z]'},0,regex = True)


# ## method
# 

# In[ ]:




