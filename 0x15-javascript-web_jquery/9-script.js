$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (reponse) {
    $('DIV#hello').text(reponse.hello);
  });
});
