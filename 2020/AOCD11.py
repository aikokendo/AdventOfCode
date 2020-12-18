from classes.helper import Helper
from classes.seatLayout import SeatLayout


def findEquilibrium(state, tolerance, deep = False):
    curState = state
    while True:
        newState = changeState(curState,tolerance,deep)
        if curState == newState:
            break
        curState = newState
    return curState


def changeState(state,tolerance,deep=False):
    w = len(state[0])
    h = len(state)
    newState = []

    for i in range(h):
        newRow = []
        for j in range(w):
            item = state[i][j]
            if item == '.':
                newRow.append('.')
            if item == 'L':
                if deep:
                    itemsAround = getItemsAroundUntilSeat(state,i,j)
                else:
                    itemsAround = getItemsAround(state,i,j)
                if '#' not in itemsAround:
                    newRow.append('#')
                else:
                    newRow.append('L')
            if item == '#':
                if deep:
                    itemsAround = getItemsAroundUntilSeat(state,i,j)
                else:
                    itemsAround = getItemsAround(state, i, j)
                if itemsAround.count('#')>=tolerance:
                    newRow.append('L')
                else:
                    newRow.append('#')

        newState.append(''.join(newRow))
    return newState


def getItemsAround(state,i,j):
    w = len(state[0])
    h = len(state)
    items = []
    if i > 0:
        items.append(state[i-1][j])
        if j > 0:
            items.append(state[i-1][j-1])
        if j < w - 1:
            items.append(state[i-1][j+1])
    if i < h-1:
        items.append(state[i+1][j])
        if j > 0:
            items.append(state[i + 1][j - 1])
        if j < w - 1:
            items.append(state[i + 1][j + 1])
    if j > 0:
        items.append(state[i][j-1])
    if j < w - 1:
        items.append(state[i][j+1])
    return items



def getItemsAroundUntilSeat(state,i,j):
    w = len(state[0])
    h = len(state)
    items = []
    n = 1
    while True:
        if i-1*n >= 0:
            if state[i-1*n][j] in ['L','#']:
                items.append(state[i-1*n][j])
                break
        else:
            items.append('/')
            break
        n += 1
    n = 1
    while True:
        if i-1*n >= 0 and j - 1*n >= 0:
            if state[i-1*n][j-1*n] in ['L','#']:
                items.append(state[i-1*n][j-1*n])
                break
        else:
            items.append('/')
            break
        n += 1
    n = 1
    while True:
        if i - 1 * n >= 0 and j+ 1*n < w:
            if state[i - 1 * n][j + 1 * n] in ['L', '#']:
                items.append(state[i - 1 * n][j + 1 * n])
                break
        else:
            items.append('/')
            break
        n += 1

    n = 1
    while True:
        if i + 1 * n < h:
            if state[i + 1 * n][j] in ['L', '#']:
                items.append(state[i + 1 * n][j])
                break
        else:
            items.append('/')
            break
        n += 1
    n = 1
    while True:
        if i + 1 * n < h and j - 1 * n >= 0:
            if state[i + 1 * n][j - 1 * n] in ['L', '#']:
                items.append(state[i + 1 * n][j - 1 * n])
                break
        else:
            items.append('/')
            break
        n += 1
    n = 1
    while True:
        if i + 1 * n < h and j + 1 * n < w:
            if state[i + 1 * n][j + 1 * n] in ['L', '#']:
                items.append(state[i + 1 * n][j + 1 * n])
                break
        else:
            items.append('/')
            break
        n += 1

    n = 1
    while True:
        if j - 1 * n >= 0:
            if state[i][j - 1 * n] in ['L', '#']:
                items.append(state[i][j - 1 * n])
                break
        else:
            items.append('/')
            break
        n += 1
    n = 1
    while True:
        if j + 1 * n < w:
            if state[i][j  + 1 * n] in ['L', '#']:
                items.append(state[i][j  + 1 * n])
                break
        else:
            items.append('/')
            break
        n += 1

    return items


#inputs
file_name = 'input\inputd11.txt'


file = Helper.read_file(file_name).split('\n')


print('Part 1 solution:', ''.join(findEquilibrium(file,4)).count('#'))
print('Part 2 solution:', ''.join(findEquilibrium(file,5,True)).count('#'))


sol1 = SeatLayout(file,4)
sol2 = SeatLayout(file,5,True)
print('Part 1 solution:', ''.join(sol1.findEquilibrium()).count('#'))
print('Part 2 solution:', ''.join(sol2.findEquilibrium()).count('#'))

