#!/usr/bin/env python
# coding: utf-8

# ### what is pandas Append Function?
# #### Pandas append function is used to append rows of other dataframe to the end of the given dataframe, returning a new dataframe object.
# 
# 
# #### syntax : DataFrame.append()
# 
# 
# #### parameters : other , ignore_index, sort.

# In[8]:


import pandas as pd


# In[9]:


df1 = pd.DataFrame({'A':[1,2,3],
                   'B':[10,20,30]})
df2 = pd.DataFrame({'C':[4,5,6],
                   'D':[40,50,60]})


# In[10]:


display(df1,df2)


# In[11]:


df1.append(df2)


# In[12]:


df1.append(df2,ignore_index = True)


# In[13]:


#changing position of value


# In[14]:


df2.append(df1)


# In[15]:


df1.append(df2,ignore_index = True)


# In[ ]:




