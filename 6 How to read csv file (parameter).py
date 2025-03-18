#!/usr/bin/env python
# coding: utf-8

# ## how to read csv files 3

# #### head() / tail() / dtype / true_values / false_values

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv')
df


# In[4]:


df.head()


# In[5]:


df.head(2)


# In[6]:


df.tail()


# In[7]:


df.tail(1)


# ## changing datatype of perticular columne

# In[10]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',dtype = {'ID': 'float64'})
df


# In[11]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',dtype = {'ID': 'float64','Profit':'float64'})
df


# #### true_value =if yes string value where present in any column of data set for chacking that value is present or not present in data set use true_value paramerter.
# ### insted of yes it will print true.

# In[12]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv')
df


# In[27]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',true_values = ['Yes'])
df2


# In[26]:


#false


# In[28]:


df2 = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',true_values = ['Yes'],false_values = ['No'])
df2


# In[ ]:




