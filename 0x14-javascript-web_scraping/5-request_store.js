#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error) { console.log('error:', error); } else if (response.statusCode === 404) { console.log('doesn t exist'); } else if (response.statusCode === 200) { fs.writeFile(process.argv[3], body, 'utf8', function (error) { if (error) { console.log(error); } }); }
});
