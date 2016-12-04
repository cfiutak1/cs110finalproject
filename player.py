import random

class Player:
    def __init__(self, players):
        #For debug
        print(len(players))

        self.players = players

        def checkBustOut(self,player):
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


        def player1(self, name, cards, AIflag):
            self.p1stash = stash
           


def main():
    playerclass = Player()
    startplayers = ["player1", "player2", "player3", "player4", "player5"]
    liveplayers = []
    roundplayers = []
    for player in startplayers:


    Player(startplayers)
main()