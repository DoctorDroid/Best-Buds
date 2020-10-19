import pickle
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from pydantic import BaseModel


# Load in pickle_tfidf
'''
The pickle module implements binary protocols for serializing and de-serializing
a Python object structure. “Pickling” is the process whereby a Python object hierarchy
is converted into a byte stream, and “unpickling” is the inverse operation, whereby a
byte stream (from a binary file or bytes-like object) is converted back into an object
hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,”
1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
 - from https://docs.python.org/3/library/pickle.html#module-pickle

----------`
Serialization is the process of converting an object into a stream of bytes to store the object or
transmit it to memory, a database, or a file. Its main purpose is to save the state of an object
in order to be able to recreate it when needed. The reverse process is called deserialization. 
-(prolly wikipedia) Jan 2, 2020

storage of the data in a form that allows recovery of its original structure.

Data Serialization — The Hitchhiker's Guide to Pythondocs.python-guide.org › scenarios › serialization

-----------

In information retrieval, tf–idf or TFIDF, short for 
term frequency–inverse document frequency, is a numerical statistic
that is intended to reflect how important a word is to a document
in a collection or corpus. 
  -from Wikipediaen.wikipedia.org › wiki
'''


tfidf_pickle = open('./pickles/pickle_tfidf', 'rb') # read binary
tfidf = pickle.load(tfidf_pickle)
tfidf_pickle.close()

# Load in pickle_nn
nn_pickle = open('./pickles/pickle_nn', 'rb')
nn = pickle.load(nn_pickle)
nn_pickle.close()

# Load in pickle_nn
dataset_pickle = open('./pickles/pickle_dataset', 'rb')
df = pickle.load(dataset_pickle)
dataset_pickle.close()

class PredRequest(BaseModel):
    user_input: str

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "user_input": "happy, relaxed"
    #         }
    #     }
    def pred(self):
        user_input = self.user_input # ALL? the user's input?

        # pre-process new data
        new_dtm = tfidf.transform([user_input]) # new data model; Transform a count matrix 
                                                # to a normalized tf or tf-idf representation
                                                # https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html
        '''
        (scikit link^ The goal of using tf-idf instead of the raw frequencies of occurrence of a token in a given document is to scale down the impact of tokens that 
        occur very frequently in a given corpus and that are hence empirically less informative than features that occur in a small fraction of the training corpus.
        '''
        new_dtm = pd.DataFrame(new_dtm.todense(), columns=tfidf.get_feature_names()) # todense() rtns a matrix.  Returns indices of and distances to the neighbors of each point. 
        '''
        The underscore prefix is meant as a hint to another programmer that a variable or method starting with a single underscore is intended for internal use.
        This convention is defined in PEP 8. This isn't enforced by Python. Python does not have strong distinctions between “private” and “public” variables like Java does.
        from https://dbader.org/blog/meaning-of-underscores-in-python#:~:text=The%20underscore%20prefix%20is%20meant,public%E2%80%9D%20variables%20like%20Java%20does.
        '''   

        indices_final = indices[0]
        rec_strains = [] # list to hold recommended strains
        for x in indices_final:
            print(df['Strain'][x])
            rec_strains.append(df['Strain'][x])
        return rec_strains