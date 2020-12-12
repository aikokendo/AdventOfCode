from classes.helper import Helper
import networkx as nx
import math
def find_jolt_diffs(adapters):
    jolt_difs = [0,0,1]
    adapters.sort()
    last_jolt = 0
    for adapter in adapters:
        jolt_dif = adapter - last_jolt
        jolt_difs[jolt_dif-1] += 1
        last_jolt = adapter
    return jolt_difs

def find_tot_arrangements(adapters):
    adapters.append(0)
    adapters.sort()
    print(adapters)
    bags = []
    currBag = []
    last = 0
    for adapter in adapters:
        if adapter - last == 3: #only connector
            bags.append(currBag)
            currBag = []
        currBag.append(adapter)
        last = adapter
    bags.append(currBag)
    print(bags)

    combinations = 1
    for bag in bags: #find combinations
        if len(bag) <= 2:
            continue
        else:
            #combinations.append(len(bag)-1)
            #n = len(bag)
            #combinations.append(math.factorial(n) / (math.factorial(2) * math.factorial(n - 2)))
            combinations *= find_paths(bag)
    return combinations


def find_paths(bag):
    G = nx.DiGraph()
    #bag.append(0)
    #bag.append(max(bag)+3)
    bag.sort()
    for i in range(len(bag)):
        for j in range(i+1,len(bag)):
            if i != j:
                if bag[j] - bag[i] <= 3:
                    G.add_edge(bag[i],bag[j])

    return len(list(nx.all_simple_paths(G,bag[0],bag[-1])))




#inputs
file_name = 'input\inputd10.txt'

file = [int(num) for num in Helper.read_file(file_name).split()]
jolt_diffs = find_jolt_diffs(file)

# print(find_paths(file))

print(find_tot_arrangements(file))
print('Part 1 solution:', jolt_diffs[0]*jolt_diffs[2])
# print('Part 2 solution:', max(weakness) + min(weakness))
