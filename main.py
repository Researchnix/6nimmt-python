#
#  main.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import sys
import time

import Deck
import GameMaster
import Field
import LogWriter




if __name__ == "__main__":
    t = time.time()


    master = GameMaster.GameMaster("results.txt")
    master.playGames(100)


    """
    f = Field.Field()
    f.initialize([10,20,30,40])
    f.printField()
    print f.addCard(84)
    f.printField()
    print f.addCard(85)
    f.printField()
    print f.addCard(86)
    f.printField()
    print f.addCard(87)
    f.printField()
    print f.addCard(28)
    f.printField()
    """



    print "\n\nDone in " + str(time.time() - t) + " s"
