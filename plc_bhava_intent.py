from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Comprehensive Bhāva → Sample Intent Mapping
SAMPLE_INTENTS = {
    "Śāntiḥ": [
        "I seek peace and rest",
        "Calmness is my goal",
        "Let the world be tranquil"
    ],
    "Vīryam": [
        "I will fight with courage",
        "Strength arises within me",
        "Let us act with power and resolve"
    ],
    "Karunā": [
        "I feel deep compassion for others",
        "May all beings be happy and free",
        "This suffering touches my heart"
    ],
    "Bhaktiḥ": [
        "I surrender to the divine",
        "All I do is for my beloved deity",
        "Let my devotion guide me"
    ],
    "Jñānam": [
        "I seek the truth in all things",
        "Knowledge is the path to liberation",
        "Let wisdom light the way"
    ],
    "Utsāha": [
        "I feel energized and motivated",
        "Let's take this challenge with enthusiasm",
        "There's so much to do and I'm ready"
    ],
    "Raudram": [
        "This injustice must be destroyed",
        "Let fury cleanse the wrongs",
        "I burn with righteous anger"
    ],
    "Ādaraḥ": [
        "I value your opinion deeply",
        "Let’s listen with respect",
        "Honor each person equally"
    ],
    "Vismayaḥ": [
        "This fills me with wonder",
        "Amazed by the divine creation",
        "What a miraculous thing!"
    ],
    "Hāsyaḥ": [
        "Let's laugh and be joyful",
        "This is truly hilarious",
        "Laughter is healing"
    ],
    "Śṛṅgāraḥ": [
        "I feel so much love for you",
        "Let beauty and romance bloom",
        "This love is divine"
    ]
}

def get_training_data():
    X = []
    y = []
    for intent, phrases in SAMPLE_INTENTS.items():
        for phrase in phrases:
            X.append(phrase)
            y.append(intent)
    return X, y

def train_intent_model():
    X, y = get_training_data()
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    model = pipeline.fit(X, y)
    return model

def predict_intent(model, sentence):
    return model.predict([sentence])[0]