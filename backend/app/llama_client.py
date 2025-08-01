import os
import re
import requests

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TOGETHER_LLM_MODEL = os.getenv("TOGETHER_LLM_MODEL", "meta-llama/Llama-3-70b-chat-hf")
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

def extract_sql_from_llm_response(response_content):
    """
    Extracts the first SQL code block or statement from the LLM output.
    Handles code fences (```), explanations, etc.
    """
    # Try to extract from code block (``` ... ```)
    match = re.search(r"```(?:sql)?\s*([\s\S]+?)\s*```", response_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Fallback: Try to find the first SQL-ish statement
    match = re.search(r"(SELECT|INSERT|UPDATE|DELETE)[\s\S]+?;", response_content, re.IGNORECASE)
    if match:
        return match.group(0).strip()

    # Otherwise, return the original
    return response_content.strip()

def get_sql_from_nl(nl_query, schema_info=None):
    # prompt = (
    # "You are a helpful assistant that converts natural language questions into SQL queries."
    # "\nIf a schema is provided, use ONLY those tables and columns."
    # "\nIf NO schema is provided, MAKE REASONABLE ASSUMPTIONS about table and column names and still generate the SQL."
    # "\nReturn ONLY the SQL query, nothing else."
    # )   
    prompt = (
    "You are a helpful assistant that converts natural language questions into SQL queries."
    "\nIf a schema is provided, use ONLY those tables and columns."
    "\nIf NO schema is provided, make reasonable assumptions about table and column names and still generate the SQL."
    "\nReturn ONLY the SQL query, nothing else."
    "\n"
    "\n**SQL Best Practice:**"
    "\nWhen filtering for records without matches in another table (such as 'customers with no orders'), "
    "use 'NOT EXISTS' or 'LEFT JOIN ... IS NULL' instead of 'NOT IN (SELECT ...)', because 'NOT IN' can return incorrect results if the subquery contains NULLs."
    )
    if schema_info and schema_info.strip():
        prompt += f"\nSchema:\n{schema_info.strip()}\n"
    prompt += f"\nQuestion: {nl_query}\nSQL:"

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": TOGETHER_LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 256,
        "temperature": 0
    }
    print("Together API key loaded:", TOGETHER_API_KEY)
    try:
        resp = requests.post(TOGETHER_API_URL, headers=headers, json=payload)
        print("Status code:", resp.status_code)
        print("Response text:", resp.text)
        resp.raise_for_status()
        llm_output = resp.json()["choices"][0]["message"]["content"].strip()
        sql = extract_sql_from_llm_response(llm_output)
        return sql
    except Exception as e:
        print("Exception in get_sql_from_nl:", e)
        print("Response text (in except):", resp.text)
        raise
