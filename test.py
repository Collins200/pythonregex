#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
def read_remote(url):
  # assumes the url is already encoded (see urllib.parse.urlencode)
  with requests.get(url) as response:
    response.encoding = 'utf-8'
    if response.status_code == requests.codes.ok: # (that is 200)
      return response.text
  return None

#HAMLET_URL = "fill me in"
HAMLET_URL = "https://www.gutenberg.org/cache/epub/2265/pg2265.txt"
hamlet = read_remote(HAMLET_URL)
print(hamlet)


# In[2]:


def get_hash(text):
  import hashlib
  return hashlib.md5(text.encode('utf-8')).hexdigest()
value=get_hash(hamlet)
expected_value= 'c4ffbf1618bda98a82314e6e21b1b7e7'
if value == expected_value:
    print ("Equal")
else:
    print ("Not equal")


# In[3]:


def get_hamlet():
    import os
    
    HAMLET_URL  = "https://www.gutenberg.org/cache/epub/2265/pg2265.txt"
    HAMLET_FILE = "hamlet.txt"
    
    text = None
     # write the code to read from HAMLET_FILE
    if os.path.exists(HAMLET_FILE):
        with open(HAMLET_FILE, 'rb') as f:
            f.read()
            text = ''
    else:
        text = read_remote(HAMLET_URL)
        # write the code to write text to HAMLET_FILE
        f = open(HAMLET_FILE, "w")
        f.write(text)
        f.close()
        
        
    return text
hamlet = get_hamlet()
get_hamlet=get_hamlet
print(hamlet[0:100])


# In[4]:


ANSWER_TO_LIFE = 42
def answer_to_life():
#     text = get_hamlet()
    text=hamlet
    idx = text.find('To be,')
    ans = text[idx:idx+ANSWER_TO_LIFE]
    return ans
print(answer_to_life())


# In[181]:


import re
def clean_hamlet(text):
    idx_start=text.find('Reed')
#     idx_end=idx_start+text[idx_start:].find('FINIS')
    remove=text[idx_start+5:]
    remove=remove.lstrip(" ").rstrip(" ")
    remove=remove.strip()
    pattern=r'\n\s+'
    remove=re.sub(pattern,'\n',remove)
    remove=remove.strip()
    return remove

clean_hamlet(hamlet)

# In[35]:


import collections
from collections import Counter
import re

def find_lucky(text,num):
    
    text = text.split(" ")
    pattern = r'^[A-Za-z\']+$'
    pattern = re.compile(pattern)
    possibleWords = {}
    for word in text:
        word = word.strip()
        if(re.match(pattern,word)):
            if(word.startswith("'") and word.endswith("'")):
                word = word.strip("'")
            
            word = word.lower()
            if(len(word)==num):
                if word not in possibleWords:
                    possibleWords[word] = 1 
                else:
                    possibleWords[word] += 1
    
    luckyWords = []
    for key in possibleWords:
        if(possibleWords[key] == num):
            luckyWords.append(key)
    if(len(luckyWords)==num):
        luckyWords.sort()
        return luckyWords
    else:
        return []
find_lucky(hamlet,2)


# In[7]:


def test_777():
    hamlet = clean_hamlet(get_hamlet())
    print(find_lucky(hamlet, 7))
test_777()


# In[ ]:




