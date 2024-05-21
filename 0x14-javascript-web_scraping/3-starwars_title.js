#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];

request(`${url}/${id}`, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(response.body).title);
  }
});
