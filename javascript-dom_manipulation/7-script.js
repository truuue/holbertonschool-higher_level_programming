const moviesId = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    const movies = data.results;
    movies.forEach((movie) => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      moviesId.appendChild(li);
    });
  });
