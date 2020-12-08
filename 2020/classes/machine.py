import copy

class Machine:
    def __init__(self):
        self.accumulator = 0

    def resetAcc(self):
        self.accumulator = 0

    def addAcc(self,num):
        self.accumulator += num

    def getAcc(self):
        return self.accumulator

    def canStart(self,code): #return True if it can start, false if it cant
        currCursor = 0
        self.resetAcc()
        codeLeft = copy.deepcopy(code)
        while currCursor < len(code):
            if len(codeLeft[currCursor]) == 0: # reached a loop
                return False
            codeLeft[currCursor] = ''
            opr = code[currCursor][0]
            arg = int(code[currCursor][1])
            jumpInt = 1  # default
            if opr == 'acc':
                self.addAcc(arg)
            elif opr == 'jmp':
                jumpInt = arg
            currCursor += jumpInt
        return True