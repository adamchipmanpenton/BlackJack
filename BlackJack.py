
from os import read
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

def firstTwoCards(playersHand, fullDeck):
    print("Your card's:")
    playersHandValue = getPlayersHandValue(playersHand) 
    for _ in range(2):
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
    i = 0 
    for i in range(len(playersHand)):
        print(playersHand[i][0])
        i = i +1
    playersHandValue = getPlayersHandValue(playersHand) 
    print("Your points: ", playersHandValue)

    

def add(playersHand, fullDeck):
    print("Your card's:")
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
    
    i = 0 
    for i in range(len(playersHand)):
        print(playersHand[i][0])
        i = i +1
    playersHandValue = getPlayersHandValue(playersHand) 
    print("Your points: ", playersHandValue)
    fullDeck.pop(cardNumber)


def dealerGetsCard(fullDeck, dealersHand):
    NewestCard = []
    cardNumber = random.randint(0, len(fullDeck))
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
    return winnings

def getPlayersHandValue(playersHand):
    playersHandValue = 0
    i = 0
    for i in range(len(playersHand)):
        amount = playersHand[i][1]
        playersHandValue = playersHandValue + amount
        i = i + 1
    return playersHandValue

def getdealersHandValue(dealersHand):
    dealersHandValue = 0
    i = 0
    for i in range(len(dealersHand)):
        amount = dealersHand[i][1]
        dealersHandValue = dealersHandValue + amount
        i = i + 1
    return dealersHandValue

def placeBet(moneyInWallett):
    while True:
        try:
            while True:
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
    while again.lower() == "y":
    
        playersHand = []
        dealersHand = []
        moneyInWallett = amountInWallet()
        betAmount = placeBet(moneyInWallett)
        print()
        print("Dealer's show card: ")
        dealerGetsCard(fullDeck, dealersHand)
        print()
        firstTwoCards(playersHand, fullDeck)
        

        while True:
            print()
            command = input("Hit/stand: ")
            
            if command == "view":
                print(playersHand)
                print(playersHand[0][1])
                print(playersHand[1][1])
                print(getPlayersHandValue(playersHand) )
                print(len(playersHand))
            elif command == "hit":
                print()
                add(playersHand, fullDeck)
                if (getPlayersHandValue(playersHand)  > 21):
                    break
                elif (len(fullDeck) < 5):
                    fullDeck = readFullDeck()
            elif command == "stand":
                break
            else:
                print("Not a valid command. Please try again.\n")
        print()
        print("Dealer's cards:")
        while True:
            if (getdealersHandValue(dealersHand) <= 17):
                dealerGetsCard(fullDeck, dealersHand)
            elif (len(fullDeck) < 5):
                    fullDeck = readFullDeck()
            else:
                i = 0 
                break
        i = 0 
        for i in range(len(dealersHand)):
            print(dealersHand[i][0])
            i = i +1


        playerTotal = getPlayersHandValue(playersHand) 
        dealerTotal = getdealersHandValue(dealersHand)
        print()
        print("Your points: ", playerTotal)
        print("Dealer's points: ", dealerTotal)
        print()
        
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
        elif(dealerTotal > 21 and playerTotal > 21 or dealerTotal == playerTotal):
            print("Tie")
            winnings = moneyInWallett

        print("Money: ", winnings)
        wallet.changeAmount(str(winnings))
        print()
        again = input("Play again? (y/n): ")

    print()
    print("Bye!")

if __name__ == "__main__":
    main()
