#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus import brown, gutenberg, indian, treebank, wordnet


# In[3]:


# Download necessary corpora
nltk.download('brown')
nltk.download('gutenberg')
nltk.download('indian')
nltk.download('treebank')
nltk.download('wordnet')


# In[4]:


# Accessing the Brown Corpus
print("Brown Corpus Categories:", brown.categories())
print("Number of Sentences in Brown Corpus:", len(brown.sents()))
print("Number of Words in Brown Corpus:", len(brown.words()))


# In[5]:


# Accessing the Gutenberg Corpus
print("\nGutenberg Corpus File IDs:", gutenberg.fileids())
emma_words = gutenberg.words('austen-emma.txt')
print("Number of Words in Austen's Emma:", len(emma_words))


# In[7]:


# Accessing the Indian Corpus
print("Number of Sentences in Indian Corpus:", len(indian.sents()))


# In[8]:


# Accessing the Treebank Corpus
print("\nNumber of Sentences in Treebank Corpus:", len(treebank.sents()))
print("Number of Words in Treebank Corpus:", len(treebank.words()))


# In[9]:


# Accessing WordNet
synsets = list(wordnet.all_synsets('n'))  # Get all noun synsets
print("\nNumber of Synsets in WordNet (Nouns):", len(synsets))


# In[ ]:




