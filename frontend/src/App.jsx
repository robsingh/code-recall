import { useState, useEffect } from "react";
import './App.css'

function App() {
  const[dueProblems, setDueProblems] = useState([]);
  
  async function loadDueProblems() {
    const res = await fetch("http://127.0.0.1:5000/problems/due")
    const data = await res.json()
    setDueProblems(data.due)
  }

  async function handleReview(title) {
    await fetch(`http://127.0.0.1:5000/problems/${title}/review`, {
      method: "PUT",
    });
    loadDueProblems(); //refresh the list
  }
  
  useEffect(() => {
    loadDueProblems();
  }, []);

  return (
  <div className="app">
    <header className="app-header">
      <h1>Code Recall</h1>
      <p className="subtitle">Spaced repetition for coding problems</p>
    </header>

    <main className="dashboard">
      {dueProblems.length === 0 ? (
        <p className="empty-state">No problems due today. 🎉</p>
      ) : (
        dueProblems.map((problem) => (
          <div className="problem-card" key={problem.title}>
            <div className="card-header">
              <h3>{problem.title}</h3>
              <span className="stage-badge">Stage {problem.current_stage}</span>
            </div>
            <p className="review-date">Next review: {problem.next_review_date}</p>
            <pre>{problem.solution}</pre>
            <button className="review-btn" onClick={() => handleReview(problem.title)}>
              Mark Reviewed
            </button>
          </div>
        ))
      )}
    </main>
  </div>
);
}

export default App;
