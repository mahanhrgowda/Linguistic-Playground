import nltk
from nltk import pos_tag, word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def analyze_grammar(sentence):
    tokens = word_tokenize(sentence)
    return pos_tag(tokens)