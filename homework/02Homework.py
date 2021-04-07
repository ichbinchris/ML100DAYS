#!/usr/bin/env python
# coding: utf-8

# In[ ]:


[簡答題] 請問 type(...) 跟 a.dtype 這兩個語法有什麼不同？


# In[1]:


import numpy as np
a=np.arange(12).reshape(3,4)
print(a)
print('dtype:',a.dtype)
print('type(a):', type(a))

#type(...)得出的是numpy array的類型
#a.dtype則是得出a 的data 種類


# In[ ]:


[簡答題] 承上題，請判斷下列三種寫法為何不正確？


# In[18]:


def is_dtype(a, t):
    return a.dtype is t
# is 必須跟 np.dtype比較

def is_dtype(a, t):
    return type(a) == np.dtype(t)
# type(a) 為numpy array的類型, 而非比較內容 data type

def is_dtype(a, t):
    return type(a) is np.dtype(t)
#同上


# In[ ]:


請撰寫一個判斷 a 的元素是否等於指定資料型態的函式


# In[19]:


a=np.random.randint(10,size=(3,4))
print(a)
print('a.dtype:',a.dtype)


# In[24]:


print(a.dtype == "int32")
print(type(a) == np.dtype("int32"))
print(a.dtype == np.dtype('int32'))
print(type(a) is np.dtype('int32'))
print(a.dtype is np.dtype('int32'))

# 進階
# In[ ]:




