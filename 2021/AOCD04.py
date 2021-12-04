from classes.helper import Helper
import copy

def generateValidCombinations(board):
    t_board = [list(i) for i in zip(*board)]
    return board + t_board

def callNumberAndCheckWinCondition(ExpandedBoards,num):
    WinConditionFound = False
    for EBoard in ExpandedBoards:
        for line in EBoard:
            if num in line:
                line.remove(num)
                if len(line) == 0:
                    WinConditionFound = True
    return WinConditionFound

def part1(numDrawn,boards):
    ExpandedBoards = []
    for board in boards:
        ExpandedBoards.append(generateValidCombinations(board))
    i = 0
    while not callNumberAndCheckWinCondition(ExpandedBoards, numDrawn[i]):
        i+=1
    for EBoard in ExpandedBoards:
        if [] in EBoard:
            return sum([int(x) for x in sum(EBoard[:5],[])]) * int(numDrawn[i])


def part2(numDrawn,boards):
    ExpandedBoards = []
    for board in boards:
        ExpandedBoards.append(generateValidCombinations(board))
    i = 0
    while i < len(numDrawn):
        if callNumberAndCheckWinCondition(ExpandedBoards,numDrawn[i]):
            if len(ExpandedBoards)>1:
                #We should discard every board that won this round
                indicesToPop = []
                for index, EBoard in enumerate(ExpandedBoards):
                    if [] in EBoard:
                        indicesToPop.append(index)
                ExpandedBoards = [x for ix, x in enumerate(ExpandedBoards) if ix not in indicesToPop]
            else:
                #We found our losing board winning move
                break
        i+=1
    return sum([int(x) for x in sum(ExpandedBoards[0][:5],[])]) * int(numDrawn[i])



file_name = 'input\inputd04.txt'
my_file_data = Helper.read_file(file_name)
input = my_file_data.split('\n')
NumDrawn = input[0].split(',')
boards = []
for i in range(len(input[1:])//6):
    boards.append([x.split() for x in input[2+i*6:7+i*6]])

print('Part 1 solution:', part1(NumDrawn,copy.deepcopy(boards)))
print('Part 2 solution:', part2(NumDrawn,copy.deepcopy(boards)))


