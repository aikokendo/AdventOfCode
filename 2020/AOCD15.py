from classes.helper import Helper

# inputs
file_name = 'input\inputd15.txt'

def memoryGame(file,nth):
    memory = {}
    prevStepNum = 0
    prevStepNth = 0
    n = 0
    while True:
        n += 1
        if n <= len(file):
            if n > 1:
                memory[prevStepNum] = prevStepNth
            prevStepNum = file[n-1]
            prevStepNth = n
        else:
            #find if number has been said
            if prevStepNum in memory.keys():
                newNum = prevStepNth - memory[prevStepNum]
                memory[prevStepNum] = prevStepNth
                prevStepNth = n
                prevStepNum = str(newNum)
            else:
                memory[prevStepNum] = prevStepNth
                prevStepNum = '0'
                prevStepNth = n
        if n == nth:
            return prevStepNum


file = Helper.read_file(file_name).split(',')

nth = 2020
print('Part 1 solution:', memoryGame(file,nth))

nth = 30000000
print('Part 1 solution:', memoryGame(file,nth))



