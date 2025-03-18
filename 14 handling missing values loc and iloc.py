#!/usr/bin/env python
# coding: utf-8

# ### loc
# #### access a group of rows and colums by label(s) or a boolan array.
# #return desired value location
# 
# syntax : DataFrame.loc[]
# 

# In[4]:


import pandas as pd


# In[5]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\student_results.csv')
df


# In[6]:


df.loc[0] # [0] is lable or index


# In[7]:


df.loc[4]


# In[8]:


df.loc[[0,1]]


# In[9]:


df.loc[[2,4]]


# In[10]:


df.loc[4,'Class']


# In[11]:


df.loc[0:3,'Class']


# In[13]:


df.loc[0:2,'Percantege']


# In[19]:


df.loc[[False,False,True]]


# In[22]:


df.loc[df['Class']< 11,['Percantege']]


# ## iloc
# #### integer location - based indexing
# 
# #syntax = DataFrame.iloc[]
# 
# 
# #in iloc we can phech data throuh index to access row and columns
# #Data selecting opration perform

# In[24]:


df


# In[23]:


df.iloc[4]


# In[25]:


df.iloc[[0]]


# In[27]:


df.iloc[:,0] # : means all columnes


# In[28]:


df.iloc[[0,1]]


# In[32]:


df.loc[:,0] #loc cant do lable indexing 


# In[30]:


df.iloc[[True,False,True]]


# In[ ]:




