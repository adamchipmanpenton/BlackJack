
from os import read
import random
import csv
import db as wallet


FILENAME = "BlackJackDeckOfCards.csv"

def write_contacts(contacts):
    with open(FILENAME, "w") as file:
        writer = csv.writer(file)
        writer.writerows(contacts) 

def readFullDeck():
    fullDeck = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            fullDeck.append(row)
    return fullDeck

def dealerShowCard(fullDeck, dealersHand, dealersHandValue):
    print("Dealer's show card: ")
    NewestCard = []
    cardNumber = random.randint(0, len(fullDeck))
    newSuit = fullDeck[cardNumber][0]
    cardValue = int(fullDeck[cardNumber][1])
    if (cardValue == 999):
        if (sum(dealersHandValue) >= 11):
            cardValue = 1
        elif (sum(dealersHandValue) < 11):
            cardValue = 11
    
    NewestCard.append(newSuit)
    NewestCard.append(cardValue)
    
    dealersHand.append(NewestCard)
    dealersHandValue.append(cardValue)
    
    i = 0 
    for i in range(len(dealersHand)):
        print(dealersHand[i][0])
        i = i +1
    print("Dealer's points: ", sum(dealersHandValue))
    fullDeck.pop(cardNumber)

def firstTwoCards(playersHand, playersHandValue, fullDeck):
    print("Your card's:")
    for _ in range(2):
        NewestCard = []
        cardNumber = random.randint(0, (len(fullDeck)-1))
        
        newSuit = fullDeck[cardNumber][0]
        cardValue = int(fullDeck[cardNumber][1])
        if (cardValue == 999):
            if (sum(playersHandValue) >= 11):
                cardValue = 1
            elif (sum(playersHandValue) < 11):
                cardValue = 11
        

        NewestCard.append(newSuit)
        NewestCard.append(cardValue)
        playersHand.append(NewestCard)
        playersHandValue.append(cardValue)
        fullDeck.pop(cardNumber)
    i = 0 
    for i in range(len(playersHand)):
        print(playersHand[i][0])
        i = i +1
    print("Your points: ", sum(playersHandValue))

    

def add(playersHand, playersHandValue, fullDeck):
    print("Your card's:")
    NewestCard = []
    cardNumber = random.randint(0, (len(fullDeck)-1))
    
    newSuit = fullDeck[cardNumber][0]
    cardValue = int(fullDeck[cardNumber][1])
    if (cardValue == 999):
        if (sum(playersHandValue) >= 11):
            cardValue = 1
        elif (sum(playersHandValue) < 11):
            cardValue = 11
    

    NewestCard.append(newSuit)
    NewestCard.append(cardValue)
    playersHand.append(NewestCard)
    playersHandValue.append(cardValue)
    
    i = 0 
    for i in range(len(playersHand)):
        print(playersHand[i][0])
        i = i +1

    print("Your points: ", sum(playersHandValue))
    fullDeck.pop(cardNumber)


def dealerGetsCard(fullDeck, dealersHand, dealersHandValue):
    NewestCard = []
    cardNumber = random.randint(0, len(fullDeck))
    newSuit = fullDeck[cardNumber][0]
    cardValue = int(fullDeck[cardNumber][1])
    if (cardValue == 999):
        if (sum(dealersHandValue) >= 11):
            cardValue = 1
        elif (sum(dealersHandValue) < 11):
            cardValue = 11
    
    NewestCard.append(newSuit)
    NewestCard.append(cardValue)
    
    dealersHand.append(NewestCard)
    dealersHandValue.append(cardValue)
    
    i = 0 
    for i in range(len(dealersHand)):
        print(dealersHand[i][0])
        i = i +1
    fullDeck.pop(cardNumber)


def dealerStands(dealersHandValue, dealersHand):
    print("Dealer Stands")
    for i in range(len(dealersHand)):
        print(dealersHand[i][0])
        i = i +1
    print(sum(dealersHandValue))
    

def winMoney(moneyInWallett, betAmount):
    winnings = moneyInWallett + betAmount
    return winnings


def loseMoney(moneyInWallett, betAmount):
    winnings = moneyInWallett - betAmount
    return winnings




def placeBet():
    bet = float(input("Bet amount: "))
    return bet



def amountInWallet():
    moneyInWallett = wallet.openWallet()
    print("Money: ", moneyInWallett)
    return moneyInWallett
    
   

      
def display_title():
    print("Blackjack!")
    print("Blackjack payout is 3:2")
    print()
    



def main():
    display_title()
   
    fullDeck = readFullDeck()
   
    
    playersHand = []
    dealersHand = []
    playersHandValue = []
    dealersHandValue = []  
    
    moneyInWallett = amountInWallet()
    betAmount = placeBet()
    print(moneyInWallett)
    print(betAmount)
    print()
    dealerShowCard(fullDeck, dealersHand, dealersHandValue)
    print()
    firstTwoCards(playersHand, playersHandValue, fullDeck)
    print()

    


    while True:
        print()
        command = input("Hit/stand: ")
        
        if command == "view":
            print(playersHand)
            print(playersHand[0][0])
            print(playersHand[1][0])
            print(fullDeck)
        elif command == "hit":
            print()
            add(playersHand, playersHandValue, fullDeck)
            if (sum(playersHandValue) > 21):
                break
        elif command == "stand":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print()
    print("Dealer's cards:")
    while True:
        if (sum(dealersHandValue) <= 17):
            dealerGetsCard(fullDeck, dealersHand, dealersHandValue)
        else:
            dealerStands(dealersHandValue, dealersHand)
            break


    playerTotal = sum(playersHandValue) 
    dealerTotal = sum(dealersHandValue) 
    print()
    print("Your points: ", playerTotal)
    print("Dealer's points: ", dealerTotal)
    print()
    winnings = 0
    if ( playerTotal > 21 and dealerTotal <= 21):
        print("You bust, you loose")
        winnings = loseMoney(moneyInWallett, betAmount)
    elif(dealerTotal > playerTotal and dealerTotal <= 21):
        print("You loose")
        winnings = loseMoney(moneyInWallett, betAmount)
    elif(dealerTotal < playerTotal and playerTotal <= 21):
        print("you win")
        winnings = winMoney(moneyInWallett, betAmount)
    elif(dealerTotal > 21 and playerTotal > 21):
        print("Tie")
        winnings = moneyInWallett

    print("Money: ", winnings)
    wallet.changeAmount(str(winnings))

    print()
    print("Bye!")

if __name__ == "__main__":
    main()
