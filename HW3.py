#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Q1
marks={'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}
for name, grade in marks.items():
    print(name,grade)


# In[33]:


# all students mean grade, max, min
#Q2   
sum_grade=sum(marks.values())
count_grade=list(marks.values())
mean_grade=sum_grade/len(count_grade)
print("All the student's mean grade is", mean_grade)
max_grade=max(marks.values())
print("The maximual grade is", max_grade)
min_grade=min(marks.values())
print("The minimal grade is", min_grade)


# In[34]:


#Q3
for name in marks.keys():
    if 'J' in name:
        break
    print(name)


# In[35]:


#Q4
for name in marks.keys():
    if 'J' in name:
        continue
    print(name)


# In[36]:


#Q5
def students(student_name):
    marks={'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}
    for student in marks:
        if student == student_name:
            print(marks[student])
            break
    else:
        print("I cannot find this student's name")
students("James")
students("Angel")


# In[37]:


#Q6
def less_than(num):
    n=0
    while n<num:
        m=n**2
        print("n is:",n,"power of n is:",m)
        n+=1
    else:
        print("Greater than",num)
less_than(8)


# In[38]:


#Q7
def integers(num):
    n=1
    total=0
    while n<=num:
        total+=n
        n+=1
    print("The sum is",total)
integers(5)


# In[39]:


#Q9
def integers(num):
    total=0
    for n in range(1,num+1):
        total+=n
        print("The sum is",total)
integers(5)


# In[40]:


#Q10
def minimal(v1,v2,v3,v4):
    min_value=v1
    if v2<min_value:
        min_value=v2
    if v3<min_value:
        min_value=v3
    if v4<min_value:
        min_value=v4
    return min_value
minimal(10,4,8,3)

