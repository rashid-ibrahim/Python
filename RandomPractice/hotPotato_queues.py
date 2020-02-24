from queue import *
from random import randint

def hotPotatoGame(names):
    ql = Queue()
    
    for name in names:
        ql.put(name)

    while ql.qsize() > 1:
        for i in range(randint(1,50)):
            ql.put(ql.get())

        ql.get()

    return ql.get()

#This is really only here to make it easier to keep running the print function
#without having to type it in over and over.
def main():
    print(hotPotatoGame(["Aaron","Johnathan","Jessica","Emily","Ken","Lisa","Tommy"]))


if __name__ == '__main__':
    main()
