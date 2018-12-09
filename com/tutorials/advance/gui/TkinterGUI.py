#  Tkinter Programming

#Example
def exampleShow():
    import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
    top = tkinter.Tk()
    # Code to add widgets will go here...
    top.mainloop()
#Python 3 - Tkinter Button

from tkinter import *
from tkinter import messagebox
def tkBtn():
    # !/usr/bin/python3
    top = Tk()
    top.geometry("500x500")

    def helloCallBack():
        msg = messagebox.showinfo("Hello Python", "Hello World")

    B = Button(top, text="Hello", command=helloCallBack)
    B.place(x=50, y=50)
    top.mainloop()
#Python 3 - Tkinter Canvas
def tkCanvas():
    top = Tk()

    C = Canvas(top, bg="blue", height=250, width=300)

    coord = 10, 50, 240, 210
    arc = C.create_arc(coord, start=0, extent=150, fill="red")
    line = C.create_line(10, 10, 200, 200, fill='white')
    C.pack()
    top.mainloop()
#Python 3 - Tkinter Checkbutton
def tkCheckbox():
    top = Tk()
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    C1 = Checkbutton(top, text="Music", variable=CheckVar1, \
                     onvalue=1, offvalue=0, height=5, \
                     width=20, )
    C2 = Checkbutton(top, text="Video", variable=CheckVar2, \
                     onvalue=1, offvalue=0, height=5, \
                     width=20)
    C1.pack()
    C2.pack()
    top.mainloop()
#Python 3 - Tkinter Entry
def tkEntry():
    top = Tk()
    L1 = Label(top, text="User Name")
    L1.pack(side=LEFT)
    E1 = Entry(top, bd=5)
    E1.pack(side=RIGHT)

    top.mainloop()
#Python 3 - Tkinter Frame
def tkFrame():
    root = Tk()
    frame = Frame(root)
    frame.pack()

    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)

    redbutton = Button(frame, text="Red", fg="red")
    redbutton.pack(side=LEFT)

    greenbutton = Button(frame, text="Brown", fg="brown")
    greenbutton.pack(side=LEFT)

    bluebutton = Button(frame, text="Blue", fg="blue")
    bluebutton.pack(side=LEFT)

    blackbutton = Button(bottomframe, text="Black", fg="black")
    blackbutton.pack(side=BOTTOM)

    root.mainloop()
#Python 3 - Tkinter Label
def tkLabel():
    root = Tk()

    var = StringVar()
    label = Label(root, textvariable=var, relief=RAISED)

    var.set("Hey!? How are you doing?")
    label.pack()
    root.mainloop()
#Python 3 - Tkinter Listbox
def tkListbox():
    top = Tk()

    Lb1 = Listbox(top)
    Lb1.insert(1, "Python")
    Lb1.insert(2, "Perl")
    Lb1.insert(3, "C")
    Lb1.insert(4, "PHP")
    Lb1.insert(5, "JSP")
    Lb1.insert(6, "Ruby")

    Lb1.pack()
    top.mainloop()
#Python 3 - Tkinter Menubutton
def tkMenuBtn():
    top = Tk()

    mb = Menubutton(top, text="condiments", relief=RAISED)
    mb.grid()
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"] = mb.menu

    mayoVar = IntVar()
    ketchVar = IntVar()

    mb.menu.add_checkbutton(label="mayo",
                            variable=mayoVar)
    mb.menu.add_checkbutton(label="ketchup",
                            variable=ketchVar)

    mb.pack()
    top.mainloop()
#Python 3 - Tkinter Menu
def tkMenu():
    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()

    root = Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="NewItem", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    root.mainloop()
#Python 3 - Tkinter Message
def tkMessage():
    root = Tk()

    var = StringVar()
    label = Message(root, textvariable=var, relief=RAISED)

    var.set("Hey!? How are you doing?")
    label.pack()
    root.mainloop()

# Enoxs TO-DO : 11 ~ 19 and Other.
if __name__ == '__main__':
    # exampleShow()
    # tkBtn()
    # tkCanvas()
    # tkCheckbox()
    # tkEntry()
    # tkFrame()
    # tkLabel()
    # tkListbox()
    # tkMenuBtn()
    # tkMenu()
    tkMessage()