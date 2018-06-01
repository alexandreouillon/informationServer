# -*- coding: utf-8 -*-
import json, requests, time

class Bitcoin():
    def __init__(self, pubKey): 
        self.pubKey = pubKey
        self.update()
    def getTricker(self,devise):
        return json.loads(self.trickerJson)[devise]['sell']
    
    def getWalletBalanceBtc(self):
        return int(json.loads(self.balanceJson)[self.pubKey]["final_balance"]) / 100000000
    
    def getWalletBalanceOtr(self, devise):
        return self.getTricker(devise) * self.getWalletBalanceBtc()

    def getDifference(self, devise, lastTricker):
        return (self.getTricker(devise) - lastTricker) * 100 / lastTricker

    def update(self):
        self.trickerJson = requests.get("https://blockchain.info/fr/ticker").text
        self.balanceJson = requests.get("https://blockchain.info/fr/balance?active=" + self.pubKey).text
    
    def verify_seuil(self, seuilHigh, seuilLow):
        if self.getWalletBalanceOtr('EUR') < seuilLow or self.getWalletBalanceOtr('EUR') > seuilHigh:
            return True
        else:
            return False
    def composeMessage(self):
        return
    def printBitcoinInfos(self):
        self.lastTricker = self.getTricker("EUR")
        self.update()

        text = str('\x1b[6;30;47m' + str(self.getWalletBalanceOtr("EUR"))[0:5]+"€"+'\x1b[0m - ')
        difference = self.getDifference("EUR", self.lastTricker)
        if difference < 0:
            text = text + str('\x1b[6;37;41m'+str(str(difference)+"000")[0:6]+"%"+'\x1b[0m')
        elif difference == 0:
            text = text + str('\x1b[6;37;44m '+str(str(difference)+"000")[0:5]+"%"+'\x1b[0m')
        elif difference > 0:
            text = text + str('\x1b[6;37;42m+'+str(str(difference)+"000\a")[0:5]+"%"+'\x1b[0m')
            #self.send_message(str(str(self.getWalletBalanceOtr("EUR"))[0:5]+"€"))
        print(text)


