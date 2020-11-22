import React, { Component } from "react";
import "./Search.css";

class Search extends Component {
  state = {
    searchValue: "",
    results: []
  };

  handleOnChange = event => {
    this.setState({ searchValue: event.target.value });
  };

  handleSearch = () => {
    this.makeApiCall(this.state.searchValue);
  };

  makeApiCall = searchInput => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({"algorithm":"use","text":this.state.searchValue});

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/semantic_similarity/api/v1.0/similarity", requestOptions)
      .then(response =>
       response.json()
      )
      .then(jsonData => {
        console.log("R "+jsonData.result.score+typeof(jsonData))
        this.setState({ results: jsonData.result });
      })
        .catch(error => console.log('error', error));
  }

  render() {
    return (
      <div id="main">
        <h1>Mutilingual Covid Document Search</h1>
        <input
          name="text"
          type="text"
          placeholder="Search"
          onChange={event => this.handleOnChange(event)}
          value={this.state.searchValue}
        />
        <button onClick={this.handleSearch}>Search</button>
        {this.state.results ? (
          <div id="results-container">
            {this.state.results.map((result, index) => (
              <div class="single-result shadow" key={index}>
                <div id="textbox">
                  <p class="alignleft">Title : {result.original_doc}</p>
                   <p class="alignright">Score : {result.score}</p>
                </div>
                <div class="clear_floar"></div>
                <p class="matched_text">{result.matched_text}</p>
              </div>
            ))}
          </div>
        ) : (
          <p>Try searching for another query</p>
        )}
      </div>
    );
  }
}

export default Search;
