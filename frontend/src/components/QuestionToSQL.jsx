import React, { useState } from "react";
import axios from "axios";
import { FiCopy } from "react-icons/fi"; // Import a copy icon

// const API_BASE = "http://localhost:5000/api";
const API_BASE = "https://text2sql-xf5w.onrender.com/api";

export default function QuestionToSQL() {
  const [question, setQuestion] = useState("");
  const [schema, setSchema] = useState("");
  const [sql, setSql] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false); // Track copy state

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSql("");
    setError("");
    setLoading(true);

    try {
      const payload = { question };
      if (schema.trim()) payload.schema = schema;
      const res = await axios.post(`${API_BASE}/nl-to-sql`, payload);
      setSql(res.data.sql || res.data.error || "No SQL generated.");
    } catch (err) {
      setError(
        err?.response?.data?.error ||
        err.message ||
        "An error occurred."
      );
    } finally {
      setLoading(false);
    }
  };

  // Copy SQL to clipboard
  const handleCopy = () => {
    if (sql) {
      navigator.clipboard.writeText(sql);
      setCopied(true);
      setTimeout(() => setCopied(false), 1200);
    }
  };

  return (
    <>
      <h2>Ask a question</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          rows={3}
          placeholder="Type your question in English..."
          value={question}
          onChange={e => setQuestion(e.target.value)}
          required
        />
        <textarea
          rows={2}
          placeholder="(Optional) Paste your table schema here for better results..."
          value={schema}
          onChange={e => setSchema(e.target.value)}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate SQL"}
        </button>
      </form>

      {/* Output Section */}
      {sql && (
        <div className="sql-output" style={{ position: "relative" }}>
          <button
            className="copy-btn"
            onClick={handleCopy}
            title="Copy SQL"
            style={{
              position: "absolute",
              top: 16,
              right: 16,
              background: "transparent",
              border: "none",
              color: "#fff",
              cursor: "pointer",
              fontSize: "1.25em",
              padding: 0
            }}
            aria-label="Copy SQL to clipboard"
          >
            <FiCopy />
          </button>
          <pre style={{
            margin: 0,
            background: "none",
            color: "inherit",
            fontFamily: "inherit",
            whiteSpace: "pre-wrap",
            wordBreak: "break-word",
            overflowX: "hidden"
          }}>
            {sql}
          </pre>
          {/* Optional: "Copied!" feedback */}
          {copied && (
            <span
              style={{
                position: "absolute",
                top: 14,
                right: 48,
                color: "#3fb37f",
                background: "#fff",
                fontSize: "0.98em",
                borderRadius: 4,
                padding: "2px 9px",
                border: "1px solid #3fb37f"
              }}
            >
              Copied!
            </span>
          )}
        </div>
      )}

      {error && (
        <div className="error-message">
          <strong>Error:</strong> {error}
        </div>
      )}
    </>
  );
}
