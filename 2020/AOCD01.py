import copy

def findSum(expReport, tot):
    for i in expReport:
        for j in expReport:
            for k in expReport:
                if i + j + k == tot:
                    return [i,j,k]


def findSumRec(expReport, entries, tot, cur=[]):
    if len(cur) == entries:
        if sum(cur) == tot:
            return cur
        return
    else: # less than entries, must go down
        cur.append(expReport[0])
        newExp = expReport[1:]
        for i in range(len(expReport)):
            result = findSumRec(newExp,entries,tot,copy.deepcopy(cur))
            if result is not None:
                return result
            if len(newExp) < 3:
                return
            cur[len(cur)-1] = newExp[0]
            newExp = newExp[1:]



f = open('inputd01.txt', 'r+')
my_file_data = f.read()
f.close()

expReport = list(map(int,my_file_data.split('\n')))

sumVal = findSum(expReport, 2020)
print(sumVal[0] * sumVal[1] * sumVal[2])

sumVal = findSumRec(expReport,3,2020)
print(sumVal[0] * sumVal[1] * sumVal[2])

