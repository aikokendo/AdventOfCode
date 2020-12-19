from classes.helper import Helper
from classes.seatLayout import SeatLayout

#inputs
file_name = 'input\inputd11.txt'

file = Helper.read_file(file_name).split('\n')

sol1 = SeatLayout(file,4)
sol2 = SeatLayout(file,5,True)
print('Part 1 solution:', ''.join(sol1.findEquilibrium()).count('#'))
print('Part 2 solution:', ''.join(sol2.findEquilibrium()).count('#'))

