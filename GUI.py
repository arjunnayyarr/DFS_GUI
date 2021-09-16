import Main
import DFS
import tkinter.messagebox
from tkinter import *
import threading


window=Tk()
window.title("DFS GUI")
window.geometry("600x440")
window.resizable(False, False)
canvas = Canvas(window, relief="solid", bd=2, width=600, height=380,bg='white')

canvas.pack()
btnFrame = Frame(window, relief="solid", width="800", height="25")
btnFrame.pack()
textFrame = Frame(window, relief="solid", width="800", height="25")
textFrame.pack()

ModeLabel = Label(textFrame, text="Current Mode: "+'Create Node Mode')
ModeLabel.pack(side="right", padx=50)

x_matrix = [] 
y_matrix = []

oval = []

Line1 = None
Line2 = None

CreateMode = True
LineMode = False

def abt():
    tkinter.messagebox.showinfo('WELCOME','Welcome To DFS GUI')

def abt1():
    tkinter.messagebox.showinfo('Thanks','Thanks For Using')
    exit()

def ChangeMode():
    global CreateMode, CurrentMode
    global LineMode
    if(not CreateMode):
        CreateMode = True
        LineMode = False
        CurrentMode = 'Create Node Mode'
    elif(not LineMode):
        LineMode = True
        CreateMode = False
        CurrentMode = 'Connect Mode'
    global ModeLabel
    ModeLabel.config(text="Current Mode: "+CurrentMode)
    ModeLabel.pack(side="right", padx=50)

def mouseClick(event):
    x = event.x
    y = event.y
    if(CreateMode):
        x_matrix.append(x)
        y_matrix.append(y)
        oval.append(0)

        DFS.search.append(0)
        Main.adjacency_matrix.append([])
        adj_qty = len(Main.adjacency_matrix)
        Main.adjacency_matrix = [[0] * adj_qty for i in range(adj_qty)]

        i = len(oval)-1
        oval[i]=canvas.create_oval(x_matrix[i]-20, y_matrix[i]-20, x_matrix[i]+20, y_matrix[i]+20, fill="Red", width=2, tags=("Node",i))
        text = canvas.create_text((x_matrix[i], y_matrix[i]), text=str(i+1), tags=("Node",i),font='bold')
        print("Added Node at " + str(x) + "," + str(y))

    if(LineMode):
        item = canvas.find_closest(x,y)
        tags = canvas.gettags(item)

        global Line1
        global Line2
        #print(tags)
        if(tags[0] == "Node"):
            if(Line1 is None):
                Line1 = int(tags[1])
                print("1st Node of line selected")
            else:
                print("2nd Node of line selected")
                Line2 = int(tags[1])
                if(Line1 != Line2):
                    Main.adjacency_matrix[Line1][Line2] = 1
                    Main.adjacency_matrix[Line2][Line1] = 1
                    canvas.create_line(x_matrix[Line1],y_matrix[Line1], x_matrix[Line2], y_matrix[Line2], fill="Yellow")
                    print("DrawLine :"+ str(Line1+1) +" and "+str(Line2+1)+ " Connected !!")
                Line1 = None


def FillOval(v, color): # Function that fills the circle in yellow
    canvas.itemconfig(oval[v], fill=color)
    
def reset():
    global x_matrix
    global y_matrix
    global oval

    x_matrix = []
    y_matrix = []
    oval = []
    
    DFS.search = []
    Main.adjacency_matrix= []

    canvas.delete("all")

def runBtn(_type):
    if(_type == 'DFS'):
        th = threading.Thread(target=DFS.DFS, args=(0,))
        th.start()

def run():
    button1 = Button(btnFrame, relief="solid", text="Run - DFS", width=10,font='Bold', command=lambda: runBtn('DFS'))
    button2 = Button(btnFrame, relief="solid", text="ChangeMode", width=10,font='Bold', command=lambda: ChangeMode())
    button3 = Button(btnFrame, relief="solid", text="RESET", width=10,font='Bold', command=lambda: reset())
    button4 = Button(btnFrame, relief="solid", text="Exit", width=10, font='Bold', command=lambda: abt1())

    button1.pack(side="left", padx = 10)
    button2.pack(side="left", padx=10)
    button3.pack(side="left", padx = 10)
    button4.pack(side="left", padx=10)

    canvas.bind("<Button-1>", mouseClick)

    window.mainloop()

