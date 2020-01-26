from tkinter import *
import time
global decision,answers,cont,done
done = False
cont = False
answers = []
decision = "unpressed"
def yes():
    global decision
    if decision=="unpressed":
        decision = "yes"
def no():
    global decision
    if decision =="unpressed":
        decision = "no"
def continues():
    global cont
    cont = True
def question(string):
    global yesf,nof,y,n,c,contf,done,decision
    done = False
    decision = 'unpressed'
    try:
        yesf.destroy()
        nof.destroy()
        y.destroy()
        n.destroy()
    except:
        pass
    try:
        contf.destroy()
        c.destroy()
    except:
        pass
    yesf = Frame(master,height = 100, width = 100)
    yesf.pack_propagate(0)
    yesf.pack()
    nof = Frame(master, height = 100, width = 100)
    nof.pack_propagate(0)
    nof.pack()
    yesf.place(x=0,y=100)
    nof.place(x=200,y=100)
    y = Button(yesf, text = "Yes", command = yes)
    n = Button(nof, text = "No", command = no)
    y.pack(fill="both",expand=1)
    n.pack(fill="both",expand=1)
    output(string)
    while decision=='unpressed':
        master.update()
    done = True
    return(decision)
def information(string):
    global yesf,nof,y,n,cont,contf,c,done
    done = False
    cont = False
    try:
        yesf.destroy()
        nof.destroy()
        y.destroy()
        n.destroy()
    except:
        pass
    try:
        contf.destroy()
        c.destroy()
    except:
        pass
    contf = Frame(master,height = 30, width = 100)
    contf.place(x=100,y=200)
    contf.pack()
    c = Button(contf, text = "Continue", command = continues)
    c.pack(fill='both',expand=1)
    output(string)
    while not cont:
        master.update()
    done = True
    return(True)
        
master = Tk()
master.geometry("300x200")
master.resizable(0,0)

textf = Frame(master,height = 100, width = 300)
textf.pack_propagate(0)
textf.pack()
text = Text(textf)
text.tag_config('a',justify='center')
text.insert(INSERT,"Hi",'a')
text.pack(fill="both",expand = 1)
text.config(state=DISABLED)
def output(something):
    text.config(state=NORMAL)
    text.delete('@0,0',END)
    text.insert(INSERT,something,'a')
    text.config(state=DISABLED)
def iq(iorq,string):
    if iorq=='i':
        information(string)
    else:
        question(string)
