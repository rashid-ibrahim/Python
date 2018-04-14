class SumOfMultiples:
    def __init__(self, firstNum, secondNum, topNum):
        self.firstNum = firstNum
        self.secondNum = secondNum
        self.topNum = topNum
        self.sum = False
        self.multNums = False

    def __getMultNums(self):
        self.multNums = []
        for i in range(0, self.topNum):
            if i%self.firstNum == 0 or i%self.secondNum == 0:
                self.multNums.append(i)
        return

    def __sumNums(self):
        if self.multNums == False:
            self.__getMultNums()

        self.sum = 0
        for i in self.multNums:
            self.sum += i

    def getSum(self):
        if self.sum == False:
            self.__sumNums()
        return self.sum

    def getTopNum(self):
        return self.topNum

    def getFirstNum(self):
        return self.firstNum

    def getSecondNum(self):
        return self.secondNum

    def getMultNums(self):
        return self.multNums
