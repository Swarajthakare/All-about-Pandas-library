#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv')
df


# In[4]:


type(df)


# In[5]:


df.columns


# ### data preprocessing = nrows mens how many rows you want to print

# In[7]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',nrows = 1)
df


# In[8]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',nrows = 5)
df


# #### usecols 

# In[10]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',usecols = [0])
df


# In[11]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',usecols = [1])
df


# In[12]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',usecols = [0,1])
df


# In[13]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',usecols = [2,4,7])
df


# ### changing header = skiprows 

# In[14]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',skiprows = 1)
df


# In[19]:


# skiping row


# In[20]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',skiprows = [1])
df


# In[21]:


#skiping perticular row


# In[18]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',skiprows = [2])
df


# In[22]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',skiprows = [1,2,3])
df


# ### index_col = changing index

# In[23]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',index_col = 'ID')
df


# In[24]:


df = pd.read_csv(r'B:\Worked dataset\Data sets\New folder\Fortune_10.csv',index_col = 2)
df


# In[ ]:




