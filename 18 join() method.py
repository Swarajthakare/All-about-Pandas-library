#!/usr/bin/env python
# coding: utf-8

# ### what is pandas join() method?
# #### DataFrame join is a convenient method for combining the columns of two potentially differently- indexed.
# 
# #### syntax: DataFram.join()
# 
# 
# ### parameters : other, on , how, isuffix, rsuffix.

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.DataFrame({'A':[1,2,3],
                   'B':[10,20,30]})
df2 = pd.DataFrame({'C':[4,5,6],
                   'D':[40,50,60]})
display(df1,df2)


# In[4]:


#other: 'DataFrame | Series',
#on: 'IndexLabel | None' = None,
#how: 'str' = 'left',
#lsuffix: 'str' = '',
#rsuffix: 'str' = '',
#sort: 'bool' = False,


# In[5]:


df1.join(df2)


# In[6]:


df2.join(df1)


# In[7]:


df1.join(df2)


# In[ ]:


#diff index not join use for it index


# In[8]:


df3 = pd.DataFrame({'A':[1,2,3],
                   'B':[10,20,30]},
                  index = ['a','b','c'])
df4 = pd.DataFrame({'C':[4,5,6],
                   'D':[40,50,60]},
                  index = ['a','b','c'])


# In[9]:


display(df3,df4)


# In[10]:


df3.join(df4)


# In[16]:


#not equal keys and values for 
#handling it use how


# In[17]:


df5 = pd.DataFrame({'A':[1,2,3],
                   'B':[10,20,30]},
                  index = ['a','b','c'])
df6 = pd.DataFrame({'C':[4,5],
                   'D':[40,50]},
                  index = ['a','b'])


# In[18]:


display(df5,df6)


# In[19]:


df5.join(df6)


# In[20]:


# for handling it use how


# In[21]:


df5.join(df6,how = 'right')


# In[24]:


df5.join(df6,how = 'left')


# In[22]:


df5.join(df6,how = 'inner')


# In[23]:


df5.join(df6,how = 'outer')


# ### same colume name

# In[25]:


df7 = pd.DataFrame({'A':[1,2,3],
                   'B':[10,20,30]},
                  index = ['a','b','c'])
df8 = pd.DataFrame({'A':[4,5],
                   'B':[40,50]},
                  index = ['a','b'])


# In[26]:


display(df7,df8)


# In[30]:


df7.join(df8)# use for lsuffix or rsuffix 


# In[31]:


df7.join(df8, lsuffix = '_1')


# In[32]:


df7.join(df8, rsuffix = '_1')


# In[ ]:




