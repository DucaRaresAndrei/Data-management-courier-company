from tkinter import *
import pyodbc
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk

string_de_conectare = r"driver={SQL SERVER}; server=DESKTOP-FA5P09O\SQLEXPRESS; database=BD_Proiect; trusted_connection=YES"

class ShowWindow:

    def __init__(self, window):
        self.show_win = window
        self.show_win.title("Show Menu")
        self.show_win.geometry("400x500")
        self.photo = PhotoImage(file="motorbike.png")
        self.show_win.iconphoto(False, self.photo)
        self.show_win.resizable(False, False)

        # BACKGROUND IMAGE
        self.bg_image = ImageTk.PhotoImage(file="poza3.jpg")
        self.bg = Label(self.show_win, image=self.bg_image).place(x=0, y=0, relwidth=1, relheight=1)

        self.canvas = Canvas(self.show_win, bg="#ccc0a6", bd=0, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        # GRID CONFIG
        self.show_win.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.show_win.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # TITLE
        self.title = Label(self.show_win, text="Show menu", bg="#ccc0a6", fg="#8b8378", font=("Impact", 35, "bold"))
        self.title.grid(row=0, columnspan=3)

        # BUTTONS
        self.image1 = PhotoImage(file="parcel_show.png")
        self.button1 = Button(self.show_win, command=self.show_orders_window, image=self.image1,
                              background="#ccc0a6", borderwidth=0)
        self.button1.grid(column=0, row=1)

        self.image2 = PhotoImage(file="courier_button.png")
        self.button2 = Button(self.show_win, image=self.image2, command=self.show_couriers_for_zone,
                              background="#ccc0a6", borderwidth=0)
        self.button2.grid(column=1, row=1)

        self.image3 = PhotoImage(file="client.png")
        self.button3 = Button(self.show_win, image=self.image3, command=self.show_parcels,
                              background="#ccc0a6", borderwidth=0)
        self.button3.grid(column=2, row=1)

        self.image4 = PhotoImage(file="area.png")
        self.button4 = Button(self.show_win, image=self.image4, command=self.show_locations,
                              background="#ccc0a6", borderwidth=0)
        self.button4.grid(column=0, row=2)

        self.image5 = PhotoImage(file="salary.png")
        self.button5 = Button(self.show_win, image=self.image5, command=self.show_top3,
                              background="#ccc0a6", borderwidth=0)
        self.button5.grid(column=2, row=2)

        self.img6 = PhotoImage(file="employer.png")
        self.button6 = Button(self.show_win, image=self.img6, command=self.show_best_emp,
                              background="#ccc0a6", borderwidth=0)
        self.button6.grid(column=0, row=3)

        self.img7 = PhotoImage(file="trend.png")
        self.button7 = Button(self.show_win, image=self.img7, command=self.show_best_year,
                              background="#ccc0a6", borderwidth=0)
        self.button7.grid(column=2, row=3)

        self.img8 = PhotoImage(file="profit.png")
        self.button8 = Button(self.show_win, image=self.img8, command=self.show_most_expensive_ord,
                              background="#ccc0a6", borderwidth=0)
        self.button8.grid(column=0, row=4)

        self.img9 = PhotoImage(file="customer-loyalty.png")
        self.button9 = Button(self.show_win, image=self.img9, command=self.show_loyal_customers,
                              background="#ccc0a6", borderwidth=0)
        self.button9.grid(column=2, row=4)

        self.icon = PhotoImage(file="analytics.png")
        self.lab = Label(self.show_win, image=self.icon, background="#ccc0a6")
        self.lab.grid(column=1, row=2, rowspan=2)

    def show_orders_window(self):
        self.show_orders_root = Toplevel()
        self.show_orders_root.title("Show orders")
        self.show_orders_root.geometry("400x400+520+100")
        self.show_orders_root.resizable(False, False)
        self.show_orders_root.config(bg="#ccc0a6")
        self.photo = PhotoImage(file="motorbike.png")
        self.show_orders_root.iconphoto(False, self.photo)

        self.canvas = Canvas(self.show_orders_root, bg="#ccc0a6", bd=0, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        # GRID CONFIG
        self.show_orders_root.columnconfigure(0, weight=1)
        self.show_orders_root.columnconfigure(1, weight=1)
        self.show_orders_root.columnconfigure(2, weight=4)
        self.show_orders_root.rowconfigure(0, weight=1)
        self.show_orders_root.rowconfigure(1, weight=1)
        self.show_orders_root.rowconfigure(2, weight=1)
        self.show_orders_root.rowconfigure(3, weight=1)
        self.show_orders_root.rowconfigure(4, weight=2)
        self.show_orders_root.rowconfigure(5, weight=2)

        self.text = Label(self.show_orders_root, text="Choose the order by parcel", bg="#ccc0a6", fg="black",
                            font=("proxima nova", 15))
        self.text.grid(row=0, columnspan=3, sticky=SW)

        self.parcel_name = Label(self.show_orders_root, text="Name", bg="#ccc0a6", fg="black",
                                 font=("proxima nova", 12))
        self.parcel_name.grid(column=0, row=1, sticky=E)
        self.parcel_name_entry = Entry(self.show_orders_root, font=("proxima nova", 12))
        self.parcel_name_entry.grid(column=1, row=1)

        self.parcel_code = Label(self.show_orders_root, text="Code", bg="#ccc0a6", fg="black",
                                 font=("proxima nova", 12))
        self.parcel_code.grid(column=0, row=2, sticky=NE)
        self.parcel_code_entry = Entry(self.show_orders_root, font=("proxima nova", 12))
        self.parcel_code_entry.grid(column=1, row=2, sticky=N)

        self.image8 = PhotoImage(file="play-button.png")
        self.button = Button(self.show_orders_root, command=self.show_orders_fct, image=self.image8, bg="#ccc0a6",
                             borderwidth=0)
        self.button.grid(column=1, row=3, sticky=N)

    def show_orders_fct(self):
        if self.parcel_name_entry.get() == "" or self.parcel_code_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.show_orders_root)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()
                cursor.execute(
                    "SELECT Col.ColetID, Col.Denumire, Col.Cod, C.Nume + ' ' + C.Prenume AS Curier, Exped.Nume + ' ' +"
                    " Exped.Prenume AS Expeditor FROM Colete Col INNER JOIN Curieri C ON Col.CurierID = C.CurierID "
                    "INNER JOIN ClientiColete CC ON Col.ColetID = CC.ColetID "
                    "INNER JOIN Clienti Exped ON CC.ClientID = Exped.ClientID AND Exped.TipClient = 'Expeditor' "
                    "WHERE Col.Cod = ? AND Col.Denumire = ?", self.parcel_code_entry.get(),
                    self.parcel_name_entry.get())

                expeditori = []
                for row in cursor.fetchall():
                    expeditori.append(row)

                cursor.execute(
                    "SELECT Col.ColetID, Col.Denumire, Dest.Nume + ' ' + Dest.Prenume AS Destinatar FROM Colete Col "
                    "INNER JOIN ClientiColete CC ON Col.ColetID = CC.ColetID "
                    "INNER JOIN Clienti Dest ON CC.ClientID = Dest.ClientID AND Dest.TipClient = 'Destinatar'"
                    "WHERE Col.Cod = ? AND Col.Denumire = ?", self.parcel_code_entry.get(),
                self.parcel_name_entry.get())

                destinatari = []
                for row in cursor.fetchall():
                    destinatari.append(row)

                string_to_show = f"Colet(Denumire & Cod): {expeditori[0][1]} {expeditori[0][2]} \n" \
                                 f"Curier: {expeditori[0][3]}\nExpeditor: {expeditori[0][4]}\n" \
                                 f"Destinatar: {destinatari[0][2]}"

                self.show_l = Label(self.show_orders_root, text=string_to_show, font=("proxima nova", 12),
                                    bg="#ccc0a6", fg="black", relief="sunken", justify="left")
                self.show_l.grid(row=4, columnspan=3)

                self.image7 = PhotoImage(file="ok.png")
                self.image_l = Label(self.show_orders_root, image=self.image7, bg="#ccc0a6")
                self.image_l.grid(row=5, columnspan=3)

                # commit changes
                cursor.commit()
                # close connection
                conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.show_orders_root)

    def show_couriers_for_zone(self):
        self.show_couriers_win = Toplevel()
        self.show_couriers_win.title("Show couriers for a zone")
        self.show_couriers_win.geometry("500x500+520+100")
        self.show_couriers_win.resizable(False, False)
        self.show_couriers_win.config(bg="#ccc0a6")
        self.photo = PhotoImage(file="motorbike.png")
        self.show_couriers_win.iconphoto(False, self.photo)

        self.canvas = Canvas(self.show_couriers_win, bg="#ccc0a6", bd=0, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        # GRID CONFIG
        self.show_couriers_win.columnconfigure(0, weight=1)
        self.show_couriers_win.columnconfigure(1, weight=1)
        self.show_couriers_win.columnconfigure(2, weight=4)
        self.show_couriers_win.rowconfigure(0, weight=1)
        self.show_couriers_win.rowconfigure(1, weight=1)
        self.show_couriers_win.rowconfigure(2, weight=1)
        self.show_couriers_win.rowconfigure(3, weight=1)
        self.show_couriers_win.rowconfigure(4, weight=3)
        self.show_couriers_win.rowconfigure(5, weight=1)

        self.text = Label(self.show_couriers_win, text="Choose a zone", bg="#ccc0a6", fg="black",
                          font=("proxima nova", 15))
        self.text.grid(row=0, columnspan=3, sticky=SW)

        self.zone_location = Label(self.show_couriers_win, text="Location", bg="#ccc0a6", fg="black",
                                 font=("proxima nova", 12))
        self.zone_location.grid(column=0, row=1, sticky=E)
        self.zone_location_entry = Entry(self.show_couriers_win, font=("proxima nova", 12))
        self.zone_location_entry.grid(column=1, row=1)

        self.zone_name = Label(self.show_couriers_win, text="Name", bg="#ccc0a6", fg="black",
                                 font=("proxima nova", 12))
        self.zone_name.grid(column=0, row=2, sticky=NE)
        self.zone_name_entry = Entry(self.show_couriers_win, font=("proxima nova", 12))
        self.zone_name_entry.grid(column=1, row=2, sticky=N)

        self.image8 = PhotoImage(file="map.png")
        self.button = Button(self.show_couriers_win, command=self.show_courires_for_zone_fct, image=self.image8,
                             bg="#ccc0a6", borderwidth=0)
        self.button.grid(column=1, row=3, sticky=N)

    def show_courires_for_zone_fct(self):
        if self.zone_location_entry.get() == "" or self.zone_name_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.show_couriers_win)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()
                cursor.execute("SELECT Z.Denumire, Z.Localitate, C.Nume + ' ' + C.Prenume AS Curier, "
                               "C.CNP, C.Telefon FROM Zone Z INNER JOIN CurieriZone CZ ON Z.ZonaID = CZ.ZonaID "
                               "INNER JOIN Curieri C ON CZ.CurierID = C.CurierID WHERE Z.Denumire = ? AND "
                               "Z.Localitate = ?", self.zone_name_entry.get(), self.zone_location_entry.get())

                self.zone_l = Label(self.show_couriers_win, text=f"Zona {self.zone_name_entry.get()}"
                                                                 f" din Localitatea {self.zone_location_entry.get()}",
                                    font=("proxima nova", 12), bg="#ccc0a6")
                self.zone_l.grid(row=4, column=1, columnspan=2, sticky=SW)

                style = ttk.Style()
                style.configure("TreeView", font=("proxima nova", 12),  background="blue", foreground="black",
                                rowheight=25, fieldbackground="silver")
                style.map("TreeView", background=[('selected', 'blue')])
                style.theme_use("clam")

                tree = ttk.Treeview(self.show_couriers_win)
                tree["show"] = "headings"

                tree["columns"] = ("Nume", "CNP", "Telefon")
                tree.column("Nume", width=100, minwidth=100, anchor=CENTER)
                tree.column("CNP", width=100, minwidth=100, anchor=CENTER)
                tree.column("Telefon", width=100, minwidth=100, anchor=CENTER)

                tree.heading("Nume", text="Name", anchor=CENTER)
                tree.heading("CNP", text="CNP", anchor=CENTER)
                tree.heading("Telefon", text="Phone", anchor=CENTER)

                i = 0
                for row in cursor:
                    tree.insert('', i, text='', values=(row[2], row[3], row[4]))
                    i = i + 1
                tree.grid(row=5, columnspan=3)

                # commit changes
                cursor.commit()
                # close connection
                conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to :{str(e)}", parent=self.show_couriers_win)

    def show_parcels(self):
        self.show_parcel_win = Toplevel()
        self.show_parcel_win.title("Show a customer's packages")
        self.show_parcel_win.geometry("600x600+520+100")
        self.show_parcel_win.resizable(False, False)
        self.show_parcel_win.config(bg="#ccc0a6")
        self.photo = PhotoImage(file="motorbike.png")
        self.show_parcel_win.iconphoto(False, self.photo)

        self.canvas = Canvas(self.show_parcel_win, bg="#ccc0a6", bd=0, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        #GRID CONFIG
        self.show_parcel_win.rowconfigure(0, weight=1)
        self.show_parcel_win.rowconfigure(1, weight=1)
        self.show_parcel_win.rowconfigure(2, weight=1)
        self.show_parcel_win.rowconfigure(3, weight=1)
        self.show_parcel_win.rowconfigure(4, weight=3)
        self.show_parcel_win.rowconfigure(5, weight=5)
        self.show_parcel_win.columnconfigure(0, weight=1)
        self.show_parcel_win.columnconfigure(1, weight=1)
        self.show_parcel_win.columnconfigure(2, weight=1)

        self.text = Label(self.show_parcel_win, text="Choose a client by name", bg="#ccc0a6", fg="black",
                          font=("proxima nova", 15))
        self.text.grid(row=0, columnspan=3, sticky=SW)

        self.f_name_client = Label(self.show_parcel_win, text="First Name", bg="#ccc0a6", fg="black",
                               font=("proxima nova", 12))
        self.f_name_client.grid(column=0, row=1)
        self.f_name_client_entry = Entry(self.show_parcel_win, font=("proxima nova", 12))
        self.f_name_client_entry.grid(column=1, row=1, sticky=W)

        self.l_name_client = Label(self.show_parcel_win, text="Last Name", bg="#ccc0a6", fg="black",
                               font=("proxima nova", 12))
        self.l_name_client.grid(column=0, row=2, sticky=N)
        self.l_name_client_entry = Entry(self.show_parcel_win, font=("proxima nova", 12))
        self.l_name_client_entry.grid(column=1, row=2, sticky=NW)

        self.image9 = PhotoImage(file="order_button.png")
        self.button = Button(self.show_parcel_win, command=self.show_parcels_fct, image=self.image9,
                             bg="#ccc0a6", borderwidth=0)
        self.button.grid(column=1, row=3, sticky=NW)

        self.image10 = PhotoImage(file="man.png")
        self.label = Label(self.show_parcel_win, image=self.image10, bg="#ccc0a6")
        self.label.grid(column=1, row=1, rowspan=3, sticky=SE)

    def show_parcels_fct(self):
        if self.l_name_client_entry.get() == "" or self.f_name_client_entry.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent=self.show_parcel_win)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()

                # SELECT UNDELIVERED PARCELS
                cursor.execute("SELECT Cl.TipClient, COUNT(Col.ColetID) AS NrColete, Col.Denumire, Col.Cod FROM Clienti Cl "
                               "INNER JOIN ClientiColete CC ON Cl.ClientID = CC.ClientID "
                               "LEFT JOIN Colete Col ON CC.ColetID = Col.ColetID "
                               "WHERE Col.DataLivrarii > GETDATE() AND Cl.Nume = ? AND Cl.Prenume = ? "
                               "GROUP BY Cl.TipClient, Col.Denumire, Col.Cod ORDER BY Col.Denumire ASC",
                               self.l_name_client_entry.get(), self.f_name_client_entry.get())

                print("SUCCESS")

                row = cursor.fetchone()
                cursor.commit()

                print("SUCCESS2")

                self.client_l = Label(self.show_parcel_win, text=f"Clientul: {self.l_name_client_entry.get()}"
                                                                 f" {self.f_name_client_entry.get()}\n"
                                                                 f"Numar colete: {row[1]}",
                                      font=("proxima nova", 12), bg="#ccc0a6", justify="left")
                self.client_l.grid(column=1, row=4, columnspan=2, sticky=SW)

                print("SUCCESS3")
                print(self.l_name_client_entry.get())
                print(self.f_name_client_entry.get())

                cursor.execute(
                    "SELECT Cl.TipClient, COUNT(Col.ColetID) AS NrColete, Col.Denumire, Col.Cod FROM Clienti Cl "
                    "INNER JOIN ClientiColete CC ON Cl.ClientID = CC.ClientID "
                    "LEFT JOIN Colete Col ON CC.ColetID = Col.ColetID "
                    "WHERE Col.DataLivrarii > GETDATE() AND Cl.Nume = ? AND Cl.Prenume = ? "
                    "GROUP BY Cl.TipClient, Col.Denumire, Col.Cod ORDER BY Col.Denumire ASC",
                    (self.l_name_client_entry.get(), self.f_name_client_entry.get())
                )

                colete_nelivrate = []
                for row in cursor.fetchall():
                    colete_nelivrate.append(row)

                cursor.execute(
                    "SELECT Cl.TipClient, COUNT(Col.ColetID) AS NrColete, Col.Denumire, Col.Cod FROM Clienti Cl "
                    "INNER JOIN ClientiColete CC ON Cl.ClientID = CC.ClientID "
                    "LEFT JOIN Colete Col ON CC.ColetID = Col.ColetID "
                    "WHERE Col.DataLivrarii < GETDATE() AND Cl.Nume = ? AND Cl.Prenume = ? "
                    "GROUP BY Cl.TipClient, Col.Denumire, Col.Cod ORDER BY Col.Denumire ASC",
                    self.l_name_client_entry.get(), self.f_name_client_entry.get())

                colete_livrate = []
                for row in cursor.fetchall():
                    colete_livrate.append(row)

                print(colete_livrate)
                print(colete_nelivrate)

                style = ttk.Style()
                style.configure("TreeView", font=("proxima nova", 12), background="blue", foreground="black",
                                rowheight=25, fieldbackground="silver")
                style.map("TreeView", background=[('selected', 'blue')])
                style.theme_use("clam")

                tree = ttk.Treeview(self.show_parcel_win)
                tree["show"] = "headings"

                tree["columns"] = ("ID", "Name", "Code", "Type", "Status")
                tree.column("ID", width=100, minwidth=60, anchor=CENTER)
                tree.column("Name", width=100, minwidth=60, anchor=CENTER)
                tree.column("Code", width=100, minwidth=60, anchor=CENTER)
                tree.column("Type", width=100, minwidth=60, anchor=CENTER)
                tree.column("Status", width=100, minwidth=60, anchor=CENTER)

                tree.heading("ID", text="ID", anchor=CENTER)
                tree.heading("Name", text="Name", anchor=CENTER)
                tree.heading("Code", text="Code", anchor=CENTER)
                tree.heading("Type", text="Type", anchor=CENTER)
                tree.heading("Status", text="Status", anchor=CENTER)


                i = 0
                if len(colete_livrate) > 0:
                    for x in range(len(colete_livrate)):
                        if colete_livrate[x][0] == "Expeditor":
                            tree.insert('', 1, text='', values=(i, colete_livrate[x][2], colete_livrate[x][3],
                                                                "Colet trimis", "Livrat"))
                        else:
                            tree.insert('', 1, text='', values=(i, colete_livrate[x][2], colete_livrate[x][3],
                                                                "Colet primit", "Livrat"))
                        i = i + 1

                if len(colete_nelivrate) > 0:
                    for y in range(len(colete_nelivrate)):
                        if colete_nelivrate[y][0] == "Expeditor" and len(colete_nelivrate) > 0:
                            tree.insert('', 1, text='', values=(i, colete_nelivrate[y][2], colete_nelivrate[y][3],
                                                                "Colet trimis", "Nelivrat"))
                        else:
                            tree.insert('', 1, text='', values=(i, colete_nelivrate[y][2], colete_nelivrate[y][3],
                                                                "Colet primit", "Nelivrat"))
                        i = i + 1
                tree.grid(columnspan=3, row=5)

                cursor.commit()
                conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.show_parcel_win)

    def show_locations(self):
        self.show_loc_win = Toplevel()
        self.show_loc_win.title("Show location for a parcel")
        self.show_loc_win.geometry("500x500+520+100")
        self.show_loc_win.resizable(False, False)
        self.show_loc_win.config(bg="#ccc0a6")
        self.photo = PhotoImage(file="motorbike.png")
        self.show_loc_win.iconphoto(False, self.photo)

        self.canvas = Canvas(self.show_loc_win, bg="#ccc0a6", bd=0, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        # GRID CONFIG
        self.show_loc_win.columnconfigure(0, weight=1)
        self.show_loc_win.columnconfigure(1, weight=1)
        self.show_loc_win.columnconfigure(2, weight=4)
        self.show_loc_win.rowconfigure(0, weight=1)
        self.show_loc_win.rowconfigure(1, weight=1)
        self.show_loc_win.rowconfigure(2, weight=1)
        self.show_loc_win.rowconfigure(3, weight=1)
        self.show_loc_win.rowconfigure(4, weight=3)
        self.show_loc_win.rowconfigure(5, weight=1)

        self.text = Label(self.show_loc_win, text="Choose a parcel", bg="#ccc0a6", fg="black",
                          font=("proxima nova", 15))
        self.text.grid(row=0, columnspan=3, sticky=SW)

        self.p_name = Label(self.show_loc_win, text="Name", bg="#ccc0a6", fg="black",
                                   font=("proxima nova", 12))
        self.p_name.grid(column=0, row=1, sticky=E)
        self.p_name_entry = Entry(self.show_loc_win, font=("proxima nova", 12))
        self.p_name_entry.grid(column=1, row=1)

        self.p_code = Label(self.show_loc_win, text="Code", bg="#ccc0a6", fg="black",
                               font=("proxima nova", 12))
        self.p_code.grid(column=0, row=2, sticky=NE)
        self.p_code_entry = Entry(self.show_loc_win, font=("proxima nova", 12))
        self.p_code_entry.grid(column=1, row=2, sticky=N)

        self.image8 = PhotoImage(file="location.png")
        self.button = Button(self.show_loc_win, command=self.show_locations_fct, image=self.image8,
                             bg="#ccc0a6", borderwidth=0)
        self.button.grid(column=1, row=3, sticky=N)

    def show_locations_fct(self):
        if self.p_name_entry.get() == "" or self.p_code_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.show_loc_win)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()
                cursor.execute("SELECT L.Localitate, GETDATE(), Col.DataExpedierii, Col.DataLivrarii, "
                               "C.Nume + ' ' + C.Prenume AS Curier, C.Telefon FROM Localizari L "
                               "INNER JOIN Colete Col ON L.LocalizareID = Col.LocalizareID "
                               "INNER JOIN Curieri C ON Col.CurierID = C.CurierID "
                               "WHERE Col.Denumire = ? AND Col.Cod = ?", self.p_name_entry.get(),
                               self.p_code_entry.get())

                row = cursor.fetchone()

                string_to_print = f"The parcel {self.p_name_entry.get()} {self.p_code_entry.get()} " \
                                  f"is located in {row[0]}\n" \
                                  f"Current data: {row[1]:%Y-%m-%d}\n" \
                                  f"Data of dispatch: {row[2]:%Y-%m-%d}\n" \
                                  f"Data of delivery: {row[3]:%Y-%m-%d}\n" \
                                  f"Courier & phone: {row[4]} {row[5]}"


                self.show_l = Label(self.show_loc_win, text=string_to_print, font=("proxima nova", 12),
                                    bg="#ccc0a6", fg="black", relief="sunken", justify="left")
                self.show_l.grid(row=4, columnspan=3)

                self.image7 = PhotoImage(file="ok.png")
                self.image_l = Label(self.show_loc_win, image=self.image7, bg="#ccc0a6")
                self.image_l.grid(row=5, columnspan=3)

                # commit changes
                cursor.commit()
                # close connection
                conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.show_loc_win)

    def show_top3(self):
        self.top3_win = Toplevel()
        self.top3_win.title("Show top 3")
        self.top3_win.geometry("550x550+520+100")
        self.top3_win.resizable(False, False)
        self.top3_win.config(bg="#ccc0a6")
        self.photo = PhotoImage(file="motorbike.png")
        self.top3_win.iconphoto(False, self.photo)

        self.canvas = Canvas(self.top3_win, bg="#ccc0a6", bd=0, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        # GRID CONFIG
        self.top3_win.columnconfigure(0, weight=1)
        self.top3_win.columnconfigure(1, weight=1)
        self.top3_win.columnconfigure(2, weight=4)
        self.top3_win.rowconfigure(0, weight=1)
        self.top3_win.rowconfigure(1, weight=1)
        self.top3_win.rowconfigure(2, weight=1)
        self.top3_win.rowconfigure(3, weight=1)
        self.top3_win.rowconfigure(4, weight=1)
        self.top3_win.rowconfigure(5, weight=1)

        self.text = Label(self.top3_win, text="Top 3 couriers with the highest salary", bg="#ccc0a6",
                          fg="black", font=("proxima nova", 15))
        self.text.grid(row=0, columnspan=3)

        self.image8 = PhotoImage(file="top3.png")
        self.button = Button(self.top3_win, command=self.show_top3_fct, image=self.image8,
                             bg="#ccc0a6", borderwidth=0)
        self.button.grid(columnspan=3, row=1)

        self.image9 = PhotoImage(file="number-one (1).png")
        self.label = Label(self.top3_win, image=self.image9, bg="#ccc0a6")
        self.label.grid(column=0, row=2, sticky=E)

        self.image10 = PhotoImage(file="number-2.png")
        self.label = Label(self.top3_win, image=self.image10, bg="#ccc0a6")
        self.label.grid(column=0, row=3, sticky=E)

        self.image11 = PhotoImage(file="number-3.png")
        self.label = Label(self.top3_win, image=self.image11, bg="#ccc0a6")
        self.label.grid(column=0, row=4, sticky=E)

    def show_top3_fct(self):

        try:
            # connect with daatbase
            conectare = pyodbc.connect(string_de_conectare)
            cursor = conectare.cursor()
            cursor.execute("SELECT TOP 3 C.Nume + ' ' + C.Prenume AS NumeCurier, C.Salariu,"
                           " Z.Localitate, Z.Denumire FROM Curieri C "
                           "INNER JOIN CurieriZone CZ ON C.CurierID = CZ.CurierID "
                           "INNER JOIN Zone Z ON CZ.ZonaID = Z.ZonaID "
                           "ORDER BY C.Salariu DESC")


            row = cursor.fetchall()
            string1 = f"Courier {row[0][0]}, salary: {row[0][1]}, zone: {row[0][3]}, {row[0][2]}"
            string2 = f"Courier {row[1][0]}, salary: {row[1][1]}, zone: {row[1][3]}, {row[1][2]}"
            string3 = f"Courier {row[2][0]}, salary: {row[2][1]}, zone: {row[2][3]}, {row[2][2]}"

            self.show_1 = Label(self.top3_win, text=string1, font=("proxima nova", 12),
                                bg="#ccc0a6", fg="black", justify="left")
            self.show_1.grid(column=1, row=2)

            self.show_2 = Label(self.top3_win, text=string2, font=("proxima nova", 12),
                                bg="#ccc0a6", fg="black", justify="left")
            self.show_2.grid(column=1, row=3)

            self.show_3 = Label(self.top3_win, text=string3, font=("proxima nova", 12),
                                bg="#ccc0a6", fg="black", justify="left")
            self.show_3.grid(column=1, row=4)

            self.image7 = PhotoImage(file="salariu.png")
            self.image_l = Label(self.top3_win, image=self.image7, bg="#ccc0a6")
            self.image_l.grid(row=5, columnspan=3)

            # commit changes
            cursor.commit()
            # close connection
            conectare.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.top3_win)

    def show_best_emp(self):
        self.best_emp_win = Toplevel(self.show_win)
        self.best_emp_win.geometry("500x400+520+100")
        self.best_emp_win.title("Employees of the year")
        self.best_emp_win.resizable(False, False)
        self.best_emp_win.config(bg="#ccc0a6")
        self.photo = PhotoImage(file="motorbike.png")
        self.best_emp_win.iconphoto(False, self.photo)

        self.canvas = Canvas(self.best_emp_win, bg="#ccc0a6", bd=0, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        self.best_emp_win.columnconfigure((0, 1, 2), weight=1)
        self.best_emp_win.rowconfigure((0, 1, 2), weight=1)
        self.best_emp_win.rowconfigure(3, weight=5)

        self.text = Label(self.best_emp_win, text="Employees of the year", bg="#ccc0a6",
                          fg="black", font=("proxima nova", 15))
        self.text.grid(row=0, columnspan=3)

        self.subtitle = Label(self.best_emp_win, text="Choose a year", bg="#ccc0a6", fg="black",
                              font=("proxima nova", 15))
        self.subtitle.grid(column=0, row=1)

        self.year = Label(self.best_emp_win, text="Year", bg="#ccc0a6", fg="black",
                              font=("proxima nova", 15))
        self.year.grid(column=0, row=2, sticky=N)
        self.year_entry = Entry(self.best_emp_win, font=("proxima nova", 12))
        self.year_entry.grid(column=1, row=2, sticky=NW)

        self.img = PhotoImage(file="schedule.png")
        self.button = Button(self.best_emp_win, image=self.img, command=self.best_emp_fct,
                             bg="#ccc0a6", borderwidth=0)
        self.button.grid(column=1, row=3, sticky=N)

    def best_emp_fct(self):
        try:
            year = self.year_entry.get()
            minus_year = int(self.year_entry.get()) - 1
            print(year)
            print(minus_year)

            # connect with daatbase
            conectare = pyodbc.connect(string_de_conectare)
            cursor = conectare.cursor()
            cursor.execute("SELECT C.Nume + ' ' + C.Prenume AS Curier, COUNT(Col.ColetID) AS NumarColete FROM Curieri C LEFT JOIN Colete Col ON C.CurierID = Col.CurierID "
                           "GROUP BY C.CurierID, C.Nume, C.Prenume "
                           "HAVING COUNT(Col.ColetID) = (SELECT TOP 1 COUNT(Col.ColetID) FROM Colete Col2 GROUP BY Col2.DataLivrarii "
                           "HAVING YEAR(Col2.DataLivrarii) BETWEEN ? AND ? ORDER BY COUNT(Col.ColetID) DESC)", minus_year, year)

            row = cursor.fetchall()
            print(row)
            text1 = "Employees of the year:\n"
            text = ""
            if len(row) == 0:
                messagebox.showerror("Error", "No orders were placed during that period.", parent=self.best_emp_win)
            else:
                for i in range(len(row)):
                    text = f"{row[i][0]} delivered {row[i][1]} parcels.\n" + text
                messagebox.showinfo("Success", text1 + text, parent=self.best_emp_win)

            # commit changes
            cursor.commit()
            # close connection
            conectare.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.best_emp_win)

    def show_best_year(self):
        try:
            # connect with daatbase
            conectare = pyodbc.connect(string_de_conectare)
            cursor = conectare.cursor()
            cursor.execute("SELECT Year(Col.DataLivrarii) AS An, COUNT(*) AS NumarColete FROM Colete Col "
                           "WHERE Year(Col.DataLivrarii) = (SELECT TOP 1 Year(Col2.DataLivrarii) FROM Colete Col2 "
                           "GROUP BY Year(Col2.DataLivrarii) ORDER BY COUNT(*) DESC) "
                           "GROUP BY Year(Col.DataLivrarii)")

            row = cursor.fetchall()

            messagebox.showinfo("Success", f"The most productive year was {row[0][0]}, we delivered {row[0][1]} packages.",
                                parent=self.show_win)

            # commit changes
            cursor.commit()
            # close connection
            conectare.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.show_win)

    def show_most_expensive_ord(self):

        try:
            self.expensive_orders_win = Toplevel(self.show_win)
            self.expensive_orders_win.geometry("500x400+520+100")
            self.expensive_orders_win.title("Expensive orders")
            self.expensive_orders_win.resizable(False, False)
            self.expensive_orders_win.config(bg="#ccc0a6")
            self.photo = PhotoImage(file="motorbike.png")
            self.expensive_orders_win.iconphoto(False, self.photo)

            self.canvas = Canvas(self.expensive_orders_win, bg="#ccc0a6", bd=0, width=1000, height=1000)
            self.canvas.place(x=0, y=0)

            self.expensive_orders_win.columnconfigure((0, 1, 2), weight=1)
            self.expensive_orders_win.rowconfigure((0, 1), weight=1)

            self.text = Label(self.expensive_orders_win, text="Most expensive orders", bg="#ccc0a6",
                              fg="black", font=("proxima nova", 15))
            self.text.grid(row=0, columnspan=3)

            self.image11 = PhotoImage(file="profits.png")
            self.image11_l = Label(self.expensive_orders_win, image=self.image11, bg="#ccc0a6")
            self.image11_l.grid(column=0, row=1, sticky=N)

            self.image12 = PhotoImage(file="package.png")
            self.image12_l = Label(self.expensive_orders_win, image=self.image12, bg="#ccc0a6")
            self.image12_l.grid(column=2, row=1, sticky=N)

            # connect with daatbase
            conectare = pyodbc.connect(string_de_conectare)
            cursor = conectare.cursor()
            cursor.execute("SELECT Col.Denumire, Col.Cod, Col.Cost FROM Colete Col "
                           "WHERE Col.Cost > ALL (SELECT AVG(C.Cost) FROM Colete C)")
            style = ttk.Style()
            style.configure("TreeView", font=("proxima nova", 12), background="blue", foreground="black",
                            rowheight=25, fieldbackground="silver")
            style.map("TreeView", background=[('selected', 'blue')])
            style.theme_use("clam")

            tree = ttk.Treeview(self.expensive_orders_win)
            tree["show"] = "headings"

            tree["columns"] = ("Denumire", "Cod", "Cost")
            tree.column("Denumire", width=80, minwidth=60, anchor=CENTER)
            tree.column("Cod", width=80, minwidth=80, anchor=CENTER)
            tree.column("Cost", width=150, minwidth=150, anchor=CENTER)

            tree.heading("Denumire", text="Name", anchor=CENTER)
            tree.heading("Cod", text="Code", anchor=CENTER)
            tree.heading("Cost", text="Cost", anchor=CENTER)

            i = 0
            for row in cursor:
                tree.insert('', i, text='', values=(row[0], row[1], row[2]))
                i = i + 1

            tree.grid(column=1, row=1, sticky=N)

            # commit changes
            cursor.commit()
            # close connection
            conectare.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.show_win)

    def show_loyal_customers(self):
        self.loyal_cust_win = Toplevel(self.show_win)
        self.loyal_cust_win.geometry("500x400+520+100")
        self.loyal_cust_win.title("Loyal customers")
        self.loyal_cust_win.resizable(False, False)
        self.loyal_cust_win.config(bg="#ccc0a6")
        self.photo = PhotoImage(file="motorbike.png")
        self.loyal_cust_win.iconphoto(False, self.photo)

        self.canvas = Canvas(self.loyal_cust_win, bg="#ccc0a6", bd=0, width=1000, height=1000)
        self.canvas.place(x=0, y=0)

        self.loyal_cust_win.columnconfigure((0, 1, 2), weight=1)
        self.loyal_cust_win.rowconfigure((0, 1, 2, 3), weight=1)
        self.loyal_cust_win.rowconfigure(4, weight=4)


        self.text = Label(self.loyal_cust_win, text="Loyal customers", bg="#ccc0a6",
                          fg="black", font=("proxima nova", 15))
        self.text.grid(row=0, columnspan=3)

        self.subtitle = Label(self.loyal_cust_win, text="Choose a location", bg="#ccc0a6", fg="black",
                              font=("proxima nova", 15))
        self.subtitle.grid(column=0, row=1)

        self.location = Label(self.loyal_cust_win, text="Location", bg="#ccc0a6", fg="black",
                          font=("proxima nova", 15))
        self.location.grid(column=0, row=2, sticky=N)
        self.location_entry = Entry(self.loyal_cust_win, font=("proxima nova", 12))
        self.location_entry.grid(column=1, row=2, sticky=NW)

        self.img = PhotoImage(file="customers.png")
        self.button = Button(self.loyal_cust_win, image=self.img, command=self.loyal_customers_fct,
                             bg="#ccc0a6", borderwidth=0)
        self.button.grid(column=1, row=3, sticky=N)

    def loyal_customers_fct(self):
        if self.location_entry.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent=self.loyal_cust_win)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()

                # SELECT UNDELIVERED PARCELS
                cursor.execute("SELECT Cl.Nume, Cl.Prenume, Cl.CNP, CC.ColetID FROM Clienti Cl INNER JOIN ClientiColete CC ON Cl.ClientID = CC.ClientID  "
                               "INNER JOIN Colete C ON CC.ColetID = C.ColetID "
                               "WHERE Cl.ClientID IN (SELECT Cl2.ClientID FROM Clienti Cl2 "
                               "WHERE Cl2.Localitate = ? AND Cl2.TipClient = 'Expeditor' AND Cl.ClientID = Cl2.ClientID) "
                               "GROUP BY Cl.ClientID, Cl.Nume, Cl.Prenume, Cl.CNP, CC.ColetID, C.Cost HAVING C.Cost > 250",
                               self.location_entry.get())

                row = cursor.fetchall()

                if len(row) == 0:
                    messagebox.showerror("Error", "No orders were placed during that period.", parent=self.loyal_cust_win)
                else:

                    style = ttk.Style()
                    style.configure("TreeView", font=("proxima nova", 12), background="blue", foreground="black",
                                    rowheight=25, fieldbackground="silver")
                    style.map("TreeView", background=[('selected', 'blue')])
                    style.theme_use("clam")

                    tree = ttk.Treeview(self.loyal_cust_win)
                    tree["show"] = "headings"

                    tree["columns"] = ("Nume", "Prenume", "CNP")
                    tree.column("Nume", width=100, minwidth=60, anchor=CENTER)
                    tree.column("Prenume", width=100, minwidth=60, anchor=CENTER)
                    tree.column("CNP", width=100, minwidth=60, anchor=CENTER)

                    tree.heading("Nume", text="Last Name", anchor=CENTER)
                    tree.heading("Prenume", text="First Name", anchor=CENTER)
                    tree.heading("CNP", text="CNP", anchor=CENTER)

                    i = 0
                    for r in row:
                        tree.insert('', i, text='', values=(r[0], r[1], r[2]))
                        i = i + 1

                    tree.grid(columnspan=3, row=4)

                    cursor.commit()
                    conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.loyal_cust_win)

# root = Tk()
# obj = ShowWindow(root)
# root.mainloop()
