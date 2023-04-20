import React, {useEffect, useState} from 'react';
import './App.css';
import { Movies } from "./components/Movies";
import { MovieForm } from "./components/MovieForm";
import { Container } from "semantic-ui-react";
//import {writeJsonFile} from 'write-json-file';
function App() {
	const [movies, setMovies] = useState([]);

	useEffect(()=> {
			fetch('https://alphatrick-averagepandora-5000.codio-box.uk/movies', { credentials: 'include' }).then(response =>response.json().then(data => {setMovies(data.movies);
			})
		);
	},[]);

	return (
		<div className="App">
		<Container>
			<MovieForm onNewMovie ={
				movie => setMovies(currentMovies => [...currentMovies, movie])
			}/>

			<Movies movies={movies}/>
		</Container>
		</div>

	);
}

export default App;


