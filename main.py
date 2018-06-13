# -*- coding: utf-8 -*-
from __future__ import print_function
import lib.bitcoin as BtcLib
import lib.tisseo as TisseoLib
import lib.newsapi as NewsApi
import lib.weather as WeatherApi
import time, sys, requests, dotenv, json, os

class Main():
    def __init__(self):
        self.readConfig()
        self.btcWallet = BtcLib.Bitcoin(self.bitcoinPubKey)
        self.tisseoInfo = TisseoLib.TisseoRSS()
        self.newsApi = NewsApi.NewsApi(self.apiNewsKey)
        self.weatherApi = WeatherApi.Weather(self.apiWeatherKey)
    def loop(self):
        while True:
            self.routine_bitcoin()
            self.tisseoInfo.printLastInformation()
            self.send_message(str(self.newsApi.getTopSource("google-news-fr")))
            self.send_message("☭☭☭Mise en commun des moyens de communication camarade☭☭☭")
            self.send_message(str(self.weatherApi.getActualWeather("toulouse")))
            time.sleep(10000)
#            self.guid = self.tisseoRSS.get_guid(0)
#            if not self.guid == self.guid_old:
#                print("")
#            self.guid_old = self.guid

    def readConfig(self):
        dotenv.load_dotenv(".env")
        self.bitcoinPubKey, self.freeApiUser, self.freeApiPass = os.environ.get('BITCOINPUBKEY', None), os.environ.get('FREEAPIUSER', None),  os.environ.get('FREEAPIPASS', None)
        self.apiNewsKey, self.apiWeatherKey = os.environ.get('APINEWSKEY', None), os.environ.get('APIWEATHERKEY', None)
	#self.params = json.loads(str(open("config/routine.json", "r").readlines()).replace("\n"," "))
        

    def taskHandle(self):
        print("pute")
    

    def routine_bitcoin(self):
        self.send_message(str(self.btcWallet.printBitcoinInfos()))
        
    def send_message(self, message):
        message = str(message).replace(" ", "%20")
        url = "https://smsapi.free-mobile.fr/sendmsg?user="+self.freeApiUser+"&pass="+self.freeApiPass+"&msg="+message
        print("pute",requests.get(url).status_code)
   # def routine_tisseo(self):

main = Main()
main.loop()
