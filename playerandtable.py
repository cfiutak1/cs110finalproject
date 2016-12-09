from datetime import datetime, timedelta

class Player:
	def __init__(self):
		self.p1betaccum = 0
		self.p2betaccum = 0
		self.p3betaccum = 0
		self.p4betaccum = 0
		self.p5betaccum = 0
		self.p1stash = 10000
		self.p2stash = 10000
		self.p3stash = 10000
		self.p4stash = 10000
		self.p5stash = 10000


	def checkBustOut(self, player):
		if player == "player1":
			if self.p1stash == 0:
				return "Bust"
			else:
				return "Alive"

		if player == "player2":
			if self.p2stash == 0:
				return "Bust"
			else:
				return "Alive"

		if player == "player3":
			if self.p3stash == 0:
				return "Bust"
			else:
				return "Alive"

		if player == "player4":
			if self.p4stash == 0:
				return "Bust"
			else:
				return "Alive"

		if player == "player5":
			if self.p5stash == 0:
				return "Bust"
			else:
				return "Alive"

	def player1(self, tocall, decision, bigblind):
		self.p1tocall = tocall
		self.p1decision = decision
		self.bigblind = bigblind
		#self.p1betaccum = 0
		

		if self.p1tocall >= self.p1stash:
			if self.p1decision == "Fold":
				return 0
			elif self.p1decision != "Fold":
				p1bet = self.p1stash
				self.p1stash = 0
				return p1bet

		if self.p1decision == "Fold":
			return 0

		elif self.p1decision == "Call":
			p1bet = int(self.p1tocall) - int(self.p1betaccum)
			self.p1stash -= p1bet
			self.p1betaccum += p1bet
			return p1bet

		elif self.p1decision == "Raise2BB":
			p1bet = (int(self.p1tocall) * 2)- int(self.p1betaccum)
			self.p1stash -= p1bet
			self.p1betaccum += p1bet
			return p1bet

		elif self.p1decision == "Raise3BB":
			p1bet = (int(self.p1tocall) * 3)- int(self.p1betaccum)
			self.p1stash -= p1bet
			self.p1betaccum += p1bet
			return p1bet

		elif self.p1decision == "RaisePot":
			p1bet = (int(self.p1tocall) * 5)- int(self.p1betaccum)
			self.p1stash -= p1bet
			self.p1betaccum += p1bet
			return p1bet

		elif self.p1decision == "AllIn":
			p1bet = self.p1stash
			self.p1stash = 0
			return p1bet

	def player2(self, tocall, decision, bigblind):

		self.p2tocall = tocall
		self.p2decision = decision
		self.bigblind = bigblind
		#self.p2betaccum = 0
		

		if self.p2tocall >= self.p2stash:
			if self.p2decision == "Fold":
				return 0
			elif self.p2decision != "Fold":
				p2bet = self.p2stash
				self.p2stash = 0
				return p2bet

		if self.p2decision == "Fold":
			return 0

		elif self.p2decision == "Call":
			p2bet = int(self.p2tocall) - int(self.p2betaccum)
			self.p2stash -= p2bet
			self.p2betaccum += p2bet
			return p2bet

		elif self.p2decision == "Raise2BB":
			p2bet = (int(self.p2tocall) * 2)- int(self.p2betaccum)
			self.p2stash -= p2bet
			self.p2betaccum += p2bet
			return p2bet

		elif self.p2decision == "Raise3BB":
			p2bet = (int(self.p2tocall) * 3)- int(self.p2betaccum)
			self.p2stash -= p2bet
			self.p2betaccum += p2bet
			return p2bet

		elif self.p2decision == "RaisePot":
			p2bet = (int(self.p2tocall) * 5)- int(self.p2betaccum)
			self.p2stash -= p2bet
			self.p2betaccum += p2bet
			return p2bet

		elif self.p2decision == "AllIn":
			p2bet = self.p2stash
			self.p2stash = 0
			return p2bet

	def player3(self, tocall, decision, bigblind):

		self.p3tocall = tocall
		self.p3decision = decision
		self.bigblind = bigblind
		#self.p3betaccum = 0
		

		if self.p3tocall >= self.p3stash:
			if self.p3decision == "Fold":
				return 0
			elif self.p3decision != "Fold":
				p3bet = self.p3stash
				self.p3stash = 0
				return p3bet

		if self.p3decision == "Fold":
			return 0

		elif self.p3decision == "Call":
			p3bet = int(self.p3tocall) - int(self.p3betaccum)
			self.p3stash -= p3bet
			self.p3betaccum += p3bet
			return p3bet

		elif self.p3decision == "Raise2BB":
			p3bet = (int(self.p3tocall) * 2)- int(self.p3betaccum)
			self.p3stash -= p3bet
			self.p3betaccum += p3bet
			return p3bet

		elif self.p3decision == "Raise3BB":
			p3bet = (int(self.p3tocall) * 3)- int(self.p3betaccum)
			self.p3stash -= p3bet
			self.p3betaccum += p3bet
			return p3bet

		elif self.p3decision == "RaisePot":
			p3bet = (int(self.p3tocall) * 5)- int(self.p3betaccum)
			self.p3stash -= p3bet
			self.p3betaccum += p3bet
			return p3bet

		elif self.p3decision == "AllIn":
			p3bet = self.p3stash
			self.p3stash = 0
			return p3bet

	def player4(self, tocall, decision, bigblind):
		self.p4tocall = tocall
		self.p4decision = decision
		self.bigblind = bigblind
		#self.p4betaccum = 0
		

		if self.p4tocall >= self.p4stash:
			if self.p4decision == "Fold":
				return 0
			elif self.p4decision != "Fold":
				p4bet = self.p4stash
				self.p4stash = 0
				return p4bet

		if self.p4decision == "Fold":
			return 0

		elif self.p4decision == "Call":
			p4bet = int(self.p4tocall) - int(self.p4betaccum)
			self.p4stash -= p4bet
			self.p4betaccum += p4bet
			return p4bet

		elif self.p4decision == "Raise2BB":
			p4bet = (int(self.p4tocall) * 2)- int(self.p4betaccum)
			self.p4stash -= p4bet
			self.p4betaccum += p4bet
			return p4bet

		elif self.p4decision == "Raise3BB":
			p4bet = (int(self.p4tocall) * 3)- int(self.p4betaccum)
			self.p4stash -= p4bet
			self.p4betaccum += p4bet
			return p4bet

		elif self.p4decision == "RaisePot":
			p4bet = (int(self.p4tocall) * 5)- int(self.p4betaccum)
			self.p4stash -= p4bet
			self.p4betaccum += p4bet
			return p4bet

		elif self.p4decision == "AllIn":
			p4bet = self.p4stash
			self.p4stash = 0
			return p4bet

	def player5(self, tocall, decision, bigblind):
		self.p5tocall = tocall
		self.p5decision = decision
		self.bigblind = bigblind
		#self.p5betaccum = 0
		

		if self.p5tocall >= self.p5stash:
			if self.p5decision == "Fold":
				return 0
			elif self.p5decision != "Fold":
				p5bet = self.p5stash
				self.p5stash = 0
				return p5bet

		if self.p5decision == "Fold":
			return 0

		elif self.p5decision == "Call":
			p5bet = int(self.p5tocall) - int(self.p5betaccum)
			self.p5stash -= p5bet
			self.p5betaccum += p5bet
			return p5bet

		elif self.p5decision == "Raise2BB":
			p5bet = (int(self.p5tocall) * 2)- int(self.p5betaccum)
			self.p5stash -= p5bet
			self.p5betaccum += p5bet
			return p5bet

		elif self.p5decision == "Raise3BB":
			p5bet = (int(self.p5tocall) * 3)- int(self.p5betaccum)
			self.p5stash -= p5bet
			self.p5betaccum += p5bet
			return p5bet

		elif self.p5decision == "RaisePot":
			p5bet = (int(self.p5tocall) * 5)- int(self.p5betaccum)
			self.p5stash -= p5bet
			self.p5betaccum += p5bet
			return p5bet

		elif self.p5decision == "AllIn":
			p5bet = self.p5stash
			self.p5stash = 0
			return p5bet


	def BBPlayer(self, player, bigblind):
		self.bigblind = bigblind
		if player == "player1":
			self.p1stash -= self.bigblind
			self.p1betaccum += self.bigblind
            

		if player == "player2":
			self.p2stash -= self.bigblind
			self.p2betaccum += self.bigblind
            

		if player == "player3":
			self.p3stash -= self.bigblind
			self.p3betaccum += self.bigblind
            

		if player == "player4":
			self.p4stash -= self.bigblind
			self.p4betaccum += self.bigblind
            

		if player == "player5": 
			self.p5stash -= self.bigblind
			self.p5betaccum += self.bigblind
            



	def SBPlayer(self, player, bigblind):
		self.bigblind = bigblind

		if player == "player1":
			self.p1stash -= self.bigblind // 2
			self.p1betaccum += self.bigblind // 2
            

		if player == "player2":
			self.p2stash -= self.bigblind // 2
			self.p2betaccum += self.bigblind // 2
            

		if player == "player3":
			self.p3stash -= self.bigblind // 2
			self.p3betaccum += self.bigblind // 2
            

		if player == "player4":
			self.p4stash -= self.bigblind // 2
			self.p4betaccum += self.bigblind // 2
            

		if player == "player5": 
			self.p5stash -= self.bigblind // 2
			self.p5betaccum += self.bigblind // 2
            

	def checkStash(self, player):
		if player == "player1":
			return self.p1stash

		elif player == "player2":
			return self.p2stash

		elif player == "player3":
			return self.p3stash

		elif player == "player4":
			return self.p4stash

		elif player == "player5":
			return self.p5stash

	def resetBets(self):
		self.p1betaccum = 0
		self.p2betaccum = 0
		self.p3betaccum = 0
		self.p4betaccum = 0
		self.p5betaccum = 0

	def award(self, player, amount):
		if player == "player1":
			self.p1stash += amount

		elif player == "player2":
			self.p2stash += amount

		elif player == "player3":
			self.p3stash += amount

		elif player == "player4":
			self.p4stash += amount

		elif player == "player5":
			self.p5stash += amount


class Table:
	def __init__(self):
		self.dealeraccum = 0
		self.roundaccum = 0
		self.mainpot = 0

	def blinds(self, bigblind, starttime, nowtime):
		self.bigblind = bigblind
		self.starttime = starttime
		self.nowtime = nowtime

		if self.nowtime < self.starttime + timedelta(minutes = 10):
			return int(bigblind)

		elif self.starttime + timedelta(minutes = 20) > self.nowtime >= self.starttime + timedelta(minutes = 10):
			return int(bigblind * 2)

		elif self.starttime + timedelta(minutes = 30) > self.nowtime >= self.starttime + timedelta(minutes = 20):
			return int(bigblind * 3)

		elif self.starttime + timedelta(minutes = 40) > self.nowtime >= self.starttime + timedelta(minutes = 30):
			return int(bigblind * 4)

		elif self.starttime + timedelta(minutes = 50) > self.nowtime >= self.starttime + timedelta(minutes = 40):
			return int(bigblind * 6)

		elif self.starttime + timedelta(minutes = 60) > self.nowtime >= self.starttime + timedelta(minutes = 50):
			return int(bigblind * 8)

		elif self.starttime + timedelta(minutes = 70) > self.nowtime >= self.starttime + timedelta(minutes = 60):
			return int(bigblind * 10)

		elif self.starttime + timedelta(minutes = 80) > self.nowtime >= self.starttime + timedelta(minutes = 70):
			return int(bigblind * 12)

		elif self.starttime + timedelta(minutes = 90) > self.nowtime >= self.starttime + timedelta(minutes = 80):
			return int(bigblind * 14)

		elif self.nowtime >= self.starttime + timedelta(minutes = 90):
			return int(bigblind * 20)



	def assignDealer(self, players):
		self.players = players

		if self.dealeraccum > (len(self.players) - 1):
			self.dealeraccum = 0
		return self.players[self.dealeraccum]



	def assignSB(self, players):
		if self.players[self.dealeraccum] == self.players[0]:
			return self.players[1]

		if self.players[self.dealeraccum] == self.players[-1]:
			return self.players[0]

		elif self.players[self.dealeraccum] == self.players[-2]:
			return self.players[-1]

		elif self.players[self.dealeraccum] == self.players[-3]:
			return self.players[-2]

		elif self.players[self.dealeraccum] == self.players[-4]:
			return self.players[-3]



	def assignBB(self, players):
		if self.players[self.dealeraccum] == self.players[0]:
			return self.players[2]

		if self.players[self.dealeraccum] == self.players[-1]:
			return self.players[1]

		elif self.players[self.dealeraccum] == self.players[-2]:
			return self.players[0]

		elif self.players[self.dealeraccum] == self.players[-3]:
			return self.players[-1]

		elif self.players[self.dealeraccum] == self.players[-4]:
			return self.players[-2]



	def moveDealer(self):
		self.dealeraccum += 1
		 


	def mainPot(self, bet):
		self.bet = bet
		self.mainpot += int(bet)


	def sidePot(self, bet):
		self.sidepot += bet


	def checkGameStatus(self, players, player1stash):
		if len(players) == 1 or player1stash <= 0:
			return "Over"
		else:
			return "InProgress"

	def roundStatus(self):
		if self.roundaccum == 0:
			return "preflop"
		if self.roundaccum == 1:
			return "postflop"
		elif self.roundaccum == 2:
			return "postturn"
		elif self.roundaccum == 3:
			return "postriver"

	def advanceRound(self):
		self.roundaccum += 1

	def resetRoundAccum(self):
		self.roundaccum = 0

	def getMainPot(self):
		return self.mainpot

	def resetMainPot(self):
		self.mainpot = 0
		
'''
DEBUG STUFF
AS OF 11:51 PM 12/8/16, I AM CURRENTLY A VERY SAD MAN

def main():
	table = Table()
	playerclass = Player()
	bigblind = 100
	tocall = bigblind
	print(table.getMainPot())
	liveplayers = ["player1", "player2", "player3", "player4", "player5"]
	myplayers3 = ["player3", "player4", "player5", "player1", "player2"]
	accum = 0
	count = 0

	while str(input("Is the game over?: ")) != "yes":
		while count == 0:
			#Applies big blind to player when they are two seats to the left of the dealer chip.
			for player in liveplayers:
				if myplayers3[-1] == "player1":
					playerclass.BBPlayer("player1", bigblind)
					table.mainPot(bigblind)

				elif myplayers3[-1] == "player2":
					playerclass.BBPlayer("player2", bigblind)
					table.mainPot(bigblind)
				elif myplayers3[-1] == "player3":
					playerclass.BBPlayer("player3", bigblind)
					table.mainPot(bigblind)
				elif myplayers3[-1] == "player4":
					playerclass.BBPlayer("player4", bigblind)
					table.mainPot(bigblind)
				elif myplayers3[-1] == "player5":
					playerclass.BBPlayer("player5", bigblind)
					table.mainPot(bigblind)

			#Applies small blind to player when they are one seat to the left of the dealer chip.
			for player in liveplayers:
				if myplayers3[-2] == "player1":
					playerclass.SBPlayer("player1", bigblind)
					table.mainPot(bigblind // 2)
				elif myplayers3[-2] == "player2":
					playerclass.SBPlayer("player2", bigblind)
					table.mainPot(bigblind // 2)
				elif myplayers3[-2] == "player3":
					playerclass.SBPlayer("player3", bigblind)
					table.mainPot(bigblind // 2)
				elif myplayers3[-2] == "player4":
					playerclass.SBPlayer("player4", bigblind)
					table.mainPot(bigblind // 2)
				elif myplayers3[-2] == "player5":
					playerclass.SBPlayer("player5", bigblind)
					table.mainPot(bigblind // 2)


			p1bet = playerclass.player1(100, "Call", bigblind)
			p2bet = playerclass.player2(100, "Call", bigblind)
			p3bet = playerclass.player3(100, "Call", bigblind)
			p4bet = playerclass.player4(100, "Call", bigblind)
			p5bet = playerclass.player5(100, "Call", bigblind)
			table.mainPot(p1bet)
			table.mainPot(p2bet)
			table.mainPot(p3bet)
			table.mainPot(p4bet)
			table.mainPot(p5bet)

			print("player1")
			print(playerclass.checkStash("player1"))
			print("player2")
			print(playerclass.checkStash("player2"))
			print("player3")
			print(playerclass.checkStash("player3"))
			print("player4")
			print(playerclass.checkStash("player4"))
			print("player5")
			print(playerclass.checkStash("player5"))


			print(table.getMainPot())
			print(accum)
			accum += 1
			if table.checkGameStatus(myplayers3, playerclass.checkStash("player1")) == "Over":
				count += 1

		print("It's finally over")
main()
'''
