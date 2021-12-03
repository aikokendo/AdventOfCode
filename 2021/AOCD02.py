from classes.helper import Helper


def CalculateNewPosWithAim(input):
    h = 0
    d = 0
    aim = 0
    for i in input:
        instruction,value = i.split()
        value = int(value)
        if instruction == 'forward':
            h += value
            d += aim * value
        elif instruction == 'down':
            aim += value
        else:
            aim -= value
    return h * d

def CalculateNewPos(input):
    h = 0
    d = 0
    for i in input:
        instruction,value = i.split()
        value = int(value)
        if instruction == 'forward':
            h += value
        elif instruction == 'down':
            d += value
        else:
            d -= value
    return h * d



file_name = 'input\inputd02.txt'
my_file_data = Helper.read_file(file_name)

input = my_file_data.split('\n')

print('Part 1 solution:', CalculateNewPos(input))
print('Part 2 solution:', CalculateNewPosWithAim(input))


