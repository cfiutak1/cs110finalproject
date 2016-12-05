import random

class Cards:
	def __init__(self):
		self.myvar = 0

	def interpretCardNum(self, card):
		if card[0] == "2":
			return "Deuce of"

		elif card[0] == "3":
			return "Three of"

		elif card[0] == "4":
			return "Four of"

		elif card[0] == "5":
			return "Five of"

		elif card[0] == "6":
			return "Six of"

		elif card[0] == "7":
			return "Seven of"

		elif card[0] == "8":
			return "Eight of"

		elif card[0] == "9":
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

	def interpretCardSuit(self, card):
		if card[1] == "c":
			return "clubs"

		elif card[1] == "d":
			return "diamonds"

		elif card[1] == "h":
			return "hearts"

		elif card[1] == "s":
			return "spades"

	def cardText(self, card):
		return self.interpretCardNum(card) + " " + self.interpretCardSuit(card)

class Deck:
	def __init__(self):
		self.deck = []
		self.accum = 0

		for val in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
			for suit in ["h", "c", "d", "s"]:
				self.deck.append(val + suit)

		random.shuffle(self.deck)
		print(self.deck)

	def dealPlayer1(self):
		self.player1 = self.deck[self.accum] + self.deck[self.accum + 1]
		self.accum += 2

		return self.player1
	
	def dealPlayer2(self):
		self.player2 = self.deck[self.accum] + self.deck[self.accum + 1]
		self.accum += 2

		return self.player2		

	def dealPlayer3(self):
		self.player3 = self.deck[self.accum] + self.deck[self.accum + 1]
		self.accum += 2

		return self.player3

	def dealPlayer4(self):
		self.player4 = self.deck[self.accum] + self.deck[self.accum + 1]
		self.accum += 2

		return self.player4

	def dealPlayer5(self):
		self.player5 = self.deck[self.accum] + self.deck[self.accum + 1]
		self.accum += 2

		return self.player5		

	def dealFlop(self):
		self.flopcard1 = self.deck[self.accum]
		self.accum += 1

		self.flopcard2 = self.deck[self.accum]
		self.accum += 1

		self.flopcard3 = self.deck[self.accum]
		self.accum += 1

		return self.flopcard1 + self.flopcard2 + self.flopcard3

	def dealTurn(self):
		self.turncard = self.deck[self.accum]
		self.accum += 1

		return self.turncard

	def dealRiver(self):
		self.rivercard = self.deck[self.accum]

		return self.rivercard

def main():
	deck = Deck()
	cards = Cards()
	players = ["player1", "player2", "player3", "player4", "player5"]
	mycards = deck.dealPlayer1()
	mycard1 = mycards[0] + mycards[1]
	mycard2 = mycards[2] + mycards[3]

	print(mycards)
	print(deck.dealPlayer2())
	print(deck.dealPlayer3())
	print(deck.dealPlayer4())
	print(deck.dealPlayer5())
	print(deck.dealFlop())
	print(deck.dealTurn())
	print(deck.dealRiver())
	print("========MY CARDS========")
	print(mycard1)
	print(mycard2)
	
	print(cards.cardText(mycard1))
	print(cards.cardText(mycard2))
	
main()