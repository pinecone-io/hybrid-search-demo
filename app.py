import os
from flask import Flask, flash, render_template, request, send_from_directory
from sentence_transformers import SentenceTransformer
from collections import Counter
import hybrid_pinecone_client
api_key="1f136ea0-a50c-4af1-a9ad-93de37970fab"
pinecone_env = "us-west1-gcp"
index_name = "hybrid-test"

pinecone = hybrid_pinecone_client.HybridPinecone(api_key,pinecone_env)
pinecone.connect_index(index_name)

# ...
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ksr*LrP3EtfJQiT!gG*i_wURj'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        search = request.form['search']
        alpha = request.form['alpha']
        if not alpha:
            alpha = 0.3

        #TODO cleanse search terms

        if not search:
            flash('Please enter your search')
        else:
            results = hybrid_query(search, 20, alpha)
            pinecone_results = [{'resultArray': results}]
            return render_template('index.html', results=pinecone_results)

    return render_template('index.html', initialPage=True)

# Helpers
from transformers import BertTokenizerFast

# load bert tokenizer from huggingface
tokenizer = BertTokenizerFast.from_pretrained(
    'bert-base-uncased'
)

from sentence_transformers import SentenceTransformer

# load a sentence transformer model from huggingface
model = SentenceTransformer(
    'multi-qa-MiniLM-L6-cos-v1'
)
model

def build_dict(input_batch):
  # store a batch of sparse embeddings
    sparse_emb = []
    # iterate through input batch
    for token_ids in input_batch:
        # convert the input_ids list to a dictionary of key to frequency values
        d = dict(Counter(token_ids))
        # remove special tokens and append sparse vectors to sparse_emb list
        sparse_emb.append({key: d[key] for key in d if key not in [101, 102, 103, 0]})
    # return sparse_emb list
    return sparse_emb

def generate_sparse_vectors(context_batch):
    # create batch of input_ids
    inputs = tokenizer(
            context_batch, padding=True,
            truncation=True,
            max_length=512
    )['input_ids']
    # create sparse dictionaries
    sparse_embeds = build_dict(inputs)
    return sparse_embeds

def hybrid_query(question, top_k, alpha):
    # convert the question into a sparse vector
    sparse_vec = generate_sparse_vectors([question])
    # convert the question into a dense vector
    dense_vec = model.encode([question]).tolist()
    # set the query parameters to send to pinecone
    query = {
      "topK": top_k,
      "vector": dense_vec,
      "sparseVector": sparse_vec[0],
      "alpha": alpha,
      "includeMetadata": True
    }
    # query pinecone with the query parameters
    result = pinecone.query(query)
    # return search results as json
    return result


