import React from "react";
import styled from "styled-components";
import KnowledgeBaseSearch from "./KnowledgeBaseSearch";
import "bootstrap/dist/css/bootstrap.min.css";
import "bulma/css/bulma.css";


const Wrapper = styled.div`
  background-color: #e3f2fd;
  padding: 20px;
  text-align: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;


const Button = styled.button`
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  font-size: 18px;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
  
  &:hover {
    background-color: #0056b3;
  }
`;

function App() {
  return (
    <Wrapper>
      <h1>Self-Service Knowledge Base</h1>
      <p>Search for solutions to common issues below:</p>
      <KnowledgeBaseSearch />
      <Button>Learn More</Button>
    </Wrapper>
  );
}

export default App;
