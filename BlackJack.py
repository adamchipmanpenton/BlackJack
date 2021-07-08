
from os import read
import random
import csv


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
    print("Dearl's cards:")
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

def dealerStands(dealersHandValue, dealersHand):
    print("Dealer Stands")
    for i in range(len(dealersHand)):
        print(dealersHand[i][0])
        i = i +1
    print(sum(dealersHandValue))
    


   

      
def display_title():
    print("Blackjack!")
    print()



def main():
    
   
    fullDeck = readFullDeck()
   
    
    playersHand = []
    dealersHand = []
    playersHandValue = []
    dealersHandValue = []  
        
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
            print()

            if (sum(dealersHandValue) <= 17):
                dealerGetsCard(fullDeck, dealersHand, dealersHandValue)
            else:
                dealerStands(dealersHandValue, dealersHand)
       
        elif command == "stand":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print()
    if (sum(playersHandValue) > 21 & sum(dealersHandValue) <= 21):
        print("You bust, you loose")
    elif(sum(dealersHandValue) > sum(playersHandValue)):
        print("You loose")
    elif(sum(dealersHandValue) < sum(playersHandValue)):
        print("you win")
    elif(sum(dealersHandValue) > 21 & sum(playersHandValue) > 21):
        print("Tie")

    print("Bye!")

if __name__ == "__main__":
    main()
