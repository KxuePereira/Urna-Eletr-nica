var express = require('express');
var app = express();

// respond with "hello world" when a GET request is made to the homepage
app.get('/', function(req, res) {
  res.send('hello world');
});

// GET method route
app.get('/', function (req, res) {
    res.send('GET request to the homepage');
  });
  
  // POST method route
  app.post('/', function (req, res) {
    res.send('POST request to the homepage');
  });

  app.get('/', function (req, res) {
    res.send('root');
  });
  
  
var cb0 = function (req, res, next) {
    console.log('CB0');
    next();
  }
  
  var cb1 = function (req, res, next) {
    console.log('CB1');
    next();
  }
  
  var cb2 = function (req, res) {
    res.send('Hello from C!');
  }
  
  app.get('/example/c', [cb0, cb1, cb2]);