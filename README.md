# 6nimmt-python

  README.md
  6nimmt

  Created by Lennart Doppenschmitt on 2016-08-06.
  Copyright 2016 Researchnix. All rights reserved.



This is again an implementation of the board game 6nimmt, this time in python. Most people are probably more familiar with python and if I decide to play around with machine learning, it is easier to experiment with tensorFlow and other things in python.

#How to code a player for this game

If you want to implement your own player for this game, all you need to do is:

1) Write a derived class to the base class Player

2) Import your class in Gamemaster.py

3) Change the function 'initializePlayers' in GameMaster.py line 21 by adding an instance of your class as a new player

            p3 = Myplayer.Myplayer("YOUR_NAME")

            self.players.append(p3)


Then execute 'make' and find the resulting score in the file 'results.txt'.
Feel free to play around and modify other bits and pieces of the code.
