import re
import math
class Seat:
    def __init__(self,BSP, rows, columns):
        self.location = self.maskBSP(BSP)
        self.row = self.findPos(self.location[0], 0, rows)
        self.column = self.findPos(self.location[1], 0, columns)

    def getPos(self):
        return [self.row,self.column]

    def getSeatId(self, rm = 1, cm = 1):
        return (self.row * rm) + (self.column * cm)

    def maskBSP(self,BSP):
        location = re.findall(r"[FB]+|[LR]+", BSP)
        location = [re.sub('[FL]', '0', l) for l in location]
        location = [re.sub('[BR]', '1', l) for l in location]
        return location

    def findPos(self,BSP,start,end):
        mid = math.trunc((start+end)/2)
        if len(BSP)>0:
            if BSP[0] == '0': # get first half
                end = mid
            else: # get second half
                start = mid + 1
            return self.findPos(BSP[1:],start,end)
        return start