#
#  Evaluation.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

class Evaluation:
    n = 0
    players = {}
    data = []

    def evaluate(self, filename):
        self.loadData(filename)


    def loadData(self, filename):
        with open(filename, "r") as f:
            for line in f:
                line = line.split()
