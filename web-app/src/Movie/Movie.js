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

    if (window.confirm('Are you sure you want to delete' + Mcid.title + 'from your Movie list ?')) {
      document.getElementById("MC"+Mcid.id).remove();
      console.log('Thing was saved to the database.');
    } else {
      // Do nothing!
      console.log('Thing was not saved to the database.');
    }
  }

  render() {

    const Movies = {
      content: {
        body: [
          {
            
            title: "Casablanca",
            rating: "8.5",
            image: "Casablanca.jpg",
            id: "0"
          },
          {
            
            title: "King Kong",
            rating: "7.2",
            image: "King_Kong.jpg",
            id: "1"
          },
          {
            
            title: "Marriage Story",
            rating: "7.9",
            image: "Marriage_Story.jpg",
            id: "2"
          },
          {
            
            title: "Interstellar",
            rating: "8.6",
            image: "Interstellar.jpg",
            id: "3"
          },
          {
            
            title: "Avengers Endgame",
            rating: "8.4",
            image: "Avengers.jpg",
            id: "4"
          },
          {
            
            title: "Get Out",
            rating: "7.7",
            image: "Get_Out.jpg",
            id: "5"
          }
          ,
          {
            
            title: "Titanic",
            rating: "7.8",
            image: "Titanic.jpg",
            id: "6"
          }
          ,
          {
            
            title: "Indiana Jones",
            rating: "8.4",
            image: "Indiana_Jones.jpg",
            id: "7"
          }
          ,
          {
            
            title: "Godzilla",
            rating: "6.4",
            image: "Godzilla.jpg",
            id: "8"
          },
          {
            
            title: "Jurassic Park",
            rating: "8.1",
            image: "Jurassic_Park.jpg",
            id: "9"
          }
         
          
          
          
        ]
      }
    };


    const items=[]


    for (let number of Object.keys(Movies.content.body)){
      let current_object = Movies.content.body[number];
      let title = current_object.title;
      let rating = current_object.rating;
      let image = "img/" + current_object.image;
      let id = current_object.id;
      let MCid = "MC"+id;
      let Did = "D"+id;
    


        items.push(
        <div style={{backgroundImage:"url("+image+")"}} class="Movies" id={id}>

          
          <div class="Ratings">{rating}</div> 
          <i class="fas fa-times Mdelete" id={Did} onClick={this.deleteMovie.bind(this, Movies.content.body[number])}></i>
          
          <div class="MovieContainer" id={MCid} onClick={this.editMovie.bind(this, Movies.content.body[number])}  > 
              <i class="fas fa-edit Medit"></i>
          </div>
        </div>)

      
      

    }

    return <React.Fragment>{items}</React.Fragment>


    
  }
}

export default Movie;
