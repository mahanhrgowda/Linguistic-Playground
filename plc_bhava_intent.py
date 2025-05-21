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
    "Ānandaḥ": [
        "Joy arises from within",
        "Let bliss guide every action",
        "I am one with divine joy"
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
    "Vīryam": [
        "I will fight with courage",
        "Strength arises within me",
        "Let us act with power and resolve"
    ],
    "Utsāhaḥ": [
        "I feel energized and motivated",
        "Let's take this challenge with enthusiasm",
        "There's so much to do and I'm ready"
    ],
    "Karunā": [
        "I feel deep compassion for others",
        "May all beings be happy and free",
        "This suffering touches my heart"
    ],
    "Raudram": [
        "This injustice must be destroyed",
        "Let fury cleanse the wrongs",
        "I burn with righteous anger"
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
    "Śokaḥ": [
        "My heart is heavy with grief",
        "Tears cleanse the soul",
        "Let me mourn and heal"
    ],
    "Bhayaṁ": [
        "I feel fear but I face it",
        "This unknown frightens me",
        "Even fear has a message"
    ],
    "Jugupsā": [
        "I must reject what is impure",
        "This disgust calls for cleansing",
        "Let me purify my surroundings"
    ],
    "Ratiḥ": [
        "I feel so much love for you",
        "Let beauty and romance bloom",
        "This love is divine"
    ],
    "Ādaraḥ": [
        "I value your opinion deeply",
        "Let’s listen with respect",
        "Honor each person equally"
    ],
    "Lajjā": [
        "I feel shy and modest",
        "Let humility protect me",
        "I bow in sacred shame"
    ],
    "Smṛtiḥ": [
        "I remember the ancient wisdom",
        "The past speaks through memory",
        "Let remembrance guide my steps"
    ],
    "Dhṛtiḥ": [
        "I hold firm in adversity",
        "Endurance is my inner strength",
        "Let steadfastness light my path"
    ],
    "Śraddhā": [
        "I trust the process",
        "My faith is unwavering",
        "Let deep conviction sustain me"
    ],
    "Āśā": [
        "Hope lifts my spirit",
        "A better future is possible",
        "Let this hope carry me forward"
    ],
    "Mamatā": [
        "I feel affectionate closeness",
        "This is my own, my heart says",
        "Let care and bonding grow"
    ],
    "Tṛṣṇā": [
        "I yearn for more",
        "Desire pulls me forward",
        "Let me transform craving into clarity"
    ],
    "Mohaḥ": [
        "I'm lost in illusion",
        "Attachment clouds my sight",
        "Let clarity dispel delusion"
    ],
    "Harṣaḥ": [
        "Joy bubbles within me",
        "Let us celebrate success",
        "This happiness is contagious"
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
