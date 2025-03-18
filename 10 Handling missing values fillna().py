#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# #### parameters :  value , method, axis, inplace, limit, downcast, **kwargs

# ## fillina fills the NaN values with given values(input)
# 
# #### syntax : DataFrame.fillna()
# 

# In[3]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_5.csv')
df


# ### value = fill any scaler value like 0,3,4,2

# In[4]:


df.fillna(0)


# ### filling values using dict for specific colume

# In[5]:


df.fillna({'Name':'none','Profit':0,'Growth':0})


# ### method = us for filling value by forword backword upside downside
# 
# ## backfill = fill backword value means 
# ## bfill = fill backword value means filling upside value
# ## pad = same as ffill
# ## ffill = fill forword value mean downside value 
# ## None =
# 

# In[6]:


#ffill
df.fillna(method = 'ffill')


# In[7]:


#bfill and

df.fillna(method = 'bfill')


# ### axis
# 
# #### method is complsary
# 

# In[9]:


df.fillna(method = 'ffill' ,axis = 0) # axis 0 means rows


# In[10]:


df.fillna(method = 'ffill',axis = 1)


# In[11]:


df.fillna(method = 'bfill',axis = 1)


# In[12]:


df.fillna(method = 'bfill',axis = 0)


# ## limit
# 
# ### defalut value is None.
# ### fill only one value if provided value is only one like limit = 1
# ### 
# 

# In[14]:


df.fillna(0,limit = 1)


# In[16]:


df.fillna(0,limit = 2)


# In[15]:


df.fillna(method = 'ffill',limit = 2)


# ## inplace
# 
# #### modife previous data frame

# In[17]:


df.fillna(5, inplace = True)


# In[18]:


df


# In[ ]:




