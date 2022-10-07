from tkinter import *

global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev
firstSelect = None
currentStage = "main"
currentSelect = None
b1 = None
b2 = None
numb = None
convNumb = None

def toDec(n,b):
    e = 0
    f = 0
    b = int(b)
    n1,n2,n3 = None,None,None
    h = None
    for i in range(len(n)):
        if n[len(n)-i-1] == 'A':
            n1 = n[0:len(n)-i-2]
            n2 = '10'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1] == 'B':
            n1 = n[0:len(n)-i-2]
            n2 = '11'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1] == 'C':
            n1 = n[0:len(n)-i-2]
            n2 = '12'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1] == 'D':
            n1 = n[0:len(n)-i-2]
            n2 = '13'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1] == 'E':
            n1 = n[0:len(n)-i-2]
            n2 = '14'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1] == 'F':
            n1 = n[0:len(n)-i-2]
            n2 = '15'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        else:
            h = False
        if h == False:
            x = int(n[len(n)-i-1])
        else:
            x = int(n2)
        nc = x * pow(b,e)
        e += 1
        f += nc
    return f
def decTo(n,b):
    r = ''
    f = ''
    n = int(n)
    b = int(b)
    while n > 0:
        rs = n%b
        n -= rs
        n /= b
        if rs == 10:
            r += 'A'
        elif rs == 11:
            r += 'B'
        elif rs == 12:
            r += 'C'
        elif rs == 13:
            r += 'D'
        elif rs == 14:
            r += 'E'
        elif rs == 15:
            r += 'F'
        else:
            r += str(int(rs))
    f = r[::-1]
    return f

def main():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev
    # titolo
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=30, fill=BOTH, expand=True, side=TOP)


    # opzioni
    Aopt1 = Button(root, text="CONVERTI", background="#303030",foreground="white", font='Helvetica 10 bold', command=bBin)
    Aopt1.pack(padx=100, pady=(40,0), fill=BOTH, expand=True)

    Aopt2 = Button(root, text="HELP", background="#303030",foreground="white", font='Helvetica 10 bold', command=bOtt)
    Aopt2.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt3 = Button(root, text="RICONOSCIMENTI", background="#303030",foreground="white", font='Helvetica 10 bold', command=bDec)
    Aopt3.pack(padx=100, pady=(0,40), fill=BOTH, expand=True)


    # stage change
    Aprev = Button(root, text="PREV", background="#404040",foreground="white", font='Helvetica 10 bold', command=Prev, activebackground='#404040', activeforeground='white')
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

    Anext = Button(root, text="NEXT", background="#303030",foreground="white", font='Helvetica 10 bold', command=Next)
    Anext.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)
def selectFirstBase():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev
    # title
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=(30,0), fill=BOTH, expand=True, side=TOP)

    # subtitle
    Asubtitle = Label(root, text="PRIMA BASE", background="#505050",foreground="white", font='Helvetica 12 bold')   #   <---    Select the first base
    Asubtitle.pack(padx=100, pady=(0,30), fill=BOTH, expand=True, side=TOP)


    # opt
    Aopt1 = Button(root, text="BINARIO", background="#303030",foreground="white", font='Helvetica 10 bold', command=bBin)
    Aopt1.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt2 = Button(root, text="OTTALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=bOtt)
    Aopt2.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt3 = Button(root, text="DECIMALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=bDec)
    Aopt3.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt4 = Button(root, text="ESADECIMALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=bHex)
    Aopt4.pack(padx=100, pady=(0, 30), fill=BOTH, expand=True)


    # stage change
    Aprev = Button(root, text="PREV", background="#303030",foreground="white", font='Helvetica 10 bold', command=Prev)
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

    Anext = Button(root, text="NEXT", background="#303030",foreground="white", font='Helvetica 10 bold', command=Next)
    Anext.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)
def selectSecondBase():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev
    # title
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=(30,0), fill=BOTH, expand=True, side=TOP)

    # subtitle
    Asubtitle = Label(root, text="SECCONDA BASE", background="#505050",foreground="white", font='Helvetica 12 bold')   #   <---    Select the first base
    Asubtitle.pack(padx=100, pady=(0,30), fill=BOTH, expand=True, side=TOP)


    # opt
    Aopt1 = Button(root, text="BINARIO", background="#303030",foreground="white", font='Helvetica 10 bold', command=bBin1)
    Aopt1.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt2 = Button(root, text="OTTALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=bOtt1)
    Aopt2.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt3 = Button(root, text="DECIMALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=bDec1)
    Aopt3.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt4 = Button(root, text="ESADECIMALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=bHex1)
    Aopt4.pack(padx=100, pady=(0, 30), fill=BOTH, expand=True)


    # stage change
    Aprev = Button(root, text="PREV", background="#303030",foreground="white", font='Helvetica 10 bold', command=Prev)
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

    Anext = Button(root, text="NEXT", background="#303030",foreground="white", font='Helvetica 10 bold', command=Next)
    Anext.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)
def digitNumb():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev
    # title
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=(30,0), fill=BOTH, expand=True, side=TOP)

    # subtitle
    Asubtitle = Label(root, text="DIGIT NUMBER", background="#505050",foreground="white", font='Helvetica 12 bold')   #   <---    Select the first base
    Asubtitle.pack(padx=100, pady=(0,30), fill=BOTH, expand=True, side=TOP)


    # opt
    Aopt1 = Entry(root, background="#303030", foreground="white",font='Helvetica 10 bold')
    Aopt1.pack(padx=100, pady=87, fill=BOTH, expand=True)



    # stage change
    Aprev = Button(root, text="PREV", background="#303030",foreground="white", font='Helvetica 10 bold', command=Prev)
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

    Anext = Button(root, text="NEXT", background="#303030",foreground="white", font='Helvetica 10 bold', command=Next)
    Anext.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)
def seeConvertedNumb():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev
    # title
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=(30,0), fill=BOTH, expand=True, side=TOP)

    # subtitle
    Asubtitle = Label(root, text="THE CONVERTED NUMBER IS",background="#505050", foreground="white", font='Helvetica 12 bold')   #<---    Select the first base
    Asubtitle.pack(padx=100, pady=(0,30), fill=BOTH, expand=True, side=TOP)


    # opt
    Aopt1 = Label(root, text=f"{convNumb}", background="#303030",foreground="white", font='Helvetica 10 bold')
    Aopt1.pack(padx=100, pady=86, fill=BOTH, expand=True)


    # stage change
    Aprev = Button(root, text="NEW CONV", background="#303030",foreground="white", font='Helvetica 10 bold', command=Prev)
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

    #Anext = Button(root, text="NEXT", background="#303030",foreground="white", font='Helvetica 10 bold', command=Next, activebackground='#404040', activeforeground='white')
    #Anext.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

def Prev():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    if currentStage == "main":
        pass
    elif currentStage == "selectFirstBase":
        Atitle.destroy()
        Asubtitle.destroy()
        Aopt1.destroy()
        Aopt2.destroy()
        Aopt3.destroy()
        Aopt4.destroy()
        Aprev.destroy()
        Anext.destroy()
        main()
        currentStage = "main"
    elif currentStage == "selectSecondBase":
        Atitle.destroy()
        Asubtitle.destroy()
        Aopt1.destroy()
        Aopt2.destroy()
        Aopt3.destroy()
        Aopt4.destroy()
        Aprev.destroy()
        Anext.destroy()
        selectFirstBase()
        currentStage = "selectFirstBase"
    elif currentStage == "digitNumb":
        Atitle.destroy()
        Asubtitle.destroy()
        Aopt1.destroy()
        Aopt2.destroy()
        Aopt3.destroy()
        Aopt4.destroy()
        Aprev.destroy()
        Anext.destroy()
        selectSecondBase()
        currentStage = "selectSecondBase"
    elif currentStage == "seeConvertedNumb":
        Atitle.destroy()
        Asubtitle.destroy()
        Aopt1.destroy()
        Aopt2.destroy()
        Aopt3.destroy()
        Aopt4.destroy()
        Aprev.destroy()
        Anext.destroy()
        digitNumb()
        currentStage = "digitNumb"
def Next():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    if currentStage == "main":
        Atitle.destroy()
        Aopt1.destroy()
        Aopt2.destroy()
        Aopt3.destroy()
        Aprev.destroy()
        Anext.destroy()
        selectFirstBase()
        currentStage = "selectFirstBase"
    elif currentStage == "selectFirstBase":
        print(b1)
        Atitle.destroy()
        Asubtitle.destroy()
        Aopt1.destroy()
        Aopt2.destroy()
        Aopt3.destroy()
        Aopt4.destroy()
        Aprev.destroy()
        Anext.destroy()
        selectSecondBase()
        currentStage = "selectSecondBase"
    elif currentStage == "selectSecondBase":
        Atitle.destroy()
        Asubtitle.destroy()
        Aopt1.destroy()
        Aopt2.destroy()
        Aopt3.destroy()
        Aopt4.destroy()
        Aprev.destroy()
        Anext.destroy()
        digitNumb()
        currentStage = "digitNumb"
    elif currentStage == "digitNumb":
        convNumb = Aopt1.get()
        var = toDec(convNumb, b1)
        convNumb = decTo(var, b2)
        print(type(convNumb))
        Atitle.destroy()
        Asubtitle.destroy()
        Aopt1.destroy()
        Aopt2.destroy()
        Aopt3.destroy()
        Aopt4.destroy()
        Aprev.destroy()
        Anext.destroy()
        seeConvertedNumb()
        currentStage = "seeConvertedNumb"
    elif currentStage == "seeConvertedNumb":
        pass

def bBin():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    b1 = 2
    
def bOtt():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    b1 = 8 
def bDec():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    b1 = 10 
def bHex():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    b1 = 16
   

def bBin1():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    b2 = 2
def bOtt1():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    b2 = 8
def bDec1():
    global currentStage,currentSelect,b1,b2,numb,convNumb
    b2 = 10
def bHex1():
    
    global currentStage,currentSelect,b1,b2,numb,convNumb
    b2 = 16

root = Tk()
root.title("Il nostro programma")
root.geometry("600x400")
root.resizable(False,False)
root.configure(bg='#414141')



main()

root.mainloop()