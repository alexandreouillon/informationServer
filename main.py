from __future__ import print_function
import lib.bitcoin as BtcLib
import lib.tisseo as TisseoLib
import time, sys, requests

class Main():
    def __init__(self):
        self.btcWallet = BtcLib.Bitcoin("1AgEqqVJws4mEfK4PaMqM7pubhBUqkZ3zJ")
        self.freeApiUser, self.freeApiPass = 
        self.tisseoRSS = TisseoLib.TisseoRSS()
        self.guid_old = ""

    def read_json_conf():
        json = 

    def loop(self):
        while True:
            time.sleep(1)
            self.routine_bitcoin()
            self.guid = self.tisseoRSS.get_guid(0)
            if not self.guid == self.guid_old:

            self.guid_old = self.guid

    def routine_bitcoin(self):
        lastTricker = self.btcWallet.getTricker("EUR")
        self.btcWallet.update()
        #sys.stdout.write(f'\033[{91}m')
        print('\x1b[6;30;47m' + str(self.btcWallet.getWalletBalanceOtr("EUR"))[0:5]+"€"+'\x1b[0m',end=" - ")
        difference = self.btcWallet.getDifference("EUR", lastTricker)
        if difference < 0:
            print('\x1b[6;37;41m'+str(str(difference)+"000")[0:6]+"%"+'\x1b[0m')
        elif difference == 0:
            print('\x1b[6;37;44m '+str(str(difference)+"000")[0:5]+"%"+'\x1b[0m')
        elif difference > 0:
            print('\x1b[6;37;42m+'+str(str(difference)+"000")[0:5]+"%"+'\x1b[0m')
            #self.send_message(str(str(self.btcWallet.getWalletBalanceOtr("EUR"))[0:5]+"€"))
        else:
            print("wtf")
        
    def send_message(self, message):
        message = str(message).replace(" ", "%20")
        url = "https://smsapi.free-mobile.fr/sendmsg?user="+self.freeApiUser+"&pass="+self.freeApiPass+"&msg="+message
        
        print(requests.get(url).status_code)
   # def routine_tisseo(self):


main = Main()
main.loop()
