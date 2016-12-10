#
#  Field.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

class Field:
    """The field of cards on the table"""
    cards = []
    
    
    
    def initialize(self, initValues):
        self.cards = []
        for e in initValues:
            self.cards.append([e])

    def printField(self):
        print "The current field is "
        for row in self.cards:
            print row


    def sortField(self):
        def compare(x, y):
            try:
                return y[-1] - x[-1]
            except IndexError:
                return -1
        self.cards = sorted(self.cards, cmp=compare)
            
    # Try to add the single number n to the row r
    def tryToAdd(self, r, n):
       # The last entry of the row might be too big
       if self.cards[r][-1] > n:
           return "greater, move on to next row"
       # Only if this is not the case,
       # it is relevant to check whether the row r might be too long
       elif len(self.cards[r]) >= 5:
           return "full"
       # Otherwise we can add the n to the row
       else:
           self.cards[r].append(n)
           self.sortField()
           return "fit"

    '''
        There are three possible cases:
            A)  the card was added successully, all good
            B)  the card can not be added and the current player has to take a specific row of cards
            C)  the card can not be added and the current player can pick a row
    '''
    def addCard(self, c):
        """docstring for addCard"""
        for row in range(4):
            ans = self.tryToAdd(row,c)
            # print ans
            # Case A, everything is fine, move on with your life!
            if  ans == "fit":
                return ("added", 0)
            # Case B, make the player pick up this specific row
            elif ans == "full":
                #print "found a fit, but the row is to full"
                return ("sixNimmt", row)
        # Case C, the current player has to pick a row
        #print "All rows are incompatible"
        return ("noFit", 0)
        
    def replaceRow(self, row, c):
        self.cards.append([c])
        return self.cards.pop(row)
