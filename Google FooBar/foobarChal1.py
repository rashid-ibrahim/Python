class FindExtra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sortX = sorted(x, key=int, reverse=True)
        self.sortY = sorted(y, key=int, reverse=True)

    def getLongList(self):
        if len(self.sortX) > len(self.sortY):
            return 1
        else:
            return 2

    def getExtra(self):
        q = self.getLongList()
        if q == 1:
            a = self.sortX
            b = self.sortY
        else:
            a = self.sortY
            b = self.sortX
        for i in range(len(list(b))):
            print('loop')
            print(a)
            print(b)
            if a[-1] == b[-1]:
                a = a[:-1]
                b = b[:-1]
            else:
                return a.pop()
    


def main():
    x = list(map(int,[14, 27, 1, 4, 2, 50, 3, 1]))
    y = list(map(int,[2, 4, -4, 3, 1, 1, 14, 27, 50]))
    finder = FindExtra(x,y)
    ans = finder.getExtra()
    print(ans)

main()
