const axios = require('axios');

async function getMovieCharacters(movieId) {
    try {
        const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
        const movieData = response.data;
        const charactersUrls = movieData.characters;

        for (const characterUrl of charactersUrls) {
            const characterResponse = await axios.get(characterUrl);
            const characterData = characterResponse.data;
            console.log(characterData.name);
        }
    } catch (error) {
        console.error('Error fetching data:', error.message);
    }
}

const movieId = process.argv[2];
if (!movieId) {
    console.error('Please provide a movie ID as a command line argument.');
} else {
    getMovieCharacters(movieId);
}
