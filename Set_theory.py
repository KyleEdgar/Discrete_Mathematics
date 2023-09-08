#!/usr/bin/env python
# coding: utf-8

# In[11]:


from venn import venn
get_ipython().run_line_magic('matplotlib', 'inline')

HUH = {
    "People Sure of the Assignment": {"John", "Peter", "Joseph"},
    "People Who thought it was Easy ": {"Steve", "Jobs", "Bill", "Gates", "Not Kyle"},
    "People Who Don't Know": {"Kyle", "Edgar", "Mikhael"}, "People Unsure of Assignment": {"Kyle", "Edgar", "Mikhael"}
}
venn(HUH)


# In[ ]:





# In[ ]:




