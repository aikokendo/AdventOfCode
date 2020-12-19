from classes.helper import Helper


def calculatePosition(initPos, instructions):
    vertical = initPos[0]
    horizontal = initPos[1]
    actions = {'N': [1, 0], 'S': [-1, 0], 'E': [0, 1], 'W': [0, -1]}
    rotations = {'L':-1,'R':1}
    newFrontCalc = {0:[0,1],90:[-1,0],180:[0,-1],270:[1,0]}
    curDegree = 0
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action in actions.keys():
            direction = actions[action]
            vertical += value * direction[0]
            horizontal += value * direction[1]
        if action in rotations.keys():
            curDegree += value * rotations[action]
            curDegree = curDegree % 360
        if action == 'F':
            direction = newFrontCalc[curDegree]
            vertical += value * direction[0]
            horizontal += value * direction[1]
    return [vertical,horizontal]


def calculatePositionWithWaypoint(initPos, initWayPoint, instructions):
    wayPointVertical = initWayPoint[0]
    wayPointHorizontal = initWayPoint[1]
    boatVertical = initPos[0]
    boatHorizontal = initPos[1]
    actions = {'N': [1, 0], 'S': [-1, 0], 'E': [0, 1], 'W': [0, -1]}
    rotations = {'L':-1,'R':1}
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action in actions.keys():
            direction = actions[action]
            wayPointVertical += value * direction[0]
            wayPointHorizontal += value * direction[1]
        if action in rotations.keys():
            for rotation in range(int(value // 90)):
                temp = wayPointHorizontal * rotations[action]
                wayPointHorizontal = wayPointVertical * rotations[action]
                wayPointVertical = -1 * temp
        if action == 'F':
            boatVertical += value * wayPointVertical
            boatHorizontal += value * wayPointHorizontal
    return [boatVertical,boatHorizontal]


def manhattanDistance(initPos,finalPos):
    return abs(initPos[0] - finalPos[0]) + abs(initPos[1] - finalPos[1])

# inputs
file_name = 'input\inputd12.txt'

file = Helper.read_file(file_name).split('\n')
initPos = [0,0]
newPos = calculatePosition(initPos,file)

print('Part 1 solution:', manhattanDistance(initPos,newPos))

initPos = [0, 0]
initWayPoint = [1, 10]
newPos = calculatePositionWithWaypoint(initPos, initWayPoint, file)
print('Part 2 solution:', manhattanDistance(initPos,newPos))
