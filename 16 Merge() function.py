#!/usr/bin/env python
# coding: utf-8

# ### what is pandas merge fuction?
# 
# #### Pandas merge connects columns or indexes in DataFrame based on one or more keys.

# In[1]:


import pandas as pd


# In[4]:


df1 = pd.DataFrame({'ID':[1,2,3,4],
                  'Class':[9,10,11,12]})
df1


# In[13]:


df2 = pd.DataFrame({'ID':[1,2,3,4],
                   'Name':['A','B','C','D']})
df2


# In[14]:


pd.merge(df1,df2,on = 'ID')


# In[15]:


pd.merge(df2,df1,on = 'ID')


# In[16]:


pd.merge(df2,df1,on = 'ID') #if ID is not similer then it ll skip that row insted of use how


# #how

# In[18]:


pd.merge(df1,df2,on = 'ID', how = 'left')


# In[19]:


pd.merge(df1,df2,on = 'ID', how = 'right')


# In[21]:


pd.merge(df1,df2,on = 'ID', how = 'outer')## for accessing all rows, all diff values.


# In[23]:


pd.merge(df1,df2,on = 'ID', how = 'outer',indicator = True)#to identify which are the values present in which data frame.


# In[24]:


pd.merge(df1,df2, left_index = True, right_index = True)## when we have multy index use left right index.


# In[25]:


pd.merge(df1,df2)## if index is not same then it will not return anything


# In[26]:


##if there is 2 diff columnes of class not index then how to access it?


# In[29]:


df3 = pd.DataFrame({'ID':[1,2,3,4],
                  'Class':[9,10,11,12]})
df1


# In[31]:


df4 = pd.DataFrame({'ID':[1,2,3,4],
                  'Class':[9,10,11,12]})
df4


# In[33]:


pd.merge(df3,df4, on = 'ID')# see class is showing diffrently and her is suffixes parmeter working


# In[34]:


pd.merge(df3,df4,on = 'ID',suffixes = ('_Higher','_Middle'))


# In[ ]:




