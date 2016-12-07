import json
import requests
from cardsanddeck import Deck

class handStrength:
	#default amount of players
	players = 5
	#table = table status class
	deck = Deck()
	def getP1Hand(self):
		p1Hand = self.deck.dealPlayer1()
		return p1Hand
	
	def getP2Hand(self):
		p2Hand = self.deck.dealPlayer2()
		return p2Hand
	
	def getP3Hand(self):
		p3Hand = self.deck.dealPlayer3()
		return p3Hand
	
	def getP4Hand(self):
		p4Hand = self.deck.dealPlayer4()
		return p4Hand
	
	def getP5Hand(self):
		p5Hand = self.deck.dealPlayer5()
		return p5Hand
	#waiting for table class to get roundstatus
#	def getBoard(self):
#		if(table.roundStatus() == "preFlop"):
#			return ""
#		if(table.roundStatus() == "postFlop"):
#			return self.deck.dealFlop()
#		if(table.roundStatus() == "postTurn"):
#			return self.deck.dealFlop() + self.deck.dealTurn()
#		if(table.roundStatus() == "postRiver"):
#			return self.deck.dealFlop() + self.deck.dealTurn() + self.deck.dealRiver()
	
	#filler for test until roundstatus implemented
	def getBoard(self):
		return self.deck.dealFlop() + self.deck.dealTurn() + self.deck.dealRiver()
	
	#gets info from the api and takes the odds value
	def getAPI(self, players, hand, board):
		oddsUrl = 'http://stevenamoore.me/projects/holdemapi/?cards='+hand+'&board='+board+'&num_players='+str(players)
		holder = requests.get(oddsUrl)
		api = holder.json()
		odds = 0
		odds = api['odds']
		return(odds)
	
	#gets the odds
	def getOdds(self,players,hand,board):
		odds = self.getAPI(self.players,hand,board)
		return odds
	
	#calls odds for player1
	def player1Odds(self):
		return self.getOdds(self.players,self.getP1Hand(),self.getBoard())
	
	#calls odds for player2
	def player2Odds(self,board):
		return self.getOdds(self.players,self.getP2Hand(),self.getBoard())
	
	#calls odds for player3
	def player3Odds(self,board):
		return self.getOdds(self.players,self.getP3Hand(),self.getBoard())
	
	#calls odds for player4
	def player4Odds(self,board):
		return self.getOdds(self.players,self.getP4Hand(),self.getBoard())

	#calls odds for player5
	def player5Odds(self,board):
		return self.getOdds(self.players,self.getP5Hand(),self.getBoard())

	def maxOdds(self, numplayers, roundstatus):
		if roundstatus == "preflop":
			return self.getAPI(numplayers, "AsAh", "")
		elif roundstatus == "postflop" or "postturn" or "postriver":
			return 1


	def minOdds(self, numplayers, roundstatus):
		if roundstatus == "preflop":
			return self.getAPI(numplayers, "2s3c", "")
		elif roundstatus == "postflop":
			return self.getAPI(numplayers, "2s3c", "7d5c8h")
		elif roundstatus == "postturn":
			return self.getAPI(numplayers, "2s3c", "7d5c8h9s")
		elif roundstatus == "postriver":
			return self.getAPI(numplayers, "2s3c", "7d5c8h9s4h")

	def findWinner(self, hands, board, playerCards):
		winnerUrl = 'http://stevenamoore.me/projects/holdemapi/?cards='+hands+'&board='+board
		holder = requests.get(winnerUrl)
		api = holder.json()
		winner = ""
		cards = api['cards']
		if "-" not in cards:
			for i in playerCards:
				if(playerCards.get(i) == cards[:4]):
					winner = i
		else:
			for i in playerCards:
				if(playerCards.get(i) == cards[:4]):
					winner = i+":"
			for i in playerCards:
				if(playerCards.get(i) == cards[15:19]):
					winner += i
			for i in playerCards:
				if(len(cards) > 30):
					if(playerCards.get(i) == cards[30:34]):
						winner += ":"+i
			for i in playerCards:
				if(len(cards) > 45):
					if(playerCards.get(i) == cards[45:49]):
						winner += ":"+i
			for i in playerCards:
				if(len(cards) > 60):
					if(playerCards.get(i) == cards[60:64]):
						winner += ":"+i
		return winner

