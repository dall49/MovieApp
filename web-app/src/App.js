import logo from './logo.svg';
import './App.css';
import Movie from './Movie'
import Sidebar from './Sidebar'
import React from "react";


function App() {
  return (
    <React.Fragment>
      <Sidebar></Sidebar>
      <Movie></Movie>
   </React.Fragment>
     
   
  );
}

export default App;
