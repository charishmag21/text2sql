# 🧠 Natural Language to SQL Generator

This project is a Flask-based web app that converts plain English questions into SQL queries using a fine-tuned T5 model trained on the Spider dataset.

> ⚙️ Built for showcasing AI + Web App skills in interviews and real-world use cases.

---

## 🚀 Features

- 🔁 Converts natural language → SQL queries
- 🎛 Schema presets (Employee, Orders, etc.)
- 📋 Copy SQL button
- 🌓 Dark mode toggle
- 🗂 View logs directly in the browser
- 🧠 Powered by a fine-tuned T5 model from Hugging Face

---

## 🗂 Folder Structure

sql-text2sql-app/
    |- app.py
    |- requirements.txt
    |- README.md
    |- .gitignore
    |- templates/
        |- index.html
        |- logs.html
    
---

## 🧑‍💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SQL-Text2SQL-App.git
cd SQL-Text2SQL-App

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the App
python app.py

### Then open your browser and go to:
http://localhost:5000

### Model Fine-Tuning
This app uses a custom fine-tuned T5 model trained on the Spider dataset using Hugging Face Transformers.

🔧 Fine-Tuning Summary:
-> Base model: t5-small
-> Dataset: Spider (Yale LILY Lab)
-> Tokenizer: T5Tokenizer
-> Training Method: Hugging Face Trainer API
-> Epochs: (mention if needed, e.g., 3)
-> Output folder: t5_spider_enhanced_finetuned/ (not included in the repo)

--> You can re-train the model using the script or adapt it for your own schema-aware text-to-SQL datasets.


Note
-> This app is local-first. Model weights are stored locally and excluded from GitHub via .gitignore.
-> If deploying publicly, it's recommended to add authentication, rate limiting, or an API key to secure your endpoint.

🧠 Credits
-> Model: Fine-tuned T5 on Spider Dataset
-> Backend: Python + Flask
-> Frontend: HTML + JavaScript (Vanilla)
-> NLP: Hugging Face Transformers