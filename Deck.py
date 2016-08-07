#
#  Deck.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

from random import randint

class Deck:
    """A deck of cards"""
    content = []
    
    def fill(self, num):
        self.content = range(1, num + 1)
    
    def draw(self, num):
        result = self.content[:num]
        self.content = self.content[num:]
        return result

    def shuffle(self):
        for e in range(10*len(self.content)):
            a = randint(0,len(self.content)-1)
            n = self.content.pop(a)
            self.content.append(n)
