#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
import matplotlib.pyplot as plt
import numpy as np
y1=np.array([1,2,3,4,5])
y2=np.array([5,6,7,8,9])
y3=np.array([9,10,11,12,13])
plt.plot(y1,linewidth='2')
plt.plot(y2,linewidth='2')
plt.plot(y3,linewidth='2')
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()


# In[2]:


#Q2
import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(0,0.2,800)
plt.hist(x)
plt.show()


# In[3]:


#Q3
mydic={"Apples":45,"Bananas":25,"Cherries":15,"Dates":20}
fruit_list=list(mydic.keys())
count_list=list(mydic.values())
print(fruit_list)
print(count_list)

import matplotlib.pyplot as plt
import numpy as np
y=np.array(count_list)
mylabels=fruit_list
myexplode=[0.1,0.1,0.1,0.1]
plt.pie(y,labels=mylabels,explode=myexplode)
plt.legend()
plt.show()

x=np.array(fruit_list)
y=np.array(count_list)
plt.bar(x,y,width=0.8)
plt.show()


# In[4]:


#Q4
import matplotlib.pyplot as plt
import numpy as np
math_marks = [88, 92, 80, 89, 90, 80, 60, 88, 80, 84]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range,math_marks,color='r')

science_marks = [75, 59, 69, 48, 65, 56, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range,science_marks,color='g')

plt.legend(['math_marks','science_marks'])
plt.title("Scatter Plot")
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")

plt.show()


# In[5]:


#Q5
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2])
y = np.array([99,86,87,88,111,86,103])
plt.subplot(1, 4, 1)
plt.scatter(x,y)
plt.title("Scatter Plot")

y1 = np.array([5,7,9,12,14])
y2 = np.array([2,5,7,5,8])
plt.subplot(1, 4, 2)
plt.plot(y1)
plt.plot(y2)
plt.title("Multiple Line Plot")

x = np.array(["Male","Female"])
y = np.array([40,60])
plt.subplot(1, 4, 3)
plt.bar(x,y)
plt.title("Bar Chat")

y = np.array([20,46,15,35])
plt.subplot(1, 4, 4)
plt.pie(y)
plt.title("Pie Chat")

plt.show()


# In[ ]:




