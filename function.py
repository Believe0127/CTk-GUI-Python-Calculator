import Calculator as clt
import customtkinter as CTk

def C():
    value = len(clt.write_entry.get())-1#終わりの1つ前
    clt.write_entry.delete(value, CTk.END)

def AC():
    clt.write_entry.delete(0, CTk.END)

def percent_calculate():
    value = int(clt.write_entry.get())
    ans =  value / 100
    clt.write_entry.delete(0, CTk.END)
    clt.write_entry.insert(0, ans)

def write0():
    clt.write_entry.insert(CTk.END, '0')

def write00():
    clt.write_entry.insert(CTk.END, '00')

def write1():
    clt.write_entry.insert(CTk.END, '1')

def write2():
    clt.write_entry.insert(CTk.END, '2')

def write3():
    clt.write_entry.insert(CTk.END, '3')

def write4():
    clt.write_entry.insert(CTk.END, '4')

def write5():
    clt.write_entry.insert(CTk.END, '5')

def write6():
    clt.write_entry.insert(CTk.END, '6')

def write7():
    clt.write_entry.insert(CTk.END, '7')

def write8():
    clt.write_entry.insert(CTk.END, '8')

def write9():
    clt.write_entry.insert(CTk.END, '9')

def write_plus(): 
    clt.write_entry.insert(CTk.END, '+')

def write_minus():
    clt.write_entry.insert(CTk.END, '-')

def write_multiplication():
    clt.write_entry.insert(CTk.END, '*')

def write_divide():
    clt.write_entry.insert(CTk.END, '/')

def write_konma():
    clt.write_entry.insert(CTk.END, '.')

def Calculate():
    value = eval(clt.write_entry.get())
    clt.write_entry.insert(CTk.END, '=' + str(value))