#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const getCharacter = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

const getCharacters = async () => {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  try {
    const filmResponse = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });

    const film = JSON.parse(filmResponse);
    const characters = film.characters;

    for (const characterUrl of characters) {
      const characterName = await getCharacter(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
};

getCharacters();
