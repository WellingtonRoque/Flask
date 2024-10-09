import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&api_key=f7a2e2bbcd3d5aa26450826691511060"

resposta = urllib.request.urlopen(url)
dados = resposta.read()

jsondata = json.loads(dados)

#print(resposta)
#print(dados)
print(jsondata['results'])
