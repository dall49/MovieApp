import React from "react";
import logo from './Newlogo.png';


class Header extends React.Component{

 

  render() {
    
    return (
    <nav class="navbar navbar-light bg-light" style={{zIndex: "2"}}>
      <a class="navbar-brand" href="/#">
        <img src={logo} width="22" height="30" class="d-inline-block align-top" alt=""/>
        ozos
      </a>
    </nav>      
    );
  }

}

export default Header;
