BHAVA_VISUALS = {
    "Śāntiḥ":    {"emoji": "🕊️", "color": "#A0E7E5"},
    "Vīryam":    {"emoji": "⚔️", "color": "#FF7F50"},
    "Karunā":    {"emoji": "💗", "color": "#FFB6C1"},
    "Bhaktiḥ":   {"emoji": "🙏", "color": "#D1B3FF"},
    "Jñānam":    {"emoji": "📘", "color": "#89CFF0"},
    "Utsāha":    {"emoji": "🔥", "color": "#FFA500"},
    "Raudram":   {"emoji": "🌋", "color": "#DC143C"},
    "Ādaraḥ":    {"emoji": "🤝", "color": "#C0C0C0"},
    "Vismayaḥ":  {"emoji": "🌠", "color": "#E6E6FA"},
    "Hāsyaḥ":    {"emoji": "😂", "color": "#FFFF66"},
    "Śṛṅgāraḥ":  {"emoji": "💘", "color": "#FF69B4"}
}

def get_bhava_visual(bhava):
    return BHAVA_VISUALS.get(bhava, {"emoji": "❓", "color": "#CCCCCC"})