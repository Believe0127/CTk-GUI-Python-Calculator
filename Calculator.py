import func
import customtkinter as CTk

CTk.set_appearance_mode('Dark')
CTk.set_default_color_theme('dark-blue')

app = CTk.CTk()
app.title("電卓 - Ver.5.6")
app.geometry("299x330")
app.iconbitmap(default="data/icon.ico")
app.resizable(0,0)

write_entry = CTk.CTkEntry(master=app, state="readonly", placeholder_text="0", placeholder_text_color="gray", height=50, width=250, bg_color='gray', font=("Segoe UI", 19), corner_radius=2, border_color="#22a6e3")
write_entry.pack()
write_entry.place(x=25, y=20)

zero_btn = CTk.CTkButton(master=app, text="0", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("0"))
zerozero_btn = CTk.CTkButton(master=app, text="00", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("00"))
one_btn = CTk.CTkButton(master=app, text="1", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("1"))
two_btn = CTk.CTkButton(master=app, text="2", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("2"))
three_btn = CTk.CTkButton(master=app, text="3", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("3"))
four_btn = CTk.CTkButton(master=app, text="4", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("4"))
five_btn = CTk.CTkButton(master=app, text="5", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("5"))
six_btn = CTk.CTkButton(master=app, text="6", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("6"))
seven_btn = CTk.CTkButton(master=app, text="7", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("7"))
eight_btn = CTk.CTkButton(master=app, text="8", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("8"))
nine_btn = CTk.CTkButton(master=app, text="9", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("9"))

zero_btn.place(x=85, y=270)
zerozero_btn.place(x=20, y=270)
one_btn.place(x=20, y=225)
two_btn.place(x=85, y=225)
three_btn.place(x=150, y=225)
four_btn.place(x=20, y=180)
five_btn.place(x=85, y=180)
six_btn.place(x=150, y=180)
seven_btn.place(x=20, y=135)
eight_btn.place(x=85, y=135)
nine_btn.place(x=150, y=135)

AC_btn = CTk.CTkButton(master=app, text="AC", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=func.AC)
C_btn = CTk.CTkButton(master=app, text="C", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838",command=func.C)
percent_btn = CTk.CTkButton(master=app, text="%", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=func.percent_calculate)
plus_btn = CTk.CTkButton(master=app, text='+', height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("+"))
minus_btn = CTk.CTkButton(master=app, text='ー', height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("-"))
multiplication_btn = CTk.CTkButton(master=app, text='×', height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("×"))
divide_btn = CTk.CTkButton(master=app, text="÷", height=45, width=65, font=("Segoe UI", 26), hover_color="#484848", fg_color="#383838", command=lambda:func.write("÷"))
konma_btn = CTk.CTkButton(master=app, text=".", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=lambda:func.write("."))
equal_btn = CTk.CTkButton(master=app, text="=", height=45, width=65, font=("Segoe UI", 28), hover_color="#484848", fg_color="#383838", command=func.Calculate)

AC_btn.place(x=20, y=90)
C_btn.place(x=150, y=90)
percent_btn.place(x=85, y=90)
equal_btn.place(x=215, y=270)
konma_btn.place(x=150, y=270)
plus_btn.place(x=215, y=90)
minus_btn.place(x=215, y=180)
multiplication_btn.place(x=215, y=135)
divide_btn.place(x=215, y=225)

app.mainloop()