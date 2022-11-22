# hybrid-search-demo
Demo with Python Flask UI based on a web-crawl of Pinecone.io as source data

# References
https://docs.google.com/document/d/1Tx3tHC8PA9r5NfsTONpGMLurwZUj5phYcDa5JI6qJAU/edit#heading=h.8fup2t4burfu

overall_score = alpha * dense_score + (1-alpha)*sparse_score  
sparse_score = (overall_score - alpha * dense_score) / (1-alpha)
avg_doc_len = (# terms in the corpus) / (# docs in the corpus)
