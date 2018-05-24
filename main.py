from __future__ import print_function
import lib.bitcoin as BtcLib
import time, sys

class Main():
    def __init__(self):
        self.btcWallet = BtcLib.Bitcoin("1AgEqqVJws4mEfK4PaMqM7pubhBUqkZ3zJ")
    def loop(self):
        while True:
            time.sleep(1)
            self.routine_bitcoin()
            
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
        else:
            print("wtf")


main = Main()
main.loop()
