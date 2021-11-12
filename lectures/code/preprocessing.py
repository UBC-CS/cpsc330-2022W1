import os, sys
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from scipy.sparse import coo_matrix, csr_matrix
import string

class MyPreprocessor:
    
    def __init__(self):
        self.stop_words = list(set(stopwords.words('english')))
        punctuation = string.punctuation
        self.stop_words += list(punctuation)
        self.stop_words.extend(['``','’', '`','br','"',"”", "''", "'s"])        
        
    def __preprocess(self, text):
        """
        Given a text, this function returns a preprocessed 
        text which is tokenized and free from stopwords. 

        Parameters
        ----------        
        text : str
            text to be preprocessed

        Returns: 
        ----------        
        list 
            a list containing tokens in the preprocessed text

        """
        # Replace line break tags with a whitespace 
        text = text.replace(r'<br />',' ')
        preprocessed = []    
        
        # Tokenization using nltk word tokenization
        tokenized = word_tokenize(text)
        for token in tokenized:
            token = token.lower()
            if token not in self.stop_words:
                preprocessed.append(token)
        return preprocessed

    def preprocess_corpus(self, doc_list):
        """
        Given a list of documents doc_list (e.g., reviews, news articles) 
        this function carries out sentence tokenization and other preprocessing
        and returns a preprocessed corpus. 

        Parameters
        ----------
        doc_list : list
            a list of strings, each string representing a document. 

        Returns:
        ----------
        list 
            a list of lists of preprocessed (tokenized and stopword-removed)
            
        sentences in the documents with the following format. 
        [[sent1_word1, sent1_word2, sent1_word3, ...], [sent2_word1, sent2_word2, sent2_word3, ...], ...]        
            
        Examples
        --------
        >>> corpus = ["It was a great day. I loved the movie and spending time with you.", 
              "The sky is always blue underneath. Remember that."]
        >>> preprocess_corpus(corpus)
        [['great', 'day'], ['loved', 'movie', 'spending', 'time'], 
        ['sky', 'always', 'blue', 'underneath'], ['remember']]
        
        """
        preprocessed_corpus = []
        for doc in doc_list:
            # sentence tokenization using nltk sent_tokenize
            try: 
                sentences = sent_tokenize(doc)        
            except:
                print('Sentence tokenization failed', doc)
                sys.exit(0)    
            preprocessed_corpus.extend([self.__preprocess(sentence) for sentence in sentences])            
        return preprocessed_corpus 
    
    
if __name__=="__main__":
    pp = MyPreprocessor()
    corpus = ["It was a great day. I loved the movie and spending time with you.", 
              "The sky is always blue underneath. Remember that."]
    
    print(pp.preprocess_corpus(corpus))