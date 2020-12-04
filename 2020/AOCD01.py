import helper

def findSumSol1(expReport, tot):
    expReport.sort()
    for i in range(0,len(expReport)):
        if expReport[i] * 2 >tot:
            break
        for j in range(i+1, len(expReport)):
                if expReport[i] + expReport[j] == tot:
                    return [expReport[i],expReport[j]]
    return [0,0]

def findSumSol2(expReport, tot):
    expReport.sort()
    for i in range(0,len(expReport)):
        if expReport[i]>tot:
            break
        for j in range(i+1, len(expReport)):
            if expReport[i] + (expReport[j]*2) > tot:
                break
            for k in range(j+1,len(expReport)):
                if expReport[i] + expReport[j] + expReport[k] == tot:
                    return [expReport[i],expReport[j],expReport[k]]
    return [0,0,0]


file_name = 'input\inputd01.txt'
my_file_data = helper.read_file(file_name)

expReport = list(map(int,my_file_data.split('\n')))

sumVal = findSumSol1(expReport, 2020)
print('Part 1 solution:', sumVal[0] * sumVal[1])

sumVal = findSumSol2(expReport, 2020)
print('Part 2 solution:', sumVal[0] * sumVal[1] * sumVal[2])


