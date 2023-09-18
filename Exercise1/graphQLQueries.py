import requests
graphEndpoint = "http://localhost:4000/graphql"
rhcpQuery = """
{
  artist(where: { name: "Red Hot Chili Peppers" }) {
    name
    albums {
      title
    }
  }
}
"""

u2Query = """
{
  artist(where: {name: "U2"}) {
    name,
    albums{
      albumId,
     tracks{
      genre{
        name
      }
    } 
    }
  }
}"""

grungeQuery = """
query{
  playlists(where:{name:"Grunge"}){
    playlistId,
    tracks{
      name,
      album{
        title,
        artist{
          name
        }
      }
    }
  }
}"""

# Create a dictionary with the query and variables if needed
rhcpData = {
    "query": rhcpQuery
}

u2Data = {
    "query": u2Query
}

grungeData = {
    "query": grungeQuery
}
# Make a Get request to the GraphQL endpoint

def graphQlReq(endpoint, data):
    response = requests.get(endpoint, json=data)

    if response.status_code==200:
        return response.json()
    else:
        errStr = "Error: {Errcode}, {ErrorText}.".format(Errcode = response.status_code, ErrorText=response.text)
        return errStr

rhcpRes = graphQlReq(graphEndpoint,rhcpData)
print("Albums Associated to Red Hot Chili Peppers \n")
for albums in rhcpRes['data']['artist']['albums']:
    print(albums['title'])

u2Res = graphQlReq(graphEndpoint,u2Data)
trackslist = u2Res['data']['artist']['albums']
generes = []
for tracks in trackslist:
    for genere in tracks['tracks']:
        generes.append(genere['genre']['name'])
print("\n####################################################\n")
print("Generes Associated with U2.")
print(set(generes))

print("\n####################################################\n")

print("\n Tracks, Album and Artist associated to playlist Grunge\n")
grungeRes = graphQlReq(graphEndpoint,grungeData)
songsInfoLst = []
tracksInfoList = grungeRes['data']['playlists'][0]['tracks']
for songInfo in tracksInfoList:
    songsInfoLst.append({"Name":songInfo['name'], "Album":songInfo['album']['title'], "Artist":songInfo['album']['artist']['name']})

for info in songsInfoLst:
    print(info)
    print()
