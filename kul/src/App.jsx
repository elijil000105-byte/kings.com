import { useState, useEffect } from "react";
import "./App.css";

export default function App() {
  const [text, setText] = useState("");
  const message = "Välkommen till min fräcka hemsida 😎";

  useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      setText(message.slice(0, i));
      i++;
      if (i > message.length) clearInterval(interval);
    }, 80);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="container">
      <h1 className="typewriter">{text}</h1>

      <button className="boop-btn">
        Tryck på mig 🍺
      </button>
    </div>
  );
}
