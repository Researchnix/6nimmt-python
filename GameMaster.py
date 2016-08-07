#
#  GameMaster.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import Deck
import LogWriter
import Field
import Player

class GameMaster:
    players = []
    field = Field.Field()
    roundCount = 0
    deck = Deck.Deck()
    loggy = LogWriter.LogWriter("results.txt")

    def initializePlayers(self):
        # Initialize the players
        p1 = Player.Player("Lennart")
        p2 = Player.Player("DaVinci")
        self.players.append(p1)
        self.players.append(p2)
        '''
        for p in self.players:
            print "Player " + p.name + " has on his hands "
            print p.hand
            print "\n\n"
        '''


    def initializeGame(self):
        """docstring for initializeGame, i.e the deck and the field,
            the players are still fields of this object
        """
        # Fill deck with cards and shuffle it
        self.deck.fill(104)
        self.deck.shuffle()
        #print "Deck initialized"

        # Initialize the field
        self.field.initialize(self.deck.draw(4))
        self.field.sortField()
        #self.field.printField()

        # Set players to initial state again
        # Distribute cards and set bulls to 0
        for p in self.players:
            p.bulls = 0
            p.setHand(self.deck.draw(10))



    def playRound(self):
        # Let every player play a card first to sort them
        dic = {}
        for p in range(len(self.players)):
            dic[self.players[p].playCard(self.field)] = p
        for playedCard in sorted(dic):
            player = self.players[dic[playedCard]]
            #print player.name + " played " + str(playedCard)
            attempt = self.field.addCard(playedCard)
            # A
            if attempt[0] == "added":
                continue
            # B
            elif attempt[0] == "sixNimmt":
                choice = attempt[1]
            # C
            elif attempt[0] == "noFit":
                choice = player.pickRow(self.field)
            else:
                print "something is wrong here"

            bulls = len(self.field.replaceRow(choice, playedCard))
            player.addBulls(bulls)
            self.field.sortField()

        # Get a quick overview of the current players status    
        #self.field.printField()
        #for p in self.players:
            #print p.name + " has " + str(p.bulls) + " bulls"
            #print p.hand

    def playRounds(self, n):
        for i in range(n):
            #print "############## ROUND " + str(i) +  " ##############"
            self.playRound()

    def playGames(self, n):
        # delete all results in the file
        self.loggy.delete()
        self.initializePlayers()
        for m in range(n):
            print " ########### Game " + str(m) + "  ########### "
            self.initializeGame()
            print "game initialized"
            self.playRounds(10)

            # save the results to a file
            results = {}
            for p in self.players:
                results[p.name] = p.bulls
            self.loggy.save(results)
            print results
            print '\n'
            
        
