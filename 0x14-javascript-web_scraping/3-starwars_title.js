#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) { console.log('error:', error); } else if (response.statusCode === '404') { console.log('doesn t exist'); } else { console.log(JSON.parse(body).title); }
});
