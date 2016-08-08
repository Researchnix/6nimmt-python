#
#  Evaluation.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

#from pylab import *
import matplotlib.pyplot as plt

class Evaluation:
    n = 0
    players = []
    data = []
    winner = []
    chart = []
    cumulativeChart = []

    def evaluate(self, filename):
        self.loadData(filename)


    def loadData(self, filename):
        f = open(filename, "r")
        content = f.readlines()
        line = content[0].split()

        # Collect the names of all players
        # They are at the even entries of line
        for i in range(int(0.5 * len(line))):
            self.players.append(line[2 * i])

        self.n = len(self.players)
        # parse the results of each game (=each line) in data,
        # this time only the odd indexed entries
        for l in content:
            l = l.split()
            row = []
            for j in range(int(0.5 * len(line))):
                row.append(int(l[2*j+1]))
            self.data.append(row)

    def findWinner(self):
        for e in self.data:
            self.winner.append(e.index(max(e)))

    def basisVector(self, n, i):
        result = [0 for j in range(n)]
        result[i] = 1
        return result


    def makeChart(self):
        for i in self.winner:
            row = self.basisVector(self.n,i)
            self.chart.append(row)
        self.chart = self.tr(self.chart)

        # Make cumulative chart
        for pl in self.chart:
            self.cumulativeChart.append(self.cumSum(pl))



    def cumSum(self, a):
        for i in range(1, len(a)):
            a[i] += a[i-1]
        return a





    def showData(self, showPlot=False):
        trata = self.tr(self.data)
        self.findWinner()
        self.makeChart()
        print "Total number of wins:\n"
        for j in range(self.n):
            print self.players[j] + " has won " + str(self.winner.count(j)) + " times"
        #y = trata[0]
        #y = self.chart[0]
        plt.subplot(111)
        plt.title("Evaluation of 6nimmt")
        plt.xlabel("Number of played games")
        plt.ylabel("Number of games won (cumulative sum)")
        for j in range(self.n):
            plt.plot(range(len(self.cumulativeChart[j])), self.cumulativeChart[j], label= self.players[j])
        plt.legend()
        if showPlot:
            plt.show()
        else:
            plt.savefig("results.png")


    # The transpose of a list of lists
    def tr(self, a):
        b = []
        n = len(a[0])
        for j in range(n):
            b.append([])
        for j in range(n):
            for elem in a:
                b[j].append(elem[j])
        return b

