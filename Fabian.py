#
#  Fabian.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import Player

class Fabian(Player.Player):
    
    def playCard(self, field):
        self.bulls = 10000
        return self.hand.pop()
