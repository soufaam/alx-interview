#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const charactersUrls = film.characters;

  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        process.exit(1);
      }

      if (response.statusCode !== 200) {
        console.error('Request failed with status code:', response.statusCode);
        process.exit(1);
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
