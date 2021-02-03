import React, { Component } from "react";
import './Movie.css';





//<img src={image} style={{height:'100%',width:'100%',objectFit:'cover'}}></img>

//const Movies2Component = Movies.map((movie) => <Movie key={movie.id} title={movie.title} rating={movie.rating} image={movie.image} />);
//{Movies.content.body.map(block => block.title)}
//{Object.keys(Movies.content.body).length}
class Movie extends Component {

  
 
  editMovie(Mcid){
    console.log(Mcid.title);
    document.getElementById("wrapper").style.opacity = "1";
    document.getElementById("wrapper").style.visibility = "visible";

    document.getElementById("movImg").src = "img/"+Mcid.image;

    document.getElementById("movTitle").value = Mcid.title;

    document.getElementById("movRating").value = Mcid.rating;

  }

  deleteMovie(Mcid){
    console.log(Mcid.title);

    if (window.confirm('Are you sure you want to delete ' + Mcid.title + ' from your Movie list ?')) {
      document.getElementById(Mcid.id).style.opacity = "0";
      document.getElementById(Mcid.id).style.display = "none";
      
      //Send request to API to remove Movie from DB containing ID = MCid
      console.log(document.getElementById("MC"+Mcid.id));
    } else {
      // Do nothing!
      console.log('Thing was not saved to the database.');
    }
  }

  constructor(props){
    super(props);
    this.state = {
      items: [],
      isLoaded: false,
    }
  }



  componentDidMount(){
    fetch('http://127.0.0.1:5000/movies')
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
      return <React.Fragment>
        <div class="row justify-content-center" style={{height:"50px",color:"white",marginTop:"260px"}}>
        <h1>Seems like your Back-End server is offline</h1>
        </div>
          <div class="row justify-content-center" style={{height:"500px"}}>
          
          <img src="https://i.pinimg.com/originals/21/83/f3/2183f3dd15b25d1bfc923199e13f3ef6.png" style={{height:"500px",width:"500px",marginTop:"100px"}} />

          </div> 
      </React.Fragment>
    }
    else{
     
      return  <React.Fragment>
        
        {items.map(items => (

          <div style={{backgroundImage:"url(img/"+items.image+")"}} class={items.category} id={items.id}>
            
            <div class="Ratings">{items.rating}</div> 
            <i class="fas fa-times Mdelete" id={"D"+items.id} onClick={this.deleteMovie.bind(this, items)}></i>
              <div class="MovieContainer" id={"MC"+items.id} onClick={this.editMovie.bind(this, items)}  > 
                  <i class="fas fa-edit Medit"></i>
              </div>
          
          </div>

      ))} 
      
      </React.Fragment>


    }
    
  }
}

export default Movie;
