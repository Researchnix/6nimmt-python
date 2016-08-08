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
import Evaluation




if __name__ == "__main__":
    t = time.time()

    filename = "results.txt"

    master = GameMaster.GameMaster(filename)
    master.playGames(1000, verbose=False)

    eva = Evaluation.Evaluation()
    eva.loadData(filename)
    print "\n\nDone in " + str(time.time() - t) + " s"
    eva.showData(showPlot=False)
