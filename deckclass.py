import random

class Deck:
    def __init__(self):
        self.deck = []
        for val in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
            for suit in ["h", "c", "d", "s"]:
                self.deck.append(val + suit)

        self.players = ["player1", "player2", "player3", "player4", "player5"]
        print(self.players)
        self.shuffleCards()
        self.dealHands(self.players)
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



def main():
    Deck()
main()