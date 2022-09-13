#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.

4.a Create a variable of type int with the value of 8
 .b Create an empty list 
 .c Using type(), add the type of 4.a to this list
 .d Add 0.39 to 4.c
 .e append the type of 0.39 to the list
 .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    decimal places, and append to list.
 .g append the type to the list


# In[105]:


four_a = int(8)


# In[106]:


four_b = []


# In[107]:


four_c = four_b.append(type(four_a))
print(four_b)


# In[108]:


four_d = four_b.append(0.39)
print(four_b)


# In[109]:


four_e = four_b.append(type(0.39))
print(four_b)


# In[110]:


four_f1 = round(0.39**-10)
print(four_f1)


# In[111]:


four_f = four_b.append(four_f1)
print(four_b)


# In[112]:


four_g = four_b.append(type(four_f1))
print(four_b)


# In[ ]:


#Problem 5: More variable type changes

Continue from where you left off in Problem 4.

5.a Manually create a dictionary where the values are items in the list from where we left in 
    problem 4, and the keys should be their index in the list. Print the dictionary.
 .b Add 300 and coerce it into a string
 .c append the type to the list
 .d slice the string up to the 2nd element
 .e append the type to the list
 .f use list comprehension to convert this into a new list of integers
 .g append the type to the list
 .h append the type of three_setA to the list
"""


# In[113]:


five_a = {"integer": 0.39, "float": 12284}


# In[117]:


five_b = str(300)
print(type(five_b))


# In[118]:


five_c = four_b.append(type(five_b))
print(four_b)


# In[119]:


five_d = five_b[:2]
print(five_d)


# In[120]:


five_e = four_b.append(type(five_d))
print(four_b)


# In[122]:


five_f = list(five_d)
print(five_f)


# In[123]:


five_g = four_b.append(type(five_f))
print(four_b)


# In[124]:


three_setA = {1,2,3,4,5}


# In[125]:


five_h = four_b.append(type(three_setA))
print(four_b)

