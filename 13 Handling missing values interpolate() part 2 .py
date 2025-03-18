#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ##  interpolate 
# 
# ### parameters = axis, inplace, limit, limit_direcction, limit_area

# In[2]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Student_10.csv')
df


# In[3]:


df.interpolate()


# ### axis
# 

# In[4]:


df.interpolate(axis = 1) #data type must be flot and integer


# In[5]:


type(df)


# In[6]:


df.dtypes #data type must be flot and integer


# ### limit

# In[7]:


df.interpolate(limit = 1) #fill only one value by linear


# In[ ]:


#limit_direction = default forword


# In[8]:


df.interpolate(limit_direction = 'backward')


# In[9]:


df.interpolate(limit = 1,limit_direction = 'backward')


# In[11]:


df.interpolate(limit = 1,limit_direction = 'both')# one value fill forword and other one fill back word


# In[14]:


#limit_area = default = None
#inside = only fill Nan surrounded by valid values
#outside = only fill nan outside valid values


# In[12]:


df.interpolate(limit_area = 'inside')


# In[18]:


df.interpolate(limit_area = 'outside')


# #### inplace = update the same data frame in place if possible
# 
# 
# #by default fill value linearly
# 

# In[21]:


df.interpolate(inplace = True)


# In[22]:


df


# In[ ]:




