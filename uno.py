import random

global colours
global cards
global cardData
global lastPlayed

colours = ["Red", "Yellow", "Green", "Blue"]
cards = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

#--------------------------------------------------------------------------------------------------------------------------------------------

def drawCards():            #using function to easily draw cards when needed later
    randomColour = colours[random.randint(0, len(colours) - 1)]         #finds random number for colours
    randomCard = cards[random.randint(0, len(cards) - 1)]           #-1 to ensure it will stay in range

    if randomCard ==  "Wildcard" or randomCard == "+Four":      #Makes sure not to add a colour to colour-less cards
        return randomCard           #returns to easily output needed variables
    else:
        return randomColour + " " + randomCard

#--------------------------------------------------------------------------------------------------------------------------------------------

def playCard(playerSelection):
    
    global cardData
    global lastPlayed
    
    validCard = False
    
    while validCard != True:
        cardSelection = input("Please enter what card you would like to play\n>> ")
        cardsLower = []
        
        for x in range(1, len(playerCards[playerSelection - 1])):
            cardsLower.append(playerCards[playerSelection - 1][x].lower())

        try:            
            if cardSelection.lower() in cardsLower:
                selectedCard = cardsLower.index(cardSelection.lower())
                
                if cardData[0] in playerCards[playerSelection - 1][selectedCard + 1] or cardData[1] in playerCards[playerSelection - 1][selectedCard  + 1]:
                    print("\nPlayed " + playerCards[playerSelection - 1][selectedCard + 1] + "\n")
                    lastPlayed = playerCards[playerSelection - 1][selectedCard + 1]
                    cardData = playerCards[playerSelection - 1][selectedCard + 1].split(" ")
                    del(playerCards[playerSelection - 1][selectedCard + 1])
                    validCard = True
                    
                else:
                    print("That card is invalid. Please choose another card.")

            elif int(cardSelection) >= 1 and int(cardSelection) <= len(playerCards[playerSelection - 1]):
                
                if cardData[0] in playerCards[playerSelection - 1][int(cardSelection)] or cardData[1] in playerCards[playerSelection - 1][int(cardSelection)]:
                    print("\nPlayed " + playerCards[playerSelection - 1][int(cardSelection)] + "\n")
                    lastPlayed = playerCards[playerSelection - 1][int(cardSelection)]
                    cardData = playerCards[playerSelection - 1][int(cardSelection)].split(" ")
                    del(playerCards[playerSelection -1][int(cardSelection)])
                    validCard = True
                    
                else:
                    print("That card is invalid. Please choose another card.")

            else:
                print("You do not have that card in your deck. Please try again.")

        except ValueError:
            print("You do not have that card in your deck. Please try again.")
        
#--------------------------------------------------------------------------------------------------------------------------------------------

lastPlayed = drawCards()
cardData = lastPlayed.split(" ")

playerAmount = 0
while playerAmount == 0:
    try:
        playerAmount = int(input("How many people are going to be playing UNO?\n>> "))
    except ValueError:
        print("Please try again.")

playerCards = []

for x in range(0, playerAmount):
    tempPlayerCards = [x + 1]
    for y in range(0, 7):
        tempPlayerCards.append(drawCards())

    playerCards.append(tempPlayerCards)
    
playerSelection = 1
reverse = False

while True:
#--------------------------------------------------------------------------------------------------------------------------------------------
    while playerSelection < playerAmount + 1 and playerSelection > 0:
        print("\nThe card on top of the deck is " + lastPlayed + "\n")
        menuSelection = input("Player " + str(playerSelection) + ", what would you like to do?\n1) Play A Card\n2) View Your Deck\n3) Draw a new card\n>> ")
        if "play" in menuSelection.lower() or "1" in menuSelection:
            playCard(playerSelection)

            if reverse == False:
                playerSelection += 1
            else:
                playerSelection -= 1

#--------------------------------------------------------------------------------------------------------------------------------------------
            
        elif "view" in menuSelection.lower() or "2" in menuSelection:
            message = ""
            for x in range(0, len(playerCards[playerSelection - 1]) - 1):
                message += str(x + 1) + ") " + playerCards[playerSelection - 1][x + 1] + "\n"
            print(message)

#--------------------------------------------------------------------------------------------------------------------------------------------
            
        elif "draw" in menuSelection.lower() or "3" in menuSelection:
            playerCards[playerSelection - 1].append(drawCards())
            print("\nYou drew " + playerCards[playerSelection - 1][len(playerCards[playerSelection - 1]) - 1] + "\n")

#--------------------------------------------------------------------------------------------------------------------------------------------
            
        else:
            print("That is an invalid option. Please try again.")

    if reverse == False:        
        playerSelection = 1
    else:
        playerSelection = playerAmount
