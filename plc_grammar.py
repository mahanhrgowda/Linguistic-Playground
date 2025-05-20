import nltk

# Ensure NLTK tokenizer resources are available
nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)

from nltk import word_tokenize, pos_tag

def analyze_grammar(sentence):
    tokens = word_tokenize(sentence)
    return pos_tag(tokens)
