#!/usr/bin/env python
# coding: utf-8

# ### what id pandas concat() function?
# #### pandas provides various facilties for easily combining together Series, DataFrame and Panel objects.
# 
# 
# #syntax = pandas.concat()
# 
# #### paramerters: objs , axis, join, join_axes,  ignore_index, keys, sort

# In[1]:


import pandas as pd


# In[2]:


sr1 = pd.Series([0,1,2])
sr1


# In[3]:


sr2 = pd.Series([3,4,5])
sr2


# In[4]:


pd.concat([sr1,sr2])#objs


# In[5]:


sr3 = pd.Series([0,1,2])
sr3


# In[6]:


sr4 = pd.Series([5,6,7,8,9])
sr4


# In[7]:


pd.concat([sr3,sr4])


# In[8]:


#concating 2 unequal DataFrame


# In[9]:


df1 = pd.DataFrame({'ID':[1,2,3,4],
             'Name':['A','B','C','D'],
             'Class':[5,6,7,8]})
df1


# In[10]:


df2 = pd.DataFrame({'ID':[5,6,7,8],
             'Name':['E','F','G','H'],
             'Class':[9,10,11,12]})
df2


# In[11]:


pd.concat([df1,df2])


# In[12]:


pd.concat([df2,df1])


# In[13]:


pd.concat([df1,df2],axis = 1)# concate columne vise


# In[14]:


pd.concat([df1,df2],axis = 0,ignore_index = True)#for systemetic index


# # part 2

# #join
# #join_axis
# #keys
# #sort

# In[15]:


#unequal elemet data frame or unequal items concatination.


# In[16]:


df3 = pd.DataFrame({'ID':[1,2,3,4],
             'Name':['A','B','C','D'],
             'Class':[5,6,7,8]})
df3


# In[17]:


df4 = pd.DataFrame({'ID':[3,4],
             'Name':['C','D'],
             'Class':[7,8]})
df4


# In[18]:


pd.concat([df3,df4], axis = 1)


# #join

# In[19]:


pd.concat([df3,df4],axis = 1, join = 'inner')


# In[21]:


pd.concat([df3,df4],axis = 1, join = 'outer')


# #join_axes

# In[24]:


pd.concat([df3,df4],axis = 1, join_axes = [df3.index])


# #keys = for labeling to data set

# In[27]:


pd.concat([df1,df2],keys = ['df1','df2'])


# In[28]:


pd.concat([df1,df2],keys = ['First_df','Second_df'])


# In[29]:


pd.concat([df1,df2],axis = 1,keys = ['First_df','Second_df'])


# #different dataframe names of coumnes

# In[30]:


df5 = pd.DataFrame({'ID':[1,2,3,4],
             'Name':['A','B','C','D'],
             'Class':[5,6,7,8]})
df5


# In[32]:


df6 = pd.DataFrame({'Marks':[40,63,91,34]})
df6


# In[33]:


pd.concat([df5,df6])


# In[34]:


pd.concat([df5,df6],sort = False)


# In[35]:


pd.concat([df5,df6],sort = True)


# In[ ]:




