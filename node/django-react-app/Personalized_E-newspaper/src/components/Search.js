import React, { useState } from 'react';
import axios from 'axios';
import "./Search.css"
function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.get('http://localhost:8000/tasks/', {
        params: { q: query },
      });
      setResults(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div class="search">
      <div class="searchbar">
      <input type="text" placeholder="Search"value={query} onChange={(e) => setQuery(e.target.value)} class="txt" /><br></br>
      < button onClick={handleSearch} class="btn">Search</button>
      </div>
      <ul>
        {results.map((result) => (
          <li key={result.text} class="output">
            <h3>{result.text}</h3>
            <p>Score: {result.score}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Search;
