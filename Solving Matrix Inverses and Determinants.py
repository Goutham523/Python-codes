#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import linalg


# In[2]:


A = np.array(
       [
            [1, 9, 2, 1, 1],
            [10, 1, 2, 1, 1],
            [1, 0, 5, 1, 1],
            [2, 1, 1, 2, 9],
            [2, 1, 2, 13, 2],
       ]
)


# In[3]:


b = np.array([170, 180, 140, 180, 350]).reshape((5, 1))


# In[4]:


A_inv = linalg.inv(A)


# In[5]:


x = A_inv @ b


# In[20]:


print("\nInverse of,\n", A,"\nis : \n",A_inv)


# In[9]:


linalg.det(A)


# In[10]:


B = np.array(
       [
            [11, 91, 2, 33, 51],
            [10, 11, 2, 1, 11],
            [101, 0, 5, 11, 14],
            [20, 1, 10, 2, 9],
            [2, 13, 2, 13, 82],
       ]
)


# In[12]:


B_inv = linalg.inv(B)


# In[21]:


print("\nInverse of,\n", B,"\nis : \n",B_inv)


# In[ ]:




