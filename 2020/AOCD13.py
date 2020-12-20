from classes.helper import Helper

# inputs
file_name = 'input\inputd13.txt'

def getNextBusTime(total,buses):
    times = []
    for bus in buses:
        if bus == 'x':
            times.append(bus)
        else:
            times.append(int(bus) - int(total) % int(bus))
    return times

def getSol1(buses,nextBusTimes):
    lowest = int(min(buses))
    lowest_bus = -1
    for i in range(len(buses)):
        if buses[i] == 'x':
            continue
        elif lowest > int(nextBusTimes[i]):
            lowest = nextBusTimes[i]
            lowest_bus = buses[i]
    return lowest * int(lowest_bus)

def getContestResult(buses):
    cleanBuses2 = {}
    #cleanup
    for i in range(len(buses)):
        if buses[i] != 'x':
            cleanBuses2[int(buses[i])] = i
    tot = 0
    inc = list(cleanBuses2.keys())[0]
    for bus in list(cleanBuses2.keys())[1:]:
        # find next match
        while True:
            tot += inc
            nextBus = (tot + cleanBuses2[bus]) % bus
            if nextBus == bus:
                nextBus = 0
            if nextBus == 0:
                #found match, calculate new increment
                inc *= bus
                break
    return tot


file = Helper.read_file(file_name).split('\n')
total = file[0]
buses = file[1].split(',')

nextBusTimes = getNextBusTime(total,buses)

print('Part 1 solution:', getSol1(buses,nextBusTimes))
print('Part 2 solution:', getContestResult(buses))


