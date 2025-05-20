import streamlit as st
from plc_phonetics import extract_phonemes
from plc_grammar import analyze_grammar
from plc_clustering import visualize_clusters
from plc_utils import load_sample_sentences
from plc_bhava_intent import train_intent_model, predict_intent
from bhava_visuals import get_bhava_visual

st.set_page_config(page_title="PLC Bhāva Tool", layout="wide")

st.title("🔤 PLC Streamlit Tool")
st.markdown("**Phonetic + Language + Clustering + Bhāva Prediction Tool**")

# Load model
@st.cache_resource
def get_intent_model():
    return train_intent_model()

model = get_intent_model()

# User input
st.subheader("✍️ Enter your own sentence:")
user_input = st.text_input("Write something meaningful...", placeholder="e.g. I feel so much love for all beings")

if user_input:
    phonemes = extract_phonemes(user_input)
    grammar_tags = analyze_grammar(user_input)
    bhava = predict_intent(model, user_input)
    visual = get_bhava_visual(bhava)

    st.subheader("🧬 Phoneme Extraction")
    st.write(phonemes)

    st.subheader("🧠 Grammar Analysis")
    st.write(grammar_tags)

    st.subheader("🌸 Predicted Bhāva (Intent)")
    st.markdown(
        f"<div style='background-color:{visual['color']}; padding:1rem; border-radius:10px; text-align:center'>"
        f"<h2>{visual['emoji']} {bhava}</h2>"
        "</div>",
        unsafe_allow_html=True
    )

    st.subheader("📊 Cluster Visualization")
    visualize_clusters([user_input])
else:
    st.info("Type a sentence above to begin Bhāva analysis.")