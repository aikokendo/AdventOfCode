from classes.helper import Helper

# inputs
file_name = 'input\inputd16.txt'

def parseRules(rules):
    ruleDict = {}
    for rule in rules:
        elements = rule.split(': ')
        ranges = elements[1].split(' or ')
        value = []
        for range in ranges:
            value.append([int(v) for v in range.split('-')])
        ruleDict[elements[0]] = value
    return ruleDict

def flattenTickets(tickets):
    # flattened tickets
    flatTickets = {}  # key number, value counter
    for ticket in tickets:
        values = ticket.split(',')
        for value in values:
            if int(value) in flatTickets:
                flatTickets[int(value)] += 1
            else:
                flatTickets[int(value)] = 1
    return flatTickets

def valueIsValid(rules,value):
    inRange = False
    for rule, ranges in rules.items():
        for range in ranges:
            if value >= range[0] and value <= range[1]:
                inRange = True
                break
    return inRange

def findInvalidTicketValues(rules, tickets):
    flatTickets = flattenTickets(tickets)
    invalidValues = []
    for k in flatTickets.keys():
        if not valueIsValid(rules,k):
            invalidValues.append(k)
    result = 0
    for iv in invalidValues:
        result  += iv * flatTickets[iv]
    return result

def discardInvalidTickets(rules, tickets):
    flatTickets = flattenTickets(tickets)
    invalidValues = []
    validTickets = []
    for k in flatTickets.keys():
        if not valueIsValid(rules,k):
            invalidValues.append(k)
    for ticket in tickets:
        values = ticket.split(',')
        valid = True
        for value in values:
            if int(value) in invalidValues:
                valid = False
        if valid:
            validTickets.append(ticket.split(','))
    return validTickets

def findOrder(validTickets, rules):
    order = {}
    for column in range(len(validTickets[0])):
        for rule, ranges in rules.items():
            match = True
            for tid, ticket in enumerate(validTickets):
                value = int(ticket[column])
                if (value < ranges[0][0] or value > ranges[0][1]) and (value < ranges[1][0] or value > ranges[1][1]):
                    match = False
                    break
            if match and tid + 1 == len(validTickets):
                if rule in order:
                    order[rule].append(column)
                else:
                    order[rule] = [column]
    #reduce because rules can match more than one column
    alreadyAssigned = []
    while True:
        needsReduce = False
        for k in order.keys():
            if len(order[k]) == 1:
                if order[k][0] not in alreadyAssigned:
                    alreadyAssigned.append(order[k][0])
            else: #check if it needs to be cleaned
                order[k] = [o for o in order[k] if o not in alreadyAssigned]
        if len(alreadyAssigned) == len(validTickets[0]):
            break

    return order

def calculateSol2(myTicket, order):
    tot = 1
    for item, pos in order.items():
        if item.startswith('departure'):
            tot *= int(myTicket[pos[0]])
    return tot


file = Helper.read_file(file_name).split('\n\n')

rules = parseRules(file[0].split('\n'))
myTicket = file[1].split('\n')[1:][0].split(',')
otherTickets = file[2].split('\n')[1:]
sol1 = findInvalidTicketValues(rules,otherTickets)

validTickets = discardInvalidTickets(rules, otherTickets)
validTickets.append(myTicket)
ticketOrder = findOrder(validTickets, rules)

print('Part 1 solution:', sol1)
print('Part 1 solution:', calculateSol2(myTicket, ticketOrder))
#
