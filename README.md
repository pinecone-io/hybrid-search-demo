# Pinecone Hybrid Search Demo
**Description**: Pinecone challenge Web UI searching Pinecone.io using hybrid search  
**Author**: Kevin M. Butler  
**Date**: Nov-2022  
**Version**: 1.0  
**Purpose**: This repository contains code to deploy a Python Flask application that is able to query Pinecone using vector search and more consicely, hybrid search to include dense and sparse vectors.  

## Table of contents
[Introduction](#introduction)  
[Getting started](#getting-started)  
[Resources](#resources)  

### Introduction
The Pinecone [vector database](https://www.pinecone.io/learn/vector-database/) makes it easy to build high-performance vector search applications. Developer-friendly, fully managed, and easily scalable without infrastructure hassles.
Vector databases have become very popular in semantic use-cases and now, Pinecone has introduced the ability to combine dense and sparse vectors together to perform hybrid search.  
Hybrid search is the ability to use tokenized keywords (sparse vectors) and semantic representations (dense vectors) together to perform searches based on both lexical and semantic meanings. Traditionally, this would require two technologies, multiple queries, and post-processing to accomplish this task. With Pinecone hybrid search, you can now merge these technologies together in one fast, scalable, fully managed system.
This repository aims to demonstrate a web-crawl of [pinecone.io](pinecone.io), stored in Pinecone, and queried using a Python Flask application as the web UI. The web UI processes the query into sparse and dense vectors, then sends the query to Pinecone. The results are json responses which can include metadata values as part of the response.  
The distinction of lexical versus semantic is controlled by the 'alpha' parameter which is passed in as a value between 0 and 1. A lower value closer to 0 is considered more lexical or keyword oriented. A higher value closer to 1 is more semantic and gives more weight to the meaning of the words rather than the more exact matching of the terms that lexical is suited for. 

### Getting started
This is how to get started  

### Resources
#### Pinecone
[Hybrid search early access documentation](https://docs.google.com/document/d/1Tx3tHC8PA9r5NfsTONpGMLurwZUj5phYcDa5JI6qJAU/edit#heading=h.8fup2t4burfu)  
[Introducing the hybrid index to enable keyword-aware semantic search](https://www.pinecone.io/learn/hybrid-search/?utm_medium=email&_hsmi=231739825&_hsenc=p2ANqtz-_KdCTL8VpX0tqZ_e3Z9MSJSM6toQaESiTgWZCBVIbYMByQiG3rxb7GBh4WGY2mF9J44eYp_lrs9kEL-oQ_y8ivEdFjcQ&utm_content=231739825&utm_source=hs_email)  
[Getting Started with Hybrid Search](https://www.pinecone.io/learn/hybrid-search-intro/)  
[Pinecone's New *Hybrid* Search - the future of search?](https://youtu.be/0cKtkaR883c)  
#### Python
[Python Flask](https://flask.palletsprojects.com/en/2.2.x/)  
#### Digital Ocean
[Digital Ocean](https://www.digitalocean.com/)