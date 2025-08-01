from flask import Blueprint, request, jsonify
from .llama_client import get_sql_from_nl

bp = Blueprint("api", __name__)

# @bp.route("/nl-to-sql", methods=["POST"])
# def nl_to_sql():
#     data = request.json
#     question = data.get("question")
#     schema = data.get("schema")  # Optional
#     if not question:
#         return jsonify({"error": "Missing question"}), 400
#     try:
#         sql = get_sql_from_nl(question, schema)
#         return jsonify({"sql": sql})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
    
@bp.route("/nl-to-sql", methods=["POST"])
def nl_to_sql():
    data = request.json
    questions = data.get("questions", None)
    schema = data.get("schema")  # Optional

    # Handle batch questions
    if isinstance(questions, list) and len(questions) > 0:
        results = []
        for q in questions:
            try:
                sql = get_sql_from_nl(q, schema)
                results.append({"question": q, "sql": sql})
            except Exception as e:
                results.append({"question": q, "error": str(e)})
        return jsonify(results)

    # Handle single question
    question = data.get("question", None)
    if isinstance(question, str) and question.strip():
        try:
            sql = get_sql_from_nl(question, schema)
            return jsonify({"sql": sql})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # If neither is present or valid
    return jsonify({"error": "Missing question(s)"}), 400
