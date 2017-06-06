# Spotify-Playlists

## Requirements
Python 2.7
* Spotipy: 
```
pip install spotipy
```

* flask
* Django

## Usage
### Input:
1. *data/artists.txt*
	* `\n` separated list of artists
2. *data/input.json*
	* username, playlist_name, tracks

### Run:
In Terminal, `cd` to **src**
**python MainLogic.py**

When running first time, you will be redirected to Login into your Spotify Account. Login using your credentials and allow the application to connect to your account.
You will be redirected to a url which might be invalid. 
**Copy the entire url**
`http://localhost:5000/?code=<somehting>`
and paste in the terminal. (The program will wait for your input.)

Hit **Enter** and Voila!
