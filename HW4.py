#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Q1
import numpy as np
numbers=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
numbers*2


# In[18]:


numbers.ndim


# In[19]:


numbers.shape


# In[21]:


#Q2
for row in numbers:
    for column in row:
        print(column, end=' ')
    print()


# In[1]:


#Q3
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,6])
ypoints=np.array([5,10])
plt.plot(xpoints,ypoints)
plt.show()


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([3,6,9,12])
ypoints=np.array([2,8,1,10])
plt.plot(xpoints,ypoints,marker='D')
plt.show()


# In[12]:


#Q5
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([2,4,6,14,10,12])
plt.plot(ypoints,'D:r',ms=10,mec='g',mfc='g')
plt.show()


# In[ ]:




