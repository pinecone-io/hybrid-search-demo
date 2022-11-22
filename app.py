import os
from flask import Flask, flash, render_template, request, send_from_directory
from sentence_transformers import SentenceTransformer
from collections import Counter
import hybrid_pinecone_client
import mmh3
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

api_key="1f136ea0-a50c-4af1-a9ad-93de37970fab"
pinecone_env = "us-west1-gcp"
index_name = "hybrid-search-demo"

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

        if not search:
            flash('Please enter your search')
        else:
            results = hybrid_query(search, 20, alpha)
            pinecone_results = [{'resultArray': results}]
            return render_template('index.html', results=pinecone_results)

    return render_template('index.html', initialPage=True)


# load a sentence transformer model from huggingface
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# create a tokenizer
class Tokenizer:
  def __init__(self):
    self.stemmer = SnowballStemmer('english')

  def encode(self, text):
    words = [self.stemmer.stem(word) for word in word_tokenize(text)]
    ids = [mmh3.hash(word, signed=False) for word in words]
    return dict(Counter(ids))

tokenizer = Tokenizer()

def hybrid_query(question, top_k, alpha):
    # convert the question into a sparse vector
    sparse_vec = tokenizer.encode(str(question))
    # convert the question into a dense vector
    dense_vec = model.encode([question]).tolist()
    # set the query parameters to send to pinecone
    query = {
      "topK": top_k,
      "vector": dense_vec,
      "sparseVector": sparse_vec,
      "alpha": alpha,
      "includeMetadata": True
    }
    # query pinecone with the query parameters
    result = pinecone.query(query)
    # return search results as json
    return result