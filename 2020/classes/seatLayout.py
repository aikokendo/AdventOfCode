class SeatLayout:
    def __init__(self, state, tolerance, deep = False):
        self.state = state
        self.tolerance = tolerance
        self.deep = deep

    def changeState(self):
        w = len(self.state[0])
        h = len(self.state)
        newState = []

        for i in range(h):
            newRow = []
            for j in range(w):
                item = self.state[i][j]
                if item == '.':
                    newRow.append('.')
                if item == 'L':
                    itemsAround = self.getItemsAroundBasedOnDepth(i, j)
                    if '#' not in itemsAround:
                        newRow.append('#')
                    else:
                        newRow.append('L')
                if item == '#':
                    itemsAround = self.getItemsAroundBasedOnDepth(i, j)
                    if itemsAround.count('#') >= self.tolerance:
                        newRow.append('L')
                    else:
                        newRow.append('#')

            newState.append(''.join(newRow))
        return newState


    def getItemsAroundBasedOnDepth(self, i, j):
        w = len(self.state[0])
        h = len(self.state)
        items = []
        n = 1
        while True:
            if i - 1 * n >= 0:
                if self.state[i - 1 * n][j] in ['L', '#']:
                    items.append(self.state[i - 1 * n][j])
                    break
            else:
                break
            if not self.deep:
                break
            n += 1
        n = 1
        while True:
            if i - 1 * n >= 0 and j - 1 * n >= 0:
                if self.state[i - 1 * n][j - 1 * n] in ['L', '#']:
                    items.append(self.state[i - 1 * n][j - 1 * n])
                    break
            else:
                break
            if not self.deep:
                break
            n += 1
        n = 1
        while True:
            if i - 1 * n >= 0 and j + 1 * n < w:
                if self.state[i - 1 * n][j + 1 * n] in ['L', '#']:
                    items.append(self.state[i - 1 * n][j + 1 * n])
                    break
            else:
                break
            if not self.deep:
                break
            n += 1

        n = 1
        while True:
            if i + 1 * n < h:
                if self.state[i + 1 * n][j] in ['L', '#']:
                    items.append(self.state[i + 1 * n][j])
                    break
            else:
                break
            if not self.deep:
                break
            n += 1
        n = 1
        while True:
            if i + 1 * n < h and j - 1 * n >= 0:
                if self.state[i + 1 * n][j - 1 * n] in ['L', '#']:
                    items.append(self.state[i + 1 * n][j - 1 * n])
                    break
            else:
                break
            if not self.deep:
                break
            n += 1
        n = 1
        while True:
            if i + 1 * n < h and j + 1 * n < w:
                if self.state[i + 1 * n][j + 1 * n] in ['L', '#']:
                    items.append(self.state[i + 1 * n][j + 1 * n])
                    break
            else:
                break
            if not self.deep:
                break
            n += 1

        n = 1
        while True:
            if j - 1 * n >= 0:
                if self.state[i][j - 1 * n] in ['L', '#']:
                    items.append(self.state[i][j - 1 * n])
                    break
            else:
                break
            if not self.deep:
                break
            n += 1
        n = 1
        while True:
            if j + 1 * n < w:
                if self.state[i][j + 1 * n] in ['L', '#']:
                    items.append(self.state[i][j + 1 * n])
                    break
            else:
                break
            if not self.deep:
                break
            n += 1

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