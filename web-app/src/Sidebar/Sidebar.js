import React, { Component } from "react";
import './Sidebar.css';



class Sidebar extends Component {



  constructor(props){
    super(props);
    this.state = {
      items: [],
      isLoaded: false,
    }
  }
/*
  addmovie(e){
    e.preventDefault();
    fetch("image.php", {
      method: "POST",
      body: new FormData(document.getElementById('addMov'))
    }).then((res) => {
      if (res.ok){
        alert('we got the answer!');
      } 
      else{
        console.log(res.status);
        alert("FAILURE");
        console.log(res.statusText);
        console.log(res.type);
      }
  });
}
*/

deleteAllMovies(){

  if(window.confirm("Are you sure you want to delete ALL movies ?")){

    fetch('http://localhost:5000/movies', {
      method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => { console.log(data); })
    .catch(error => { console.log(error); })

  }

    


}

  delCategory(event){
    const id = event.target.id.replace('DelC','');

    if(window.confirm("Are you sure you want to delete ALL movies ?")){
      fetch('http://localhost:5000/categories/'+id, {
        method: 'DELETE'
      })
      .then(response => response.json())
      .then(data => { console.log(data); })
      .catch(error => { console.log(error); })
    }
  }

  addmovie(event) {

    console.log("Uploading movie initiated");
    
    event.preventDefault();
    const files = event.target.file.files
    const title = event.target.title.value
    const rating = event.target.rating.value
    const category = event.target.categorie.value

    const formAdd = new FormData()
    formAdd.append('title', title)
    formAdd.append('rating', rating)
    formAdd.append('category',category)

    const post_data = (formData) => {
      console.log('WE ARE GOING TO POST THIS FORM !');
      console.log(formAdd.get('title'));
        console.log(formAdd.get('rating'));
        console.log(formAdd.get('category'));
      fetch('http://localhost:5000/movies', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {console.log('FORM UPLOADEEEEDD !'); console.log(data); })
      .catch(error => {console.log('FORM FUCKING FAILED !'); console.log(error); })
    };

    const upload_file = (formData) => {
      console.log("Uploading movie...");
	  fetch('http://localhost:5000/upload', {
	    method: 'POST',
		body: formData
	  })
	  .then(response => response.json())
	  .then(data => data.filename)
      .then(filename => {
        formAdd.append('image',filename);
        console.log("Movie uploaded, Going to Post Data from for form :");
        console.log(formAdd.get('title'));
        console.log(formAdd.get('rating'));
        console.log(formAdd.get('category'));
        post_data(formAdd);
        console.log('MOVIE UPLOADED !');
        
      })
	  .catch(error => { console.error(error) })
    };

    if (event.target.file.files.length !== 0) {
      let file = new FormData();
	  file.append('file', files[0]);
      upload_file(file);
    }
    else {
      formAdd.append('image','');
      post_data(formAdd);
    }

  }



  componentDidMount(){
    fetch('http://127.0.0.1:5000/categories')
      .then(res => res.json())
      .then(json => {
        this.setState({
          isLoaded: true,
          items: json
        })
      })
  }

  

  render() {



    var { isLoaded, items} = this.state;

    if(!isLoaded){
      return <div>Loading...</div>
    }
    else{
     
      return <div id="sidenav">

        <h4 href="#" id="sideh4">Filter <i class="fas fa-sort"></i></h4>

        {items.map((items, index) => (

        <div class="form-check catego" key={index} style={{textAlign: "center",paddingTop: "20px",paddingBottom: "20px"}}>
        <input class="form-check-input" type="checkbox" value="" id={"C"+items.id}  style={{left: "50px"}} />
        <label class="form-check-label" for={"C"+items.id} style={{color: "white",cursor: "pointer"}}>
          {items.name}
        </label>
        <i class="fas fa-times Cdelete" id={"DelC"+items.id}  onClick={this.delCategory} ></i>
        </div>

        ))}

        <hr id="sidehr" />

        <div class="btn-group dropright">

          <button type="button" id="sidebutton" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Add Movie
          </button>
          
          <div class="dropdown-menu" >

          <form class="px-4 py-3" id="addMov" onSubmit={this.addmovie}>
                <div class="form-group">
                  <label for="movTitle">Movie Title</label>
                  <input name="title" type="text" class="form-control" id="createTitle" />
                </div>

                <div class="form-group" >
                  <label for="movRating">Ratings</label>
                  <input name="rating" class="form-control" type="number" step="0.1" id="createRatings" defaultValue="5"  />
                </div>

                <div class="form-group" >
                  <label for="movCat">Categorie</label>
                  <input name="categorie" class="form-control" type="text"  id="createCategorie" defaultValue="Action"  />
                </div>


                
                  <div class="form-group">
                    <label for="exampleFormControlFile1">Cover Image</label>
                    <input name="file" type="file" class="form-control-file" id="createImage" />
                  </div>
                
                
                <button type="submit" class="btn btn-primary" >Add</button>
              </form>
            
          </div>
        </div>

        <button type="button" id="deleteallbtn" onClick={this.deleteAllMovies} class="btn btn-danger">Clear Movies</button>

        </div>


    }

    
    /*
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

    return  <React.Fragment>

        <h4 href="#" id="sideh4">Filter <i class="fas fa-sort"></i></h4>

        {items}

        <hr id="sidehr" />

        <div class="btn-group dropright">

          <button type="button" id="sidebutton" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Add Movie
          </button>
          
          <div class="dropdown-menu" >

          <form class="px-4 py-3" id="addMov">
                <div class="form-group">
                  <label for="movTitle">Movie Title</label>
                  <input type="text" class="form-control" id="createTitle"  />
                </div>
                <div class="form-group" >
                  <label for="movRating">Ratings</label>
                  <input class="form-control" type="number" step="0.1" id="createRatings" defaultValue="5"  />
                </div>
                
                  <div class="form-group">
                    <label for="exampleFormControlFile1">Cover Image</label>
                    <input type="file" class="form-control-file" id="createImage" />
                  </div>
                
                
                <button type="submit" class="btn btn-primary" onClick="addmovie()">Add</button>
              </form>
            
          </div>
        </div>
      </React.Fragment>
    */
  }
}

export default Sidebar;
