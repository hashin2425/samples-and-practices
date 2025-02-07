// run: node server.js

const myModules = require("./modules.js");

const http = require("http");

// Create a server
const server = http.createServer((req, res) => {
  const url = req.url;

  if (url === "/") {
    res.writeHead(200, { "Content-Type": "text/html" });
    res.write("<h1>Home Page</h1>");
    res.write(`<p>${myModules.twoTimes(4)}</p>`);
    res.end();
  } else if (url === "/about") {
    res.writeHead(200, { "Content-Type": "text/html" });
    res.write("<h1>About Page</h1>");
    res.end();
  } else {
    res.writeHead(404, { "Content-Type": "text/html" });
    res.write("<h1>Page Not Found</h1>");
    res.end(); // 一般的な関数におけるreturnと同じ
  }
});

// Listen on port 3000
server.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
