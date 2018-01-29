from tkinter import *
import tkinter

class buttons:
    def __init__(self, root):
        self.exitButton(root)
        
    def exitButton(self, root):
        root.button = Button(root, text="Exit", command=root.destroy)
        root.button.place(x=550, y=600)

def main():
    root = Tk()
    root.geometry("700x650+200+50")
    buttons(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
