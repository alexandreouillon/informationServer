# -*- coding: utf-8 -*-
from __future__ import print_function
import lib.bitcoin as BtcLib
#import lib.tisseo as TisseoLib
import time, sys, requests, dotenv, json

class Main():
    def __init__(self):
        self.readConfig()


    def loop(self):
        while True:
            self.routine_bitcoin()
            time.sleep(0)
#            self.guid = self.tisseoRSS.get_guid(0)
#            if not self.guid == self.guid_old:
#                print("")
#            self.guid_old = self.guid

    def readConfig(self):
        dotenv.load_dotenv(".env")
        self.btcWallet, self.freeApiUser, self.freeApiPass = 
            os.environ.get('BITCOINPUBKEY', None),
            os.environ.get('FREEAPIUSER', None), 
            os.environ.get('FREEAPIPASS', None)
        self.params = json.loads(open("config/routine.json", "r"))
        

    def taskHandle(self):
        
    

    def routine_bitcoin(self):
        lastTricker = self.btcWallet.getTricker("EUR")
        self.btcWallet.update()
        #sys.stdout.write(f'\033[{91}m')
        print('\x1b[6;30;47m' + str(self.btcWallet.getWalletBalanceOtr("EUR"))[0:5]+"€"+'\x1b[0m',end=" - ")
        difference = self.btcWallet.getDifference("EUR", lastTricker)
        if difference < 0:
            print('\x1b[6;37;41m'+str(str(difference)+"000")[0:6]+"%"+'\x1b[0m',end="")
        elif difference == 0:
            print('\x1b[6;37;44m '+str(str(difference)+"000")[0:5]+"%"+'\x1b[0m',end="")
        elif difference > 0:
            print('\x1b[6;37;42m+'+str(str(difference)+"000\a")[0:5]+"%"+'\x1b[0m',end="")
            #self.send_message(str(str(self.btcWallet.getWalletBalanceOtr("EUR"))[0:5]+"€"))
        else:
            print("wtf")
        print("\t")
        
    def send_message(self, message):
        message = str(message).replace(" ", "%20")
        url = "https://smsapi.free-mobile.fr/sendmsg?user="+self.freeApiUser+"&pass="+self.freeApiPass+"&msg="+message
        
        print(requests.get(url).status_code)
   # def routine_tisseo(self):

main = Main()
main.loop()
