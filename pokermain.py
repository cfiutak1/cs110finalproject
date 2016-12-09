from datetime import datetime, timedelta
import math
import random
import requests
import pygame
from ai import AI
from cardsanddeck import Cards, Deck
import json
#from gui import mainmenu, gamegui
#from netprofits import netprofits
from handstrength import handStrength
from playersandtable import Player, Table

def assignRandPersonality(integer):
	if integer <= 24:
		return "tightaggressive"
	elif 23 < integer <= 46:
		return "looseaggressive"
	elif 46 < integer <= 69:
		return "tightpassive"
	elif 69 < integer <= 92:
		return "loosepassive"
	elif integer > 92:
		return "madman"

def main():
	table = Table()
	playerclass = Player()
	ai = AI()
	hs = handStrength()
	#mainmenu = mainMenu()
	#gamegui = Game()
	cards = Cards()
	deck = Deck()
	#netprofits = netprofits()

	bigblind = 100
	
	starttime = datetime.now()
	players = ["player1", "player2", "player3", "player4", "player5"]
	liveplayers = ["player1", "player2", "player3", "player4", "player5"]
	
	#Assigns random personalities to AI
	p2pers = assignRandPersonality(random.randrange(0,101))
	p3pers = assignRandPersonality(random.randrange(0,101))
	p4pers = assignRandPersonality(random.randrange(0,101))
	p5pers = assignRandPersonality(random.randrange(0,101))

	while game != "over":
		playercards = {}
		playercardsstr = ""	
		nowtime = datetime.now()
		bigblind = table.blinds(100, starttime, nowtime)
		tocall = bigblind

		#Creates a list with the order of players in the round.
		myplayers1 = []
		myplayers1.append(table.assignDealer(liveplayers))
		myplayers1.append(table.assignSB(liveplayers))
		myplayers1.append(table.assignBB(liveplayers))
		myplayers2 = []
		for player in players:
			if player not in myplayers1:
				myplayers2.append(player)
		if players[-1] and players[0] in myplayers2:
			if "player2" not in myplayers2:
				myplayers2.reverse()
		orderedplayers = myplayers2 + myplayers1


		#Applies big blind to player when they are two seats to the left of the dealer chip.
		if orderedplayers[-1] == "player1":
			playerclass.player1(bigblind, "Call", bigblind)
			table.mainPot(bigblind)

		elif orderedplayers[-1] == "player2":
			playerclass.player2(bigblind, "Call", bigblind)
			table.mainPot(bigblind)

		elif orderedplayers[-1] == "player3":
			playerclass.player3(bigblind, "Call", bigblind)
			table.mainPot(bigblind)

		elif orderedplayers[-1] == "player4":
			playerclass.player4(bigblind, "Call", bigblind)
			table.mainPot(bigblind)

		elif orderedplayers[-1] == "player5":
			playerclass.player5(bigblind, "Call", bigblind)
			table.mainPot(bigblind)

	#Applies small blind to player when they are one seat to the left of the dealer chip.
		if orderedplayers[-2] == "player1":
			playerclass.player1(bigblind // 2, "Call", bigblind)
			table.mainPot(bigblind // 2)

		elif orderedplayers[-2] == "player2":
			playerclass.player1(bigblind // 2, "Call", bigblind)
			table.mainPot(bigblind // 2)

		elif orderedplayers[-2] == "player3":
			playerclass.player1(bigblind // 2, "Call", bigblind)
			table.mainPot(bigblind // 2)

		elif orderedplayers[-2] == "player4":
			playerclass.player1(bigblind // 2, "Call", bigblind)
			table.mainPot(bigblind // 2)

		elif orderedplayers[-2] == "player5":
			playerclass.player1(bigblind // 2, "Call", bigblind)
			table.mainPot(bigblind // 2)


		if "player1" in orderedplayers:
			p1cards = deck.dealPlayer1()
			playercards["player1"] = p1cards
			
		if "player2" in orderedplayers:
			p2cards = deck.dealPlayer2()
			playercards["player2"] = p2cards
			p2odds = hs.getAPI(len(orderedplayers), p2cards, "")
			
		if "player3" in orderedplayers:
			p3cards = deck.dealPlayer3()
			playercards["player3"] = p3cards
			p3odds = hs.getAPI(len(orderedplayers), p3cards, "")

		if "player4" in orderedplayers:
			p4cards = deck.dealPlayer4()
			playercards["player4"] = p4cards
			p4odds = hs.getAPI(len(orderedplayers), p4cards, "")

		if "player5" in orderedplayers:
			p5cards = deck.dealPlayer5()
			playercards["player5"] = p5cards
			p5odds = hs.getAPI(len(orderedplayers), p5cards, "")


		#Create ordered list of players, calculate odds and decisions as the list cycles through the player's cards
		p2refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "preflop"), hs.maxOdds(len(liveplayers), "preflop"), p2odds, tocall, playerclass.checkStash("player2"), "preflop", bigblind, len(liveplayers))
		p3refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "preflop"), hs.maxOdds(len(liveplayers), "preflop"), p3odds, tocall, playerclass.checkStash("player3"), "preflop", bigblind, len(liveplayers))
		p4refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "preflop"), hs.maxOdds(len(liveplayers), "preflop"), p4odds, tocall, playerclass.checkStash("player4"), "preflop", bigblind, len(liveplayers))
		p5refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "preflop"), hs.maxOdds(len(liveplayers), "preflop"), p5odds, tocall, playerclass.checkStash("player5"), "preflop", bigblind, len(liveplayers))

		playerbets = []

		if "player1" in orderedplayers:
			p1decision = str(input("Enter decision: "))

		if "player2" in orderedplayers:
			p2decision = ai.aiDecision(p2refodds, p2pers)

		if "player3" in orderedplayers:
			p3decision = ai.aiDecision(p3refodds, p3pers)

		if "player4" in orderedplayers:
			p4decision = ai.aiDecision(p4refodds, p4pers)

		if "player5" in orderedplayers:
			p5decision = ai.aiDecision(p5refodds, p5pers)


		if "player1" in orderedplayers:
			if p1decision == "Fold":
				orderedplayers.remove("player1")

			elif p1decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p1bet = playerclass.player1(tocall, p1decision, bigblind)
				table.mainPot(p1bet)
				if tocall <= p1bet:
					tocall = p1bet
				playerbets.append(p1bet)

		if "player2" in orderedplayers:
			if p2decision == "Fold":
				orderedplayers.remove("player2")

			elif p2decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p2bet = playerclass.player2(tocall, p2decision, bigblind)
				table.mainPot(p2bet)
				if tocall <= p2bet:
					tocall = p2bet
				playerbets.append(p2bet)

		if "player3" in orderedplayers:
			if p3decision == "Fold":
				orderedplayers.remove("player3")

			elif p3decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p3bet = playerclass.player3(tocall, p3decision, bigblind)
				table.mainPot(p3bet)
				if tocall <= p3bet:
					tocall = p3bet
				playerbets.append(p3bet)

		if "player4" in orderedplayers:
			if p4decision == "Fold":
				orderedplayers.remove("player4")

			elif p4decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p4bet = playerclass.player4(tocall, p4decision, bigblind)
				table.mainPot(p4bet)
				if tocall <= p4bet:
					tocall = p4bet
				playerbets.append(p4bet)

		if "player5" in orderedplayers:
			if p5decision == "Fold":
				orderedplayers.remove("player5")

			elif p5decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p5bet = playerclass.player5(tocall, p5decision, bigblind)
				table.mainPot(p5bet)
				if tocall <= p5bet:
					tocall = p5bet
				playerbets.append(p5bet)

#=================================================================================================================================================
		tocall = 0
		playerclass.resetBets()
		flop = deck.dealFlop()

		if "player2" in orderedplayers:
			p2odds = hs.getAPI(len(orderedplayers), p2cards, flop)
			p2refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postflop"), hs.maxOdds(len(liveplayers), "postflop"), p2odds, tocall, playerclass.checkStash("player2"), "postflop", bigblind, len(liveplayers))

		if "player3" in orderedplayers:
			p3odds = hs.getAPI(len(orderedplayers), p3cards, flop)
			p3refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postflop"), hs.maxOdds(len(liveplayers), "postflop"), p3odds, tocall, playerclass.checkStash("player3"), "postflop", bigblind, len(liveplayers))

		if "player4" in orderedplayers:
			p4odds = hs.getAPI(len(orderedplayers), p4cards, flop)
			p4refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postflop"), hs.maxOdds(len(liveplayers), "postflop"), p4odds, tocall, playerclass.checkStash("player4"), "postflop", bigblind, len(liveplayers))

		if "player5" in orderedplayers:
			p5odds = hs.getAPI(len(orderedplayers), p5cards, flop)
			p5refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postflop"), hs.maxOdds(len(liveplayers), "postflop"), p5odds, tocall, playerclass.checkStash("player5"), "postflop", bigblind, len(liveplayers))
		

		if "player1" in orderedplayers:
			p1decision = str(input("Enter decision: "))

		if "player2" in orderedplayers:
			p2decision = ai.aiDecision(p2refodds, p2pers)

		if "player3" in orderedplayers:
			p3decision = ai.aiDecision(p3refodds, p3pers)

		if "player4" in orderedplayers:
			p4decision = ai.aiDecision(p4refodds, p4pers)

		if "player5" in orderedplayers:
			p5decision = ai.aiDecision(p5refodds, p5pers)		

		
		if "player1" in orderedplayers:
			if p1decision == "Fold":
				orderedplayers.remove("player1")

			elif p1decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p1bet = playerclass.player1(tocall, p1decision, bigblind)
				table.mainPot(p1bet)
				if tocall <= p1bet:
					tocall = p1bet
				playerbets.append(p1bet)

		if "player2" in orderedplayers:
			if p2decision == "Fold":
				orderedplayers.remove("player2")

			elif p2decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p2bet = playerclass.player2(tocall, p2decision, bigblind)
				table.mainPot(p2bet)
				if tocall <= p2bet:
					tocall = p2bet
				playerbets.append(p2bet)

		if "player3" in orderedplayers:
			if p3decision == "Fold":
				orderedplayers.remove("player3")

			elif p3decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p3bet = playerclass.player3(tocall, p3decision, bigblind)
				table.mainPot(p3bet)
				if tocall <= p3bet:
					tocall = p3bet
				playerbets.append(p3bet)

		if "player4" in orderedplayers:
			if p4decision == "Fold":
				orderedplayers.remove("player4")

			elif p4decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p4bet = playerclass.player4(tocall, p4decision, bigblind)
				table.mainPot(p4bet)
				if tocall <= p4bet:
					tocall = p4bet
				playerbets.append(p4bet)

		if "player5" in orderedplayers:
			if p5decision == "Fold":
				orderedplayers.remove("player5")

			elif p5decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p5bet = playerclass.player5(tocall, p5decision, bigblind)
				table.mainPot(p5bet)
				if tocall <= p5bet:
					tocall = p5bet
				playerbets.append(p5bet)

#===============================================================================================================================================================================
		tocall = 0
		playerclass.resetBets()
		turn = deck.dealTurn()
		board = flop + turn


		if "player2" in orderedplayers:
			p2odds = hs.getAPI(len(orderedplayers), p2cards, board)
			p2refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postturn"), hs.maxOdds(len(liveplayers), "postturn"), p2odds, tocall, playerclass.checkStash("player2"), "postturn", bigblind, len(liveplayers))

		if "player3" in orderedplayers:
			p3odds = hs.getAPI(len(orderedplayers), p3cards, board)
			p3refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postturn"), hs.maxOdds(len(liveplayers), "postturn"), p3odds, tocall, playerclass.checkStash("player3"), "postturn", bigblind, len(liveplayers))

		if "player4" in orderedplayers:
			p4odds = hs.getAPI(len(orderedplayers), p4cards, board)
			p4refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postturn"), hs.maxOdds(len(liveplayers), "postturn"), p4odds, tocall, playerclass.checkStash("player4"), "postturn", bigblind, len(liveplayers))

		if "player5" in orderedplayers:
			p5odds = hs.getAPI(len(orderedplayers), p5cards, flop)
			p5refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postturn"), hs.maxOdds(len(liveplayers), "postturn"), p5odds, tocall, playerclass.checkStash("player5"), "postturn", bigblind, len(liveplayers))

		
		if "player1" in orderedplayers:
			p1decision = str(input("Enter decision: "))

		if "player2" in orderedplayers:
			p2decision = ai.aiDecision(p2refodds, p2pers)

		if "player3" in orderedplayers:
			p3decision = ai.aiDecision(p3refodds, p3pers)

		if "player4" in orderedplayers:
			p4decision = ai.aiDecision(p4refodds, p4pers)

		if "player5" in orderedplayers:
			p5decision = ai.aiDecision(p5refodds, p5pers)		


		if "player1" in orderedplayers:
			if p1decision == "Fold":
				orderedplayers.remove("player1")

			elif p1decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p1bet = playerclass.player1(tocall, p1decision, bigblind)
				table.mainPot(p1bet)
				if tocall <= p1bet:
					tocall = p1bet
				playerbets.append(p1bet)

		if "player2" in orderedplayers:
			if p2decision == "Fold":
				orderedplayers.remove("player2")

			elif p2decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p2bet = playerclass.player2(tocall, p2decision, bigblind)
				table.mainPot(p2bet)

				if tocall <= p2bet:
					tocall = p2bet
				playerbets.append(p2bet)

		if "player3" in orderedplayers:
			if p3decision == "Fold":
				orderedplayers.remove("player3")
			elif p3decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p3bet = playerclass.player3(tocall, p3decision, bigblind)
				table.mainPot(p3bet)
				if tocall <= p3bet:
					tocall = p3bet
				playerbets.append(p3bet)

		if "player4" in orderedplayers:
			if p4decision == "Fold":
				orderedplayers.remove("player4")
			elif p4decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p4bet = playerclass.player4(tocall, p4decision, bigblind)
				table.mainPot(p4bet)
				if tocall <= p4bet:
					tocall = p4bet
				playerbets.append(p4bet)

		if "player5" in orderedplayers:
			if p5decision == "Fold":
				orderedplayers.remove("player5")
			elif p5decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p5bet = playerclass.player5(tocall, p5decision, bigblind)
				table.mainPot(p5bet)
				if tocall <= p5bet:
					tocall = p5bet
				playerbets.append(p5bet)

#================================================================================================================================
		tocall = 0
		playerclass.resetBets()
		river = deck.dealTurn()
		board = flop + turn + river


		if "player2" in orderedplayers:
			p2odds = hs.getAPI(len(orderedplayers), p2cards, board)
			p2refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postriver"), hs.maxOdds(len(liveplayers), "postriver"), p2odds, tocall, playerclass.checkStash("player2"), "postriver", bigblind, len(liveplayers))

		if "player3" in orderedplayers:
			p3odds = hs.getAPI(len(orderedplayers), p3cards, board)
			p3refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postriver"), hs.maxOdds(len(liveplayers), "postriver"), p3odds, tocall, playerclass.checkStash("player3"), "postriver", bigblind, len(liveplayers))


		if "player4" in orderedplayers:
			p4odds = hs.getAPI(len(orderedplayers), p4cards, board)
			p4refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postriver"), hs.maxOdds(len(liveplayers), "postriver"), p4odds, tocall, playerclass.checkStash("player4"), "postriver", bigblind, len(liveplayers))

		if "player5" in orderedplayers:
			p5odds = hs.getAPI(len(orderedplayers), p5cards, flop)
			p5refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "postriver"), hs.maxOdds(len(liveplayers), "postriver"), p5odds, tocall, playerclass.checkStash("player5"), "postriver", bigblind, len(liveplayers))


		if "player1" in orderedplayers:
			p1decision = str(input("Enter decision: "))

		if "player2" in orderedplayers:
			p2decision = ai.aiDecision(p2refodds, p2pers)

		if "player3" in orderedplayers:
			p3decision = ai.aiDecision(p3refodds, p3pers)

		if "player4" in orderedplayers:
			p4decision = ai.aiDecision(p4refodds, p4pers)

		if "player5" in orderedplayers:
			p5decision = ai.aiDecision(p5refodds, p5pers)		


		if "player1" in orderedplayers:
			playercardsstr += p1cards
			if p1decision == "Fold":
				orderedplayers.remove("player1")
			elif p1decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p1bet = playerclass.player1(tocall, p1decision, bigblind)
				table.mainPot(p1bet)
				if tocall <= p1bet:
					tocall = p1bet
				playerbets.append(p1bet)

		if "player2" in orderedplayers:
			playercardsstr += p2cards
			if p2decision == "Fold":
				orderedplayers.remove("player2")
			elif p2decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p2bet = playerclass.player2(tocall, p2decision, bigblind)
				table.mainPot(p2bet)
				if tocall <= p2bet:
					tocall = p2bet
				playerbets.append(p2bet)

		if "player3" in orderedplayers:
			playercardsstr += p3cards
			if p3decision == "Fold":
				orderedplayers.remove("player3")
			elif p3decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p3bet = playerclass.player3(tocall, p3decision, bigblind)
				table.mainPot(p3bet)
				if tocall <= p3bet:
					tocall = p3bet
				playerbets.append(p3bet)

		if "player4" in orderedplayers:
			playercardsstr += p4cards
			if p4decision == "Fold":
				orderedplayers.remove("player4")
			elif p4decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p4bet = playerclass.player4(tocall, p4decision, bigblind)
				table.mainPot(p4bet)
				if tocall <= p4bet:
					tocall = p4bet
				playerbets.append(p4bet)

		if "player5" in orderedplayers:
			playercardsstr += p5cards
			if p5decision == "Fold":
				orderedplayers.remove("player5")
			elif p5decision == "Call" or "Raise2BB" or "Raise3BB" or "RaisePot" or "AllIn":
				p5bet = playerclass.player5(tocall, p5decision, bigblind)
				table.mainPot(p5bet)
				if tocall <= p5bet:
					tocall = p5bet
				playerbets.append(p5bet)

		
		winner = hs.findWinner(playercardsstr, board, playercards)


		if "player1" == winner:
			playerclass.award("player1", table.getMainPot())
		elif "player2" == winner:
			playerclass.award("player2", table.getMainPot())
		if "player3" == winner:
			playerclass.award("player3", table.getMainPot())
		if "player4" == winner:
			playerclass.award("player4", table.getMainPot())
		if "player5" == winner:
			playerclass.award("player5", table.getMainPot())

		elif ":" in winner:
			winner = winner.split(":")
			n = len(winner)
			if "player1" in winner:
				playerclass.award("player1", table.getMainPot() // n)
			if "player2" in winner:
				playerclass.award("player2", table.getMainPot() // n)
			if "player3" in winner:
				playerclass.award("player3", table.getMainPot() // n)
			if "player4" in winner:
				playerclass.award("player4", table.getMainPot() // n)
			if "player5" in winner:
				playerclass.award("player5", table.getMainPot() // n)

		p1stash = playerclass.checkStash("player1")
		p2stash = playerclass.checkStash("player2")
		p3stash = playerclass.checkStash("player3")
		p4stash = playerclass.checkStash("player4")
		p5stash = playerclass.checkStash("player5")

		if p1stash == 0:
			game = "over"
			p1status = "lose"

		if p2stash == 0:
			liveplayers.remove("player2")

		if p3stash == 0:
			liveplayers.remove("player3")

		if p4stash == 0:
			liveplayers.remove("player4")

		if p5stash == 0:
			liveplayers.remove("player5")

		if len(myplayers) == 1:
			if "player1" in myplayers:
				p1status = "win"
				game = "over"
			else:
				p1status = "lose"
				game = "over"

		playerclass.resetBets()
		deck.resetAccum()
		deck.forceShuffle()
		table.resetMainPot()
		table.moveDealer()
		bigblind = table.blinds(bigblind, startime, nowtime)
main()