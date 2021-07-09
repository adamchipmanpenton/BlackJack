db = "money.txt"
import sys

def openWallet():
    try:
        wallet = open(db)
        wallet = round(float(wallet.readline()),)
        return wallet
    except FileNotFoundError:
        print("count not find money.txt")
        print("Exiting program. Bye!")
        sys.exit()


def changeAmount(winnings):

    with open(db, "w") as file:
        for item in winnings:
            file.write(item)
