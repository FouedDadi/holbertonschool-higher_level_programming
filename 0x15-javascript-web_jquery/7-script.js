$.get('https://swapi-api.hbtn.io/api/people/4/?format=json', function (reponse) {
  $('DIV#character').text(reponse.name);
});
