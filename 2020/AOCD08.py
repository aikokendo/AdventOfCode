from classes.helper import Helper
from classes.machine import Machine
import copy

def parseToCode(file):
    return [c.split() for c in file.split('\n')]

def fixLoop(machine, code):
    for i, line in enumerate(code):
        if line[0] in ['nop','jmp']:
            newCode = copy.deepcopy(code)
            newCode[i][0] = 'nop' if line[0] == 'jmp' else 'jmp'
            if machine.canStart(newCode):
                return newCode

#inputs
file_name = 'input\inputd08.txt'

file = Helper.read_file(file_name)
code = parseToCode(file)

machine = Machine()
machine.canStart(code)
print('Part 1 solution:', machine.getAcc())

fixedCode = fixLoop(machine, code)
if fixedCode is not None:
    machine.canStart(fixedCode)
    print('Part 2 solution:', machine.getAcc())
else:
    print('Part 2 solution: - error - ')
