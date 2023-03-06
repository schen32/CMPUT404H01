import React, { useState, useEffect } from 'react';
import { Box } from '@material-ui/core';
import Nav from './Nav';
import axios from 'axios';

function Profile() {

	

	const [user, setUser] = useState(null);
    React.useEffect(() => {
        // Fetch user data and set it to state
        axios.get('http://localhost:8000/api/users/')
          .then(res => setUser(res.data))
          .catch(err => console.log(err));
      }, []);
	

 
    return (
        <div>
            <h1>Profile</h1>
			<div style={{
                display: "flex",
                justifyContent: "space-around",
                margin: "18px 0px",
                borderBottom: "1px solid grey"

            }}>
                <div>
                    <img style={{width: "200px", height: "200px", borderRadius: "100px"}}
                    src="https://images.unsplash.com/photo-1564564321837-a57b7070ac4f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjh8fHBlcnNvbnxlbnwwfDB8MHx8&auto=format&fit=crop&w=500&q=60"
                    />
                    <h4>@therealjohndoe</h4>
                </div>
                <div>
                    <h3>John Doe</h3>
                    
                    <h3>test@gmail.com</h3>
                    <h3>github.com/test</h3>
                    <div style={{display: "flex", justifyContent: "space-between", width: "108%" }}>
                        <h4>3 Posts</h4>
                        <h4>4 Followers</h4>
                        <h4>6 Following</h4>
                    </div>
                </div>
            </div>
            <Nav/>
            
            <div className='gallery'>
                <h2>Put posts here: </h2>
            </div>
        
        </div>

    )
}

export default Profile;