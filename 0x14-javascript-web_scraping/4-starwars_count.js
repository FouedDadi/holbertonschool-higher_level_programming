#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) { console.log('error:', error); } else if (response.statusCode === '404') { console.log('doesn t exist'); } else {
    const movies = JSON.parse(body).results;
    let count = 0;
    let chars = '';
    for (const film in movies) {
      chars = movies[film].characters;
      for (const char in chars) {
        if (chars[char].endsWith('18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
