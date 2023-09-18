#Genres associated with the artist “U2.”
import requests

soulEndPoint = "http://localhost:8000/api/tables/"
artists = "artists"


firstParams = {"_search":"U2"}



def getResponse(endPoint, tableName, params):
    rows = "/rows"

    response = requests.get(endPoint+tableName+rows, params=params)
    return response.json()

#to fetch the artist Id related with U2
firstResponse = getResponse(soulEndPoint,artists,firstParams)



#Variables for Second request
artistId = firstResponse['data'][0]['ArtistId']

albums = "albums"
artistIdStr = "ArtistId:{artId}".format(artId=artistId)
secondParams = {"_schema":"AlbumId","_filters":artistIdStr}


#to filter out AlbumsId based on ArtistId of U2 i.e 150
secondResponse = getResponse(soulEndPoint,albums,secondParams)
albumsIdList = []

for albmsId in secondResponse['data']:
    albumsIdList.append(albmsId['AlbumId'])    
tracks = "tracks"
albumIdStr = "AlbumId:{albmId}".format(albmId= albumsIdList)
thirdParams = {'_limit':'200','_schema':'GenreId','_extend':'GenreId','_filters':albumIdStr}

thirdResponse = getResponse(soulEndPoint,tracks,thirdParams)

genreList = []

for genreData in thirdResponse['data']:
    genreList.append(genreData['GenreId_data']['Name'])


#Genere's Associated with U2
print(set(genreList))
