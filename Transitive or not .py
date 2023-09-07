#!/usr/bin/env python
# coding: utf-8

# In[4]:


def is_transitive(input_set):
    # Create a set of all pairs (a, b) and (b, c) in the input_set
    all_pairs = {(a, b): c for a in input_set for b in input_set for c in input_set if (a, b) in input_set and (b, c) in input_set}
    
    # Check if for every pair (a, b) and (b, c), the pair (a, c) is also in the set
    for (a, b), c in all_pairs.items():
        if (a, c) not in input_set:
            return False
    
    # If all pairs satisfy the condition, the set is transitive
    return True


# In[3]:


input_set = {(1, 2), (2, 3), (1, 3), (3, 4)}
result = is_transitive(input_set)
print("Is the set transitive?", result)


# In[ ]:





# In[ ]:




