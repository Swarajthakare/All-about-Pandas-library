#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# #### def = pandas DataFrame is two dimenstional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (row and columns).

# ## how to create python pandas dataframe

# In[2]:


import pandas as pd


# In[5]:


empt_df = pd.DataFrame()
print(empt_df)


# In[4]:


type(empt_df)


# In[6]:


lst = ['a','b','c']
print(lst)


# In[8]:


df1 = pd.DataFrame(lst)
print(df1)


# In[9]:


df1


# ### creating list of list for 2 dimentional array

# In[12]:


ls_of_ls = [[1,2,3],[1,2,3],[1,2,3]]
print(ls_of_ls)


# In[13]:


df2 = pd.DataFrame(ls_of_ls)
df2


# ### creating pandas datafrom using dictionary

# In[14]:


dict1 = {'ID': [11,2,33,44]}
dict1


# In[15]:


df3 = pd.DataFrame(dict1)
df3


# In[18]:


dict3 = {'ID': [11,2,33,44],'ST':[1,2,3,4]}
dict3


# In[19]:


df3 = pd.DataFrame(dict3)
df3


# ### list of dictionary

# In[20]:


lst_dict = [{'a':1,'b':2,},{'a':3,'b':4}]
df5 = pd.DataFrame(lst_dict)
df5


# In[22]:


lst_dict1 = [{'a':1,'b':2,},{'a':3,'b':4,'c':5}]
df6 = pd.DataFrame(lst_dict1)
df6


# ### creating dictionaries of series

# In[23]:


dict_sr = {'ID':pd.Series([1,2,3]), 'ST':([11,22,33])}
df7 = pd.DataFrame(dict_sr)
df7


# In[ ]:




