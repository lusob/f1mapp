var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var timer = null;
var fs = require('fs')
var read_data = function(){
  fs.readFile('cars_data.json', 'utf8', function(err, data) {
    if (err) throw err;
    console.log('Read cars data OK');
    io.emit('cars_data', data);
  });
}
io.on('connection', function(socket){ 
    if (timer!=null) clearInterval(timer);
    timer = setInterval(read_data, 1000); 
});

app.get('/', function(req, res){
  res.send('<h1>Hello world</h1>');
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});
