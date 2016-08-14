# -*- coding: cp1252 -*-
import random as r
from Tkinter import *
import threading

#
#   Ohjelmoija: Arttu Koskinen
#   
#   Kuvaus:
#   
#   Huomioitavaa: " THREADING " importtia käytetään vain viiveen luomiseen " TIME.SLEEP " sijasta.
#   




#    Tkinter käyttöliittymän luonti
root = Tk()
root.minsize(450,275)
root.maxsize(450,275)
root.title("NoteCal v0.01")

#spacer0 = Label(root, text="").grid(row=0,column=0,columnspan=1) #spacer <- luodaan tyhjä rivi


#spacer1 = Label(root, text="").grid(row=0,column=0,columnspan=1)

spacer0 = Label(root, text="").grid(row=0,column=0,columnspan=5)

his1 = StringVar()
his2 = StringVar()
his3 = StringVar()


history1 = Label(root, textvariable=his1, width=27, anchor=E, text="", justify=RIGHT).grid(row=1,column=0,columnspan=6)
history2 = Label(root, textvariable=his2, width=27, anchor=E, text="", justify=RIGHT).grid(row=2,column=0,columnspan=6)
history3 = Label(root, textvariable=his3, width=27, anchor=E, text="", justify=RIGHT).grid(row=3,column=0,columnspan=6)



#spacer1 = Label(root, text="").grid(row=4,column=0,columnspan=7)

#   Luodaan tekstiruutu

#ruutuvariable = ruutu.get(1.0, END)
#ruutuvar = IntVar()





ruutu = Entry(root, width=28, relief=FLAT, justify='right')
ruutu.insert(END, "")
ruutucontent = ruutu.get()

ruutu.grid(row=5, column=0, columnspan=6, ipady=10, pady=8)
#spacer2 = Label(root, text="").grid(row=6,column=0,columnspan=7)


notepad = Text(root, width=38, height=16).grid(row=0, column=6, rowspan=11, padx=5)




# Luodaan nappulat
# 7 8 9
# 4 5 6
# 1 2 3
# 0

numButton0var = StringVar()
numButton0var.set("0")

numButton1var = StringVar()
numButton1var.set("1")

numButton2var = StringVar()
numButton2var.set("2")

numButton3var = StringVar()
numButton3var.set("3")

numButton4var = StringVar()
numButton4var.set("4")

numButton5var = StringVar()
numButton5var.set("5")

numButton6var = StringVar()
numButton6var.set("6")

numButton7var = StringVar()
numButton7var.set("7")

numButton8var = StringVar()
numButton8var.set("8")

numButton9var = StringVar()
numButton9var.set("9")

numButtonPILKKUvar = StringVar()
numButtonPILKKUvar.set(",")

numButtonJAKOvar = StringVar()
numButtonJAKOvar.set("/")

numButtonKERTOvar = StringVar()
numButtonKERTOvar.set("*")

numButtonMIINUSvar = StringVar()
numButtonMIINUSvar.set("-")

numButtonPLUSvar = StringVar()
numButtonPLUSvar.set("+")

def num0():
    ruutu.insert(END, numButton0var.get())
    return

def num1():
    ruutu.insert(END, numButton1var.get())
    return

def num2():
    ruutu.insert(END, numButton2var.get())
    return

def num3():
    ruutu.insert(END, numButton3var.get())
    return

def num4():
    ruutu.insert(END, numButton4var.get())
    return

def num5():
    ruutu.insert(END, numButton5var.get())
    return

def num6():
    ruutu.insert(END, numButton6var.get())
    return

def num7():
    ruutu.insert(END, numButton7var.get())
    return

def num8():
    ruutu.insert(END, numButton8var.get())
    return
def num9():
    ruutu.insert(END, numButton9var.get())
    return

def numJAKO():
    ruutu.insert(END, numButtonJAKOvar.get())
    return

def numPILKKU():
    ruutu.insert(END, numButtonPILKKUvar.get())
    return

def numKERTO():
    ruutu.insert(END, numButtonKERTOvar.get())
    return

def numMIINUS():
    ruutu.insert(END, numButtonMIINUSvar.get())
    return

def numPLUS():
    ruutu.insert(END, numButtonPLUSvar.get())
    return

def backspace():
    todo= ruutu.get()[:-1]
    ruutu.delete(0, END)
    ruutu.insert(END, todo)
    

def jakolasku():
    
    















    
    



numButton0 = Button(root, textvariable=numButton0var, command=num0, text="0",height="2", width="10", bd=2)
numButton0.grid(row=10,column=1, columnspan=2)

        
numButton1 = Button(root, textvariable=numButton1var, command=num1, text="1",height="2", width="4", bd=2)
numButton1.grid(row=9,column=1, columnspan=1)

numButton2 = Button(root, textvariable=numButton2var, command=num2, text="2",height="2", width="4", bd=2)
numButton2.grid(row=9,column=2, columnspan=1)

numButton3 = Button(root, textvariable=numButton3var, command=num3, text="3",height="2", width="4", bd=2)
numButton3.grid(row=9,column=3, columnspan=1)


numButton4 = Button(root, textvariable=numButton4var, command=num4, text="4",height="2", width="4", bd=2)
numButton4.grid(row=8,column=1, columnspan=1)

numButton5 = Button(root, textvariable=numButton5var, command=num5, text="5",height="2", width="4", bd=2)
numButton5.grid(row=8,column=2, columnspan=1)

numButton6 = Button(root, textvariable=numButton6var, command=num6, text="6",height="2", width="4", bd=2)
numButton6.grid(row=8,column=3, columnspan=1)


numButton7 = Button(root, textvariable=numButton7var, command=num7, text="7",height="2", width="4", bd=2)
numButton7.grid(row=7,column=1, columnspan=1)

numButton8 = Button(root, textvariable=numButton8var, command=num8, text="8",height="2", width="4", bd=2)
numButton8.grid(row=7,column=2, columnspan=1)

numButton9 = Button(root, textvariable=numButton9var, command=num9, text="9",height="2", width="4", bd=2)
numButton9.grid(row=7,column=3, columnspan=1)


numButtonPILKKU = Button(root, textvariable=numButtonPILKKUvar, command=numPILKKU, text=",",height="2", width="4", bd=2)
numButtonPILKKU.grid(row=10,column=3, columnspan=1)

numButtonJAKO = Button(root, textvariable=numButtonJAKOvar, command=numJAKO, text="/",height="2", width="4", bd=2)
numButtonJAKO.grid(row=7,column=4, columnspan=1)

numButtonKERTO = Button(root, textvariable=numButtonKERTOvar, command=numKERTO, text="*",height="2", width="4", bd=2)
numButtonKERTO.grid(row=8,column=4, columnspan=1)

numButtonMIINUS = Button(root, textvariable=numButtonMIINUSvar, command=numMIINUS, text="-",height="2", width="4", bd=2)
numButtonMIINUS.grid(row=9,column=4, columnspan=1)

numButtonPLUS = Button(root, textvariable=numButtonPLUSvar, command=numPLUS, text="+",height="2", width="4", bd=2)
numButtonPLUS.grid(row=10,column=4, columnspan=1)

numButtonBACK = Button(root, command=backspace, text="<-",height="2", width="4", bd=2)
numButtonBACK.grid(row=7,column=5, columnspan=1)

numButtonNOLLAA = Button(root, text="C",height="2", width="4", bd=2)
numButtonNOLLAA.grid(row=8,column=5, columnspan=1)

numButtonYHTKUIN = Button(root, text="=",height="2", width="4", bd=2, pady=19)
numButtonYHTKUIN.grid(row=9,column=5, columnspan=1, rowspan=2)






# käynnistetään käyttöliittymä

root.mainloop()




















































