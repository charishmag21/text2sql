from flask import Flask, request, jsonify, render_template
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from datetime import datetime

app = Flask(__name__)

# Load model and tokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_path = "t5_spider_enhanced_finetuned"

model = T5ForConditionalGeneration.from_pretrained(model_path).to(device)
tokenizer = T5Tokenizer.from_pretrained(model_path)

@app.route("/")
def home():
    return render_template("index.html")

SCHEMA_PRESETS = {
    "Employee": ["id", "name", "department", "salary", "joining_year"],
    "Orders": ["order_id", "customer_id", "product_id", "order_value", "channel", "year"],
    "Stadium": ["stadium_id", "name", "average_attendance"],
    "Customers": ["customer_id", "name", "state", "status"],
    "Products": ["product_id", "product_name", "price", "stock"]
}

# 🔹 Endpoint to get schema preset options
@app.route("/get_presets")
def get_presets():
    return jsonify(SCHEMA_PRESETS)

@app.route("/generate_sql", methods=["POST"])
def generate_sql():
    data = request.get_json()
    question = data.get("question")
    headers = data.get("headers", [])

    if not question or not headers:
        return jsonify({"error": "Missing question or headers"}), 400

    input_text = f"translate English to SQL: {question} table: {', '.join(headers)}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)
    output_ids = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
    sql_query = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Post-process
    sql_query = sql_query.replace("  ", " ").strip()
    sql_query = re.sub(r"WHERE\s*;$", ";", sql_query)

    # 🔥 Log the interaction
    with open("logs.txt", "a") as f:
        f.write("\n" + "="*60 + "\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write(f"Question: {question}\n")
        f.write(f"Headers: {headers}\n")
        f.write(f"Generated SQL: {sql_query}\n")

    return jsonify({"sql": sql_query})

@app.route("/logs")
def view_logs():
    try:
        with open("logs.txt", "r") as f:
            lines = f.readlines()[-50:]  # last 50 lines (change as needed)
    except FileNotFoundError:
        lines = ["No logs yet."]
    return render_template("logs.html", logs="".join(lines))



if __name__ == "__main__":
    app.run(debug=True)
