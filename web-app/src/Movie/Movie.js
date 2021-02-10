import React, { Component } from "react";
import './Movie.css';


//<img src={image} style={{height:'100%',width:'100%',objectFit:'cover'}}></img>

//const Movies2Component = Movies.map((movie) => <Movie key={movie.id} title={movie.title} rating={movie.rating} image={movie.image} />);
//{Movies.content.body.map(block => block.title)}
//{Object.keys(Movies.content.body).length}
class Movie extends Component {

  
  
 
  editMovie(Mcid, category_list,index){

    //display of the Pop up div with movie clicked info 

    document.getElementById("wrapper").style.opacity = "1";
    document.getElementById("wrapper").style.visibility = "visible";


    document.getElementById("movImg").src = "http://localhost:5000/img/"+Mcid.image;

    document.getElementById("movTitle").value = Mcid.title;

    document.getElementById("movRating").value = Mcid.rating;

    document.getElementById('modify').value =  Mcid.id; // You change the id of the element modify, so when you reclick it can't find it's id :/



    category_list.unshift("<option name='"+Mcid.category+"'>"+Mcid.category +"</option>"); //Make the clicked movie's category the first in the list



    category_list = category_list.filter((item, index) => category_list.indexOf(item) === index); //Filter the category list duplicates
    
    document.getElementById("movCat").innerHTML = category_list;

    // Sending the Update to the API in the index.html <script> tag when button is clicked

    //let updated_items = this.state.items;
    //var updatedComment = update(updated_items[index], {text: {$set: text}}); 

    /*
    if (index !== -1){
      updated_list.splice(index,1); //Remove item from status array that has position items[index]
      this.setState({items:updated_list}) //Update component array state with new array
    }

    */


  }

  deleteMovie(Mcid,index){


    if (window.confirm('Are you sure you want to delete ' + Mcid.title + ' from your Movie list ?')) {
      
      
			fetch('http://localhost:5000/movies/'+Mcid.id, {
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
    
      let updated_list = this.state.items; // Make Copy of Status array of items

      if (index !== -1){
        updated_list.splice(index,1); //Remove item from status array that has position items[index]
        this.setState({items:updated_list}) //Update component array state with new array
      }
      

    } else {
      // Do nothing!
      console.log('Thing was not saved to the database.');
    }

    

  }

updateSB(event){



    this.setState({
      searchTerm: event.target.value
    })

  }


		

  constructor(props){
    super(props);
    this.state = {
      items: [],
      isLoaded: false,
      searchTerm: ''
    }
    this.updateSB = this.updateSB.bind(this);
  }




  async componentDidMount(){
    await fetch('http://127.0.0.1:5000/movies')
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
        <div class="row justify-content-center" style={{height:"50px",color:"white",marginTop:"340px"}}>
        <h1>Seems like your Back-End server is offline</h1>
        </div>
          <div class="row justify-content-center" style={{height:"500px"}}>
          
          <img alt="Backend Server Offline" src="https://i.pinimg.com/originals/21/83/f3/2183f3dd15b25d1bfc923199e13f3ef6.png" style={{height:"500px",width:"500px",marginTop:"190px"}} />

          </div> 
      </React.Fragment>
    }
    else{

      //const [searchTerm, setSearchTerm] = useState('');
      //const category_list = {items}.items.category;
      //console.log(category_list);

      // Keep Our Categories saved in a List 
      let category_list = []
      items.forEach(item => category_list.push("<option name='"+item.category+"'>"+item.category +"</option>"));
      
      

      return  <React.Fragment>


        


          <div id="staticheadcontainer">
            <div class="row justify-content-center">
              <div style="height: 100px;display: inline;margin-top: 10px;" class="col-md-5">
                <h1 style="margin-top: 20px;text-align: center;color: white;">New Releases</h1>
              </div>
            </div>
        
            <div class="row justify-content-center" >
              <div style="height: 20px;display: inline;" class="col-md-5">
                <form class="form-inline my-2 my-lg-0 justify-content-center" >
                  <div id="Shere">
                      <input id="special"
                        type="text" 
                        placeholder={this.state.searchTerm} 
                        onChange={this.updateSB} 
                    />
                    <button class="btn btn-primary my-2 my-sm-0" type="submit">Search</button>
                  </div>
                  
                  
                </form>
              </div>
            </div>
          </div>

        <div style="width: 100%;height: 720px;">
          <div class="row justify-content-center" style="height: 370px;margin-top: 30px;" id="Row">
          {items.filter((item)=>{



          if ( this.state.searchTerm == ''){ // We want to verify with our search tearm is equal to what we want
            return item
          }
          else if (item.title.toLowerCase().includes(this.state.searchTerm.toLowerCase())){
            return item
          }
          }).map((items, index) => (


          <div key={index} style={{backgroundImage:"url(http://localhost:5000/img/"+items.image+")"}} class={items.category + " MoviePoster"} id={items.id}>
            
            <div class="Ratings">{items.rating}</div> 
            <i class="fas fa-times Mdelete" id={"D"+items.id} onClick={this.deleteMovie.bind(this, items,index)}></i>
              <div class="MovieContainer" id={"MC"+items.id} onClick={this.editMovie.bind(this, items,category_list,index)}  > 
                  <i class="fas fa-edit Medit"></i>
              </div>

          </div>


          ))} 
          
          </div>

       
          <div class="row justify-content-center" style="height: 300px;margin-top: 50px;">
            <div style="width: 350px;height: 100%;background-color: black;">

            </div>
            <div style="width: 350px;height: 100%;background-color: black;margin-left: 100px;">

            </div>
            <div style="width: 350px;height: 100%;background-color: black;margin-left: 100px;">

            </div>
          </div>

     
          
          
        </div>




        
        
      
      </React.Fragment>


    }
    
  }
}

export default Movie;
