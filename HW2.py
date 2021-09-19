#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
n=0
while n <10:
    print(n)
    n=n+1
    if n==5:
        break


# In[2]:


#Q2
n=0
while n < 5:
    print(n)
    n += 1
else:
    print(n,"is not less than 5")


# In[3]:


#Q3
fruits=["banana","blueberry","apple","strawberry"]
for fruit in fruits:
    if fruit == "apple":
        break
    print("I like",fruit)
print("apple is really a fruit?") 


# In[4]:


#Q4
sum=0
i=1
while i <=30:
    sum=sum+i
    i=i+1
print("The sum is", sum)


# In[5]:


#Q5
weather={'Sunny': 'play', 'Rainy': 'watch TV', 'Cloudy': 'walk'}
for name,values in weather.items():
    print("When", name, "let us", values)
weather.update({"snowy":"ski"})
print(weather)


# In[11]:


#Q6
weather={'Sunny': 'play', 'Rainy': 'watch TV', 'Cloudy': 'walk'}
for name,values in weather.items():
    if name =='Sunny':
        print("When", name, "let us", values)
    elif name=='Rainy':
        print("When", name, "let us", values)
    else:
        print("When", name, "let us", values)


# In[23]:


#Q7
grade=90
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

