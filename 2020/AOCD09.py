from classes.helper import Helper

def findFirstWrongNum(xmas,n):
    currentCache = dict.fromkeys(xmas,0)
    #preamble
    currentCache.update(dict.fromkeys(xmas[:n],1))
    start = 0
    end = n

    #start processing
    for x in xmas[n:]:
        #check if valid
        valid = False
        for i in xmas[start:end]:
            if (x - i) in xmas[start:end]:
                if (x != i*2 and currentCache[x - i] > 0) or (x == i*2 and currentCache[x - i] > 1):
                    valid = True
                    break
        if valid:
            #update cache
            currentCache[xmas[start]] -= 1
            currentCache[xmas[end]] += 1
            start += 1
            end += 1
        else:
            return x

    return currentCache

def findWeakness(xmas,wrongNum):
    sumList = []
    for x in xmas:
        sumList.append(x)
        while True:
            if sum(sumList) == wrongNum:
                return sumList
            elif sum(sumList) > wrongNum:
                sumList = sumList[1:]
            else:
                break
    return []


#inputs
file_name = 'input\inputd09.txt'
n = 25

file = [int(num) for num in Helper.read_file(file_name).split()]
wrongNum = findFirstWrongNum(file,n)
weakness = findWeakness(file,wrongNum)


print('Part 1 solution:', wrongNum)
print('Part 2 solution:', max(weakness) + min(weakness))
