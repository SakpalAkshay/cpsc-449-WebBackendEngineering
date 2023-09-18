#Albums by the artist “Red Hot Chili Peppers.”
import requests

soulEndPoint = "http://localhost:8000/api/tables/"
artists = "artists"


firstParams = {"_filters":"name:Red Hot Chili Peppers"}



def getResponse(endPoint, tableName, params):
    rows = "/rows"

    response = requests.get(endPoint+tableName+rows, params=params)
    return response.json()

#to fetch the artist Id related with Red Hot Chili Peppers
firstResponse = getResponse(soulEndPoint,artists,firstParams)


#Variables for Second request
artistId = firstResponse['data'][0]['ArtistId']
albums = "albums"
artistIdStr = "ArtistId:{artId}".format(artId=artistId)
secondParams = {"_filters":artistIdStr}


#to filter out Albums based on ArtistId i.e 127
secondResponse = getResponse(soulEndPoint,albums,secondParams)
for albms in secondResponse['data']:
    print(albms['Title'])


