# -*- coding: cp1252 -*-
import random as r
from Tkinter import *
import threading
from decimal import Decimal

#
#   Ohjelmoija: Arttu Koskinen
#   
#   Kuvaus:
#   
#   Huomioitavaa: " THREADING " importtia käytetään vain viiveen luomiseen " TIME.SLEEP " sijasta.
#   



#    Tkinter käyttöliittymän luonti
root = Tk()
root.minsize(450,285)
root.maxsize(450,285)
root.title("NoteCal v0.01")


spacer0 = Label(root, text="").grid(row=0,column=0,columnspan=5) #spacer <- luodaan tyhjä rivi


# Luodaan StringVar muuttujat laskuhistorian näyttämistä varten


his1 = StringVar()
his2 = StringVar()
his3 = StringVar()
his1.set("")
his2.set("")
his3.set("")

#luodaan muuttuja, joka määrittelee mitä seuraavaksi tehdään

laskutoimitus = IntVar()
laskutoimitus.set(-1)

# -1 = ei laskutoimitusta
# 0  = Jakolasku
# 1  = Kertolasku
# 2  = Miinuslasku
# 3  = Pluslasku
# 4  = Jakolasku uudelleen
# 5  = Kertolasku uudelleen
# 6  = Miinuslasku uudelleen
# 7  = Pluslasku uudelleen


# Luodaan Labelit historian näyttämiseen

history1 = Label(root, textvariable=his1, width=22, anchor=E, text="", justify=RIGHT).grid(row=1,column=0,columnspan=5)
history2 = Label(root, textvariable=his2, width=22, anchor=E, text="", justify=RIGHT).grid(row=2,column=0,columnspan=5)
history3 = Label(root, textvariable=his3, width=22, anchor=E, text="", justify=RIGHT).grid(row=3,column=0,columnspan=5)

# Luodaan funktiot nappuloille, jotka tulevat historialabeleiden viereen

def historyB1():
    if len(notepad.get(1.0, END)) > 1:
        notepad.insert(INSERT, "\n" + str(his1.get()))
    else:
        notepad.insert(INSERT, str(his1.get()))


def historyB2():
    if len(notepad.get(1.0, END)) > 1:
        notepad.insert(INSERT, "\n" + str(his2.get()))
    else:
        notepad.insert(INSERT, str(his2.get()))


def historyB3():
    if len(notepad.get(1.0, END)) > 1:
        notepad.insert(INSERT, "\n" + str(his3.get()))
    else:
        notepad.insert(INSERT, str(his3.get()))

def historyB4():
    if len(notepad.get(1.0, END)) > 1:
        notepad.insert(INSERT, "\n" + str(ruutu.get()))
    else:
        notepad.insert(INSERT, str(ruutu.get()))

# Luodaan nappulat historian liikuttelua varten

history1button = Button(root, command=historyB1, height=0, width=1, text=">" ).grid(row=1,column=5,columnspan=1)
history2button = Button(root, command=historyB2, height=0, width=1, text=">"  ).grid(row=2,column=5,columnspan=1)
history3button = Button(root, command=historyB3, height=0, width=1, text=">"  ).grid(row=3,column=5,columnspan=1)



# Luodaan ruutu, johon voi näppäillä numeroita

ruutu = Entry(root, width=22, relief=FLAT, justify='right') #28
ruutu.insert(END, "")
ruutucontent = ruutu.get()

ruutu.grid(row=5, column=0, columnspan=5, ipady=10, pady=8) #colspan 6

# Luodaan vielä yksi historianappi numeroikkunan viereen

history4button = Button(root, command=historyB4, height=0, width=1, text=">"  ).grid(row=5,column=5,columnspan=1)

# Luodaan teksti-ikkuna, jossa tekstinkäsittely tapahtuu

notepad = Text(root, width=38, height=18) #width 38 height 16
notepad.grid(row=0, column=6, rowspan=11, padx=5)



lasku = False # Muuttuja keskeneräiselle toiminnolle



# Luodaan paljon muuttujia nappuloille, jotta niiden sisältöä voi muuttaa funktioista käsin


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
numButtonPILKKUvar.set(".")

numButtonJAKOvar = StringVar()
numButtonJAKOvar.set(" / ")

numButtonKERTOvar = StringVar()
numButtonKERTOvar.set(" * ")

numButtonMIINUSvar = StringVar()
numButtonMIINUSvar.set(" - ")

numButtonPLUSvar = StringVar()
numButtonPLUSvar.set(" + ")

# Luodaan funktiot numeronäppäimistölle


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



# Funktio laskutoimenpiteelle, jokainen näistä tekee suunnilleen samat asiat

def numJAKO():
    if lasku == False:
        global value1
        value1 = float(ruutu.get())
        laskutoimitus.set(0)
        ruutu.insert(END, numButtonJAKOvar.get())
        his3.set(ruutu.get())
        root.update()
        ruutu.delete(0, END)
        return value1
    else:
        return

# Funktio, joka ensin ottaa laskutoimituksen nimen ja sitten hoitaa value1 ja value2 oikein laskennan
    
def numYHTKUIN():
    if laskutoimitus.get() == 0:
        value2 = float(ruutu.get())
        lopputulos = float(value1) / float(value2)
        ruutu.delete(0, END)
        ruutu.insert(END, lopputulos)
        lopputulos = float(lopputulos)
        global value1
        value1 = lopputulos
        global value2
        value2 = value2
        his1.set(his2.get())
        his2.set(his3.get())
        his3.set(his3.get() + str(value2) + " = " + str(lopputulos))
        laskutoimitus.set(4)

    elif laskutoimitus.get() == 1:
        value2 = float(ruutu.get())
        lopputulos = float(value1) * float(value2)
        ruutu.delete(0, END)
        ruutu.insert(END, lopputulos)
        lopputulos = float(lopputulos)
        global value1
        value1 = lopputulos
        global value2
        value2 = value2
        his1.set(his2.get())
        his2.set(his3.get())
        his3.set(his3.get() + str(value2) + " = " + str(lopputulos))
        laskutoimitus.set(5)

    elif laskutoimitus.get() == 2:
        value2 = float(ruutu.get())
        lopputulos = float(value1) - float(value2)
        ruutu.delete(0, END)
        ruutu.insert(END, lopputulos)
        lopputulos = float(lopputulos)
        global value1
        value1 = lopputulos
        global value2
        value2 = value2
        his1.set(his2.get())
        his2.set(his3.get())
        his3.set(his3.get() + str(value2) + " = " + str(lopputulos))
        laskutoimitus.set(6)

    elif laskutoimitus.get() == 3:
        value2 = float(ruutu.get())
        lopputulos = float(value1) + float(value2)
        ruutu.delete(0, END)
        ruutu.insert(END, lopputulos)
        lopputulos = float(lopputulos)
        global value1
        value1 = lopputulos
        global value2
        value2 = value2
        his1.set(his2.get())
        his2.set(his3.get())
        his3.set(his3.get() + str(value2) + " = " + str(lopputulos))
        laskutoimitus.set(7)

    elif laskutoimitus.get() == 4:
        lopputulos = float(value1) * float(value2)
        ruutu.delete(0, END)
        ruutu.insert(END, lopputulos)
        lopputulos = float(lopputulos)
        his1.set(his2.get())
        his2.set(his3.get())
        his3.set(str(value1) + " / " + str(value2) + " = " + str(lopputulos))
        global value1
        value1 = lopputulos
        global value2
        value2 = value2
        laskutoimitus.set(4)
        return

    elif laskutoimitus.get() == 5:
        lopputulos = float(value1) * float(value2)
        ruutu.delete(0, END)
        ruutu.insert(END, lopputulos)
        lopputulos = float(lopputulos)
        his1.set(his2.get())
        his2.set(his3.get())
        his3.set(str(value1) + " * " + str(value2) + " = " + str(lopputulos))
        global value1
        value1 = lopputulos
        global value2
        value2 = value2
        laskutoimitus.set(5)
        return


    elif laskutoimitus.get() == 6:
        lopputulos = float(value1) - float(value2)
        ruutu.delete(0, END)
        ruutu.insert(END, lopputulos)
        lopputulos = float(lopputulos)
        his1.set(his2.get())
        his2.set(his3.get())
        his3.set(str(value1) + " - " + str(value2) + " = " + str(lopputulos))
        global value1
        value1 = lopputulos
        global value2
        value2 = value2
        laskutoimitus.set(6)
        return


    elif laskutoimitus.get() == 7:
        lopputulos = float(value1) + float(value2)
        ruutu.delete(0, END)
        ruutu.insert(END, lopputulos)
        lopputulos = float(lopputulos)
        his1.set(his2.get())
        his2.set(his3.get())
        his3.set(str(value1) + " + " + str(value2) + " = " + str(lopputulos))
        global value1
        value1 = lopputulos
        global value2
        value2 = value2
        laskutoimitus.set(7)
        return

# Nollausnappulan funktio


def numNOLLAA():
    value1 = 0
    value2 = 0
    ruutu.delete(0, END)
    laskutoimitus.set(-1)

# Pilkkunappulan funktio

def numPILKKU():
    ruutu.insert(END, numButtonPILKKUvar.get())
    return

# Kertolasku

def numKERTO():
    if lasku == False:
        global value1
        value1 = float(ruutu.get())
        laskutoimitus.set(1)
        ruutu.insert(END, numButtonKERTOvar.get())
        his3.set(ruutu.get())
        root.update()
        ruutu.delete(0, END)
        return value1
    else:
        return

# Vähennyslasku

def numMIINUS():
    if lasku == False:
        global value1
        value1 = float(ruutu.get())
        laskutoimitus.set(2)
        ruutu.insert(END, numButtonMIINUSvar.get())
        his3.set(ruutu.get())
        root.update()
        ruutu.delete(0, END)
        return value1
    else:
        return

# Yhteenlasku

def numPLUS():
    if lasku == False:
        global value1
        value1 = float(ruutu.get())
        laskutoimitus.set(3)
        ruutu.insert(END, numButtonPLUSvar.get())
        his3.set(ruutu.get())
        root.update()
        ruutu.delete(0, END)
        return value1
    else:
        return

# Numeroiden poistonappula

def backspace():
    todo = ruutu.get()[:-1]
    ruutu.delete(0, END)
    ruutu.insert(END, todo)
    



# Luodaan numeronäppäimistön nappulat

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

numButtonNOLLAA = Button(root, command=numNOLLAA, text="C",height="2", width="4", bd=2)
numButtonNOLLAA.grid(row=8,column=5, columnspan=1)

numButtonYHTKUIN = Button(root, command=numYHTKUIN, text="=",height="2", width="4", bd=2, pady=19)
numButtonYHTKUIN.grid(row=9,column=5, columnspan=1, rowspan=2)



# Viimein käynnistetään käyttöliittymä

root.mainloop()




















































