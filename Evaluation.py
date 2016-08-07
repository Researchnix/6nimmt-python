#
#  Evaluation.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

class Evaluation:
    n = 0
    players = []
    data = []

    def evaluate(self, filename):
        self.loadData(filename)


    def loadData(self, filename):
        f = open(filename, "r")
        content = f.readlines()
        line = content[0].split()
        # Collect the names of all players
        for e in line:
            if type(e) is str:
                self.players.append(e)

        # parse the results of each game (=each line) in data
        for l in content:
            l = l.split()
            row = []
            for m in l:
                if type(m) is str:
                    row.append(m)
            self.data.append(row)
