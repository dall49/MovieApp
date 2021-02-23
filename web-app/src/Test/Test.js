import {useState} from 'react' 
import React from "react";
import Movies from "../Movie"


function Test(){
    const [searchTerm, setSearchTerm] = useState('');
    

    return (
        <React.Fragment>
        <input 
            type="text" 
            placeholder={searchTerm} 
            onChange={event =>{
                setSearchTerm(event.target.value)
            }} 
        />
        <Movies onChange={() => alert("change")}/>
        </React.Fragment>
    )
        
    
    
}

export default Test;