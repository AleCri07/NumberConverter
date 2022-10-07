# import tkinter
from tkinter import *

# variables
global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev
firstSelect,currentSelect,b1,b2,numb,convNumb,syntaxError = None,None,None,None,None,None,None
currentStage = "main"

# this function changes the number base to decimal
def toDec(n,b):
    e = 0
    f = 0
    b = int(b)
    n1,n2,n3 = None,None,None
    h = None
    for i in range(len(n)):
        if n[len(n)-i-1].lower() == 'a':
            n1 = n[0:len(n)-i-2]
            n2 = '10'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1].lower() == 'b':
            n1 = n[0:len(n)-i-2]
            n2 = '11'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1].lower() == 'c':
            n1 = n[0:len(n)-i-2]
            n2 = '12'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1].lower() == 'd':
            n1 = n[0:len(n)-i-2]
            n2 = '13'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1].lower() == 'e':
            n1 = n[0:len(n)-i-2]
            n2 = '14'
            n3 = n[len(n)-i:len(n)-(len(n)-i)]
            n = f'{n1}{n2}{n3}'
            h = True
        elif n[len(n)-i-1].lower() == 'f':
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

# this function converts a number from the decimal base to another base
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

# create the menu stage
def main():

    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Aopt1, Aopt2, Aopt3

    # tittle
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=30, fill=BOTH, expand=True, side=TOP)

    # options
    Aopt1 = Button(root, text="CONVERTI", background="#303030",foreground="white", font='Helvetica 10 bold', command=Next)
    Aopt1.pack(padx=100, pady=(40,0), fill=BOTH, expand=True)

    Aopt2 = Button(root, text="HELP", background="#303030",foreground="white", font='Helvetica 10 bold')
    Aopt2.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt3 = Button(root, text="RICONOSCIMENTI", background="#303030",foreground="white", font='Helvetica 10 bold')
    Aopt3.pack(padx=100, pady=(0,40), fill=BOTH, expand=True)


# this function selects the first number base
def selectFirstBase():

    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev

    # title
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=(30,0), fill=BOTH, expand=True, side=TOP)

    # subtitle
    Asubtitle = Label(root, text="PRIMA BASE", background="#505050",foreground="white", font='Helvetica 12 bold')   #   <---    Select the first base
    Asubtitle.pack(padx=100, pady=(0,30), fill=BOTH, expand=True, side=TOP)


    # options
    Aopt1 = Button(root, text="BINARIO", background="#303030",foreground="white", font='Helvetica 10 bold', command=b1Bin)
    Aopt1.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt2 = Button(root, text="OTTALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=b1Oct)
    Aopt2.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt3 = Button(root, text="DECIMALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=b1Dec)
    Aopt3.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt4 = Button(root, text="ESADECIMALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=b1Hex)
    Aopt4.pack(padx=100, pady=(0, 30), fill=BOTH, expand=True)


    # scrolls to stages
    Aprev = Button(root, text="MENU", background="#303030",foreground="white", font='Helvetica 10 bold', command=menu)
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

# this function selects the second number base
def selectSecondBase():

    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev

    # title
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=(30,0), fill=BOTH, expand=True, side=TOP)

    # subtitle
    Asubtitle = Label(root, text="SECCONDA BASE", background="#505050",foreground="white", font='Helvetica 12 bold')   #   <---    Select the first base
    Asubtitle.pack(padx=100, pady=(0,30), fill=BOTH, expand=True, side=TOP)


    # options
    Aopt1 = Button(root, text="BINARIO", background="#303030",foreground="white", font='Helvetica 10 bold', command=b2Bin)
    Aopt1.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt2 = Button(root, text="OTTALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=b2Oct)
    Aopt2.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt3 = Button(root, text="DECIMALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=b2Dec)
    Aopt3.pack(padx=100, pady=0, fill=BOTH, expand=True)

    Aopt4 = Button(root, text="ESADECIMALE", background="#303030",foreground="white", font='Helvetica 10 bold', command=b2Hex)
    Aopt4.pack(padx=100, pady=(0, 30), fill=BOTH, expand=True)


    # scrolls to stages
    Aprev = Button(root, text="MENU", background="#303030",foreground="white", font='Helvetica 10 bold', command=menu)
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

    Anext = Button(root, text="BACK", background="#303030",foreground="white", font='Helvetica 10 bold', command=Prev)
    Anext.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)


# this function creates the input stage of the number
def digitNumb():

    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev

    # title
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=(30,0), fill=BOTH, expand=True, side=TOP)

    # subtitle
    Asubtitle = Label(root, text="DIGIT NUMBER", background="#505050",foreground="white", font='Helvetica 12 bold')   #   <---    Select the first base
    Asubtitle.pack(padx=100, pady=(0,30), fill=BOTH, expand=True, side=TOP)


    # options
    Aopt1 = Entry(root, background="#303030", foreground="white",font='Helvetica 10 bold')
    Aopt1.pack(padx=100, pady=(30,10), fill=BOTH, expand=True)

    Aopt2 = Button(root, text="CONVERTI", background="#303030", foreground="white",font='Helvetica 10 bold', command=Next)
    Aopt2.pack(padx=100, pady=(10,30), fill=BOTH, expand=True)



    # scrolls to stages
    Aprev = Button(root, text="MENU", background="#303030",foreground="white", font='Helvetica 10 bold', command=menu)
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

    Anext = Button(root, text="BACK", background="#303030",foreground="white", font='Helvetica 10 bold', command=Prev)
    Anext.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

# funzione che crea lo stage seeConvertedNumb
def seeConvertedNumb():

    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb
    global Atitle, Asubtitle, Aopt1, Aopt2, Aopt3, Aopt4, Anext, Aprev
    # title
    Atitle = Label(root, text="CONVERTITORE", background="#505050",foreground="white", font='Helvetica 12 bold')
    Atitle.pack(padx=100, pady=(30,0), fill=BOTH, expand=True, side=TOP)

    # subtitle
    Asubtitle = Label(root, text="THE CONVERTED NUMBER IS",background="#505050", foreground="white", font='Helvetica 12 bold')   #<---    Select the first base
    Asubtitle.pack(padx=100, pady=(0,30), fill=BOTH, expand=True, side=TOP)


    # options
    Aopt1 = Label(root, text=f"{convNumb}", background="#303030",foreground="white", font='Helvetica 10 bold')
    Aopt1.pack(padx=100, pady=86, fill=BOTH, expand=True)


    # scrolls to stages
    Aprev = Button(root, text="MENU", background="#303030",foreground="white", font='Helvetica 10 bold', command=menu)
    Aprev.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

    Anext = Button(root, text="NEW CONV", background="#303030",foreground="white", font='Helvetica 10 bold', command=Next)
    Anext.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

# funzione per tornare al menu
def menu():

    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # cancella i widget esistenti
    try: Atitle.destroy()
    except: pass
    try: Asubtitle.destroy()
    except: pass
    try: Aopt1.destroy()
    except: pass
    try: Aopt2.destroy()
    except: pass
    try: Aopt3.destroy()
    except: pass
    try: Aopt4.destroy()
    except: pass
    try: Aprev.destroy()
    except: pass
    try: Anext.destroy()
    except: pass

    # crea il menu
    main()

    # imposto lo stage menu come stage corrente
    currentStage = "main"


# funzione per tornare al campo precedente
def Prev():

    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # se lo stage corrente è selectFirstBase
    if currentStage == "selectFirstBase":

        # cancella i widget esistenti
        try: Atitle.destroy()
        except: pass
        try: Asubtitle.destroy()
        except: pass
        try: Aopt1.destroy()
        except: pass
        try: Aopt2.destroy()
        except: pass
        try: Aopt3.destroy()
        except: pass
        try: Aopt4.destroy()
        except: pass
        try: Aprev.destroy()
        except: pass
        try: Anext.destroy()
        except: pass

        # crea il menu
        main()

        # imposto lo stage menu come stage corrente
        currentStage = "main"
    
    # se lo stage corrente è selectSecondBase
    elif currentStage == "selectSecondBase":

        # cancella i widget esistenti
        try: Atitle.destroy()
        except: pass
        try: Asubtitle.destroy()
        except: pass
        try: Aopt1.destroy()
        except: pass
        try: Aopt2.destroy()
        except: pass
        try: Aopt3.destroy()
        except: pass
        try: Aopt4.destroy()
        except: pass
        try: Aprev.destroy()
        except: pass
        try: Anext.destroy()
        except: pass

        # crea lo stage selectFirstBase
        selectFirstBase()

        # imposto lo stage selectFirstBase come stage corrente
        currentStage = "selectFirstBase"
    
    # se lo stage corrente è digitNumb
    elif currentStage == "digitNumb":

        # cancella i widget esistenti
        try: Atitle.destroy()
        except: pass
        try: Asubtitle.destroy()
        except: pass
        try: Aopt1.destroy()
        except: pass
        try: Aopt2.destroy()
        except: pass
        try: Aopt3.destroy()
        except: pass
        try: Aopt4.destroy()
        except: pass
        try: Aprev.destroy()
        except: pass
        try: Anext.destroy()
        except: pass

        # crea lo stage selectSecondBase
        selectSecondBase()
        currentStage = "selectSecondBase"
    
    # se lo stage corrente è seeConvertedNumb
    elif currentStage == "seeConvertedNumb":

        # cancella i widget esistenti
        try: Atitle.destroy()
        except: pass
        try: Asubtitle.destroy()
        except: pass
        try: Aopt1.destroy()
        except: pass
        try: Aopt2.destroy()
        except: pass
        try: Aopt3.destroy()
        except: pass
        try: Aopt4.destroy()
        except: pass
        try: Aprev.destroy()
        except: pass
        try: Anext.destroy()
        except: pass

        # crea lo stage main
        main()

        # imposto lo stage main come stage corrente
        currentStage = "main"

# funzione per andare al campo successio
def Next():

    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb,syntaxError

    # se lo stage corrente è main
    if currentStage == "main":

        # cancella i widget esistenti
        try: Atitle.destroy()
        except: pass
        try: Asubtitle.destroy()
        except: pass
        try: Aopt1.destroy()
        except: pass
        try: Aopt2.destroy()
        except: pass
        try: Aopt3.destroy()
        except: pass
        try: Aopt4.destroy()
        except: pass
        try: Aprev.destroy()
        except: pass
        try: Anext.destroy()
        except: pass

        # crea lo stage selectFirstBase
        selectFirstBase()

        # imposto lo stage selectFirstBase come stage corrente
        currentStage = "selectFirstBase"

    # se lo stage corrente è selectFirstBase
    elif currentStage == "selectFirstBase":

        # cancella i widget esistenti
        try: Atitle.destroy()
        except: pass
        try: Asubtitle.destroy()
        except: pass
        try: Aopt1.destroy()
        except: pass
        try: Aopt2.destroy()
        except: pass
        try: Aopt3.destroy()
        except: pass
        try: Aopt4.destroy()
        except: pass
        try: Aprev.destroy()
        except: pass
        try: Anext.destroy()
        except: pass

        # crea lo stage selectSecondBase
        selectSecondBase()

        # imposto lo stage selectSecondBase come stage corrente
        currentStage = "selectSecondBase"

    # se lo stage corrente è selectSecondBase
    elif currentStage == "selectSecondBase":

        # cancella i widget esistenti
        try: Atitle.destroy()
        except: pass
        try: Asubtitle.destroy()
        except: pass
        try: Aopt1.destroy()
        except: pass
        try: Aopt2.destroy()
        except: pass
        try: Aopt3.destroy()
        except: pass
        try: Aopt4.destroy()
        except: pass
        try: Aprev.destroy()
        except: pass
        try: Anext.destroy()
        except: pass

        # crea lo stage digitNumb
        digitNumb()

        # imposto lo stage digitNumb come stage corrente
        currentStage = "digitNumb"

    # se lo stage corrente è digitNumb
    elif currentStage == "digitNumb":

        # number to convert
        numb = Aopt1.get()
        if numb != "":
            try:
                if b1 == 2:
                    for i in range(len(numb)):
                        if int(numb[i]) < 2:
                            syntaxError = False
                        else:
                            syntaxError = True
                elif b1 == 8:
                    for i in range(len(numb)):
                        if int(numb[i]) < 8:
                            syntaxError = False
                        else:
                            syntaxError = True
                elif b1 == 10:
                    for i in range(len(numb)):
                        if int(numb[i]) < 10:
                            syntaxError = False
                        else:
                            syntaxError = True
                elif b1 == 16:
                    for i in range(len(numb)):
                        if numb[i].lower() == 'a' or numb[i].lower() == 'b' or numb[i].lower() == 'c' or numb[i].lower() == 'd' or numb[i].lower() == 'e' or numb[i].lower() == 'f' or int(numb[i]) < 10:
                            syntaxError = False
                        else:
                            syntaxError = True
                if syntaxError != True:
                    # decimal number
                    var = toDec(numb, b1)
                    syntaxError = True
                    # number converted
                    convNumb = decTo(var, b2)
                    syntaxError = False
            except:
                syntaxError = True

            if syntaxError == False:

                # cancella i widget esistenti
                try: Atitle.destroy()
                except: pass
                try: Asubtitle.destroy()
                except: pass
                try: Aopt1.destroy()
                except: pass
                try: Aopt2.destroy()
                except: pass
                try: Aopt3.destroy()
                except: pass
                try: Aopt4.destroy()
                except: pass
                try: Aprev.destroy()
                except: pass
                try: Anext.destroy()
                except: pass

                # crea lo stage seeConvertedNumb
                seeConvertedNumb()

                # imposto lo stage seeConvertedNumb come stage corrente
                currentStage = "seeConvertedNumb"
                syntaxError = None
    # se lo stage corrente è seeConvertedNumb
    elif currentStage == "seeConvertedNumb":

        # cancella i widget esistenti
        try: Atitle.destroy()
        except: pass
        try: Asubtitle.destroy()
        except: pass
        try: Aopt1.destroy()
        except: pass
        try: Aopt2.destroy()
        except: pass
        try: Aopt3.destroy()
        except: pass
        try: Aopt4.destroy()
        except: pass
        try: Aprev.destroy()
        except: pass
        try: Anext.destroy()
        except: pass

        # crea lo stage selectFirstBase
        selectFirstBase()

        # imposto lo stage selectFirstBase come stage corrente
        currentStage = "selectFirstBase"

# first base is binary
def b1Bin():
    
    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # set the first base to 2
    b1 = 2

    # scrolls to the next stage
    Next()

# first base is octal
def b1Oct():
    
    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # set the first base to 8
    b1 = 8

    # scrolls to the next stage
    Next()

# first base is decimal
def b1Dec():
    
    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # set the first base to 10
    b1 = 10

    # scrolls to the next stage
    Next()

# first base is hexadecimal
def b1Hex():
    
    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # set the first base to 16
    b1 = 16

    # scrolls to the next stage
    Next()

# second base is binary
def b2Bin():
    
    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # set the second base to 2
    b2 = 2

    # scrolls to the next stage
    Next()

# second base is octal
def b2Oct():
    
    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # set the second base to 8
    b2 = 8

    # scrolls to the next stage
    Next()

# second base is decimal
def b2Dec():
    
    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # set the second base to 10
    b2 = 10

    # scrolls to the next stage
    Next()

# second base is hexadecimal
def b2Hex():
    
    # global variables
    global currentStage,currentSelect,b1,b2,numb,convNumb

    # set the second base to 16
    b2 = 16

    # scrolls to the next stage
    Next()

# creates root
root = Tk()

# sets the title of the root
root.title("Il nostro programma")

# sets the size of the root
root.geometry("600x400")

# sets root not resizable
root.resizable(False,False)

# set the root color
root.configure(bg='#414141')

# main stage
main()

# starts loop
root.mainloop()
