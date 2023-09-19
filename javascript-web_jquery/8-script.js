$.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (movies) {
      $.each(movies.results, function (index, result) {
        $('#list_movies').append('<li>' + result.title + '</li>');
      });
    }
  });
