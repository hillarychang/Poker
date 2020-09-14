import random
 
print('''Welcome to the Game.''')
 
class Card:
 
  SUIT = ['♥', '♦', '♣', '♠']
  RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
 
  def __init__(self, rank, suit):
  	self.rank = rank
  	self.suit = suit
  	
  # Returns a numerical value for cards 1-13 dependistack_of_cards the rank of the card
  def getValue(self):
  	if self.rank == 'A':
      	return(1)
  	elif self.rank == 'J':
      	return(11)
  	elif self.rank == 'Q':
      	return(12)
  	elif self.rank == 'K':
      	return(13)
  	elif self.rank in '23456789' or self.rank == '10':
      	return(int(self.rank))
  	else:
      	raise ValueError('{} is of unkwown value'.format(self.rank))
 
  def getRank(self):  
  	return(self.rank)
 
  def getSuit(self):  
  	return(self.suit)
 
  def __str__(self):
  	return('{}{}'.format(self.rank, self.suit))
 
class StackOfCards:
 
  def __init__(self):
  	'''
  	Constructor
  	'''
  	self.cards = []
  	
  # returns a string of all the cards in the 'deck'
  def __str__(self):
  	s = ''
  	for card in self.cards:
      	if len(s) == 1:
          	s = s + str(card)
      	else:
          	s = s + ' ' + str(card)
  	s = s
  	return(s)
 
  # Add card to the 'bottom' of the deck of cards
  def add(self, card):
  	self.cards.append(card)
          	
  def remove(self, pos):
  	card = self.cards.pop(pos)
  	return card
          	
  # Deal card from the 'top' of the deck of cards
  def deal(self):
  	return self.cards.pop(0)
  	
  def shuffle(self):
  	random.shuffle(self.cards)
  	
  def size(self):
  	return(len(self.cards))
 
  def getCard(self, pos):
  	return(self.cards[pos])
 
class Player:
 
  # inputs:
  #	name - string for the player's name
  #	amount - integer for how much money the player has
  #	cards - a StackOfCards
  def __init__(self, name, amount, cards):
  	'''
  	Constructor
  	'''
  	self.name = name
  	self.money = amount
  	self.hand = cards
	
  # prints out name and the hand of stack_of_cards	
  def __str__(self):
  	return("{}: {}".format(self.name, self.hand))
 
  def introduce(self):
  	print("Hi, my name is {}".format(self.name))
  	
  def getName(self):
  	return(self.name)
 
  def getMoney(self):
  	return self.money
 
  # add (or subtract) player's money	
  def addMoney(self, amount):
  	self.money += amount
 
  # when player given another card, add it it player's hand	
  def addCard(self, card):
  	self.hand.add(card)
  	
  def getCard(self, pos):
  	return self.hand.getCard(pos)
 
  def removeCard(self, pos):
  	return self.hand.remove(pos)
 
class PokerPlayer(Player):
 
  def __init__(self, name, amt, cards):
	self.name = name
	self.amt = amt
	self.cards = cards
  	
  def askHoldChoice(self):
  	return(input("Which cards would you like to hold? (ex. 1 4 5)"))
 
# These are the winning hands in order of strength
WINNING_HANDS = [ "Royal Flush", \
            	"Straight Flush", \
            	"Four of a Kind", \
            	"Full House", \
            	"Flush", \
            	"Straight", \
            	"3 of a Kind", \
            	"Two Pairs", \
            	"Pair (Jacks or better)" ]
 
# make a PokerCard Class inherit from Card
 
  # make the player
  #player = PokerPlayer("Player", 1)
 
  # make a deck of card
  # deck = PokerHand()  # make empty deck
  # add the 52-cards and shuffle
 
  
#Get name of the player
#Ask how much money/credits you have
#Shuffle deck of 52 cards
 
class PokerCard(Card): 
  def __init__(self, rank, suit):
  	self.rank = rank
  	self.suit = suit
 
  def getSuit(self):
	return self.suit
  	
  def getValue(self):
  	if self.rank == 'A':
      	return(14)
  	else:
      	return self.rank
  	
  def __eq__(self, otherRank):
	return self.rank == otherRank
      	
  def __lt__(self, otherRank):
  	return self.rank < otherRank
  	
#class below represents either a deck of 52 PokerCards or the player’s hand of 5 PokerCards    	
class PokerHand(StackOfCards):
  def __init__(self, cards, suit):
	self.cards = cards
	self.suit = suit
  	#10 J Q K A
 
  def sort(self):
	self.cards.sort()
 
#Cases
  def handType(self):
	c0 = self.getCard(0)
	c1 = self.getCard(1)
	c2 = self.getCard(2)
	c3 = self.getCard(3)
	c4 = self.getCard(4)
 
	s0 = self.suit[0]
	s1 = self.suit[1]
	s2 = self.suit[2]
	s3 = self.suit[3]
	s4 = self.suit[4]
 
	if c1-c0==1 and c2-c1==1 and c3-c2==1 and c4-c3==1:
  #make sure cards are incrementing by 1
  	if (c0==10 and c1 == 11 and c2== 12 and c3==13 and c4==14) and (s0==s1 and s1==s2 and s2==s3 and s3==s4):
    	return ("Royal Flush")
  	elif (s0==s1 and s1==s2 and s2==s3 and s3==s4):	#make sure the flush are the same (and the cards are increment by 1)
    	return ("Straight Flush")
 
  ##FOUR OF A KIND
	if (self.cards.count(1)==2 or self.cards.count(2)==2 or self.cards.count(3)==2 or self.cards.count(4)==2 or self.cards.count(5)==2 or self.cards.count(6)==2 or self.cards.count(7)==2 or self.cards.count(8)==2 or self.cards.count(9)==2 or self.cards.count(10)==2 or self.cards.count(11)==2 or self.cards.count(12)==2 or self.cards.count(13)==2) and(self.cards.count(1)==3 or self.cards.count(2)==3 or self.cards.count(3)==3 or self.cards.count(4)==3 or self.cards.count(5)==3 or self.cards.count(6)==3 or self.cards.count(7)==3 or self.cards.count(8)==3 or self.cards.count(9)==3 or self.cards.count(10)==3 or self.cards.count(11)==3 or self.cards.count(12)==3 or self.cards.count(13)==3):
  	result = "Full House"
  	return ("Full House")
	elif (s0==s1 and s1==s2 and s2==s3 and s3==s4) :
  	result = "Flush"
  	return ("Flush")
	elif (c1-c0==1 and c2-c1==1 and c3-c2==1 and c4-c3==1):
  	result = "Straight"
  	return ("Straight")
	elif (c0-c1==0 and c2-c3==0)or (c1-c2==0 and c3-c4==0) or (c0-c1==0 and c3-c4==0):
  	result = "Two Pair"
  	return ("Two Pair")  
  #below codes for: jacks+, three of a kind, and four of a kind
  placeval = 0
  matches = 0
  matcheslist = []
  while placeval < len(self.cards):
  	for n in range(1,15):
    	if self.cards(placeval) == n:
        	matches += 1
        	matcheslist.append(self.cards(placeval))
        	placeval += 1
    	else:
        	placeval += 1
  if matches == 2:  
	for x in matcheslist:
  	if sum(matcheslist) >= 22:
    	result = "Pair (Jacks or better)"
    	return ("Pair (Jacks or better)")
  	else:
    	result = "Nothing"
    	return ("Nothing")  
  elif matches == 3:  
	result = "3 of a Kind"
	return ("3 of a Kind")
  elif matches == 4:
	result = "Four of a Kind"
	return ("Four of a Kind")
  else:
	result = "Nothing"
	return ("Nothing")
 
# in playRound()
  r = result
  if r == "Royal Flush":
	reward = 250
  elif r == "Straight Flush":
	reward = 50
  elif r == "Full House":
	reward = 9
  elif r == "Flush":
	reward = 6
  elif r == "Straight":
	reward = 4
  elif r == "Pair (Jacks or better)":
	reward = 1
  elif r == "3 of a Kind":
	reward = 3
  elif r == "Four of a Kind":
	reward = 25
	
#add forloop
  currentMoney = "You earned " + reward + " coins."
  print(Fore.RED + currentMoney)
reply = input('''Play again?
''')
while reply != "Yes" or reply != "yes" or reply != "y" or reply != "Y" or reply != "No" or reply != "no" or reply != "n" or reply != "N":
  reply = input('''Play again?
''')
  if reply == "Yes" or reply == "yes" or reply == "y" or reply == "Y" or reply == "No" or reply == "no" or reply == "n" or reply == "N":
	break
 
 
#this is the function that will control all the objects to play the poker game. In this function I made a player (PokerPlayer) and a deck of 52 (PokerHand) and play the game.
def PokerGame(): 
  PokerPlayer = Player
  PokerHand = StackOfCards
  playRound(PokerPlayer, PokerHand)
 
#this function takes in two inputs – a PokerPlayer and a shuffled deck of cards (PokerHand). It will play 1 round of the game. It will update the player’s money accordingly.
def playRound(player, deck):
  print(PokerHand.handType.hand)
  PokerPlayer.self.amt += PokerHand.handType.reward
  currentMoney=currentMoney-1
  deck.deal()  #PokerHand.deal()
  deck.sort()
  print(deck)
  holdcards=input("Which cards would you like to hold? (ex. 1 4 5)")
 
for p in len(holdcards): #holdcards is a string
  crds=""
  if holdcards[p] =="1" or holdcards[p] =="2" or holdcards[p] =="3" or holdcards[p] =="4" or holdcards[p] =="5":
	crds=p+crds #crds="123"
 
for i in len(deck): 
  if c[i] not in crds:
	deck.remove(i) #remove cards player doesn't want
print (deck)
 
for u in (5-len(deck)): #deal new cards (e)
  deck.deal()
print (deck)
  	
 
 
def main():
  PokerGame()
 
if __name__ == "__main__":
  main()
