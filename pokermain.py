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
	tocall = bigblind
	starttime = datetime.now()
	players = ["player1", "player2", "player3", "player4", "player5"]
	liveplayers = ["player1", "player2", "player3", "player4", "player5"]
	
	p2pers = assignRandPersonality(random.randrange(0,101))
	p3pers = assignRandPersonality(random.randrange(0,101))
	p4pers = assignRandPersonality(random.randrange(0,101))
	p5pers = assignRandPersonality(random.randrange(0,101))

	print(p2pers, p3pers, p4pers, p5pers)


	while str(input("meme")) != "over":
		while str(input("round status")) == "preflop":
			
			nowtime = datetime.now()
			bigblind = table.blinds(100, starttime, nowtime)

			#Creates a list with the order of players in the round.
			myplayers1 = []
			myplayers1.append(table.assignDealer(players))
			myplayers1.append(table.assignSB(players))
			myplayers1.append(table.assignBB(players))
			myplayers2 = []
			for player in players:
				if player not in myplayers1:
					myplayers2.append(player)
			if players[-1] and players[0] in myplayers2:
				if "player2" not in myplayers2:
					myplayers2.reverse()
			myplayers3 = myplayers2 + myplayers1
			print(myplayers3)

			# #Applies big blind to player when they are two seats to the left of the dealer chip.
			# for player in liveplayers:
			# 	if myplayers3[-1] == "player1":
			# 		playerclass.blindplayer1("big", bigblind)
			# 		table.mainPot(bigblind)
			# 	elif myplayers3[-1] == "player2":
			# 		playerclass.blindplayer2("big", bigblind)
			# 		table.mainPot(bigblind)
			# 	elif myplayers3[-1] == "player3":
			# 		playerclass.blindplayer3("big", bigblind)
			# 		table.mainPot(bigblind)
			# 	elif myplayers3[-1] == "player4":
			# 		playerclass.blindplayer4("big", bigblind)
			# 		table.mainPot(bigblind)
			# 	elif myplayers3[-1] == "player5":
			# 		playerclass.blindplayer5("big", bigblind)
			# 		table.mainPot(bigblind)

			# #Applies small blind to player when they are one seat to the left of the dealer chip.
			# for player in liveplayers:
			# 	if myplayers3[-2] == "player1":
			# 		player.blindplayer1("small", bigblind)
			# 		table.mainPot(bigblind / 2)
			# 	elif myplayers3[-2] == "player2":
			# 		player.blindplayer2("small", bigblind)
			# 		table.mainPot(bigblind / 2)
			# 	elif myplayers3[-2] == "player3":
			# 		player.blindplayer3("small", bigblind)
			# 		table.mainPot(bigblind / 2)
			# 	elif myplayers3[-2] == "player4":
			# 		player.blindplayer4("small", bigblind)
			# 		table.mainPot(bigblind / 2)
			# 	elif myplayers3[-2] == "player5":
			# 		player.blindplayer5("small", bigblind)
			# 		table.mainPot(bigblind / 2)


			if "player1" in liveplayers:
				p1cards = deck.dealPlayer1()
				print("P1 Cards", p1cards)
				
			if "player2" in liveplayers:
				p2cards = deck.dealPlayer2()
				print("P2 Cards", p2cards)
				p2odds = hs.getAPI(len(liveplayers), p2cards, "")
				print("P2 Odds", p2odds)
				
			if "player3" in liveplayers:
				p3cards = deck.dealPlayer3()
				print("P3 Cards", p3cards)
				p3odds = hs.getAPI(len(liveplayers), p3cards, "")
				print("P3 Odds", p3odds)
				
			if "player4" in liveplayers:
				p4cards = deck.dealPlayer4()
				print("P4 Cards", p4cards)
				p4odds = hs.getAPI(len(liveplayers), p4cards, "")
				print("P4 Odds", p4odds)

			if "player5" in liveplayers:
				p5cards = deck.dealPlayer5()
				print("P5 Cards", p5cards)
				p5odds = hs.getAPI(len(liveplayers), p5cards, "")
				print("P5 Odds", p5odds)

			#Create ordered list of players, calculate odds and decisions as the list cycles through the player's cards
			p2refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "preflop"), hs.maxOdds(len(liveplayers), "preflop"), p2odds, tocall, playerclass.checkStash("player2"), "preflop", bigblind, len(liveplayers))
			p3refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "preflop"), hs.maxOdds(len(liveplayers), "preflop"), p3odds, tocall, playerclass.checkStash("player3"), "preflop", bigblind, len(liveplayers))
			p4refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "preflop"), hs.maxOdds(len(liveplayers), "preflop"), p4odds, tocall, playerclass.checkStash("player4"), "preflop", bigblind, len(liveplayers))
			p5refodds = ai.refineOdds(hs.minOdds(len(liveplayers), "preflop"), hs.maxOdds(len(liveplayers), "preflop"), p5odds, tocall, playerclass.checkStash("player5"), "preflop", bigblind, len(liveplayers))

			print(p2refodds, p3refodds, p4refodds, p5refodds)



			print("HS MAX ODDS", hs.maxOdds(len(liveplayers), "preflop"))
			print("HS MAX ODDS", hs.maxOdds(len(liveplayers), "postflop"))
			print("HS MIN ODDS", hs.minOdds(len(liveplayers), "preflop"))
			print("HS MIN ODDS", hs.minOdds(len(liveplayers), "postflop"))
			print("HS MIN ODDS", hs.minOdds(len(liveplayers), "postturn"))
			print("HS MIN ODDS", hs.minOdds(len(liveplayers), "postriver"))



			
			if "player1" in myplayers3:
				p1decision = str(input("Enter decision: "))
			if "player2" in myplayers3:
				p2decision = ai.aiDecision(p2refodds, p2pers)
			if "player3" in myplayers3:
				p3decision = ai.aiDecision(p3refodds, p3pers)
			if "player4" in myplayers3:
				p4decision = ai.aiDecision(p4refodds, p4pers)
			if "player5" in myplayers3:
				p5decision = ai.aiDecision(p5refodds, p5pers)

			print("P1", p1decision, "P2", p2decision, "P3", p3decision, "P4", p4decision, "P5", p5decision)

		deck.resetAccum()
		deck.forceShuffle()


































		table.moveDealer()
		#table.gameStatus()
main()