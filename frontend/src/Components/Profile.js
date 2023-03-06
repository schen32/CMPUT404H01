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
        <Box>
            <h1>Profile: </h1>
			<Box>
			<li>ID: Sam</li>
        	<li>Host: </li>
        	<li>Display Name: </li>
        	<li>Username:</li>
        	<li>URL: </li>
        	<li>GitHub: </li>
        	<li>Profile Image:</li>			
			</Box>

            <Nav/>

        </Box>

    )
}

export default Profile;