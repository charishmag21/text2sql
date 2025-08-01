import os
import psycopg2
import psycopg2.extras

def get_connection():
    return psycopg2.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT", 5432),
        dbname=os.getenv("PG_DATABASE"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        sslmode='require'
    )

def execute_sql(sql):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        cursor.execute(sql)
        if cursor.description:  # SELECT query
            result = cursor.fetchall()
        else:
            conn.commit()
            result = {"affected_rows": cursor.rowcount}
    finally:
        cursor.close()
        conn.close()
    return result
