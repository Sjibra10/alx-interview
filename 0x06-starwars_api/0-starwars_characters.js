#!/usr/bin/node
""" Prints all characters of a Star Wars movie """

const axios = require('axios');

function getMovieCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    
    axios.get(url)
        .then(response => {
            const charactersUrls = response.data.characters;
            
            charactersUrls.forEach(characterUrl => {
                axios.get(characterUrl)
                    .then(characterResponse => {
                        console.log(characterResponse.data.name);
                    })
                    .catch(error => {
                        console.error(`Failed to fetch character data for URL: ${characterUrl}`);
                    });
            });
        })
        .catch(error => {
            console.error(`Failed to fetch movie data for ID: ${movieId}`);
        });
}

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
