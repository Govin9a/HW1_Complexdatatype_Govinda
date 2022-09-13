#!/usr/bin/env python
# coding: utf-8

# In[ ]:


2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    two_a, ensure the key names are the same as the dictionary names.
 .b Using keys, retrieve the Dango's name from 2.a
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
 .e Coerce the keys of 2.d into a list
 .f Coerce the values of 2.d into a list
 .g Use the zip function to combine 2.e and 2.f into a dictionary again


two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}


# In[6]:


two_patient_dictionary_kinoko = {"name" : "Kinoko", "year" : 2021}
two_patient_dictionary_dango = {"name" : "Dango", "year" : 2019}
two_patient_dictionary_mochi  = {"name" : "Mochi", "year" : 2020}


# In[8]:


two_a = {"two_patient_dictionary_kinoko" : two_patient_dictionary_kinoko,"two_patient_dictionary_dango":two_patient_dictionary_dango,"two_patient_dictionary_mochi":two_patient_dictionary_mochi}
print(two_a)


# In[10]:


two_b = two_a['two_patient_dictionary_dango']['name']
print(two_b)


# In[15]:


two_a['two_patient_dictionary_mochi']={"name" : "Mochi", "year" : 2018}
print(two_a)


# In[18]:


two_d = {"kinoko":2021,"Dango":2019,"Mochi":2018}


# In[21]:


two_e = list(two_d.keys())
print(two_e)


# In[23]:


two_f = list(two_d.values())
print(two_f)


# In[25]:


two_g = dict(zip(two_e, two_f))
print(two_g)

