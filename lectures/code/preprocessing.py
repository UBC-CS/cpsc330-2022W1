# -*- coding: utf-8 -*-
import os, sys
import numpy as np
import pandas as pd

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

class MyPreprocessor:
    
    def __init__(self, texts, stopwords = list(set(stopwords.words('english'))), strip_puncts=True):
        self.stop_words = stopwords
        self.texts = texts
        if strip_puncts: 
            punctuation = string.punctuation            
            self.stop_words += list(punctuation)
            self.stop_words.extend(['``','’', '`','br','"',"”", "''", "'s"])        
            
    def __iter__(self):
        for text in self.texts: 
            text = text.replace(r'<br />',' ')            
            sentences = sent_tokenize(text)
            for sent in sentences: 
                tokenized = word_tokenize(sent)
                preprocessed = []
                for token in tokenized:
                    token = token.lower()
                    if token not in self.stop_words:
                        preprocessed.append(token)
                yield preprocessed            
    
if __name__=="__main__":
    corpus = ["It was a great day. I loved the movie and spending time with you. I wish we had more time.", 
              "The sky is always blue underneath. Remember that."]
    sentences = MyPreprocessor(corpus)
    print(sentences)
    for sent in sentences:
        print(sent)

