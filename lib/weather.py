import requests, json

class Weather:
	def __init__(self, apiKey):
		self.apiKey = apiKey
		self.emojisCorres = {"Rain":"☔", "llCouds":"☁️"}
	def getActualWeather(self, city):
		url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + self.apiKey
		weatherPage = requests.get(url).text
		print(weatherPage)
		weatherJson = json.loads(weatherPage)
		temp = str(weatherJson["main"]["temp"] - 273.15)
		sky = weatherJson["weather"][0]["main"]
		text = "La temperature à " + city + " est de " + temp + "degres, le ciel est " + sky + self.emojisCorres[sky]
		return text
