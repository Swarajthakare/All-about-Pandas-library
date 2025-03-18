#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ### dropna()

# In[7]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_5.csv')
df


# In[8]:


df.dropna() #8 th


# ## axis by default is 0 and 0 means row 1 means column

# In[10]:


# drop value from columne using axis parameter
df.dropna(axis = 1)

# and print those columne who had not null values


# In[11]:


#how = if any row and column has nan value that will deleted by how
#how by default input is 0 

df.dropna(how = 'any')


# In[12]:


df.dropna(axis = 1,how = 'any')


# In[13]:


#all - if data set has all nan value in a row that row will deleted 
#all delete only all vlaues when data set has all nan values
df.dropna(how = 'all')


# In[14]:


#thresh = thresh print that row who has atleatst one nan value
#or given input values
#by default input is zero


df.dropna(thresh = 1)


# In[16]:


df.dropna(thresh = 2)


# In[17]:


df.dropna(thresh = 4)


# In[18]:


df.dropna(thresh = 5)


# In[19]:


#subset = use when want to delete specific column or nan value column


# In[21]:


df.dropna(subset = ['Name'])


# In[22]:


df.dropna(subset = ['Profit'])


# In[24]:


# inplace = update that dataframe and remove nan values

df.dropna(inplace = True)
df


# In[ ]:




