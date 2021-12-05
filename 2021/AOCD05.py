from classes.helper import Helper
import copy

class cloud_line:
    def __init__(self,pos1,pos2):
        self.X1 = int(pos1[0])
        self.Y1 = int(pos1[1])
        self.X2 = int(pos2[0])
        self.Y2 = int(pos2[1])

    def getPos(self):
        return [self.X1,self.Y1],[self.X2,self.Y2]

    def isHorizontalOrVertical(self):
        return self.X1 == self.X2 or self.Y1 == self.Y2

    def getAllPoints(self):
        points = []
        xSign = 1
        ySign = 1
        if self.X2-self.X1 < 0:
            xSign = -1
        if self.Y2-self.Y1 < 0:
            ySign = -1
        curX = self.X1
        curY = self.Y1
        while curX != self.X2 or curY != self.Y2:
            if curX != self.X2 and curY != self.Y2:     #handle diagonal
                points.append(str(curX) + ',' + str(curY))
                curX += xSign
                curY += ySign
            elif curX != self.X2:
                points.append(str(curX) + ',' + str(curY))
                curX += xSign
            else:
                points.append(str(curX) + ',' + str(curY))
                curY += ySign
        points.append(str(self.X2) + ',' + str(self.Y2))
        return points

def getLines(input):
    lines = []
    for item in input:
        elements = item.split()
        lines.append(cloud_line(elements[0].split(','), elements[2].split(',')))
    return lines

def buildDiagram(lines,includeDiagonal):
    diagram = {}
    for line in lines:
        if (not includeDiagonal and line.isHorizontalOrVertical()) or includeDiagonal:
            for p in line.getAllPoints():
                if p in diagram:
                    diagram[p] = diagram[p] + 1
                else:
                    diagram[p] = 1
    return diagram

def getNumOfDangerous(input,includeDiagonal):
    diagram = buildDiagram(getLines(input),includeDiagonal)
    tot = 0
    for key in diagram:
        if diagram[key] > 1:
            tot += 1
    return tot





file_name = 'input\inputd05.txt'
my_file_data = Helper.read_file(file_name)
input = my_file_data.split('\n')

print('Part 1 solution:', getNumOfDangerous(input,False))
print('Part 2 solution:', getNumOfDangerous(input,True))


