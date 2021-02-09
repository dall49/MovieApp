import React, { Component } from "react";
import './Movie.css';





//<img src={image} style={{height:'100%',width:'100%',objectFit:'cover'}}></img>

//const Movies2Component = Movies.map((movie) => <Movie key={movie.id} title={movie.title} rating={movie.rating} image={movie.image} />);
//{Movies.content.body.map(block => block.title)}
//{Object.keys(Movies.content.body).length}
class Movie extends Component {

  
 
  editMovie(Mcid, category_list){

    //display of the Pop up div with movie clicked info 

    document.getElementById("wrapper").style.opacity = "1";
    document.getElementById("wrapper").style.visibility = "visible";

    document.getElementById("movImg").src = `${process.env.REACT_APP_API_URL}/img/`+Mcid.image;

    document.getElementById("movTitle").value = Mcid.title;

    document.getElementById("movRating").value = Mcid.rating;

    document.getElementById('modify').value =  Mcid.id; // You change the id of the element modify, so when you reclick it can't find it's id :/



    category_list.unshift("<option name='"+Mcid.category+"'>"+Mcid.category +"</option>"); //Make the clicked movie's category the first in the list



    category_list = category_list.filter((item, index) => category_list.indexOf(item) === index); //Filter the category list duplicates
    
    document.getElementById("movCat").innerHTML = category_list;

    // Sending the Update to the API in the index.html <script> tag when button is clicked


    




  }

  deleteMovie(Mcid){


    if (window.confirm('Are you sure you want to delete ' + Mcid.title + ' from your Movie list ?')) {
      document.getElementById(Mcid.id).style.opacity = "0";
      document.getElementById(Mcid.id).style.display = "none";

			fetch(`${process.env.REACT_APP_API_URL}/movies/`+Mcid.id, {
				method: 'DELETE'
			})
			.then(response => response.json())
			.then(data => {
        
        //UPLOAD IMAGE DONE, WE NEED TO POST SEND MOVIE INFO TO API NOW
        console.log(data); //the previous POST returns the uploaded file name
			})
			.catch(error => {
        console.error(error);
			})

      
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
    fetch(`${process.env.REACT_APP_API_URL}/movies`)
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
    console.log(process.env.REACT_APP_API_URL);
    if(!isLoaded){
      document.getElementById("staticheadcontainer").innerHTML = ""; //hide Searchbar
      return <React.Fragment>
        <div class="row justify-content-center" style={{height:"50px",color:"white",marginTop:"340px"}}>
        <h1>Seems like your Back-End server is offline</h1>
        </div>
          <div class="row justify-content-center" style={{height:"500px"}}>
          
          <img src="https://i.pinimg.com/originals/21/83/f3/2183f3dd15b25d1bfc923199e13f3ef6.png" style={{height:"500px",width:"500px",marginTop:"190px"}} />

          </div> 
      </React.Fragment>
    }
    else{

      //const category_list = {items}.items.category;
      //console.log(category_list);

      // Keep Our Categories saved in a List 
      let category_list = []
      items.forEach(item => category_list.push("<option name='"+item.category+"'>"+item.category +"</option>"));
      


      return  <React.Fragment>
        
        {items.map(items => (


          <div key={items.id} style={{backgroundImage:`url(${process.env.REACT_APP_API_URL}/img/${items.image})`}} class={items.category + " MoviePoster"} id={items.id}>
            
            <div class="Ratings">{items.rating}</div> 
            <i class="fas fa-times Mdelete" id={"D"+items.id} onClick={this.deleteMovie.bind(this, items)}></i>
              <div class="MovieContainer" id={"MC"+items.id} onClick={this.editMovie.bind(this, items,category_list)}  > 
                  <i class="fas fa-edit Medit"></i>
              </div>
          
          </div>
          

      ))} 
      
      </React.Fragment>


    }
    
  }
}

export default Movie;
