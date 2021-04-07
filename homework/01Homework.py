#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
a=np.arange(15).reshape(3,5)
print(a)


# In[20]:


print('list(a):',list(a))
print('tolist():',a.tolist())
#list(a)是使用python裡面的list將array 轉換
#tolist()則是利用np的公式,只提列出list裡面的數字


# In[15]:


a = np.random.randint(10, size=6) 
b = np.random.randint(10, size=(3,4)) 
c = np.random.randint(10, size=(2,3,2))


# In[174]:


a=np.random.randint(10,size=6)
print(a)


# In[181]:


a=np.random.randint(10,size=6)
print(a)
print('ndim:',a.ndim)
print('shape:',a.shape)
print('size:',a.size)
print('dtype:',a.dtype)
print('itemsize:',a.itemsize)
print('data:',a.data)


# In[190]:


b=np.random.randint(10,size=(3,4))
print(b)
print('ndim:',b.ndim)
print('shape:',b.shape)
print('size:',b.size)
print('dtype:',b.dtype)
print('itemsize:',b.itemsize)
print('data:',b.data)


# In[193]:


c = np.random.randint(10, size=(2,3,2))
print(c)
print('ndim:',c.ndim)
print('shape:',c.shape)
print('size:',c.size)
print('dtype:',c.dtype)
print('itemsize:',c.itemsize)
print('data:',c.data)


# In[194]:


a = np.random.randint(10, size=6) 

print(a.tolist())
print(list(a))


# In[199]:


b = np.random.randint(10, size=(3,4)) 

print(b.tolist())
print(list(b))

list(b)


# In[241]:


c = np.random.randint(10, size=(2,3,2)) 
print(c)
print(c.tolist())
print(list(c))


# In[ ]:


#進階


# In[ ]:




