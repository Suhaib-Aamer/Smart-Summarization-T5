# 🧠 T5 Summarizer - Streamlit Application

A sleek and minimal web interface for generating concise and meaningful text summaries using fine-tuned [T5 models](https://huggingface.co/models) from Hugging Face. The app offers a choice between a lightweight `t5-small` model that prioritizes speed and efficiency, and a more robust `t5-base` model that provides deeper understanding and higher-quality summaries. Ideal for quick content digestion and productivity.

---

## 🌐 Live App

🚀 **Try it out now:**  
🔗 [summarization-cnndaily-t5.streamlit.app](https://summarization-cnndaily-t5.streamlit.app/)

Explore the app to instantly summarize your input text with just a few clicks. No installation needed!

---

## ✨ Key Features

- 📄 **Text Summarization:** Condense large bodies of text into shorter, easy-to-read summaries, preserving the essential meaning.
- ⚙️ **Model Selection:**  
  Choose between two fine-tuned T5 variants:
  - `T5-Small` — Designed for fast performance with lower resource consumption, suitable for quick summaries.
  - `T5-Base` — Offers improved accuracy and richer summarization quality, ideal when precision is critical.
- 🖥️ **User-Friendly Interface:**  
  Clean and modern UI with a dark mode theme, providing a comfortable reading experience for extended use.
- ⚡ **Built with Cutting-Edge Libraries:**  
  Powered by Hugging Face’s Transformers library for state-of-the-art NLP capabilities, integrated seamlessly into Streamlit for rapid deployment and interactive use.
- ☁️ **Cloud-Hosted Models:**  
  Models are fetched dynamically from the Hugging Face Hub, so no heavy downloads or local setup required.

---

## 🛠️ Tech Stack

| Tool/Library                             | Purpose                                         |
|----------------------------------------|------------------------------------------------|
| [Streamlit](https://streamlit.io/)                | Web framework for building interactive apps     |
| [Transformers](https://huggingface.co/docs/transformers)         | Pretrained NLP models & pipelines                |
| [Hugging Face Hub](https://huggingface.co/)                 | Model repository hosting and version control     |
| Python 3.10+                           | Programming language powering the application    |

---

## 📦 Installation Guide

Follow these steps to run the application locally on your machine:

### 🔧 Clone the repository:

```bash
git clone https://github.com/your-username/t5-summarizer-app.git
cd t5-summarizer-app
