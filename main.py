#
#  main.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#
#  Now everything is back to normal
#  This time it seems to work just fine.
#  So the trick is to close the Gstatus window before typing :Gpush
#  Yes, indeed!

import sys
import time

from game import *
from utils import *

if __name__ == "__main__":
    t = time.time()

    filename = "results.txt"

    master = GameMaster.GameMaster(filename)
    master.playGames(10000, verbose=False)

    eva = Evaluation.Evaluation()
    eva.loadData(filename)
    print "\n\nDone in " + str(time.time() - t) + " s"
    eva.showData(showPlot=True)
