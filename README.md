# 🤖 Thoughtful AI Support Agent (Claude + Gradio)

This is a simple, conversational AI support agent built with [Anthropic Claude](https://www.anthropic.com) and [Gradio](https://www.gradio.app/). It can answer questions about Thoughtful AI using a predefined knowledge base, and fall back to Claude's reasoning for unknowns.

---

## 🚀 Features

- Uses Anthropic's brand new Claude Opus 4.1 model
- Preloaded with hardcoded FAQ responses
- Gracefully handles unknown or unexpected questions
- Runs in your browser via a Gradio UI
- Includes input validation and error handling

---

## 💻 How to Run

- Set your Anthropic API key `export ANTHROPIC_API_KEY=your-key-here`
- Install dependencies: `pip install gradio anthropic`
- Run file `python main.py`
- Visit your browser🌐: http://127.0.0.1:7860

---

## 📦 Requirements

- Python 3.8+
- [Anthropic API key](https://console.anthropic.com/)
- `gradio`, `anthropic` Python packages
