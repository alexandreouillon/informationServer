import requests, json

class NewsApi:
	def __init__(self, apiKey):
		self.apiKey = apiKey

	def getTopSource(self, source):
		url = "https://newsapi.org/v2/top-headlines?sources=" + source +"&apiKey=" + self.apiKey
		news = str(requests.get(url).text)
		print(news)
		newsJson = json.loads(news)
		return str(newsJson["articles"][0]["title"] +" - "+ newsJson["articles"][0]["description"]+" ("+ newsJson["articles"][0]["url"]+") " )

	#def readAllList(self, command, source)
