
import random
import csv
import db as wallet
import sys

FILENAME = "BlackJackDeckOfCards.csv"


def readFullDeck():
    fullDeck = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                fullDeck.append(row)
            return fullDeck
    except FileNotFoundError:
        print("count not find BlackJackDeckOfCards.csv")
        print("Exiting program. Bye!")
        sys.exit()

def playersTurn(playersHand, fullDeck):
    while True:
            print()
            command = input("Hit/stand: ").lower()
            if command == "hit":
                print()
                print("Your cards:")
                playerGetsCard(playersHand, fullDeck)
                showPlayersCards(playersHand)
                if (getPlayersHandValue(playersHand)  > 21):
                    break
            elif command == "stand":
                break
            else:
                print("Not a valid command. Please try again.\n")


def getCards(fullDeck, playersHand):
    NewestCard = []
    playersHandValue = getPlayersHandValue(playersHand) 
    cardNumber = random.randint(0, (len(fullDeck)-1))
    newSuit = fullDeck[cardNumber][0]
    cardValue = int(fullDeck[cardNumber][1])
    if (cardValue == 999):
        if playersHandValue >= 11:
            cardValue = 1
        elif playersHandValue < 11:
            cardValue = 11
    NewestCard.append(newSuit)
    NewestCard.append(cardValue)
    playersHand.append(NewestCard)  
   
def dealersTurn(playersHand, dealersHand, fullDeck):
    while True:
            if (getPlayersHandValue(playersHand)  > 21):
                break
            elif (getdealersHandValue(dealersHand) <= 17):
                dealerGetsCard(fullDeck, dealersHand)
            else:
                break

def playerGetsCard(playersHand, fullDeck):
    playersHandValue = getPlayersHandValue(playersHand) 
    NewestCard = []
    cardNumber = random.randint(0, (len(fullDeck)-1))
    newSuit = fullDeck[cardNumber][0]
    cardValue = int(fullDeck[cardNumber][1])
    if (cardValue == 999):
        if playersHandValue >= 11:
            cardValue = 1
        elif playersHandValue < 11:
            cardValue = 11
    NewestCard.append(newSuit)
    NewestCard.append(cardValue)
    playersHand.append(NewestCard)
    fullDeck.pop(cardNumber)

def showPlayersCards(playersHand):
    i = 0 
    for i in range(len(playersHand)):
        print(playersHand[i][0])
        i = i +1

def dealerGetsCard(fullDeck, dealersHand):
    NewestCard = []
    cardNumber = random.randint(0, (len(fullDeck)-1))
    newSuit = fullDeck[cardNumber][0]
    cardValue = int(fullDeck[cardNumber][1])
    if (cardValue == 999):
        if (getdealersHandValue(dealersHand) >= 11):
            cardValue = 1
        elif (getdealersHandValue(dealersHand) < 11):
            cardValue = 11
    NewestCard.append(newSuit)
    NewestCard.append(cardValue)
    dealersHand.append(NewestCard)
    fullDeck.pop(cardNumber)
    
def winMoney(moneyInWallett, betAmount):
    winnings = moneyInWallett + (betAmount * 1.5)
    return round(winnings, 2)

def loseMoney(moneyInWallett, betAmount):
    winnings = moneyInWallett - betAmount
    return round(winnings, 2)

def getPlayersHandValue(playersHand):
    playersHandValue = 0
    i = 0
    for i in range(len(playersHand)):
        amount = playersHand[i][1]
        playersHandValue = playersHandValue + amount
        i += 1
    return playersHandValue

def getdealersHandValue(dealersHand):
    dealersHandValue = 0
    i = 0
    for i in range(len(dealersHand)):
        amount = dealersHand[i][1]
        dealersHandValue = dealersHandValue + amount
        i += 1
    return dealersHandValue

def showDealersHand(dealersHand):
    i = 0 
    for i in range(len(dealersHand)):
        print(dealersHand[i][0])
        i += 1

def placeBet(moneyInWallett):
    while True:
        try:
            bet = float(input("Bet amount: "))
            if bet < 5 or bet > 1000:
                print("Place a bet between 5 and 1000")
            elif bet > moneyInWallett:
                print("Bet should be less then the money in your wallet")
            else:
                return bet
        except ValueError:
            print("Error, please enter a number.")
            continue

def winningConditions(playerTotal, dealerTotal, moneyInWallett, betAmount):
    if ( playerTotal > 21 and dealerTotal <= 21):
            print("You bust, you loose")
            winnings = loseMoney(moneyInWallett, betAmount)
    elif(dealerTotal > playerTotal and dealerTotal <= 21):
        print("You loose")
        winnings = loseMoney(moneyInWallett, betAmount)
    elif(dealerTotal < playerTotal and playerTotal < 22):
        print("you win")
        winnings = winMoney(moneyInWallett, betAmount)
    elif(playerTotal < 22 and dealerTotal > 21):
        print("you win")
        winnings = winMoney(moneyInWallett, betAmount)
    elif(dealerTotal == playerTotal):
        print("Tie")
        winnings = moneyInWallett
    print("Money: ", winnings)
    wallet.changeAmount(str(winnings))
    print()

def amountInWallet():
    moneyInWallett = wallet.openWallet()
    print("Money: ", moneyInWallett)
    if moneyInWallett <= 5:
        optionMoreMoney = input("Would you like more money? (y/n): ")
        if optionMoreMoney == "y":
            while True:
                try:
                    MoreMoney = float(input("How much more money?: ")) 
                    moneyInWallett += MoreMoney
                    return moneyInWallett
                except ValueError:
                    print("Error, please enter a number.")
                    continue    
        elif optionMoreMoney == "n":
            print("Good bye")
            sys.exit()
    else:
        return moneyInWallett
      
def display_title():
    print("Blackjack!")
    print("Blackjack payout is 3:2")
    print()
    
def main():
    display_title()
    fullDeck = readFullDeck()

    again = "y"
    while again == "y":
        if len(fullDeck) < 5:
            fullDeck = readFullDeck() 
        playersHand = []
        dealersHand = []
        moneyInWallett = amountInWallet()
        betAmount = placeBet(moneyInWallett)
        print()
        print("Dealer's show card: ")
        dealerGetsCard(fullDeck, dealersHand)
        showDealersHand(dealersHand)
        print()
        print("Your cards:")
        playerGetsCard(playersHand, fullDeck)
        playerGetsCard(playersHand, fullDeck)
        showPlayersCards(playersHand)

        playersTurn(playersHand, fullDeck)
        
        print()
        print("Dealer's cards:")
        dealersTurn(playersHand, dealersHand, fullDeck)
        showDealersHand(dealersHand)

        playerTotal = getPlayersHandValue(playersHand) 
        dealerTotal = getdealersHandValue(dealersHand)
        print()
        print("Your points:\t", playerTotal)
        print("Dealer's points: ", dealerTotal)
        print()
        winningConditions(playerTotal, dealerTotal, moneyInWallett, betAmount)
        while True:
            again = input("Play again? (y/n): ").lower()
            print()
            if again == "y" or again == "n":
                break
            else:
                print("Invalid input. Please try again.")
    print()
    print("Bye!")

if __name__ == "__main__":
    main()
