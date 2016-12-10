#
#  Fabian.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import Player

class Lennart(Player.Player):
    tolerance = 0

    def __init__(self, name, tolerance):
        self.name = name
        self.tolerance = tolerance
    
    def playCard(self, field):
        # Dictionary between end values and their index
        # TODO sort out by length of row, len=5 is obviously bad
        endValues = {}
        for e in range(len(field.cards)):
            if field.cards[e] < self.tolerance:
                endValues[field.cards[e][-1]] = e

        # Find the difference btw every 'endValue' in a 
        # row and the next higher card on the hand
        closeCards = {}
        for v in endValues.keys():
            higherHandCards = [c for c in self.hand if v < c]
            if len(higherHandCards) != 0:
                closeCards[v] = -min(higherHandCards)
        # Now find the difference
        diffs = [abs(sum(x)) for x in zip(closeCards.values(), closeCards.keys())]
        if len(diffs) == 0:
            return self.hand.pop()
        else:
            indexBestFit = diffs.index(min(diffs))
            closestValue = closeCards.keys()[indexBestFit]
            return endValues[closestValue]

    def pickRow(self, field):
        m = map(len,field.cards)
        return m.index(min(m))
