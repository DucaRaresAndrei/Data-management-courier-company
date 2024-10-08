import pyodbc
from tkinter import *
from tkinter import ttk

r = Tk()
r.title("test")
r.geometry("800x300")

# connect with daatbase
string_de_conectare = "driver={SQL SERVER}; server=DESKTOP-GLEEQQT\SQLEXPRESS; database=BD_Proiect; trusted_connection=YES"
conectare = pyodbc.connect(string_de_conectare)
cursor = conectare.cursor()

cursor.execute("SELECT * FROM Curieri")
# for row in cursor.fetchall():
#     print(row)

tree = ttk.Treeview(r)
tree["show"] = "headings"

tree["columns"] = ("CurierID", "Nume", "Prenume", "CNP", "Telefon", "Salariu", "Bonus")
tree.column("CurierID", width=100, minwidth=100, anchor=CENTER)
tree.column("Nume", width=100, minwidth=100, anchor=CENTER)
tree.column("Prenume", width=100, minwidth=100, anchor=CENTER)
tree.column("CNP", width=100, minwidth=100, anchor=CENTER)
tree.column("Telefon", width=100, minwidth=100, anchor=CENTER)
tree.column("Salariu", width=50, minwidth=50, anchor=CENTER)
tree.column("Bonus", width=50, minwidth=50, anchor=CENTER)

tree.heading("CurierID", text="CourierID", anchor=CENTER)
tree.heading("Nume", text="Last Name", anchor=CENTER)
tree.heading("Prenume", text="First Name", anchor=CENTER)
tree.heading("CNP", text="CNP", anchor=CENTER)
tree.heading("Telefon", text="Phone", anchor=CENTER)
tree.heading("Salariu", text="Salary", anchor=CENTER)
tree.heading("Bonus", text="Bonus", anchor=CENTER)

i = 0
for row in cursor:
    tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    i = i + 1

tree.pack()
r.mainloop()



