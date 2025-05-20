import streamlit as st
from plc_bhava_intent import train_intent_model, predict_intent
from bhava_visuals import get_bhava_visual

st.set_page_config(page_title="Bhāva Prediction Tool by Mahān", layout="wide")

st.title("🧘‍♂️ Bhāva Prediction Tool by Mahān")
st.markdown("**Enter a sentence to see its underlying emotional Bhāva.**")

@st.cache_resource
def get_intent_model():
    return train_intent_model()

model = get_intent_model()

st.subheader("✍️ Enter your sentence:")
user_input = st.text_input("e.g. I feel deep compassion for everyone")

if user_input:
    bhava = predict_intent(model, user_input)
    visual = get_bhava_visual(bhava)

    st.markdown(
        f"<div style='background-color:{visual['color']}; padding:2rem; border-radius:10px; text-align:center'>"
        f"<h1>{visual['emoji']} {bhava}</h1>"
        "</div>",
        unsafe_allow_html=True
    )
else:
    st.info("Awaiting your input to predict Bhāva.")
