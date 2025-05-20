import nltk
from nltk import pos_tag, word_tokenize

nltk.download('punkt')
# Ensure necessary NLTK resources are downloaded
nltk.download("punkt", quiet=True)
nltk.download('averaged_perceptron_tagger')
# Ensure necessary NLTK resources are downloaded
nltk.download("averaged_perceptron_tagger", quiet=True)


def analyze_grammar(sentence):
    tokens = word_tokenize(sentence)
    return pos_tag(tokens)
