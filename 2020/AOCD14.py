from classes.helper import Helper
import re
import copy


def processMasks(file):
    curMask = ''
    bitMask = []
    memory = {}
    for row in file:
        if row[:2] == 'ma': #new mask
            elements = row.split()
            curMask = elements[2]
            bitMask = [bitId for bitId, bit in enumerate(curMask) if bit != 'X']
        else:
            # use mask
            elements = row.split()
            value = int(elements[2])
            address = re.findall('[0-9]+',elements[0])[0] #may be improved with Regex
            for i in bitMask:
                if curMask[i] == '1': # must convert to 1
                    thisOne = int('0' * i + '1' + '0' * (35-i),2)
                    value = thisOne | value
                if curMask[i] == '0':  # must convert to 0
                    thisOne = int('1' * i + '0' + '1' * (35 - i), 2)
                    value = thisOne & value

            memory[address] = value
    return memory
#
def processMasksSol2(file):
    curMask = ''
    bitMask = []
    memory = {}
    for row in file:
        if row[:2] == 'ma': #new mask
            elements = row.split()
            curMask = elements[2]
            bitMask = [bitId for bitId, bit in enumerate(curMask) if bit != 'X']
        else:
            # use mask
            elements = row.split()
            value = int(elements[2])
            address = re.findall('[0-9]+',elements[0])[0] #may be improved with Regex
            addressBin = str(bin(int(address)))[2:].rjust(36,'0')
            newAddress = ''
            for i in range(len(curMask)):
                if curMask[i] == '1': # must convert to 1
                    newAddress += '1'
                elif curMask[i] == 'X':  #
                    newAddress += 'X'
                else:
                    newAddress += addressBin[i]
            allAdresses = getAllMemoryAddresses(newAddress)
            for a in allAdresses:
                memory[int(a,2)] = value
    return memory


def getAllMemoryAddresses(address):
    addresses = ['']
    for c in address:
        if c in ['1','0']:
            for i in range(len(addresses)):
                addresses[i] = addresses[i] + c
        else: # must explode
            newAddress = copy.deepcopy(addresses)
            for i in range(len(addresses)):
                addresses[i] = addresses[i] + '1'
            for i in range(len(newAddress)):
                addresses.append(newAddress[i] + '0')
    return addresses




# inputs
file_name = 'input\inputd14.txt'

file = Helper.read_file(file_name).split('\n')
memory = processMasks(file)

value = 0
for memId, item in memory.items():
    value += item

print('Part 1 solution:', value)

memory = processMasksSol2(file)
value = 0
for memId, item in memory.items():
    value += item

print('Part 2 solution:', value)


