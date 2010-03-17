var sys = require('sys'), 
    http = require('http');
    qs = require("querystring");

http.createServer(function (req, res) {
    currentTime = new Date();
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.write('Hello World');
    res.close();
}).listen(8123);
sys.puts('Server running at http://127.0.0.1:8123/');
