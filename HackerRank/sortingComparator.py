from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'{self.name}: {self.score}'

    def __repr__(self):
        return f'{self.name}: {self.score}'

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score == b.score:
            if a.name > b.name:
                return 1
            return 0
        else:
            return 1


class checker:
    pass


data = []
n = 3
vals = [('jones', 19), ('jones', 15), ('jones', 20)]

for i in range(n):
    oname, oscore = vals[i][0], vals[i][1]

    player = Player(oname, oscore)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))

for i in data:
    print(i.name, i.score)
