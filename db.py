db = "money.txt"


def openWallet():
    wallet = open(db)
    wallet = float(wallet.readline())
    return wallet


def changeAmount(winnings):

    with open(db, "w") as file:
        for item in winnings:
            file.write(item)




        