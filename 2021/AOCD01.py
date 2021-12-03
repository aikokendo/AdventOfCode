from classes.helper import Helper

def depthVariance(input):
    tot = 0
    for i in range(1,len(input)):
        if input[i] > input[i-1]:
            tot += 1
    return tot

def depthVariance3Measures(input):
    tot = 0
    for i in range(3,len(input)):
        if sum(input[i-2:i+1]) > sum(input[i-3:i]):
            tot += 1
    return tot


file_name = 'input\inputd01.txt'
my_file_data = Helper.read_file(file_name)

input = list(map(int,my_file_data.split('\n')))

print('Part 1 solution:', depthVariance(input))
print('Part 2 solution:', depthVariance3Measures(input))


#Part 1 solution: 1184
#Part 2 solution: 1158