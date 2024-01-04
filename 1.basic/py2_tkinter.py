import tkinter as tk
from tkinter import messagebox

def addstr(counter,dstr):
    # global counter, dstr
    counter[0] += 1
    print(counter[0])
    dstr.set(str(counter[0]))
    # messagebox.showinfo(title='add', message=dstr)


def addLable(root,vStr):
    l_xi = tk.Label(root,text="Hi 汐", font=("times",30)).grid(row=1,column=1,columnspan=3)
    l_var = tk.Label(root, textvariable=vStr).grid(row=2,column=1,sticky="e")


def addButton(root,counter,vStr):
    b_quit = tk.Button(root, text="quit", command=root.quit).grid(row=8,column=1,rowspan=2,columnspan=3)
    b_var = tk.Button(root,text="add",command=lambda:addstr(counter,vStr)).grid(row=2,column=2,sticky="w")


def validateEntry(e_1):
    print(e_1.get(),"=",eval(e_1.get()))


def addEntry(root):
    strVar = tk.StringVar()
    e_1 = tk.Entry(root,textvariable=strVar,width=20,validate="focusout",validatecommand=lambda:validateEntry(e_1))
    e_1.grid(row=3,column=1)
    e_1.insert(0,"100/5+3")
    print(e_1.get())


def addSpinBox(root):
    spinBoxDigital = tk.Spinbox(root, from_=1, to_=100, increment=10,width=20)
    spinBoxDigital.grid(row=3,column=2)
    print(spinBoxDigital.get())
    spinBoxAlpha = tk.Spinbox(root, values=('apple','banana','cake',)).grid(row=3,column=3)
    

def addText(root):
    text = tk.Text(root,width=45,height=6,)
    text.insert(tk.INSERT,'I am a text\n')
    text.insert(tk.INSERT,'I am a text2\n')
    text.grid(row=4,column=1,columnspan=2,sticky='w')


def delActive(lb):
    lb.delete(tk.ACTIVE)

def insEnd(lb):
    lb.insert("end","new")
    print(lb.get(lb.curselection()))

def addListbox(root):
    listbox = tk.Listbox(root)
    listbox.grid(row=4, column=3, columnspan=1)
    for i, item in zip(range(0,4),["a","b","c","d"]):
        listbox.insert(i, item)
    deleteButton = tk.Button(text="del",command=lambda:delActive(listbox)).grid(row=5,column=3,sticky="w")
    insertButton = tk.Button(text="insert",command=lambda:insEnd(listbox)).grid(row=5,column=3)


def initWindow():
    root = tk.Tk()

    root.title("GUI Practice")
    width = 500
    height = 400
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
    root.geometry(size_geo)
    root.resizable(False, False)
    # root.iconbitmap("D:/1_Michael/python/icon/icon.icon")
    
    vStr = tk.StringVar()
    counter = [0]
    vStr.set(str(counter[0]))

    addLable(root,vStr)
    addButton(root,counter,vStr)
    addEntry(root)
    addSpinBox(root)
    addText(root)
    addListbox(root)

    root.mainloop()

# initWindow()

def testFrame():
    root = tk.Tk()
    root.title("test Frame")
    root.geometry("400x300+100+100")

    row = tk.Frame(root)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    var1 = tk.StringVar()
    tk.Label(row, text="label", anchor='w').pack(side="left")
    tk.Entry(row, textvariable=var1).pack()

    row = tk.Frame(root)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    var2 = tk.StringVar()
    tk.Label(row, text="label2", anchor='w').pack(side="left")
    tk.Entry(row, textvariable=var1).pack()

    root.mainloop()


testFrame()  