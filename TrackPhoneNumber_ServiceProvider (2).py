#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install phonenumbers


# In[8]:


import phonenumbers

country_code = int(input("Country Code: +"))
number = int(input("Enter your number: "))
Your_Number = f'+{country_code} {number}'
print("Your Number: ",Your_Number)

from phonenumbers import geocoder
ch_number = phonenumbers.parse(Your_Number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(Your_Number, "RO")
print(carrier.name_for_number(service_number, "en"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




