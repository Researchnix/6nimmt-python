#
#  Player.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

class Player:
    """Class for a player"""
    name = "Player"
    bulls = 0
    hand = []

    def __init__(self, name):
        self.name = name

    def setName(self, n):
        self.name = n

    def addToHand(self, cards):
        self.hand = self.hand + cards

    def setHand(self, cards):
        self.hand = cards

    def addBulls(self, n):
        self.bulls += n

    """ These are the two functions that you have to implement """

    # Only a dummy function for now
    # Choose a card from your hand to play
    def playCard(self, field):
        return self.hand.pop()

    # Another dummy function for now
    # If you have to pick up a row, you can choose any row
    def pickRow(self, field):
        return 0
