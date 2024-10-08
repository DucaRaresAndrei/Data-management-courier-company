from tkinter import *
import pyodbc
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
from show_functions import *

class SecondWindow:
    string_de_conectare = r"driver={SQL SERVER}; server=DESKTOP-FA5P09O\SQLEXPRESS; database=BD_Proiect; trusted_connection=YES"

    def __init__(self, win):

        self.window = win
        self.window.title("Main menu")
        self.window.geometry("800x800")
        self.photo = PhotoImage(file="motorbike.png")
        self.window.iconphoto(False, self.photo)
        self.window.resizable(False, False)

        self.colet_id = None
        self.expeditor_id = None
        self.destinatar_id = None
        self.zona_id = None

        # top bar colored in blue
        top_bar = Label(self.window, text="Courier Company - Database System Manager", font=("Arial", 15), fg="white",
                        bg="#2c3c53", width=75, anchor=W, height=1)
        top_bar.place(x=0, y=0)

        # icons canvas
        Frame_icon = Canvas(self.window, bg="white", height=800, width=200)
        Frame_icon.place(x=0, y=29)

        title = Label(Frame_icon, text="Servicies", bg="white", fg="black", font=("Arial", 15), anchor=CENTER)
        title.place(x=45, y=10)

        Frame_icon.create_line(0, 50, 250, 50, fill="light grey")

        # insert meniu
        self.icon_image_insert = ImageTk.PhotoImage(file="curve-down-arrow.png")
        self.icon_insert = Label(Frame_icon, image=self.icon_image_insert, bg="white")
        self.icon_insert.place(x=0, y=55)
        self.text_insert = Label(Frame_icon, text="Insert data", bg="white", fg="grey", font=("proxima nova", 12))
        self.text_insert.place(x=25, y=53)
        self.text_insert_colet = Button(Frame_icon, command=self.insert_parcel_menu, text="Insert parcel", bg="white", fg="black", font=("proxima nova", 12),
                                        borderwidth=0)
        self.text_insert_colet.place(x=25, y=78)
        self.text_insert_courier = Button(Frame_icon, command=self.insert_courier_menu, text="Insert courier", bg="white", fg="black", font=("proxima nova", 12),
                                          borderwidth=0)
        self.text_insert_courier.place(x=25, y=103)

        Frame_icon.create_line(0, 133, 150, 133, fill="light grey")

        # update meniu
        self.icon_image_update = ImageTk.PhotoImage(file="curve-down-arrow.png")
        self.icon_update = Label(Frame_icon, image=self.icon_image_update, bg="white")
        self.icon_update.place(x=0, y=138)
        self.text_update = Label(Frame_icon, text="Update data", bg="white", fg="grey", font=("proxima nova", 12))
        self.text_update.place(x=25, y=136)
        self.text_update_colet = Button(Frame_icon, command=self.update_location_menu, text="Update location", bg="white", fg="black",
                                        font=("proxima nova", 12), borderwidth=0)
        self.text_update_colet.place(x=25, y=161)
        self.text_update_courier = Button(Frame_icon, text="Update salary", bg="white", fg="black",
                                          font=("proxima nova", 12), borderwidth=0,
                                          command=self.update_salary_menu)
        self.text_update_courier.place(x=25, y=186)

        Frame_icon.create_line(0, 216, 150, 216, fill="light grey")

        # delete meniu
        self.icon_image_delete = ImageTk.PhotoImage(file="curve-down-arrow.png")
        self.icon_delete = Label(Frame_icon, image=self.icon_image_delete, bg="white")
        self.icon_delete.place(x=0, y=221)
        self.text_delete = Label(Frame_icon, text="Delete data", bg="white", fg="grey", font=("proxima nova", 12))
        self.text_delete.place(x=25, y=219)
        self.text_delete_parcel = Button(Frame_icon, command=self.delete_parcel_menu,text="Delete parcel", bg="white", fg="black",
                                        font=("proxima nova", 12),
                                        borderwidth=0)
        self.text_delete_parcel.place(x=25, y=244)
        self.text_delete_courier = Button(Frame_icon, command=self.delete_courier_menu, text="Delete courier", bg="white", fg="black",
                                          font=("proxima nova", 12),
                                          borderwidth=0)
        self.text_delete_courier.place(x=25, y=269)

        Frame_icon.create_line(0, 299, 150, 299, fill="light grey")

        # display menu
        self.icon_image_display = ImageTk.PhotoImage(file="curve-down-arrow.png")
        self.icon_display = Label(Frame_icon, image=self.icon_image_update, bg="white")
        self.icon_display.place(x=0, y=304)
        self.text_display = Label(Frame_icon, text="Display data", bg="white", fg="grey", font=("proxima nova", 12))
        self.text_display.place(x=25, y=302)
        self.text_display_couriers = Button(Frame_icon, command=self.display_couriers, text="Display Couriers", bg="white",
                                         fg="black", font=("proxima nova", 12), borderwidth=0)
        self.text_display_couriers.place(x=25, y=327)
        self.text_display_locations = Button(Frame_icon, command=self.display_locations, text="Display Locations",
                                            bg="white",
                                            fg="black", font=("proxima nova", 12), borderwidth=0)
        self.text_display_locations.place(x=25, y=352)
        self.text_display_customers = Button(Frame_icon, command=self.display_customers, text="Display Customers",
                                             bg="white",
                                             fg="black", font=("proxima nova", 12), borderwidth=0)
        self.text_display_customers.place(x=25, y=377)
        self.text_display_parcels = Button(Frame_icon, command=self.display_parcels, text="Display Parcels",
                                             bg="white",
                                             fg="black", font=("proxima nova", 12), borderwidth=0)
        self.text_display_parcels.place(x=25, y=402)
        self.text_display_zones = Button(Frame_icon, command=self.display_zones, text="Display Zones",
                                           bg="white",
                                           fg="black", font=("proxima nova", 12), borderwidth=0)
        self.text_display_zones.place(x=25, y=427)

        # SH0W BUTTON
        self.show_button = Button(Frame_icon, command=self.show_function, text="Show", bg="white", fg="black",
                                  font=("proxima nova", 12), borderwidth=0)
        self.show_button.place(x=25, y=452)

    #####################################################################################################

    def insert_parcel_menu(self):
        self.insert_frame = Canvas(self.window, bg="white", height=650, width=500)
        self.insert_frame.place(x=250, y=70)

        self.label_parcel_data = Label(self.insert_frame, text="Parcel data", bg="white", fg="black",
                                       font=("proxima nova", 12))
        self.label_parcel_data.place(x=20, y=10)

        # NUME CURIER
        self.curier_name = Label(self.insert_frame, text="Courier", bg="white", fg="grey",
                               font=("proxima nova", 10))
        self.curier_name.place(x=20, y=40)
        self.curier_name_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.curier_name_entry.place(x=90, y=40)

        # NAME
        self.name = Label(self.insert_frame, text="Name", bg="white", fg="grey",
                          font=("proxima nova", 10))
        self.name.place(x=20, y=70)
        self.name_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.name_entry.place(x=90, y=70)

        # WEIGHT
        self.weight = Label(self.insert_frame, text="Weight", bg="white", fg="grey",
                            font=("proxima nova", 10))
        self.weight.place(x=20, y=100)
        self.weight_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.weight_entry.place(x=90, y=100)

        # LOCATION ID
        self.location_name = Label(self.insert_frame, text="Location", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.location_name.place(x=20, y=130)
        self.location_name_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.location_name_entry.place(x=90, y=130)

        # COST
        self.cost = Label(self.insert_frame, text="Cost", bg="white", fg="grey",
                            font=("proxima nova", 10))
        self.cost.place(x=20, y=160)
        self.cost_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.cost_entry.place(x=90, y=160)

        # DISPATCH DATA
        self.dispatch_data = Label(self.insert_frame, text="Dispatch Data", bg="white", fg="grey",
                            font=("proxima nova", 10))
        self.dispatch_data.place(x=250, y=40)
        self.dispatch_data_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.dispatch_data_entry.place(x=340, y=40)

        # DELIVERY DATA
        self.delivery_data = Label(self.insert_frame, text="Delivery Data", bg="white", fg="grey",
                                   font=("proxima nova", 10))
        self.delivery_data.place(x=250, y=70)
        self.delivery_data_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.delivery_data_entry.place(x=340, y=70)

        # PAYMENT METHOD
        self.payment = Label(self.insert_frame, text="Payment ", bg="white", fg="grey",
                                   font=("proxima nova", 10))
        self.payment.place(x=250, y=100)
        self.payment_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.payment_entry.place(x=340, y=100)

        # SIZE
        self.size = Label(self.insert_frame, text="Size ", bg="white", fg="grey",
                             font=("proxima nova", 10))
        self.size.place(x=250, y=130)
        self.size_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.size_entry.place(x=340, y=130)

        # PARCEL TYPE
        self.code_parcel = Label(self.insert_frame, text="Code Parcel", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.code_parcel.place(x=250, y=160)
        self.code_parcel_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.code_parcel_entry.place(x=340, y=160)

##########################################################################################################

        self.label_client_data = Label(self.insert_frame, text="Client data", bg="white", fg="black",
                                       font=("proxima nova", 12))
        self.label_client_data.place(x=20, y=200)

        # CLIENT FIRST NAME
        self.client_first_name = Label(self.insert_frame, text="First Name", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.client_first_name.place(x=20, y=230)
        self.client_first_name_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.client_first_name_entry.place(x=90, y=230)

        # CLIENT LAST NAME
        self.client_last_name = Label(self.insert_frame, text="Last Name", bg="white", fg="grey",
                                      font=("proxima nova", 10))
        self.client_last_name.place(x=20, y=260)
        self.client_last_name_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.client_last_name_entry.place(x=90, y=260)

        # CLIENT CNP
        self.cnp = Label(self.insert_frame, text="CNP", bg="white", fg="grey",
                                      font=("proxima nova", 10))
        self.cnp.place(x=20, y=290)
        self.cnp_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.cnp_entry.place(x=90, y=290)

        # COMPANY
        self.company= Label(self.insert_frame, text="Company", bg="white", fg="grey",
                         font=("proxima nova", 10))
        self.company.place(x=20, y=320)
        self.company_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.company_entry.place(x=90, y=320)

        # ADRESS
        self.address = Label(self.insert_frame, text="Address", bg="white", fg="grey",
                         font=("proxima nova", 10))
        self.address.place(x=20, y=350)
        self.address_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.address_entry.place(x=90, y=350)

        # CITY
        self.city = Label(self.insert_frame, text="City", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.city.place(x=250, y=230)
        self.city_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.city_entry.place(x=340, y=230)

        # DISTINCT
        self.distinct = Label(self.insert_frame, text="Distinct", bg="white", fg="grey",
                          font=("proxima nova", 10))
        self.distinct.place(x=250, y=260)
        self.distinct_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.distinct_entry.place(x=340, y=260)

        # COUNTRY
        self.country = Label(self.insert_frame, text="Country", bg="white", fg="grey",
                              font=("proxima nova", 10))
        self.country.place(x=250, y=290)
        self.country_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.country_entry.place(x=340, y=290)

        # POSTAL CODE
        self.zipcode = Label(self.insert_frame, text="Zipcode", bg="white", fg="grey",
                             font=("proxima nova", 10))
        self.zipcode.place(x=250, y=320)
        self.zipcode_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.zipcode_entry.place(x=340, y=320)

        # PHONE
        self.phone = Label(self.insert_frame, text="Phone", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.phone.place(x=250, y=350)
        self.phone_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.phone_entry.place(x=340, y=350)

        self.client_type = Label(self.insert_frame, text="Type", bg="white", fg="grey",
                           font=("proxima nova", 10))
        self.client_type.place(x=150, y=380)
        self.client_type_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.client_type_entry.place(x=190, y=380)

        # INSERT SENDER BUTTON
        self.insert_s_btn = Button(self.insert_frame, text="INSERT SENDER",  font=("times new roman", 12),
                                   anchor=CENTER, command=self.insert_client_function)
        self.insert_s_btn.place(x=50, y=420, height=30, width=150)

        # INSERT RECIPIENT BUTTON
        self.insert_r_btn = Button(self.insert_frame, text="INSERT RECIPIENT", font=("times new roman", 12),
                                   anchor=CENTER, command=self.insert_client_function)
        self.insert_r_btn.place(x=300, y=420, height=30, width=150)

        # INSERT PARCEL BUTTON
        self.insert_p_btn = Button(self.insert_frame, text="INSERT PARSEL", font=("times new roman", 12), anchor=CENTER,
                                  command=self.insert_parcel_function)
        self.insert_p_btn.place(x=50, y=460, height=30, width=150)

        # INSERT COMMAND
        self.insert_comm_btn = Button(self.insert_frame, text="INSERT ORDER", command=self.insert_order_window,
                                      font=("times new roman", 12), anchor=CENTER)
        self.insert_comm_btn.place(x=300, y=460, height=30, width=150)

    # insert function for database
    def insert_parcel_function(self):

        if self.curier_name_entry.get() == "" or self.name_entry.get() == "" or self.weight_entry.get() == "" or self.location_name_entry.get() == "" or self.cost_entry.get() == "" or self.dispatch_data_entry.get() == "" or self.delivery_data_entry.get() == "" or self.payment_entry.get() == "" or self.size_entry.get() == "" or self.code_parcel_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.window)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()
                cursor.execute("SELECT * FROM Curieri")
                name = self.curier_name_entry.get().split(" ")
                for row in cursor.fetchall():
                    if row[1] == name[0] and row[2] == name[1]:
                        self.curier_id = row[0]


                cursor.execute("SELECT * FROM Localizari")
                for row in cursor.fetchall():
                    if row[3] == self.location_name_entry.get():
                        self.location_id = row[0]

                # insert into table colet
                cursor.execute("INSERT INTO Colete(CurierID, LocalizareID, Denumire, Greutate, Cost, DataExpedierii, DataLivrarii, ModalitatePlata, Dimensiuni, Cod)"
                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", self.curier_id, self.location_id,
                    self.name_entry.get(), self.weight_entry.get(), self.cost_entry.get(),
                    self.dispatch_data_entry.get(), self.delivery_data_entry.get(),
                    self.payment_entry.get(), self.size_entry.get(), self.code_parcel_entry.get())
                # commit changes
                cursor.commit()
                # close connection
                conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.window)
                self.window.destroy()

        # clear all the text boxes
        self.curier_name_entry.delete(0, END)
        self.location_name_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.weight_entry.delete(0, END)
        self.cost_entry.delete(0, END)
        self.dispatch_data_entry.delete(0, END)
        self.delivery_data_entry.delete(0, END)
        self.payment_entry.delete(0, END)
        self.size_entry.delete(0, END)
        self.code_parcel_entry.delete(0, END)

    def insert_client_function(self):

        if self.client_last_name_entry.get() == "" or self.client_first_name_entry.get() == "" or self.cnp_entry.get() == "" or self.company_entry.get() == "" or self.address_entry.get() == "" or self.city_entry.get() == "" or self.distinct_entry.get() == "" or self.country_entry.get() == "" or self.zipcode_entry.get() == "" or self.phone_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.window)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()

                # insert into table clienti
                cursor.execute("INSERT INTO Clienti(Nume, Prenume, CNP, Companie, Adresa, Localitate,"
                               " Judet, Tara, CodPostal, Telefon, TipClient) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               self.client_last_name_entry.get(), self.client_first_name_entry.get(),
                               self.cnp_entry.get(), self.company_entry.get(), self.address_entry.get(),
                               self.city_entry.get(), self.distinct_entry.get(), self.country_entry.get(),
                               self.zipcode_entry.get(), self.phone_entry.get(), self.client_type_entry.get())

                # commit changes
                cursor.commit()
                # close connection
                conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.window)
                self.window.destroy()

        # clear all the text boxes
        self.client_last_name_entry.delete(0, END)
        self.client_first_name_entry.delete(0, END)
        self.cnp_entry.delete(0, END)
        self.company_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.distinct_entry.delete(0, END)
        self.delivery_data_entry.delete(0, END)
        self.country_entry.delete(0, END)
        self.zipcode_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.client_type_entry.delete(0, END)

    def insert_order_window(self):

        # new window
        self.command_win = Toplevel(self.window)
        self.command_win.geometry("600x400")
        self.command_win.title("PLACE ORDER")

        # TITLE
        self.command_win_title = Label(self.command_win, text="ORDERS", fg="black",
                                   font=("proxima nova", 15))
        self.command_win_title.place(x=250, y=20)

        # SENDER (NAME + CNP)
        self.sender = Label(self.command_win, text="SENDER", fg="black",
                            font=("proxima nova", 12))
        self.sender.place(x=30, y=80)

        self.s_f_name = Label(self.command_win, text="First Name", fg="grey",
                          font=("proxima nova", 10))
        self.s_f_name.place(x=30, y=110)
        self.s_f_name_entry = Entry(self.command_win, font=("proxima nova", 10), bg="lightgray")
        self.s_f_name_entry.place(x=110, y=110)

        self.s_l_name = Label(self.command_win, text="Last Name", font=("proxima nova", 10), fg="grey")
        self.s_l_name.place(x=30, y=140)
        self.s_l_name_entry = Entry(self.command_win, font=("proxima nova", 10), bg="lightgray")
        self.s_l_name_entry.place(x=110, y=140)

        self.cnp_sender = Label(self.command_win, text="CNP", font=("proxima nova", 10), fg="grey")
        self.cnp_sender.place(x=30, y=170)
        self.cnp_sender_entry = Entry(self.command_win, font=("proxima, 10"), bg="lightgray")
        self.cnp_sender_entry.place(x=110, y=170)

        # RECIPIENT (NAME + CNP)
        self.recipient = Label(self.command_win, text="RECIPIENT", fg="black",
                            font=("proxima nova", 12))
        self.recipient.place(x=30, y=220)

        self.r_f_name = Label(self.command_win, text="First Name", fg="grey",
                              font=("proxima nova", 10))
        self.r_f_name.place(x=30, y=250)
        self.r_f_name_entry = Entry(self.command_win, font=("proxima nova", 10), bg="lightgray")
        self.r_f_name_entry.place(x=110, y=250)

        self.r_l_name = Label(self.command_win, text="Last Name", font=("proxima nova", 10), fg="grey")
        self.r_l_name.place(x=30, y=280)
        self.r_l_name_entry = Entry(self.command_win, font=("proxima nova", 10), bg="lightgray")
        self.r_l_name_entry.place(x=110, y=280)

        self.cnp_recipient = Label(self.command_win, text="CNP", font=("proxima nova", 10), fg="grey")
        self.cnp_recipient.place(x=30, y=310)
        self.cnp_recipient_entry = Entry(self.command_win, font=("proxima, 10"), bg="lightgray")
        self.cnp_recipient_entry.place(x=110, y=310)

        # PARCEL (NAME + COD)
        self.sender = Label(self.command_win, text="PARCEL", fg="black",
                            font=("proxima nova", 12))
        self.sender.place(x=340, y=80)

        self.name = Label(self.command_win, text="Name", fg="grey",
                              font=("proxima nova", 10))
        self.name.place(x=340, y=110)
        self.name_entry = Entry(self.command_win, font=("proxima nova", 10), bg="lightgray")
        self.name_entry.place(x=420, y=110)

        self.code = Label(self.command_win, text="CODE", font=("proxima nova", 10), fg="grey")
        self.code.place(x=340, y=140)
        self.code_entry = Entry(self.command_win, font=("proxima nova", 10), bg="lightgray")
        self.code_entry.place(x=420, y=140)

        # INSERT BUTTON
        self.insert_comm_btn = Button(self.command_win, text="INSERT", command=self.insert_order_function,
                                      font=("times new roman", 12), anchor=CENTER)
        self.insert_comm_btn.place(x=225, y=350, height=30, width=150)

    def insert_order_function(self):
        if self.s_f_name_entry.get() == "" or self.s_l_name_entry.get() == "" or self.cnp_sender_entry.get() == "" or self.r_f_name_entry.get() == "" or self.name_entry.get() == "" or self.code_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.command_win)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()
                cursor.execute("SELECT * FROM Colete")
                for row in cursor.fetchall():
                    if row[3] == self.name_entry.get() and row[10] == int(self.code_entry.get()):
                        self.colet_id = row[0]

                cursor.execute("SELECT * FROM Clienti")
                for row in cursor.fetchall():
                    if row[1] == self.s_l_name_entry.get() and row[2] == self.s_f_name_entry.get() and row[3] == self.cnp_sender_entry.get():
                        self.expeditor_id = row[0]

                cursor.execute("SELECT * FROM Clienti")
                for row in cursor.fetchall():
                    if row[1] == self.r_l_name_entry.get() and row[2] == self.r_f_name_entry.get() and row[3] == self.cnp_recipient_entry.get():
                        self.destinatar_id = row[0]

                count = 0
                cursor.execute("SELECT * FROM ClientiColete")
                for row in cursor.fetchall():
                    if self.colet_id == row[0]:
                        count += 1

                print(self.colet_id)
                print(self.expeditor_id)
                print(self.destinatar_id)

                if count == 0:
                    cursor.execute("INSERT INTO ClientiColete(ColetID, ClientID) VALUES (?, ?)",
                                   self.colet_id, self.expeditor_id)
                    cursor.commit()
                    cursor.execute("INSERT INTO ClientiColete(ColetID, ClientID) VALUES (?, ?)",
                                   self.colet_id, self.destinatar_id)
                    cursor.commit()
                    messagebox.showinfo("Success", f"The parcel from {self.s_l_name_entry.get()} {self.s_f_name_entry.get()} to {self.r_l_name_entry.get()} {self.r_f_name_entry.get()} was registred.",
                                        parent=self.command_win)
                # close connection
                conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.command_win)
                self.window.destroy()

###########################################################################################################

    def insert_courier_menu(self):
        self.insert_frame = Canvas(self.window, bg="white", height=650, width=500)
        self.insert_frame.place(x=250, y=70)

        self.label_parcel_data = Label(self.insert_frame, text="Courier data", bg="white", fg="black",
                                       font=("proxima nova", 15))
        self.label_parcel_data.place(x=200, y=10)

        # LAST NAME
        self.last_name_courier = Label(self.insert_frame, text="Last Name", bg="white", fg="grey",
                               font=("proxima nova", 10))
        self.last_name_courier.place(x=20, y=60)
        self.last_name_courier_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.last_name_courier_entry.place(x=90, y=60)

        # FIRST NAME
        self.first_name_courier = Label(self.insert_frame, text="First Name", bg="white", fg="grey",
                          font=("proxima nova", 10))
        self.first_name_courier.place(x=20, y=90)
        self.first_name_courier_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.first_name_courier_entry.place(x=90, y=90)

        # CNP
        self.cnp_courier = Label(self.insert_frame, text="CNP", bg="white", fg="grey",
                            font=("proxima nova", 10))
        self.cnp_courier.place(x=20, y=120)
        self.cnp_courier_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.cnp_courier_entry.place(x=90, y=120)

        # PHONE
        self.phone_courier = Label(self.insert_frame, text="Phone", bg="white", fg="grey",
                                   font=("proxima nova", 10))
        self.phone_courier.place(x=250, y=60)
        self.phone_courier_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.phone_courier_entry.place(x=300, y=60)

        # SALARY
        self.salary_courier = Label(self.insert_frame, text="Salary", bg="white", fg="grey",
                                   font=("proxima nova", 10))
        self.salary_courier.place(x=250, y=90)
        self.salary_courier_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.salary_courier_entry.place(x=300, y=90)

        # BONUS
        self.bonus = Label(self.insert_frame, text="Bonus", bg="white", fg="grey",
                             font=("proxima nova", 10))
        self.bonus.place(x=250, y=120)
        self.bonus_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.bonus_entry.place(x=300, y=120)

        # ZONE DETAILS
        self.zone_details = Label(self.insert_frame, text="Zone details", bg="white", fg="black",
                                    font=("proxima nova", 12))
        self.zone_details.place(x=20, y=170)

        # LINE
        self.insert_frame.create_line(0, 200, 150, 200, fill="light grey")

        # ZONE NAME
        self.zone_name = Label(self.insert_frame, text="Name", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.zone_name.place(x=20, y=220)
        self.zone_name_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.zone_name_entry.place(x=90, y=220)

        # CITY WHICH THE AREA IS PART
        self.zone_city = Label(self.insert_frame, text="City", bg="white", fg="grey",
                           font=("proxima nova", 10))
        self.zone_city.place(x=250, y=220)
        self.zone_city_entry = Entry(self.insert_frame, font=("proxima nova", 10), bg="lightgray")
        self.zone_city_entry.place(x=300, y=220)

        # INSERT BUTTON
        self.inser_courier_btn = Button(self.insert_frame, text="INSERT COURIER", font=("times new roman",12),
                                        anchor=CENTER, command=self.insert_courier_function)
        self.inser_courier_btn.place(x=175, y=270, height=30, width=150)

    def insert_courier_function(self):

        if self.last_name_courier_entry.get() == "" or self.first_name_courier_entry.get() == "" or self.cnp_courier_entry.get() == "" or self.phone_courier_entry.get() == "" or self.bonus_entry.get() == "" or self.zone_name_entry.get() == "" or self.zone_city_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.window)
        else:
            try:
                # connect with daatbase
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()

                # insert into table courier
                cursor.execute("INSERT INTO Curieri(Nume, Prenume, CNP, Telefon, Salariu, Bonus)"
                               " VALUES (?, ?, ?, ?, ?, ?)",
                               self.last_name_courier_entry.get(), self.first_name_courier_entry.get(),
                               self.cnp_courier_entry.get(), self.phone_courier_entry.get(),
                               self.salary_courier_entry.get(),self.bonus_entry.get())

                # commit changes
                cursor.commit()
                cursor.execute("SELECT @@IDENTITY AS curier_id")
                curier_id = cursor.fetchone()[0]
                print(curier_id)

                cursor.execute("SELECT * FROM Zone")
                for row in cursor.fetchall():
                    if row[1] == self.zone_name_entry.get() and row[2] == self.zone_city_entry.get():
                        self.zona_id = row[0]

                cursor.execute("INSERT INTO CurieriZone(CurierID, ZonaID) VALUES (?, ?)", curier_id, self.zona_id)
                cursor.commit()
                messagebox.showinfo("Success", f"The courier {self.last_name_courier_entry.get()} {self.first_name_courier_entry.get()} was registred.",
                                    parent=self.window)

                # close connection
                conectare.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.window)
                self.window.destroy()

        # clear all the text boxes
        self.last_name_courier_entry.delete(0, END)
        self.first_name_courier_entry.delete(0, END)
        self.cnp_courier_entry.delete(0, END)
        self.phone_courier_entry.delete(0, END)
        self.salary_courier_entry.delete(0, END)
        self.bonus_entry.delete(0, END)
        self.zone_city_entry.delete(0, END)
        self.zone_name_entry.delete(0, END)

    ###########################################################################################################

    def delete_parcel_menu(self):
        self.delete_frame = Canvas(self.window, bg="white", height=300, width=500)
        self.delete_frame.place(x=250, y=70)

        # TITLE
        self.delete_title = Label(self.delete_frame, text="Delete parcel", bg="white", fg="black",
                                       font=("proxima nova", 15))
        self.delete_title.place(x=200, y=10)

        # DELETE A ROW BY ID AND NAME
        self.delete = Label(self.delete_frame, text="Delete a row by Name and Code", bg="white", fg="black",
                            font=("proxima nova", 12))
        self.delete.place(x=20, y=80)


        # LINE
        self.delete_frame.create_line(0, 110, 250, 110, fill="light grey")

        # LABEL & ENTRY FOR ID
        # LABEL & ENTRY FOR NAME
        self.name_parsel = Label(self.delete_frame, text="Name", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.name_parsel.place(x=20, y=120)
        self.name_parsel_entry = Entry(self.delete_frame, font=("proxima nova", 10), bg="lightgray")
        self.name_parsel_entry.place(x=65, y=120)

        self.id = Label(self.delete_frame, text="Code", bg="white", fg="grey",
                        font=("proxima nova", 10))
        self.id.place(x=20, y=150)
        self.id_entry = Entry(self.delete_frame, font=("proxima nova", 10), bg="lightgray")
        self.id_entry.place(x=65, y=150)

        # BUTTON FOR DELETE
        self.delete_btn = Button(self.delete_frame, text="DELETE", font=("times new roman", 12),
                                anchor=CENTER, command=self.delete_fct)
        self.delete_btn.place(x=250, y=130, height=40, width=65)


        # DELETE BY DATE (if the date is very old, delete the parcel to not aglomerate database)
        self.delete_by_date = Label(self.delete_frame, text="Delete by DATE", bg="white", fg="black",
                            font=("proxima nova", 12))
        self.delete_by_date.place(x=20, y=190)

        # LINE
        self.delete_frame.create_line(0, 220, 150, 220, fill="light grey")

        # LABEL & ENTRY FOR DATE
        self.date = Label(self.delete_frame, text="Date", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.date.place(x=20, y=240)
        self.date_entry = Entry(self.delete_frame, font=("proxima nova", 10), bg="lightgray")
        self.date_entry.place(x=65, y=240)

        # BUTTON DELETE BY DATE
        self.delete_by_date_btn = Button(self.delete_frame, text="DELETE", font=("times new roman", 12),
                                 anchor=CENTER, command=self.delete_by_date_fct)
        self.delete_by_date_btn.place(x=250, y=230, height=40, width=65)

    def delete_fct(self):
        # connect to database
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("SELECT ColetID FROM Colete WHERE Denumire = ? and Cod = ?", self.name_parsel_entry.get(),
                       self.id_entry.get())
        self.colet_id = cursor.fetchone()[0]

        cursor.execute("DELETE FROM ClientiColete WHERE ColetID = ?", self.colet_id)

        cursor.execute("DELETE FROM Colete WHERE Denumire = ? AND Cod = ?", self.name_parsel_entry.get(),
                       self.id_entry.get())
        cursor.commit()


        conectare.close()

        # clear all the entry
        self.id_entry.delete(0, END)
        self.name_parsel_entry.delete(0, END)

    def delete_by_date_fct(self):
        # connect to database
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("SELECT ColetID FROM Colete WHERE DataLivrarii < ?", self.date_entry.get())
        for row in cursor.fetchall():
            self.colet_id = row[0]
            cursor.execute("DELETE FROM ClientiColete WHERE ColetID = ?", self.colet_id)
            cursor.commit()

        cursor.execute("DELETE FROM Colete WHERE DataLivrarii < ?", self.date_entry.get())
        cursor.commit()
        conectare.close()

        # clear the entry
        self.date_entry.delete(0, END)

#####################################################################################################

    def delete_courier_menu(self):
        self.delete_c_frame = Canvas(self.window, bg="white", height=300, width=500)
        self.delete_c_frame.place(x=250, y=70)

        # TITLE
        self.del_title = Label(self.delete_c_frame, text="Delete Courier", bg="white",
                               font=("proxima nova", 15), fg="black")
        self.del_title.place(x=180, y=10)

        # DELETE A ROW BY ID AND NAME
        self.delete_courier = Label(self.delete_c_frame, text="Delete a courier by Name and CNP", bg="white", fg="black",
                            font=("proxima nova", 12))
        self.delete_courier.place(x=20, y=80)

        # LINE
        self.delete_c_frame.create_line(0, 110, 250, 110, fill="light grey")

        # FIRST NAME
        self.c_fname = Label(self.delete_c_frame, text="First name", bg="white", fg="grey",
                        font=("proxima nova", 10))
        self.c_fname.place(x=20, y=130)
        self.c_fname_entry = Entry(self.delete_c_frame, font=("proxima nova", 10), bg="lightgray")
        self.c_fname_entry.place(x=90, y=130)

        # LAST NAME
        self.c_lname = Label(self.delete_c_frame, text="Last name", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.c_lname.place(x=20, y=160)
        self.c_lname_entry = Entry(self.delete_c_frame, font=("proxima nova", 10), bg="lightgray")
        self.c_lname_entry.place(x=90, y=160)

        # CNP
        self.c_cnp = Label(self.delete_c_frame, text="CNP", bg="white", fg="grey",
                          font=("proxima nova", 10))
        self.c_cnp.place(x=20, y=190)
        self.c_cnp_entry = Entry(self.delete_c_frame, font=("proxima nova", 10), bg="lightgray")
        self.c_cnp_entry.place(x=90, y=190)

        # DELETE BUTTON
        self.c_delete_btn = Button(self.delete_c_frame, text="DELETE", font=("times new roman", 12),
                                anchor=CENTER, command=self.delete_c_fct)
        self.c_delete_btn.place(x=100, y=240, height=40, width=65)

    def delete_c_fct(self):
        # connect to database
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("SELECT CurierID FROM Curieri WHERE CNP = ? AND Nume = ? AND Prenume = ?", int(self.c_cnp_entry.get()),
                       self.c_lname_entry.get(), self.c_fname_entry.get())
        self.curier_id = cursor.fetchone()[0]

        cursor.execute("DELETE FROM CurieriZone WHERE CurierID = ?", self.curier_id)
        cursor.commit()

        cursor.execute("DELETE FROM Colete WHERE CurierID = ?", self.curier_id)
        cursor.commit()

        cursor.execute("DELETE FROM Curieri WHERE CNP = ? AND Nume = ? AND Prenume = ?",
                       int(self.c_cnp_entry.get()), self.c_lname_entry.get(), self.c_fname_entry.get())
        cursor.commit()

        conectare.close()

        # clear all the entry
        self.c_cnp_entry.delete(0, END)
        self.c_lname_entry.delete(0, END)
        self.c_fname_entry.delete(0, END)

#########################################################################################################

    def update_location_menu(self):
        self.update_l_frame = Canvas(self.window, bg="white", height=300, width=500)
        self.update_l_frame.place(x=250, y=70)

        # TITLE
        self.up_title = Label(self.update_l_frame, text="Update Location", bg="white",
                               font=("proxima nova", 15), fg="black")
        self.up_title.place(x=180, y=10)

        # CHOOSE THE PARCEL BY NAME AND ID
        self.choose = Label(self.update_l_frame, text="Choose a parcel by Name and Code", bg="white", fg="black",
                                    font=("proxima nova", 12))
        self.choose.place(x=20, y=80)

        # LINE
        self.update_l_frame.create_line(0, 110, 250, 110, fill="light grey")

        # ID
        self.name_parsel = Label(self.update_l_frame, text="Name", bg="white", fg="grey",
                        font=("proxima nova", 10))
        self.name_parsel.place(x=20, y=130)
        self.name_parsel_entry = Entry(self.update_l_frame, font=("proxima nova", 10), bg="lightgray")
        self.name_parsel_entry.place(x=80, y=130)

        # LABEL & ENTRY FOR NAME
        self.code = Label(self.update_l_frame, text="Code", bg="white", fg="grey",
                                 font=("proxima nova", 10))
        self.code.place(x=20, y=160)
        self.code_entry = Entry(self.update_l_frame, font=("proxima nova", 10), bg="lightgray")
        self.code_entry.place(x=80, y=160)

        # NEW LOCATION
        self.location = Label(self.update_l_frame, text="Location", bg="white", fg="grey",
                           font=("proxima nova", 10))
        self.location.place(x=20, y=190)
        self.location_entry = Entry(self.update_l_frame, font=("proxima nova", 10), bg="lightgray")
        self.location_entry.place(x=80, y=190)

        # UPDATE BUTTON
        self.update_btn = Button(self.update_l_frame, text="UPDATE", font=("times new roman", 12),
                                   anchor=CENTER, command=self.update_loc_fct)
        self.update_btn.place(x=100, y=240, height=40, width=80)

    def update_loc_fct(self):

        # connect to database
        global localizare_id
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()


        cursor.execute("SELECT * FROM Localizari")
        for row in cursor.fetchall():
            if(row[3] == self.location_entry.get()):
                localizare_id = row[0]

        cursor.execute("UPDATE Colete SET LocalizareID = ? WHERE Denumire = ? AND Cod = ?",
                       localizare_id, self.name_parsel_entry.get(), self.code_entry.get())
        cursor.commit()

        conectare.close()

        # clear all the entry
        self.location_entry.delete(0, END)
        self.code_entry.delete(0, END)
        self.name_parsel_entry.delete(0, END)

#######################################################################################################
    def update_salary_menu(self):
        self.update_s_frame = Canvas(self.window, bg="white", height=300, width=500)
        self.update_s_frame.place(x=250, y=70)

        # TITLE
        self.up_s_title = Label(self.update_s_frame, text="Update Salary", bg="white",
                               font=("proxima nova", 15), fg="black")
        self.up_s_title.place(x=180, y=10)

        # CHOOSE THE COURIER
        self.choose = Label(self.update_s_frame, text="Choose the courieri by name and CNP", bg="white", fg="black",
                                    font=("proxima nova", 12))
        self.choose.place(x=20, y=80)

        # LINE
        self.update_s_frame.create_line(0, 110, 250, 110, fill="light grey")

        # FIRST NAME
        self.c_fname = Label(self.update_s_frame, text="First name", bg="white", fg="grey",
                             font=("proxima nova", 10))
        self.c_fname.place(x=20, y=130)
        self.c_fname_entry = Entry(self.update_s_frame, font=("proxima nova", 10), bg="lightgray")
        self.c_fname_entry.place(x=90, y=130)

        # LAST NAME
        self.c_lname = Label(self.update_s_frame, text="Last name", bg="white", fg="grey",
                             font=("proxima nova", 10))
        self.c_lname.place(x=20, y=160)
        self.c_lname_entry = Entry(self.update_s_frame, font=("proxima nova", 10), bg="lightgray")
        self.c_lname_entry.place(x=90, y=160)

        # CNP
        self.c_cnp = Label(self.update_s_frame, text="CNP", bg="white", fg="grey",
                           font=("proxima nova", 10))
        self.c_cnp.place(x=20, y=190)
        self.c_cnp_entry = Entry(self.update_s_frame, font=("proxima nova", 10), bg="lightgray")
        self.c_cnp_entry.place(x=90, y=190)

        # NEW SALARY
        self.salary = Label(self.update_s_frame, text="Salary", bg="white", fg="grey",
                              font=("proxima nova", 10))
        self.salary.place(x=20, y=220)
        self.salary_entry = Entry(self.update_s_frame, font=("proxima nova", 10), bg="lightgray")
        self.salary_entry.place(x=90, y=220)

        # UPDATE BUTTON
        self.update_btn = Button(self.update_s_frame, text="UPDATE", font=("times new roman", 12),
                                 anchor=CENTER, command=self.update_salary_fct)
        self.update_btn.place(x=100, y=250, height=40, width=80)

    def update_salary_fct(self):

        # connect to database
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("UPDATE Curieri SET Salariu = ? WHERE Nume = ? AND Prenume = ? AND CNP = ?",
                       self.salary_entry.get(), self.c_lname_entry.get(), self.c_fname_entry.get(),
                       self.c_cnp_entry.get())
        cursor.commit()

        conectare.close()

        # clear all the entry
        self.c_fname_entry.delete(0, END)
        self.c_lname_entry.delete(0, END)
        self.c_cnp_entry.delete(0, END)
        self.salary_entry.delete(0, END)

#####################################################################################################

    def display_couriers(self):

        # new window
        self.disp_couriers_win = Toplevel(self.window)
        self.disp_couriers_win.geometry("600x400")
        self.disp_couriers_win.title("Display Couriers")

        # TITLE
        self.display_title = Label(self.disp_couriers_win, text="Couriers", fg="black",
                                  font=("proxima nova", 15))
        self.display_title.place(x=250, y=20)


        # connect with daatbase
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("SELECT * FROM Curieri")

        tree = ttk.Treeview(self.disp_couriers_win)
        tree["show"] = "headings"

        tree["columns"] = ("CurierID", "Nume", "Prenume", "CNP", "Telefon", "Salariu", "Bonus")
        tree.column("CurierID", width=60, minwidth=60, anchor=CENTER)
        tree.column("Nume", width=80, minwidth=80, anchor=CENTER)
        tree.column("Prenume", width=100, minwidth=100, anchor=CENTER)
        tree.column("CNP", width=100, minwidth=100, anchor=CENTER)
        tree.column("Telefon", width=80, minwidth=80, anchor=CENTER)
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

        tree.place(x=40,y=80)

        conectare.close()

    def display_locations(self):

        # new window
        self.disp_loc_win = Toplevel(self.window)
        self.disp_loc_win.geometry("600x400")
        self.disp_loc_win.title("Display Locations")

        # TITLE
        self.display_title = Label(self.disp_loc_win, text="Locations", fg="black",
                                   font=("proxima nova", 15))
        self.display_title.place(x=250, y=20)

        # connect with daatbase
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("SELECT * FROM Localizari")

        tree = ttk.Treeview(self.disp_loc_win)
        tree["show"] = "headings"

        tree["columns"] = ("LocalizareID", "Cod", "Adresa", "Localitate", "Tara")
        tree.column("LocalizareID", width=80, minwidth=60, anchor=CENTER)
        tree.column("Cod", width=80, minwidth=80, anchor=CENTER)
        tree.column("Adresa", width=150, minwidth=150, anchor=CENTER)
        tree.column("Localitate", width=100, minwidth=100, anchor=CENTER)
        tree.column("Tara", width=80, minwidth=80, anchor=CENTER)

        tree.heading("LocalizareID", text="LocationID", anchor=CENTER)
        tree.heading("Cod", text="Code", anchor=CENTER)
        tree.heading("Adresa", text="Address", anchor=CENTER)
        tree.heading("Localitate", text="City", anchor=CENTER)
        tree.heading("Tara", text="Country", anchor=CENTER)

        i = 0
        for row in cursor:
            tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4]))
            i = i + 1

        tree.place(x=50, y=80)

        conectare.close()

###################################################################################################################################

    def display_customers(self):

        # new window
        self.disp_loc_win = Toplevel(self.window)
        self.disp_loc_win.geometry("600x400")
        self.disp_loc_win.title("Display Customers")

        # TITLE
        self.display_title = Label(self.disp_loc_win, text="Customers", fg="black",
                                   font=("proxima nova", 15))
        self.display_title.place(x=250, y=20)

        # connect with daatbase
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("SELECT ClientID, Nume, Prenume, CNP, TipClient FROM Clienti")

        tree = ttk.Treeview(self.disp_loc_win)
        tree["show"] = "headings"

        tree["columns"] = ("ClientID", "Nume", "Prenume", "CNP", "TipClient")
        tree.column("ClientID", width=80, minwidth=60, anchor=CENTER)
        tree.column("Nume", width=80, minwidth=80, anchor=CENTER)
        tree.column("Prenume", width=150, minwidth=150, anchor=CENTER)
        tree.column("CNP", width=100, minwidth=100, anchor=CENTER)
        tree.column("TipClient", width=80, minwidth=80, anchor=CENTER)

        tree.heading("ClientID", text="ClientID", anchor=CENTER)
        tree.heading("Nume", text="Last Name", anchor=CENTER)
        tree.heading("Prenume", text="First Name", anchor=CENTER)
        tree.heading("CNP", text="CNP", anchor=CENTER)
        tree.heading("TipClient", text="Client type", anchor=CENTER)

        i = 0
        for row in cursor:
            tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4]))
            i = i + 1

        tree.place(x=50, y=80)

        conectare.close()

######################################################################################################################################

    def display_parcels(self):

        # new window
        self.disp_loc_win = Toplevel(self.window)
        self.disp_loc_win.geometry("700x500")
        self.disp_loc_win.title("Display Parcels")

        # TITLE
        self.display_title = Label(self.disp_loc_win, text="Parcels", fg="black",
                                   font=("proxima nova", 15))
        self.display_title.place(x=300, y=20)

        # connect with daatbase
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("SELECT ColetID, Denumire, Cod, DataLivrarii, LocalizareID FROM Colete")

        tree = ttk.Treeview(self.disp_loc_win)
        tree["show"] = "headings"

        tree["columns"] = ("ColetID", "Denumire", "Cod", "DataLivrarii", "LocalizareID")
        tree.column("ColetID", width=80, minwidth=60, anchor=CENTER)
        tree.column("Denumire", width=80, minwidth=80, anchor=CENTER)
        tree.column("Cod", width=150, minwidth=150, anchor=CENTER)
        tree.column("DataLivrarii", width=150, minwidth=150, anchor=CENTER)
        tree.column("LocalizareID", width=150, minwidth=150, anchor=CENTER)

        tree.heading("ColetID", text="ColetID", anchor=CENTER)
        tree.heading("Denumire", text="Name", anchor=CENTER)
        tree.heading("Cod", text="Code", anchor=CENTER)
        tree.heading("DataLivrarii", text="DataLivrarii", anchor=CENTER)
        tree.heading("LocalizareID", text="LocalizareID", anchor=CENTER)

        i = 0
        for row in cursor:
            tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4]))
            i = i + 1

        tree.place(x=70, y=80)

        conectare.close()

    def display_zones(self):

        # new window
        self.disp_loc_win = Toplevel(self.window)
        self.disp_loc_win.geometry("600x400")
        self.disp_loc_win.title("Display Areas")

        # TITLE
        self.display_title = Label(self.disp_loc_win, text="Areas", fg="black",
                                   font=("proxima nova", 15))
        self.display_title.place(x=250, y=20)

        # connect with daatbase
        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()

        cursor.execute("SELECT ZonaID, Denumire, Localitate FROM Zone")

        tree = ttk.Treeview(self.disp_loc_win)
        tree["show"] = "headings"

        tree["columns"] = ("ZonaID", "Denumire", "Localitate")
        tree.column("ZonaID", width=80, minwidth=60, anchor=CENTER)
        tree.column("Denumire", width=80, minwidth=80, anchor=CENTER)
        tree.column("Localitate", width=150, minwidth=150, anchor=CENTER)

        tree.heading("ZonaID", text="ZonaID", anchor=CENTER)
        tree.heading("Denumire", text="Name", anchor=CENTER)
        tree.heading("Localitate", text="City", anchor=CENTER)
        i = 0
        for row in cursor:
            tree.insert('', i, text='', values=(row[0], row[1], row[2]))
            i = i + 1

        tree.place(x=150, y=80)

        conectare.close()

    def show_function(self):
        show_root = Toplevel()
        ShowWindow(show_root)
        show_root.mainloop()
# #
# root = Tk()
# obj = SecondWindow(root)
# root.mainloop()