from classes.helper import Helper

def GetNewSubset(input,rank,curindex,curSet):
    curSetRows = [input[index] for index in curSet]
    t_input = [list(i) for i in zip(*curSetRows)][curindex]
    int_i = [int(x) for x in t_input]
    curMax = rank[1]
    if (curSum:=sum(int_i)) == (half:=len(t_input)/2) or curSum > half:  #practicing walrus operators lol
        curMax = rank[0]
    return [curSet[index] for index,val in enumerate(curSetRows) if val[curindex] == curMax]

def FindLastStanding(input,rank):
    curSet = [i for i in range(len(input))]
    curi = 0
    while len(curSet)>1:
        curSet = GetNewSubset(input,rank,curi,curSet)
        curi += 1
    return curSet[0]

def CalculateLifeSupportRating(input):
    Oxygen = FindLastStanding(input,['1','0'])  #rank is in order of importance
    Co2 = FindLastStanding(input,['0','1'])
    return int(input[Oxygen],2) * int(input[Co2],2)

def CalculatePowerConsumption(input):
    #Transpose input, converting the columns to rows
    #Note: This wouldn't work if the inputs are not evenly sized.
    t_input = [list(i) for i in zip(*input)]
    gamma = []
    for i in t_input:
        int_i = [int(x) for x in i]
        if sum(int_i) > len(i)/2:
            gamma.append('1')
        else:
            gamma.append('0')
    epsilon = ['1' if x == '0' else '0' for x in gamma]
    return int(''.join(gamma),2) * int(''.join(epsilon),2)




file_name = 'input\inputd03.txt'
my_file_data = Helper.read_file(file_name)
input = my_file_data.split('\n')
print('Part 1 solution:', CalculatePowerConsumption(input))
print('Part 2 solution:', CalculateLifeSupportRating(input))


