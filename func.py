import Calculator as clt

def C():
    clt.write_entry.configure(state="normal")
    value = len(clt.write_entry.get()) -1 #終わりの1つ前
    clt.write_entry.delete(value, clt.CTk.END)
    clt.write_entry.configure(state="readonly")

def AC():
    clt.write_entry.configure(state="normal")
    clt.write_entry.delete(0, clt.CTk.END)
    clt.write_entry.configure(state="readonly")

def percent_calculate():
    clt.write_entry.configure(state="normal")
    value = int(clt.write_entry.get())
    ans =  value / 100
    clt.write_entry.delete(0, clt.CTk.END)
    clt.write_entry.insert(0, ans)
    clt.write_entry.configure(state="readonly")

def write(string: str):
    clt.write_entry.configure(state="normal")
    clt.write_entry.insert(clt.CTk.END, string)
    clt.write_entry.configure(state="readonly")

def Calculate():
    clt.write_entry.configure(state="normal")
    try:
        clt.write_entry.insert(clt.CTk.END, '=' + str(eval(clt.write_entry.get().replace("×", "*").replace("÷", "/"))))
    except SyntaxError:
        clt.write_entry.delete(first_index=0, last_index=clt.CTk.END)
    clt.write_entry.configure(state="readonly")