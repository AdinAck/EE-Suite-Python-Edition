import time
import numpy as np
# main menu
print("EE Suite (Python Edition)")
print(" - By: Adin Ackerman")
time.sleep(1.5)
for i in range(100):
    print("")

class expand: # expand input into usable data
    def __init__(self):
        pass
    def incorporate(self,data):
        if int(data[0]) != 0:
            self.raw = data
            a = np.array([])
            for i in range(len(self.raw)):
                if " " in self.raw[i]:
                    self.val = float(self.raw[:i])
                    self.unit = str(self.raw[i+1:])

            self.scale = 1
            if "p" in self.unit[0]: # pico
                self.scale = 10**(-12)
            if "n" in self.unit[0]: # nano
                self.scale = 10**(-9)
            if "u" in self.unit[0]: # micro
                self.scale = 10**(-6)
            if "m" in self.unit[0]: # milli
                self.scale = 10**(-3)
            if "k" in self.unit[0]: # kilo
                self.scale = 10**(3)
            if "M" in self.unit[0]: # mega
                self.scale = 10**(6)
            if "G" in self.unit[0]: # Giga
                self.scale = 10**(9)
        else:
            self.val = 0
            self.scale = 0

    def unit(self,variable):
        if self.val < 10**(-6):
            self.scale = 10**(-9)
            self.val = round(self.val*10**(9),3)
            self.unit = "n"+variable
        elif self.val < 10**(-3):
            self.scale = 10**(-6)
            self.val = round(self.val*10**(6),3)
            self.unit = "u"+variable
        elif self.val < 1:
            self.scale = 10**(-3)
            self.val = round(self.val*10**(3),3)
            self.unit = "m"+variable
        elif self.val < 10**(3):
            self.scale = 1
            self.val = round(self.val,3)
            self.unit = variable
        elif self.val < 10**(6):
            self.scale = 10**(3)
            self.val = round(self.val*10**(-3),3)
            self.unit = "k"+variable
        elif self.val < 10**(9):
            self.scale = 10**(6)
            self.val = round(self.val*10**(-6),3)
            self.unit = "M"+variable
        elif self.val < 10**(12) or self.val >=10**(12):
            self.scale = 10**(9)
            self.val = round(self.val*10**(-9),3)
            self.unit = "G"+variable

    def format(self,value):
        self.val = value

def err1():
    print("")
    print("==Error==================")
    print("Unable to expand input\ninto usable data,\nperhaps units were not\nspecified?")
    print("==/Error/================")
    print("")
    menu()

def err2():
    print("")
    print("==Error==================")
    print("The number or position of\nunknowns in not\ncompatable with this\ncalculation.")
    print("==/Error/================")
    print("")
    menu()

def menu():
    print("==Menu===================")
    print("[1] Ohm's Law")
    print("[2] Voltage Divider")
    print("[3] Parallel Resistors")
    print("==/Menu/=================")
    print("")

    s = input("")

    if "1" in s:
        ohmLaw()
    elif "2" in s:
        voltDiv()
    elif "3" in s:
        pass

    menu()

def ohmLaw():
    print("")
    print("==Ohm's Law==============")
    print("V = IR")
    print("Enter 0 if value unkown.")
    print("")
    v = expand()
    i = expand()
    r = expand()
    try:
        expand.incorporate(v, input("V = "))
    except TypeError:
        err1()
    try:
        expand.incorporate(i, input("I = "))
    except TypeError:
        err1()
    try:
        expand.incorporate(r, input("R = "))
    except TypeError:
        err1()
    a = np.array([v.val,i.val,r.val])
    if len(np.where(a==0)[0]) != 1:
        err2()
    else:
        v.val = v.val*v.scale
        i.val = i.val*i.scale
        r.val = r.val*r.scale
        print("")
        print("Solution:")
        if v.val == 0:
            v.val = float(i.val*r.val)
            expand.unit(v,"V")
            print("V = "+str(v.val)+" "+v.unit)
        if i.val == 0:
            i.val = float(v.val/r.val)
            expand.unit(i,"A")
            print("I = "+str(i.val)+" "+i.unit)
        if r.val == 0:
            r.val = float(v.val/i.val)
            expand.unit(r,"Ohms")
            print("R = "+str(r.val)+" "+r.unit)
        w = expand()
        expand.format(w, (i.val*i.scale)*(v.val*v.scale))
        expand.unit(w, "W")
        print("W = "+str(w.val)+" "+w.unit)
    print("==/Ohm's Law/============")
    print("")

def voltDiv():
    print("")
    print("==Voltage Divider========")
    print("Vout = Vin(R2/(R1 + R2))")
    print("Enter 0 if value unkown.")
    print("")
    vin = expand()
    vout = expand()
    r1 = expand()
    r2 = expand()
    i = expand()
    try:
        expand.incorporate(vin, input("Vin = "))
    except TypeError:
        err1()
    try:
        expand.incorporate(vout, input("Vout = "))
    except TypeError:
        err1()
    try:
        expand.incorporate(r1, input("R1 = "))
    except TypeError:
        err1()
    try:
        expand.incorporate(r2, input("R2 = "))
    except TypeError:
        err1()
    a = np.array([vin.val,vout.val,r1.val,r2.val])
    if len(np.where(a==0)[0]) >= 3:
        err2()
    elif r1.val == 0 and r2.val == 0:
        print("Additional information required:")
        expand.incorporate(i, input("I = "))
        v = vin.val-vout.val

menu()
