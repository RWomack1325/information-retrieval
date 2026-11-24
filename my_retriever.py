
"""
Other examples of methods that might reasonably be added include:

a. A method to precompute the inverse document frequency value of each term in the
collection, again based just on the inverted index. Thus, the index maps each term to
the documents that contain it, whose number determines its document frequency.

b. A method to precompute the document vector size for each document in the collection.
Note that this can be computed for all documents at the same time, in a single pass over
the index. Where TF.IDF term weighting is used, the IDF values must be computed
before the document vector sizes are calculate
"""
class Retrieve:

    # Retrieval index maps: terms -> docs -> counts
    
    # Create new Retrieve object storing index and term weighting
    # scheme. (You can extend this method, as required.)
    def __init__(self,index, term_weighting): 
        self.index = index
        self.term_weighting = term_weighting
        self.num_docs = self.compute_number_of_documents()
        
    def compute_number_of_documents(self):
        self.doc_ids = set() 
        for term in self.index:
            self.doc_ids.update(self.index[term])
        return len(self.doc_ids)

    # Method performing retrieval for a single query (which is 
    # represented as a list of preprocessed terms).
    # Returns list of doc ids for relevant docs (in rank order).

    # This already runs for every query (64)
    """
    Your task is to complete the definition of the Retrieve class, so that the overall IR system
    performs retrieval based on the vector space model. Your code should allow alternative term
    weighting schemes (selected by the “-w” option) to be used, i.e. binary vs. term frequency vs.
    TFIDF. Evaluate your system’s performance over the CACM test collection under the various
    configurations that arise from the alternative choices for preprocessing and for term weighting
    
    Queries are pre-processed:
        Split on apostrophes
        Split on dashes
        Split on any punctuation?
        Numbers removed from tokens they are a part of
        Lowercase
        First 10 PRE-PROCESSED terms are taken
        
    There are 10769 unique terms (without using stemming and stopwords)
    There are 10356 unique terms (JUST using stopwords)
    There are 7218 unique terms (JUST using stemming)
    There are 6923 unique terms (using BOTH stopwords and stemming)
    """

    def for_query(self, query):

        if self.term_weighting == 'binary':
            # Building binary index
            query_term_dict = dict()
            for term in query:
                # If the term is in the full set of terms
                if term in self.index:
                    # Add the term to the dict of query terms
                    if term not in query_term_dict:
                        query_term_dict[term] = set()
                    for doc in self.index[term]:
                        query_term_dict[term].add(doc)
                else:
                    continue
                print(term, len(query_term_dict[term]))



        return query




