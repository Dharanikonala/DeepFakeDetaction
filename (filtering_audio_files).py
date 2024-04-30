#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


get_ipython().system('pip3 install --upgrade pip')


# In[3]:


import glob
import pandas as pd
import os


# In[4]:


path =  '/Users/dharani/Downloads/dfdc_train_part_1/'
video_files = glob.glob(path + "*.mp4")


# In[5]:


len(video_files)


# In[6]:


names =[]
for i in video_files:
    names.append(i.split("\\")[-1])
    


# In[7]:


len(names)


# In[8]:


media_altered = pd.read_csv('/Users/dharani/Downloads/metadata.csv')


# In[9]:


common = []
for i in names:
    if i in media_altered:
        common.append(i)


# In[10]:


len(common)


# In[11]:


len(names)


# In[12]:


import os
for i in common:
    file =path+i
    if os.path.exists(file):
        os.remove(path+i)
    else:
        print("The file does not exist")


# In[53]:


new = glob.glob(path + "*.mp4")
len(new)


# In[ ]:




