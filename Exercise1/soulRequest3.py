#Names of tracks on the playlist “Grunge” and their associated artists and albums.
import requests

soulEndPoint = "http://localhost:8000/api/tables/"
playlists = "playlists"


firstParams = {"_filters":"Name:Grunge"}



def getResponse(endPoint, tableName, params):
    rows = "/rows"

    response = requests.get(endPoint+tableName+rows, params=params)
    return response.json()

#Used Filter Name:Grunge on table playlists to get the PlaylistId
firstResponse = getResponse(soulEndPoint,playlists,firstParams)
playListId = firstResponse['data'][0]['PlaylistId']


#tracks on Playlist Grunge
playlistTrack = "playlist_track"
playlistIdStr = "PlaylistId:{plylstId}".format(plylstId=playListId)
secondParams = {'_extend':'TrackId','_filters':playlistIdStr}
secondResponse = getResponse(soulEndPoint,playlistTrack,secondParams)

tracksList = []
albumIdData = []
for track in secondResponse['data']:
    tracksList.append(track['TrackId_data']['Name'])
    albumIdData.append(track['TrackId_data']['AlbumId'])

print('Tracks on PlayList Grunge Are')
for track in tracksList:
    print(track)



albums = 'albums'
albumsIdsStr = "AlbumId:{albmsId}".format(albmsId=list(set(albumIdData)))
thirdparams = {'_extend':'ArtistId','_filters':albumsIdsStr}
thirdResponse = getResponse(soulEndPoint,albums,thirdparams)

print("###################################################################")
details = {}
print()
print("Associated albums and artist in playlist grunge")

for data in thirdResponse['data']:
    details[data['Title']] = data['ArtistId_data']['Name']


for album, artist in details.items():
    print("Album Name: "+ album + "     "+ "Artist: "+ artist)

