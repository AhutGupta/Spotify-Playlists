import json
import sys
import spotipy
import spotipy.util as util
import spotipy.client as client

#AUTH
credsfile = "../credentials/creds.json"
artistfile = "../data/artists.txt"
inputfile = "../data/input.json"
with open(credsfile) as data_file:
    creds = json.load(data_file)
with open(inputfile) as f:
    input_ = json.load(f)
with open(artistfile) as f:
    artists = [line.rstrip('\n') for line in f]
user = input_["username"]
c_id = creds["ClientID"]
c_secret = creds["ClientSecret"]
redirect = creds["redirect"]
playlist_name = input_["playlist_name"]
tracks = input_["tracks"]
scope = input_["scope"]

token = util.prompt_for_user_token(user, scope, c_id, c_secret, redirect)

def get_tracks():
    print ""


if token:
    sp = spotipy.Spotify(auth=token)
    #print "User Information:"
    user = sp.current_user()
    u_id = user["id"]
    #print json.dumps(user, indent=4, sort_keys=True)

    #Artist Search
    list_of_artists = []
    print artists
    for a in artists:
        q = '+'.join(a.split())
        res = sp.search(a, type='artist')
        #print json.dumps(res["artists"]["items"][0], indent=4, sort_keys=True)
        artist = res["artists"]["items"][0]
        if artist:
            list_of_artists.append(artist["uri"])

    #Get tracks for artist
    list_of_tracks = []
    print "Getting tracks for: "+str(len(list_of_artists))+" artists..."
    for a in list_of_artists:
        res = sp.artist_top_tracks(a, country='US')
        #print json.dumps(tracks["tracks"], indent=4, sort_keys=True)
        tracks = [t["id"] for t in res["tracks"]]
        list_of_tracks.extend(tracks)

    #Create Playlist and add tracks
    new_playlist = sp.user_playlist_create(u_id, playlist_name, public=True)
    sp.user_playlist_add_tracks(u_id, new_playlist["id"], list_of_tracks)
    print "Playlist Created: "+playlist_name
    print "Artists: "+str(artists)
else:
    print "Can't get token for "+ user