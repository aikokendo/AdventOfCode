import helper
from seat import Seat

def parseFiletoSeats(file_data, rows, columns):
    bsp = file_data.split('\n')
    return [Seat(bsp, rows, columns) for bsp in bsp]

def findMySeat(seatChart):
    for i in range(1,len(seatChart)):
        if seatChart[i-1] + 2 == seatChart[i]:
            return seatChart[i-1] + 1

def everyoneSitDown(seats, rm, cm):
    return [s.getSeatId(rm, cm) for s in seats]


#inputs
file_name = 'input\inputd05.txt'
rows = 127
columns = 7
row_multiplier = 8
column_multiplier = 1

file = helper.read_file(file_name)
seats = parseFiletoSeats(file, rows, columns)

boardingPasses = everyoneSitDown(seats, row_multiplier, column_multiplier)
boardingPasses.sort()

print('Part 1 solution:', max(boardingPasses))
print('Part 2 solution:', findMySeat(boardingPasses))
