def analyze_grammar(sentence):
    # Simple whitespace tokenizer fallback
    return [{"word": word} for word in sentence.strip().split()]
