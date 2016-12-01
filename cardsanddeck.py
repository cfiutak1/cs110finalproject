import random

class Card:
	#suit and value
	def __init__(self, card1, card2):
		self.card1 = card1
		self.card2 = card2
		self.card1 = str(self.interpretcardnum(self.card1) + " " + self.interpretcardsuite(self.card1))
		self.card2 = str(self.interpretcardnum(self.card2) + " " + self.interpretcardsuite(self.card2))
		print(self.card1, self.card2)



	def interpretcardnum(self, card):
		if card[0] == 2:
			return "Deuce of"

		elif card[0] == 3:
			return "Three of"

		elif card[0] == 4:
			return "Four of"

		elif card[0] == 5:
			return "Five of"

		elif card[0] == 6:
			return "Six of"

		elif card[0] == 7:
			return "Seven of"

		elif card[0] == 8:
			return "Eight of"

		elif card[0] == 9:
			return "Nine of"

		elif card[0] == "T":
			return "Ten of"

		elif card[0] == "J":
			return "Jack of"

		elif card[0] == "Q":
			return "Queen of"

		elif card[0] == "K":
			return "King of"

		elif card[0] == "A":
			return "Ace of"

	def interpretcardsuite(self, card):
		if card[1] == "c":
			return "clubs"

		elif card[1] == "d":
			return "diamonds"

		elif card[1] == "h":
			return "hearts"

		elif card[1] == "s":
			return "spades"

class Deck:
    def __init__(self):
        self.deck = []
        for val in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
            for suit in ["h", "c", "d", "s"]:
                self.deck.append(val + suit)
        self.shuffleCards()
        self.dealHands()
        self.dealFlop()
        self.dealTurn()
        self.dealRiver()

    def shuffleCards(self):
        random.shuffle(self.deck)
        print(self.deck)

    def dealHands(self, players):
    	accum = 0
    	for player in players:
    		self.player = self.deck[accum] + self.deck[accum + 1]
    		accum += 1
        

        print("Player 1's hand:", self.player1)
        print("Player 2's hand:", self.player2)
        print("Player 3's hand:", self.player3)
        print("Player 4's hand:", self.player4)
        print("Player 5's hand:", self.player5)


    def dealFlop(self):
        flopcard1 = self.deck[10]
        flopcard2 = self.deck[11]
        flopcard3 = self.deck[12]

        print("The flop:", flopcard1, flopcard2, flopcard3)

    def dealTurn(self):
        turncard = self.deck[13]

        print("The turn:", turncard)

    def dealRiver(self):
        rivercard = self.deck[14]

        print("The river:", rivercard)

class Deck: