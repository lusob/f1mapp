var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var fs = require('fs')
fs.readFile('cars_data.json', 'utf8', function(err, data) {
  if (err) throw err;
  // console.log('Read cars data OK');
});

io.on('connection', function(socket){
  socket.broadcast.emit('cars_data', data);
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
