class SeatLayout:
    def __init__(self, state, tolerance, deep = False,noSeat = '.',emptySeat = 'L',occupiedSeat = '#'):
        self.state = state
        self.tolerance = tolerance
        self.deep = deep
        self.noSeat = noSeat
        self.emptySeat = emptySeat
        self.occupiedSeat = occupiedSeat

    def changeState(self):
        w = len(self.state[0])
        h = len(self.state)
        newState = []

        for i in range(h):
            newRow = []
            for j in range(w):
                item = self.state[i][j]
                if item == self.noSeat:
                    newRow.append(self.noSeat)
                if item == self.emptySeat:
                    itemsAround = self.getItemsAroundBasedOnDepth(i, j)
                    if self.occupiedSeat not in itemsAround:
                        newRow.append(self.occupiedSeat)
                    else:
                        newRow.append(self.emptySeat)
                if item == self.occupiedSeat:
                    itemsAround = self.getItemsAroundBasedOnDepth(i, j)
                    if itemsAround.count(self.occupiedSeat) >= self.tolerance:
                        newRow.append(self.emptySeat)
                    else:
                        newRow.append(self.occupiedSeat)

            newState.append(''.join(newRow))
        return newState

    def findSeatInDirection(self,i,j,v,h):
        width = len(self.state[0]) - 1
        height = len(self.state) - 1
        n = 1
        while True:
            newi = i + v * n
            newj = j + h * n
            if (newi >= 0) and (newi <= height) and newj >= 0 and newj <= width:
                if self.state[newi][newj] in [self.emptySeat,self.occupiedSeat]:
                    return self.state[newi][newj]
            else:
                return '/'
            if not self.deep:
                return '/'
            n += 1


    def getItemsAroundBasedOnDepth(self, i, j):
        w = len(self.state[0])
        h = len(self.state)
        items = []
        items.append(self.findSeatInDirection(i, j, -1, 0))
        items.append(self.findSeatInDirection(i, j, -1, -1))
        items.append(self.findSeatInDirection(i, j, -1, +1))
        items.append(self.findSeatInDirection(i, j, +1, 0))
        items.append(self.findSeatInDirection(i, j, +1, -1))
        items.append(self.findSeatInDirection(i, j, +1, +1))
        items.append(self.findSeatInDirection(i, j, 0, -1))
        items.append(self.findSeatInDirection(i, j, 0, +1))
        return items

    def findEquilibrium(self):
        savedState = self.state
        while True:
            newState = self.changeState()
            if self.state == newState:
                break
            self.state = newState
        self.state = savedState
        return newState