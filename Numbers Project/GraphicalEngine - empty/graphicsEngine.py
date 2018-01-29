from tkinter import *
import tkinter

class combinatoryGUI:
##    def __init__(self, parent):
##        Frame.__init__(self, parent, background="white")
##        self.parent = parent
##        self.initUI()
##
##    def initUI(self):
##        self.parent.title("Combinatory")
##        self.style = Style()
##        self.style.theme_use("default")
##        
##        self.pack(fill=BOTH, expand=1)
##
##        quitButton = Button(self, text="Quit", command=self.destroy())
##        quitButton.place(x=50, y=50)
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="QUIT", fg="red", command=frame.destroy)
##
##        self.button.pack(side=LEFT)
##    def __init__ (self, parent):
##        frame = Frame(parent)
##        quitButton = tkinter.Button(frame, text = "Quit", command = frame.destroy)

##        quitButton.pack(pady=20, padx=20)
        #quitButton.place(bordermode=OUTSIDE, height=50, width=100)

##def nuull():
##    tkMessageBox.showinfo( "Hello Python", "Hello World")

def Pressed(root):
    root.destroy()
    print('buttons are cool')
def main():
    root = Tk()
    root.geometry("700x650+200+50")
    app = combinatoryGUI(root)
    #button = Button(root, text = 'Press', command = Pressed(root))
    #button.pack(pady=20, padx=20)
    #Pressed(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
