#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Problem 3: Set combinations

Given the predefined sets below and using set methods
3.a Is set E a subset of set A
 .b Is set E a strict subset of set A
 .c Create a set that is the intersection of set A and set B
 .d Create a set that is the union of sets C, D and E
 .e add 9 to the set
 .f Using == compare this set to the list in one_a
 .g Explain why they are not the same. What would you need to change if you
    get_ipython().set_next_input('    wanted this to be True');get_ipython().run_line_magic('pinfo', 'True')
 

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}


# In[3]:


three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}


# In[4]:


three_a = three_setE.issubset(three_setA)
print(three_a)


# In[5]:


three_b = three_setE.issuperset(three_setA)
print(three_b)


# In[7]:


three_c = three_setA.intersection(three_setB)
print(three_c)


# In[8]:


three_d = three_setC.union(three_setD,three_setE)
print(three_d)


# In[11]:


three_e = three_d.add(9)
print(three_d)


# In[13]:


#three_f
one_a = [0,1,2,3,4,5,6,7,8,9]

if one_a == three_d:
    print(True)
else: 
    print(False)


# In[ ]:


#three_g
#They are not same because they have different values.We need to add value o in three_d to make it true. 

