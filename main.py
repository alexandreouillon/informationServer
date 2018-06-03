# -*- coding: utf-8 -*-
from __future__ import print_function
import lib.bitcoin as BtcLib
import lib.tisseo as TisseoLib
import time, sys, requests, dotenv, json, os

class Main():
    def __init__(self):
        self.readConfig()
        self.btcWallet = BtcLib.Bitcoin(self.bitcoinPubKey)
        self.tisseoInfo = TisseoLib.TisseoRSS()
    def loop(self):
        while True:
            self.routine_bitcoin()
            self.tisseoInfo.printLastInformation()
            time.sleep(0)
#            self.guid = self.tisseoRSS.get_guid(0)
#            if not self.guid == self.guid_old:
#                print("")
#            self.guid_old = self.guid

    def readConfig(self):
        dotenv.load_dotenv(".env")
        self.bitcoinPubKey, self.freeApiUser, self.freeApiPass = os.environ.get('BITCOINPUBKEY', None), os.environ.get('FREEAPIUSER', None),  os.environ.get('FREEAPIPASS', None)
        self.params = json.loads(str(open("config/routine.json", "r").readlines()).replace("\n"," "))
        

    def taskHandle(self):
        print("pute")
    

    def routine_bitcoin(self):
        print(str(self.btcWallet.printBitcoinInfos()))
        
    def send_message(self, message):
        message = str(message).replace(" ", "%20")
        url = "https://smsapi.free-mobile.fr/sendmsg?user="+self.freeApiUser+"&pass="+self.freeApiPass+"&msg="+message
        
        print(requests.get(url).status_code)
   # def routine_tisseo(self):

main = Main()
main.loop()
