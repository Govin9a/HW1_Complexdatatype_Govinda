#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 1: Lists, Sets and Coersion

1#a Create a list of integers no fewer than 10 items from 0 to 9.
 #b Add 3 to the 5th indexed element
 #c Coerce all elements in the list to floats using list comprehension
 #d Coerce the list to a set
 #e Using a method, append int 10 to the set
 #f Using a method, pop an item from the set
 #g Using a length counting function, count the number of items in the set
 #h Check if the number of items in the set is the same as the 
    number of items in the list
 #i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
 #j Coerce 1.i to a set
 #k Count the number of elements in the 1.j


# In[22]:


#list of integer 0 to 9
One_a = [0,1,2,3,4,5,6,7,8,9]


# In[39]:


one_b adding 3 to the 5th indexed elements
one_b = [0,1,2,3,4,5,6,7,8,9]
one_b.insert(5,3)
print(one_b)


# In[44]:


#one_c 
one_a = [0,1,2,3,4,5,6,7,8,9]
one_c = [float(x) for x in one_a]
print(one_c)


# In[45]:


one_d = set(one_a)
print(one_d)


# In[49]:


one_e = one_d.add(10)
print(one_d)


# In[53]:


one_f= one_d.remove(0)
print(one_d)


# In[84]:


#one_g
one_g = len(one_d)
print(one_g)


# In[85]:


#one_h
one_h = len(one_b)
print(one_h)


# In[83]:


#one_h
if one_g == one_h:
    print (True)
else:
    print(False)


# In[96]:


one_i = list(one_d)
print(one_i)
add = one_i + one_a
print(add)


# In[95]:


one_j=set(add)
print(one_j)


# In[99]:


one_k = len(one_j)
print(one_k)

