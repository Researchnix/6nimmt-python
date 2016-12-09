#
#  LogWriter.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import os

class LogWriter:
    """A class to store the outcome of a game"""
    filename = ""



    def setFilename(self, filename):
        self.filename = filename

    def delete(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass
        

    def save(self, dic):
        f = open(self.filename, 'a')
        s = ""
        for k in dic.keys():
            s += k + ' ' + str(dic[k]) + ' '
        s += '\n'
        f.write(s)
        f.close()

            
