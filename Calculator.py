import customtkinter as CTk

#def main() -> None:
class Calculator(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.rendering_items = [
           'AC','%','C','+'
           ,'7','8','9','×'
           ,'4','5','6','ー'
           ,'1','2','3','÷'
           ,'00','0','.','='
        ]

        self.title("電卓")
        self.geometry("299x330")
        self.iconbitmap(default="data/icon.ico")
        self.resizable(0, 0)
        
        self.Setup_UI()

    def Setup_UI(self):
        CTk.set_default_color_theme('dark-blue')
        CTk.set_appearance_mode('Dark')

        self.write_entry = CTk.CTkEntry(
            master=self, state="readonly", placeholder_text="0", placeholder_text_color="gray", height=50, 
            width=250, bg_color='gray', font=("Segoe UI", 19), corner_radius=2, border_color="#50b4f0"
        )
        self.write_entry.place(x=25, y=20)
      
        posX = 20
        posY = 90
        for char in self.rendering_items:
            if char == "AC":
                CTk.CTkButton(
                    master=self, text="AC", height=45, width=65, font=("Segoe UI", 28),
                    hover_color="#484848", fg_color="#383838", command=self.AllClear
                ).place(x=posX, y=posY)
            elif char == "C":
                CTk.CTkButton(
                    master=self, text="C", height=45, width=65, font=("Segoe UI", 28),
                    hover_color="#484848", fg_color="#383838", command=self.Clear
                ).place(x=posX, y=posY)
            elif char == "%":
                CTk.CTkButton(
                    master=self, text="%", height=45, width=65, font=("Segoe UI", 28),
                    hover_color="#484848", fg_color="#383838", command=self.percent_calculate
                ).place(x=posX, y=posY)
            elif char == "=":
                CTk.CTkButton(
                    master=self, text="=", height=45, width=65, font=("Segoe UI", 28),
                    hover_color="#484848", fg_color="#383838", command=self.Calculate
                ).place(x=posX, y=posY)
            else:
                CTk.CTkButton(
                    master=self, text=char, height=45, width=65, font=("Segoe UI", 28),
                    hover_color="#484848", fg_color="#383838", command=lambda char=char: self.write(char)
                ).place(x=posX, y=posY)
            
            posX += 65
            if (posX > 215):
                posY += 45
                
                posX = 20 # 初期位置に戻す

    def Clear(self):
        self.write_entry.configure(state="normal")

        value = len(self.write_entry.get()) - 1 #終わりの1つ前
        self.write_entry.delete(value, CTk.END)

        self.write_entry.configure(state="readonly")

    def AllClear(self):
        self.write_entry.configure(state="normal")

        self.write_entry.delete(0, CTk.END)

        self.write_entry.configure(state="readonly")

    def percent_calculate(self):
        self.write_entry.configure(state="normal")

        value = float(self.write_entry.get())
        ans   = value / 100
        
        self.write_entry.delete(0, CTk.END)
        self.write_entry.insert(0, ans)

        self.write_entry.configure(state="readonly")

    def write(self, text: str):
        self.write_entry.configure(state="normal")

        self.write_entry.insert(CTk.END, text)

        self.write_entry.configure(state="readonly")

    def Calculate(self):
        self.write_entry.configure(state="normal")
        
        try:
            self.write_entry.insert(CTk.END, '=' + str(eval(self.write_entry.get().replace("×", "*").replace("÷", "/"))))
        except SyntaxError:
            self.write_entry.delete(first_index=0, last_index=CTk.END)

        self.write_entry.configure(state="readonly")

if __name__ == "__main__":
    calclator = Calculator()
    calclator.mainloop()
