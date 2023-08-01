#-作成に5時間かかった--

import customtkinter as CTk
import pyperclip

CTk.set_appearance_mode('Dark')
CTk.set_default_color_theme('blue')

app = CTk.CTk()
app.title("電卓 V5")
app.geometry("299x370")
app.iconbitmap(default="./icon/icon.ico")


def C():
    value = len(write_entry.get())-1#終わりの1つ前
    write_entry.delete(value, CTk.END)

def AC():
    write_entry.delete(0, CTk.END)
    ans_entry.delete(0, CTk.END)

def copy_ans():
    copys = ans_entry.get()
    pyperclip.copy(copys)

def write0():
    write_entry.insert(CTk.END, '0')

def write00():
    write_entry.insert(CTk.END, '00')

def write1():
    write_entry.insert(CTk.END, '1')

def write2():
    write_entry.insert(CTk.END, '2')

def write3():
    write_entry.insert(CTk.END, '3')

def write4():
    write_entry.insert(CTk.END, '4')

def write5():
    write_entry.insert(CTk.END, '5')

def write6():
    write_entry.insert(CTk.END, '6')

def write7():
    write_entry.insert(CTk.END, '7')

def write8():
    write_entry.insert(CTk.END, '8')

def write9():
    write_entry.insert(CTk.END, '9')

def write_plus(): 
    write_entry.insert(CTk.END, '+')

def write_minus():
    write_entry.insert(CTk.END, '-')

def write_multiplication():
    write_entry.insert(CTk.END, '*')

def write_divide():
    write_entry.insert(CTk.END, '/')

def write_konma():
    write_entry.insert(CTk.END, '.')

def Calculate():
    value = eval(write_entry.get())
    ans_entry.delete(0, CTk.END)
    ans_entry.insert(0, value)
    

write_entry = CTk.CTkEntry(master=app, height=50, width=250, bg_color='gray', text_color='#91f4ff', justify=CTk.LEFT, font=('Heaveltica', 23, 'bold'))
write_entry.pack()
write_entry.place(x=25, y=20)

zero_btn = CTk.CTkButton(master=app, text="0", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write0)
zerozero_btn = CTk.CTkButton(master=app, text="00", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write00)
one_btn = CTk.CTkButton(master=app, text="1", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write1)
two_btn = CTk.CTkButton(master=app, text="2", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write2)
three_btn = CTk.CTkButton(master=app, text="3", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write3)
four_btn = CTk.CTkButton(master=app, text="4", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write4)
five_btn = CTk.CTkButton(master=app, text="5", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write5)
six_btn = CTk.CTkButton(master=app, text="6", height=45, width=65, font=('Heavaltica', 23, 'bold'), command=write6)
seven_btn = CTk.CTkButton(master=app, text="7", height=45, width=65, font=('Heavaltica', 23, 'bold'), command=write7)
eight_btn = CTk.CTkButton(master=app, text="8", height=45, width=65, font=('Heavaltica', 23, 'bold'), command=write8)
nine_btn = CTk.CTkButton(master=app, text="9", height=45, width=65, font=('Heavaltica', 23, 'bold'), command=write9)

one_btn.pack()
zero_btn.pack()
zerozero_btn.pack()
two_btn.pack()
three_btn.pack()
four_btn.pack()
five_btn.pack()
six_btn.pack()
seven_btn.pack()
eight_btn.pack()
nine_btn.pack()

zero_btn.place(x=85, y=320)
zerozero_btn.place(x=20, y=320)
one_btn.place(x=20, y=275)
two_btn.place(x=85, y=275)
three_btn.place(x=150, y=275)
four_btn.place(x=20, y=230)
five_btn.place(x=85, y=230)
six_btn.place(x=150, y=230)
seven_btn.place(x=20, y=185)
eight_btn.place(x=85, y=185)
nine_btn.place(x=150, y=185)

AC_btn = CTk.CTkButton(master=app, text="AC", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=AC)
C_btn = CTk.CTkButton(master=app, text="C", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=C)
copy_btn = CTk.CTkButton(master=app, text="Copy", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=copy_ans)
plus_btn = CTk.CTkButton(master=app, text='+', height=45, width=65, font=('Heavaltica', 23, 'bold'), command=write_plus)
minus_btn = CTk.CTkButton(master=app, text='ー', height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write_minus)
multiplication_btn = CTk.CTkButton(master=app, text='×', height=45, width=65, font=('Heavaltica', 23, 'bold'), command=write_multiplication)
divide_btn = CTk.CTkButton(master=app, text="÷", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write_divide)
konma_btn = CTk.CTkButton(master=app, text=".", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=write_konma)
equal_btn = CTk.CTkButton(master=app, text="=", height=45, width=65, font=('Heaveltica', 23, 'bold'), command=Calculate)

AC_btn.pack()
C_btn.pack()
copy_btn.pack()
equal_btn.pack()
konma_btn.pack()
plus_btn.pack()
minus_btn.pack()
multiplication_btn.pack()
divide_btn.pack()

AC_btn.place(x=85, y=140)
C_btn.place(x=150, y=140)
copy_btn.place(x=14, y=140)
equal_btn.place(x=215, y=320)
konma_btn.place(x=150, y=320)
plus_btn.place(x=215, y=275)
minus_btn.place(x=215, y=230)
multiplication_btn.place(x=215, y=185)
divide_btn.place(x=215, y=140)

ans_entry = CTk.CTkEntry(master=app, height=35, width=135, font=('Heavaltica', 20, 'bold'))
ans_label = CTk.CTkLabel(master=app, text='Answer: ', height=20, width=20, font=('Heavaltica', 15, 'bold'))
ans_entry.pack()
ans_entry.place(x=85, y=77)
ans_label.pack()
ans_label.place(x=25, y=85)


app.mainloop()