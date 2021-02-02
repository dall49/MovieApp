import React, { Component } from "react";
import './Sidebar.css';

class Sidebar extends Component {
  render() {


    const Categories = [
          
      {
        Name: "Action",
        id:"0"
      },
      {
        Name: "Drama",
        id:"1"
      },
      {
        Name: "Thriller",
        id:"2"
      },
      {
        Name: "Adventure",
        id:"3"
      },
      {
        Name: "Romantic",
        id:"4"
      },        
  
    ];

    

    const items=[]


    for (let number of Object.keys(Categories)){
      let Name = Categories[number].Name;
      let id =  Categories[number].id;
      let Cid = "C"+id;
    


        items.push(
          <div class="form-check catego" style={{textAlign: "center",paddingTop: "20px",paddingBottom: "20px"}}>
            <input class="form-check-input" type="checkbox" value="" id={Cid} style={{left: "50px"}} />
            <label class="form-check-label" for={Cid} style={{color: "white",cursor: "pointer"}}>
              {Name}
            </label>
          </div>)

    }

    return  <div>

        <h4 href="#" id="sideh4">Filter <i class="fas fa-sort"></i></h4>

        {items}

        <hr id="sidehr" />

        <div class="btn-group dropright">

          <button type="button" id="sidebutton" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Add Movie
          </button>
          
          <div class="dropdown-menu" >

            <form class="px-4 py-3">

              <div class="form-group">
                <label for="exampleDropdownFormEmail1">Title</label>
                <input type="email" class="form-control" id="exampleDropdownFormEmail1" placeholder="email@example.com" />
              </div>

              <div class="form-group">
                <label for="example-number-input" class="col-2 col-form-label">Rating<i class="fas fa-star" id="sidelabel"></i></label>
                <div class="col-10">
                  <input class="form-control" type="number" value="5" id="example-number-input" />
                </div>
              </div>

              <div class="form-group">
                <label for="exampleDropdownFormPassword1">image</label>
                <input type="password" class="form-control" id="exampleDropdownFormPassword1" placeholder="Password" />
              </div>

              <button type="submit" class="btn btn-primary btn-lg btn-block">Add</button>
              
            </form>
            
          </div>
        </div>
      </div>

  }
}

export default Sidebar;
