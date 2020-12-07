from classes.helper import Helper
import networkx as nx
import re

def parseFiletoGraphWithWeights(file):
    rules = str.replace(file, ' no other bags', '')
    rules = rules.split('\n')
    connections = {}
    for rule in rules:
        bags = re.findall('([0-9]+)? ?([a-z]+[ ]?[a-z]*) bag[s]?', rule)
        if len(bags) > 1:
            connections[bags[0][1]] = {bag[1]:{"b":int(bag[0])} for bag in bags[1:]}
    return nx.DiGraph(connections)


def getAllCoverBags(g,bag):
    coverBags = set()
    for n in g.predecessors(bag):
        coverBags.add(n)
        newCoverBags = getAllCoverBags(g,n)
        coverBags = coverBags.union(newCoverBags)
    return coverBags

def calculateBagsInside(g,bag):
    totBags = 0
    for n in g.successors(bag):
        amountBags = g.get_edge_data(bag,n)['b']
        totBags = totBags + amountBags + amountBags * calculateBagsInside(g,n)
    return totBags

#inputs
file_name = 'input\inputd07.txt'
myBag = 'shiny gold'


file = Helper.read_file(file_name)
G = parseFiletoGraphWithWeights(file)

coverBags  = getAllCoverBags(G, myBag)
print('Part 1 solution:', len(coverBags))
totBags = calculateBagsInside(G, myBag)
print('Part 2 solution:', totBags)
