# BATTLESHIP

[<img src="https://img.shields.io/badge/GitHub-alexng353-lightgrey">](https://github.com/alexng353/battleship)

A command line battleship client written in python and a backend written in python Sanic

Server **must** run on python 3.8.10 because Sanic dependencies are very strange

Client can run on >= python 3.8.x

## Running a Battleship server
### Config
If you want to run your own server, create a config.json and set the "url" paramter to the url and port you're running the server on.
```json
{
  "url":"http://example.com:port/"
}
```

### Install all dependencies
#### Python Deps
```bash
sanic
```

#### Server deps
```bash
redis
```
Everything else is either using a builtin or will throw an error because I forgor to tell you to install it

<br><br><br>

The server is made with sanic, so there is probably an exploit in the code that hasn't been found yet. Host at your own risk, I'm just a student learning to code. 

