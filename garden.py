#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spacy


# In[ ]:


get_ipython().system('python -m spacy download en_core_web_sm')


# In[ ]:


# Load the spaCy English model 
nlp = spacy.load("en_core_web_sm")


# In[ ]:


# Your garden path sentences 
gardenpathSentences = [ 
    "Mary gave the child a Band-Aid.", 
    "That Jill is never here hurts.", 
    "The cotton clothing is made of grows in Mississippi." 
] 


# In[ ]:


# Process each sentence 
for sentence in gardenpathSentences: 
    doc = nlp(sentence) 
    print(f"Original sentence: {sentence}") 
    for ent in doc.ents: 
        print(f"Entity: {ent.text} | Label: {ent.label_} | Explanation: {spacy.explain(ent.label_)}") 


# In[ ]:


# Entities I looked up: 
# 1. Mary (PERSON): Refers to people and including fictional.
# 2. Jill (PERSON): Refers to people and including fictinal. 
# Both entities make sense in terms of the associated words. 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




