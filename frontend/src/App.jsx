import React from "react";
import QuestionToSQL from "./components/QuestionToSQL";

export default function App() {
  return (
    <div className="outer-border">
      <div className="container">
        <h1 style={{ textAlign: "center", marginTop: "0" }}>
          NL to SQL
        </h1>
        <QuestionToSQL />
      </div>
    </div>
  );
}
