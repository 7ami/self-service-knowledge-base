import React, { useState } from "react";
import axios from "axios";
import styled from "styled-components";

// Styled component for UI styling
const Container = styled.div`
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  background-color: white;
`;

const SearchInput = styled.input`
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
`;

const Button = styled.button`
  margin-top: 10px;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
`;

const Results = styled.div`
  margin-top: 20px;
  text-align: left;
`;

function KnowledgeBaseSearch() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [error, setError] = useState("");

  // Function to send the query to the Flask API
  const searchQuery = async () => {
    setError(""); // Reset error before searching
    setResponse(""); // Reset response

    try {
      const res = await axios.post(
        "http://127.0.0.1:5000/query",
        { query },
        { headers: { "Content-Type": "application/json" } } // Ensure headers are set correctly
      );

      console.log("API Response:", res.data);

      if (res.status === 200 && res.data.response) {
        setResponse(res.data.response);
      } else {
        setResponse("No relevant answer found.");
      }
    } catch (err) {
      console.error("API Error:", err);
      setError("Failed to fetch results. Please try again.");
    }
  };

  return (
    <Container>
      <h2>Search Knowledge Base</h2>
      <SearchInput
        type="text"
        placeholder="Enter your question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <Button onClick={searchQuery}>Search</Button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <Results>
        {response && (
          <div>
            <h3>Answer:</h3>
            <p style={{ color: "green", fontWeight: "bold" }}>✅ {response}</p>
          </div>
        )}
      </Results>
    </Container>
  );
}

export default KnowledgeBaseSearch;
