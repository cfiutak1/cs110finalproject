from datetime import datetime, timedelta

class Player:
    def __init__(self):
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
        self.p1bet = 0
        self.bigblind = bigblind
        self.p1bet += self.tocall

        if self.p1tocall >= self.p1stash:
            if self.p1decision == "Fold":
                return 0
            elif self.p1decision != "Fold":
                return self.p1stash

        if self.p1decision == "Fold":
            return 0

        elif self.p1decision == "Call":
            self.p1stash -= self.p1bet
            return self.p1bet

        elif self.p1decision == "Raise2BB":
            self.p1stash -= self.p1bet * 2
            return self.p1bet * 2

        elif self.p1decision == "Raise3BB":
            self.p1stash -= self.p1bet * 3
            return self.p1bet * 3

        elif self.p1decision == "RaisePot":
            table = Table()
            if table.mainPot() <= (self.p1bet * 3):
                self.p1stash -= self.p1bet * 4
                return self.p1bet * 4
            else:
                self.p1stash -= table.mainPot()
                return table.mainPot()

        elif self.p1decision == "AllIn":
            return self.p1stash



    # def player2(self, tocall, decision, bigblind):
    #     self.p2tocall = tocall
    #     self.p2decision = decision
    #     self.p2bet = 0
    #     self.bigblind = bigblind

    #     if self.tocall >= self.p2stash:
    #         if self.p2decision == "Fold":
    #             return 0
    #         elif self.p2decision != "Fold":
    #             return self.p2stash

    #     if self.p2decision == "Fold":
    #         return 0

    #     elif self.p2decision == "Call":
    #         self.p2stash -= self.p2tocall
    #         return self.p2tocall

    #     elif self.p2decision == "Raise2BB":
    #         self.p2stash -= self.p2tocall * 2
    #         return self.p2tocall * 2

    #     elif self.p2decision == "Raise3BB":
    #         self.p2stash -= self.p2tocall * 3
    #         return self.p2tocall * 3

    #     elif self.p2decision == "RaisePot":
    #         table = Table()
    #         if table.mainPot() <= (self.p2tocall * 3):
    #             self.p2stash -= self.p2tocall * 4
    #             return self.p2tocall * 4
    #         else:
    #             self.p2stash -= table.mainPot()
    #             return table.mainPot()

    #     elif self.p2decision == "AllIn":
    #         return self.p2stash



    # def player3(self, tocall, decision, bigblind):
    #     self.p3tocall = tocall
    #     self.p3decision = decision
    #     self.p3bet = 0
    #     self.bigblind = bigblind

    #     if self.p3tocall >= self.p3stash:
    #         if self.p3decision == "Fold":
    #             return 0
    #         elif self.p3decision != "Fold":
    #             return self.p3stash

    #     if self.p3decision == "Fold":
    #         return 0

    #     elif self.p3decision == "Call":
    #         self.p3stash -= self.p3tocall
    #         return self.p3tocall

    #     elif self.p3decision == "Raise2BB":
    #         self.p3stash -= self.p3tocall * 2
    #         return self.p3tocall * 2

    #     elif self.p3decision == "Raise3BB":
    #         self.p3stash -= self.p3tocall * 3
    #         return self.p3tocall * 3

    #     elif self.p3decision == "RaisePot":
    #         table = Table()
    #         if table.mainPot() <= (self.p3tocall * 3):
    #             self.p3stash -= self.p3tocall * 4
    #             return self.p3tocall * 4
    #         else:
    #             self.p3stash -= table.mainPot()
    #             return table.mainPot()

    #     elif self.p3decision == "AllIn":
    #         return self.p3stash



    # def player4(self, tocall, decision, bigblind):
    #     self.p4tocall = tocall
    #     self.p4decision = decision
    #     self.p4bet = 0
    #     self.bigblind = bigblind

    #     if self.p4tocall >= self.p4stash:
    #         if self.p4decision == "Fold":
    #             return 0
    #         elif self.p4decision != "Fold":
    #             return self.p4stash

    #     if self.p4decision == "Fold":
    #         return 0

    #     elif self.p4decision == "Call":
    #         self.p4stash -= self.p4tocall
    #         return self.p4tocall

    #     elif self.p4decision == "Raise2BB":
    #         self.p4stash -= self.p4tocall * 2
    #         return self.p4tocall * 2

    #     elif self.p4decision == "Raise3BB":
    #         self.p4stash -= self.p4tocall * 3
    #         return self.p4tocall * 3

    #     elif self.p4decision == "RaisePot":
    #         table = Table()
    #         if table.mainPot() <= (self.p4tocall * 3):
    #             self.p4stash -= self.p4tocall * 4
    #             return self.p4tocall * 4
    #         else:
    #             self.p4stash -= table.mainPot()
    #             return table.mainPot()

    #     elif self.p4decision == "AllIn":
    #         return self.p4stash

    # def player5(self, tocall, decision, bigblind):
    #     self.p5tocall = tocall
    #     self.p5decision = decision
    #     self.p5bet = 0
    #     self.bigblind = bigblind

    #     if self.p5tocall >= self.p5stash:
    #         if self.p5decision == "Fold":
    #             return 0
    #         elif self.p5decision != "Fold":
    #             return self.p5stash

    #     if self.p5decision == "Fold":
    #         return 0

    #     elif self.p5decision == "Call":
    #         self.p5stash -= self.p5tocall
    #         return self.p5tocall

    #     elif self.p5decision == "Raise2BB":
    #         self.p5stash -= self.p5tocall * 2
    #         return self.p5tocall * 2

    #     elif self.p5decision == "Raise3BB":
    #         self.p5stash -= self.p5tocall * 3
    #         return self.p5tocall * 3

    #     elif self.p5decision == "RaisePot":
    #         table = Table()
    #         if table.mainPot() <= (self.p5tocall * 3):
    #             self.p5stash -= self.p5tocall * 4
    #             return self.p5tocall * 4
    #         else:
    #             self.p5stash -= table.mainPot()
    #             return table.mainPot()

    #     elif self.p5decision == "AllIn":
    #         return self.p5stash



    def BBPlayer(self, player, bigblind):
        if self.bbplayer == "player1":
            self.p1stash -= self.bigblind
            self.p1bet -= self.bigblind
            

        if self.bbplayer == "player2":
            self.p2stash -= self.bigblind
            self.p2bet -= self.bigblind
            

        if self.bbplayer == "player3":
            self.p3stash -= self.bigblind
            self.p3bet -= self.bigblind
            

        if self.bbplayer == "player4":
            self.p4stash -= self.bigblind
            self.p4bet -= self.bigblind
            

        if self.bbplayer == "player5": 
            self.p5stash -= self.bigblind
            self.p5bet -= self.bigblind
            



    def SBPlayer(self, player, bigblind):
        self.bigblind = bigblind

        if player == "player1":
            self.p1stash -= self.bigblind / 2
            self.p1bet -= self.bigblind / 2
            

        if player == "player2":
            self.p2stash -= self.bigblind / 2
            self.p2bet -= self.bigblind / 2
            

        if player == "player3":
            self.p3stash -= self.bigblind / 2
            self.p3bet -= self.bigblind / 2
            

        if player == "player4":
            self.p4stash -= self.bigblind / 2
            self.p4bet -= self.bigblind / 2
            

        if player == "player5": 
            self.p5stash -= self.bigblind / 2
            self.p5bet -= self.bigblind / 2
            

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



class Table:
	def __init__(self):
		self.dealeraccum = 0
		self.mainpot = 0
		self.roundaccum = 0

	def blinds(self, bigblind, starttime, nowtime):
		self.bigblind = bigblind
		self.starttime = starttime
		self.nowtime = nowtime

		if self.nowtime < self.starttime + timedelta(minutes = 1):
			return int(bigblind)

		elif self.starttime + timedelta(minutes = 2) > self.nowtime >= self.starttime + timedelta(minutes = 1):
			return int(bigblind * 2)

		elif self.starttime + timedelta(minutes = 3) > self.nowtime >= self.starttime + timedelta(minutes = 2):
			return int(bigblind * 3)

		elif self.starttime + timedelta(minutes = 4) > self.nowtime >= self.starttime + timedelta(minutes = 3):
			return int(bigblind * 4)

		elif self.starttime + timedelta(minutes = 5) > self.nowtime >= self.starttime + timedelta(minutes = 4):
			return int(bigblind * 6)

		elif self.starttime + timedelta(minutes = 6) > self.nowtime >= self.starttime + timedelta(minutes = 5):
			return int(bigblind * 8)

		elif self.starttime + timedelta(minutes = 7) > self.nowtime >= self.starttime + timedelta(minutes = 6):
			return int(bigblind * 10)

		elif self.starttime + timedelta(minutes = 8) > self.nowtime >= self.starttime + timedelta(minutes = 7):
			return int(bigblind * 12)

		elif self.starttime + timedelta(minutes = 9) > self.nowtime >= self.starttime + timedelta(minutes = 8):
			return int(bigblind * 14)

		elif self.nowtime >= self.starttime + timedelta(minutes = 9):
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
		self.mainpot += self.bet



	def sidePot(self, bet):
		self.bet = bet
		self.sidepot += self.bet


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


		
'''
def main():
	table = Table()
	# playerclass = Player()
	starttime = datetime.now()
	players = ["player1","player2", "player3", "player4", "player5"]

	while str(input("Over?: ")) != "yes":
		nowtime = datetime.now()

		bigblind = table.blinds(100, starttime, nowtime)
		print("BIG BLIND", bigblind, ";", "SMALL BLIND", bigblind/2)
		print(table.assignDealer(players))
		print(table.assignSB(players))
		print(table.assignBB(players))
		

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
		# print("Check stash", playerclass.checkStash("player1"))
		# playerclass.BBPlayer("player1", bigblind)
		# print("Check stash", playerclass.checkStash("player1"))
		# print(table.retMainPot())
		table.moveDealer()

main()
'''