#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ### what is pandas interpolate() = pandas interpolate() function is basically used to fill nan values in DataFrame or series.
# 
# #Very powerful function
# 
# #Uses various interpolation techniques
# 
# 
# syntax : DataFrame.interpolate()
# 
# series.interpolate()
# 
# #parameters : method, axis, limit, inplace, limit_direction, limit_area

# In[2]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Student_10.csv')
df


# In[4]:


# fill missing value by gussing but only for numeric value not for categorical values


# In[3]:


df.interpolate()


# In[6]:


df.interpolate(method =  'linear') #same as interpolate


# In[7]:


type(df.Date[0])


# ### method = Time

# In[11]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Student_10.csv',parse_dates = ['Date'])
df2


# In[12]:


type(df2.Date[0])


# In[13]:


df.interpolate()


# In[19]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Student_10.csv',parse_dates = ['Date'],index_col ='Date')
df2


# In[16]:


df2.interpolate(method = 'time' )


# ### index

# In[17]:


df.interpolate(method = 'index')


# In[29]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Student_10.csv',index_col = 'Class')
df


# In[30]:


df.interpolate(method = 'index')


# In[31]:


df.interpolate(method = 'nearest')


# In[36]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Student_10.csv',parse_dates = ['Date'],index_col = 'Date')
df2


# In[37]:


df2.interpolate(method = 'polynomial',order = 1) #order 1 means


# In[38]:


df2.interpolate(method = 'polynomial',order = 2)


# In[40]:


df2.interpolate(method = 'spline',order = 2) #spline means a retangular key filling


# In[ ]:




