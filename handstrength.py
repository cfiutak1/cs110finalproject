import json
import requests




class handStrength:
    #default amount of players
    players = 5
    #gets info from the api and takes the odds value
    def getAPI(self,players,hand,board):
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
    def player1(self,players,hand,board):
        print("Player one odds: "+str(self.getOdds(players,hand,board)))
    #calls odds for player2
    def player2(self,players,hand,board):
        print("Player two odds: "+str(self.getOdds(players,hand,board)))
    #calls odds for player3
    def player3(self,players,hand,board):
        print("Player three odds: "+str(self.getOdds(players,hand,board)))
    #calls odds for player4
    def player4(self,players,hand,board):
        print("Player four odds: "+str(self.getOdds(players,hand,board)))
    #calls odds for player5
    def player5(self,players,hand,board):
        print("Player five odds: "+str(self.getOdds(players,hand,board)))
    def findWinner(self,hands,board):
        winnerUrl = 'http://stevenamoore.me/projects/holdemapi/?cards='+hands+'&board='+board
        holder = requests.get(winnerUrl)
        api = holder.json()
        winner = ""
        cards = api['cards']
        if "-" not in cards:
            print("The winner's cards are: " + cards[:4])
        else:
            print("There is a tie between: " + cards[:4] + " and " + cards[15:19])
    #test values for now, this calls every method
    def callMethods(self):
        self.player1(self.players,"KsAs","4s8c4h")
        self.player2(self.players,"Ts5h","4s8c4h")
        self.player3(self.players,"9cJc","4s8c4h")
        self.player4(self.players,"AhQc","4s8c4h")
        self.player5(self.players,"4c8s","4s8c4h")
        #winner test
        self.findWinner("KsAsTs5h9cJcAhQc4c8s","4s8c4hAd5c")
        #tie test
        self.findWinner("KsAsTs5h9cJcAhQc4c8s","AcAd3h3d6s")


def main():
    odds = handStrength()
    odds.callMethods()
main()
