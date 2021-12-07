from classes.helper import Helper
import copy

class fishy:
    def __init__(self, initialVal, curVal, curDay, normalLifeSpan):
        self.normalLifeSpan = int(normalLifeSpan)
        self.initialVal = int(initialVal)
        self.curDay = curDay
        self.curVal = int(curVal)

    def AgeToDay(self,day):
        newSpawns = []
        daysLeft = day - self.curDay
        if daysLeft > self.curVal:
            for newSpawn in range(self.curDay + self.curVal, day, self.normalLifeSpan):
                newSpawns.append(fishy(self.initialVal,self.initialVal,newSpawn + 1,self.normalLifeSpan))
        return newSpawns

SpawnDict = {}

def countFishiesUntilDay(curSchool, day):
    tot = len(curSchool)
    if len(curSchool) == 0:
        return 0
    for fish in curSchool:
        key = str(fish.curVal) + ',' + str(fish.curDay) # the idea is that every fish that shares this characteristics
        if key not in SpawnDict:                        # will have the same amount of spawns and subsequent spawns
             SpawnDict[key] = countFishiesUntilDay(fish.AgeToDay(day), day)
        tot += SpawnDict[key]
    return tot

def lanternFishStudy(existingFishies,normalLifeSpan, initialValSpawns,days):
    FishDict = {} #further optimization
    SpawnDict.clear()
    tot = 0
    for fish in existingFishies:
        if fish not in FishDict:
            FishDict[fish] = countFishiesUntilDay([fishy(initialValSpawns,fish,0,normalLifeSpan)],days)
        tot += FishDict[fish]
    return tot

file_name = 'input\inputd06.txt'
my_file_data = Helper.read_file(file_name)
input = my_file_data.split(',')

print('Part 1 solution:', lanternFishStudy(input,7,8,80))
print('Part 2 solution:', lanternFishStudy(input,7,8,256))


