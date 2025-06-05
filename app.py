import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Smart Text Summarizer", layout="centered")
st.markdown(
    """
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stButton>button {
            color: white;
            font-weight: bold;
            border-radius: 0.5rem;
            padding: 0.6rem 1.2rem;
        }
        .stTextArea textarea {
            border-radius: 0.5rem;
            padding: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered title and subtitle
st.markdown(
    """
    <h1 style='text-align: center; font-weight: 700; margin-bottom: 0.5rem;'>
        Smart Text Summarizer 🧠
    </h1>
    <p style='text-align: center; color: #555; font-size: 18px; margin-top: 0;'>
        Generate concise and clear summaries with fine-tuned T5 models
    </p>
    """,
    unsafe_allow_html=True
)

# Model selection keys (simple)
model_options = {
    "T5-Small": "NeonSamurai/summarization_t5_small_v2",
    "T5-Base": "NeonSamurai/summarization_cnndaily_t5_base"
}

model_choice_key = st.selectbox("Choose a model:", list(model_options.keys()))
model_name = model_options[model_choice_key]

@st.cache_resource
def load_pipeline(model_name):
    return pipeline(
        "text2text-generation",
        model=model_name,
        tokenizer=model_name,
        max_length=256,   # fixed max length
        min_length=60,
        truncation=True,
        do_sample=False
    )

summarizer = load_pipeline(model_name)

st.subheader("📄 Enter the text to summarize:")
input_text = st.text_area("", height=300, placeholder="Paste or type your text here...")

if st.button("✨ Generate Summary"):
    if not input_text.strip():
        st.warning("Please enter some text before summarizing.")
    else:
        with st.spinner("Summarizing..."):
            result = summarizer("summarize: " + input_text)
            summary = result[0]["generated_text"]

        st.subheader("🧾 Summary Result")
        st.success(summary.strip())

# Background-Image
st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://cdn-uploads.huggingface.co/production/uploads/673f5e166c2774fcc8a82f0b/tjZJvZGkJMLKhorQFfHML.png");
            background-size: cover;
            background-position: center;
            height: 100vh;
        }
        
        /* Semi-transparent overlay */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.4);  /* 40% transparency */
            z-index: -1;
        }
    </style>
    """, 
    unsafe_allow_html=True
)