# -*- coding: utf-8 -*-
import json, requests, time

PUBKEY = "1AgEqqVJws4mEfK4PaMqM7pubhBUqkZ3zJ"
class Bitcoin():
    def __init__(self):
        self.update()
    
    def getTricker(self,devise):
        return json.loads(self.trickerJson)[devise]['sell']
    
    def getWalletBalanceBtc(self):
        return int(json.loads(self.balanceJson)[PUBKEY]["final_balance"]) / 100000000
    
    def getWalletBalanceOtr(self, devise):
        return self.getTricker(devise) * self.getWalletBalanceBtc()

    def getDifference(self, devise, lastTricker):
        return (self.getTricker(devise) - lastTricker) * 100 / lastTricker

    def update(self):
        self.trickerJson = requests.get("https://blockchain.info/fr/ticker").text
        self.balanceJson = requests.get("https://blockchain.info/fr/balance?active="+PUBKEY).text
bitcoin = Bitcoin()
while True:
    lastTricker = bitcoin.getTricker("EUR")
    bitcoin.update()
    print(str(bitcoin.getWalletBalanceOtr("EUR"))[0:5],"€",end=" - ")
    print(str(bitcoin.getDifference("EUR", lastTricker))[0:5],"%")
    time.sleep(10)
