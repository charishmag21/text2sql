
# NL-to-SQL Demo

> **Transform natural language into SQL queries with Llama 3 (via Together AI) — a modern, full-stack AI demo.**


## How it Works (AI-Powered Backend)

- **Llama 3 LLM** is used to generate SQL from plain English questions
- Calls **Together AI’s API** for best-in-class generative results
- You can optionally paste your database schema for precise, context-aware SQL
- Built on a simple, robust **Flask API**


## What’s in the Frontend?

- Lightweight **React** (Vite) web UI
- One-click SQL generation and copy button
- Mobile-friendly, clean code-box UI
- Schema input is 100% optional


## Quick Start

### 1. **Clone this repo**

```bash
git clone https://github.com/your-username/nl-to-sql-demo.git
cd nl-to-sql-demo
```

### 2. **Backend Setup (Flask + Llama 3 API)**

```bash
cd backend
python -m venv venv
source venv/bin/activate   # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

- **Set your Together AI API key** as `TOGETHER_API_KEY` in a `.env` file or as an environment variable.
- Start the Flask server:
  ```bash
  python app.py
  ```

### 3. **Frontend Setup (React)**

```bash
cd frontend
npm install
npm run dev
```

- By default, the React frontend points to `localhost:5000` for the API. Change `API_BASE` in `frontend/src/components/QuestionToSQL.jsx` if your backend is deployed elsewhere.


## Tech Stack

| Layer      | Technology         | Description                      |
|------------|--------------------|----------------------------------|
| AI Model   | **Llama 3**        | Natural language → SQL (LLM)     |
| API        | **Together AI API**| Llama 3 access (cloud)           |
| Backend    | **Flask**          | Python API, LLM orchestration    |
| Frontend   | **React (Vite)**   | Modern web UI                    |



## Deploy It Yourself

### **Frontend (Netlify)**

- Push this repo to GitHub.
- Connect your repo on [Netlify](https://netlify.com), set the build directory to `frontend` (if prompted).
- (Optionally) Set `VITE_API_BASE` in Netlify’s environment if your backend URL is different.

### **Backend (Render/Railway/etc.)**

- Deploy Flask backend to [Render](https://render.com), [Railway](https://railway.app), [Azure Web App](https://portal.azure.com), etc.
- Make sure to set your `TOGETHER_API_KEY` securely.

---

## Structure

```
nl-to-sql-demo/
  frontend/    # React app (Vite)
  backend/     # Flask + Llama 3 API calls
  README.md
```


## AI/LLM Highlights

- **LLM Prompting:** Sends your question (and optional schema) to Llama 3
- **Schema-aware:** Uses schema if given, otherwise generates SQL with smart defaults
- **No local GPU needed:** Uses Together AI API for all inference


## Credits

- **AI/Backend:** Llama 3 (via Together AI), Flask API
- **Frontend:** React + Vite
- **Project by:** Charishma Garikapati
