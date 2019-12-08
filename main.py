import time
import numpy as np
# main menu
print("EE Suite (Python Edition)")
print(" - By: Adin Ackerman")
# time.sleep(1.5)
for i in range(100):
    print("")
print("==Menu===================")
print("[1] Ohm's Law")
print("[2] Voltage Divider")
print("[3] Parallel Resistors")
print("=========================")
print("")

s = input("")

class expand: # expand input into usable data
    def __init__(self,data):
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

    def unit(self,v):
        if self.val < 10**(-5):
            self.val = self.val*10**(9)
            self.unit = "n"+v
        elif self.val < 10**(-2):
            self.val = self.val*10**(6)
            self.unit = "u"+v
        elif self.val < 1:
            self.val = self.val*10**(3)
            self.unit = "m"+v
        elif self.val < 10**(3):
            self.val = self.val
            self.unit = v
        elif self.val < 10**(6):
            self.val = self.val*10**(-3)
            self.unit = "k"+v
        elif self.val < 10**(9):
            self.val = self.val*10**(-6)
            self.unit = "M"+v
        elif self.val < 10**(12) or self.val >=10**(12):
            self.val = self.val*10**(-9)
            self.unit = "G"+v

if "1" in s:
    print("")
    print("==Ohm's Law Calculator===")
    print("V = IR")
    print("Enter 0 if value unkown.")
    print("")
    v = expand(input("V = "))
    i = expand(input("I = "))
    r = expand(input("R = "))
    a = np.array([v.val,i.val,r.val])
    if len(np.where(a==0)[0]) >= 2:
        print("Insufficient data.")
    else:
        v.val = v.val*v.scale
        i.val = i.val*i.scale
        r.val = r.val*r.scale
        if v.val == 0:
            v.val = float(i.val*r.val)
        if i.val == 0:
            i.val = float(v.val/r.val)
        if r.val == 0:
            r.val = float(v.val/i.val)
        print("W: "+str(w))
        expand.unit(v,"V")
        expand.unit(i,"A")
        expand.unit(r,"Ohms")
        print("")
        print("Solution:")
        print("V = "+str(v.val)+" "+v.unit)
        print("I = "+str(i.val)+" "+i.unit)
        print("R = "+str(r.val)+" "+r.unit)
        # print("Power loss: "+str(w.val)+" "+w.unit)
    print("==Ohm's Law Calculator===")
    print("")
elif "2" in s:
    pass
elif "3" in s:
    pass
