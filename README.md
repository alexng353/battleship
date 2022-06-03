# BATTLESHIP

[<img src="https://img.shields.io/badge/GitHub-alexng353-lightgrey">](https://github.com/alexng353/battleship)

## WARNING
## Code is incomplete because it's due on Jun 7th
If you're reading this after Jun 7th its because I forgot to update the readme and the game should (probably) work
#

A command line battleship client written in python and a backend written in python Sanic

Server **must** run on python 3.8.10 because Sanic dependencies are very strange

Client can run on >= python 3.8.x

## Usage
```bash
python main.py
```
After running the game, follow in game instructions and invite a friend

## Running a Battleship server
If you don't want to run your own server, I have one running on http://battleship.ayo.icu

I do not recommend using this because the server it's hosted on is incredibly slow and if you're not on the West Coast of North America the latency will be unbearable. 
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
pip install sanic
```

#### Server deps
Run the server on **linux/ubuntu** because I literally have not tested it on anything else
```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```
Everything else is either using a builtin or will throw an error because I forgor to tell you to install it

<br><br>

The server is made with sanic, so there is probably an exploit in the code that hasn't been found yet. Host at your own risk, I'm just a student learning to code. 

