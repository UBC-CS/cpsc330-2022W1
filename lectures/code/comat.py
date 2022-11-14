from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import coo_matrix, csr_matrix

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

class CooccurrenceMatrix:
    def __init__(self, corpus, 
                       tokenizer = word_tokenize, 
                       window_size = 3):
        self.corpus = corpus
        self.tokenizer = tokenizer
        self.window_size = window_size
        self.vocab = {}
        self.cooccurrence_matrix = None    
        
    def fit_transform(self):
        """
        Creates a co-occurrence matrix. 
        
        Returns vocabulary (dict) and co-occurrence matrix (csr_matrix)
        """
        data=[]
        row=[]
        col=[]
        for tokens in self.corpus:
            for target_index, token in enumerate(tokens):
                # Get the index of the word in the vocabulary. 
                # If the word is not in the vocabulary, 
                # set the index to the size of the vocabulary. 
                i = self.vocab.setdefault(token, len(self.vocab))
                
                # Consider window_size context words on the left and 
                # on window_size context words on the right. 
                start = max(0, target_index - self.window_size)
                end = min(len(tokens), target_index + self.window_size + 1)
                
                for context_index in range(start, end):
                    # Do not consider the target word.  
                    if target_index == context_index: 
                        continue                        
                    j = self.vocab.setdefault(tokens[context_index], len(self.vocab))
                    # Set diagonal to 0
                    if i == j:
                        continue
                    data.append(1.0); row.append(i); col.append(j);
        self.cooccurrence_matrix = csr_matrix((data,(row,col)))
        return self.cooccurrence_matrix        

    def get_feature_names(self):
        return list(self.vocab.keys())    
        
    def get_word_vector(self, word):
        """
        Given a word returns the word vector associated with 
        it from the co-occurrence matrix. 

        Parameters
        -----------
        word : str 
            the word to look up in the vocab.
            
        Returns 
        -----------
        numpy sparse matrix
            The sparse word vector assoated with the word. 
        """
        if word in self.vocab: 
            return self.cooccurrence_matrix[self.vocab[word]]
        else:
            print('The word not present in the vocab')
