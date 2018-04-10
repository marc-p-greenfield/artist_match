import spotipy
import sys
import spotipy.oauth2 as auth


#Used for authorization to access Spotify data
credentials = auth.SpotifyClientCredentials(
    client_id='820c2da1dd414d2aa6297a30155c8629',
    client_secret='781e6e261f3e468d8395f7b93239792b'
)
token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

def recommend_artists():
    #Takes in the user's two favorite bands
    band1_input, band2_input, band3_input = input("Please enter three artists, separated by a comma and space: ").split(", ")

    #Loads spotify search info based on input, and takes the first band result as the band1 info.
    band1_spotify_search_info = sp.search(q='artist:' + band1_input, type='artist')
    band1_list_info = band1_spotify_search_info['artists']['items']
    band1 = band1_list_info[0]

    #Using the band1 info, loads the top 10 related artists info into band1_related_artists
    band1_related_artists_search_info = sp.artist_related_artists(band1['uri'])
    band1_related_artists = band1_related_artists_search_info['artists']


    band2_spotify_search_info = sp.search(q='artist:' + band2_input, type='artist')
    band2_list_info = band2_spotify_search_info['artists']['items']
    band2 = band2_list_info[0]

    band2_related_artists_search_info = sp.artist_related_artists(band2['uri'])
    band2_related_artists = band2_related_artists_search_info['artists']


    band3_spotify_search_info = sp.search(q='artist:' + band3_input, type='artist')
    band3_list_info = band3_spotify_search_info['artists']['items']
    band3 = band3_list_info[0]

    band3_related_artists_search_info = sp.artist_related_artists(band3['uri'])
    band3_related_artists = band3_related_artists_search_info['artists']
    print ("")


    #Tests to see if there are any matches - if it finds one, it breaks the loop
    bool_test = False
    for a in band2_related_artists:
        for b in band1_related_artists:
            for c in band3_related_artists:
                if (a['name'] == b['name'] == c['name']):
                    bool_test = True
                    break

    #Goes through band2_related_artists and band1_related_artists and prints the matches, if any
    count = 0
    if (bool_test == True):
        print ("Here are similar bands to", band1_input, ",", band2_input, "and", band3_input, ":")
        for a in band2_related_artists:
            for b in band1_related_artists:
                for c in band3_related_artists:
                    if (a['name'] == b['name'] == c['name']):
                        count = count + 1
                        print (count, a['name'])
    else:
        print ("Unfortunately, there were no similar artists between", band1_input + ",", band2_input, "and", band3_input)

def main_menu():
    choice = input("If you want to find a new artist to listen to, press 1! ")
    if choice == '1':
        recommend_artists()
    else:
        quit

main_menu()