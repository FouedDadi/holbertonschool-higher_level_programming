$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (reponse) {
  var x;
  for (x = 0; x < reponse.results.length; x++) {
    const film = reponse.results[x];
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  }
});
