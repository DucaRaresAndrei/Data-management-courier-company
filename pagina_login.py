from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pyodbc
from second_window import *


class Login:

    string_de_conectare = r"driver={SQL SERVER}; server=DESKTOP-FA5P09O\SQLEXPRESS; database=BD_Proiect; trusted_connection=YES"

    def __init__(self, root):

        self.root = root
        self.root.iconify()
        self.root.title("Logare")
        self.root.geometry("600x600")
        self.photo = PhotoImage(file="motorbike.png")
        self.root.iconphoto(False, self.photo)
        self.root.resizable(False, False)

        # aleg imaginea de background
        self.bg_image = ImageTk.PhotoImage(file="poza3.jpg")
        self.bg = Label(self.root, image=self.bg_image).place(x=0, y=0, relwidth=1, relheight=1)

        # login frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=150, y=100, height=400, width=300)

        # title
        title = Label(Frame_login, text="LogIn", bg="white", fg="#8b8378", font=("Impact", 35, "bold"))
        title.place(x=50, y=30)

        #description "Authentication"
        description = Label(Frame_login, text="Authentication",
                            bg="white", fg="#ccc0a6", font=("Goudy old style", 15, "bold"))
        description.place(x=50, y=100)

        # username
        username_label = Label(Frame_login, text="Username", bg="white",
                               fg="#09324f", font=("Goudy old style", 15, "bold"))
        username_label.place(x=50, y=140)
        self.username_text = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.username_text.place(x=50, y=170)

        # username icon
        self.user_icon_img = ImageTk.PhotoImage(file="user.png")
        self.user_icon = Label(Frame_login, image=self.user_icon_img, bg="white").place(x=32, y=144)

        # password
        password_label = Label(Frame_login, text="Password",
                               bg="white", fg="#09324f", font=("Goudy old style", 15, "bold"))
        password_label.place(x=50, y=200)
        self.password_text = Entry(Frame_login, show="*", font=("times new roman", 15), bg="lightgray")
        self.password_text.place(x=50, y=230)

        # password icon
        self.password_icon_img = ImageTk.PhotoImage(file="lock.png")
        self.password_icon = Label(Frame_login, image=self.password_icon_img, bg="white").place(x=32, y=203)

        # show password button
        self.show_password_img = ImageTk.PhotoImage(file="eye.png")
        self.show_password_btn = Button(Frame_login, image=self.show_password_img, bg="white", activebackground="white",
                                        borderwidth=0, command=self.show_function)
        self.show_password_btn.place(x=258, y=233, width=20, height=20)

        # login button
        login_button = Button(self.root, command=self.login_function, cursor="hand2", text="Login", fg="white", bg="#CDAA7D",
                        font=("times new roman", 20))
        login_button.place(x=240, y=480, width=120, height=40)

        # forgot password
        forgot_button = Button(Frame_login, command=self.forgot_password_window, text="Forgot password?",
                               cursor="hand2",
                               bd=0, bg="white", fg="#CDAA7D", font=("times new roman", 12))
        forgot_button.place(x=50, y=255)

        # courier icon
        self.courier_img = ImageTk.PhotoImage(file="delivery-courier (1).png")
        self.courier_icon = Label(Frame_login, image=self.courier_img, bg="white").place(x=200, y=30)

        # car icon
        self.car_img = ImageTk.PhotoImage(file="express-delivery.png")
        self.car_icon = Label(Frame_login, image=self.car_img, bg="white").place(x=115, y=290)

    def login_function(self):

        if self.username_text.get() == "" or self.password_text.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()
                sql_res = cursor.execute("SELECT * FROM ConturiAdministratori")
                sql_res = cursor.fetchone()
                if self.password_text.get() != sql_res[2] or self.username_text.get() != sql_res[1]:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    second_root = Toplevel(self.root)
                    SecondWindow(second_root)
                    self.root.withdraw()
                    second_root.mainloop()

            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.root)
                self.root.destroy()

    def show_function(self):
        if self.password_text.cget("show") == '':
            self.password_text.config(show="*")     # hidden password
        else:
            self.password_text.config(show="")      # visible password

    def change_password(self):
        if self.username_id.get() == "" or self.new_password.get() == "" or self.confirm_new_password.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        elif self.new_password.get() != self.confirm_new_password.get():
            messagebox.showerror("Error", "Confirm password is not identical with new password.", parent=self.root)
        else:
            try:
                conectare = pyodbc.connect(string_de_conectare)
                cursor = conectare.cursor()
                cursor.execute("SELECT NumeUtilizator FROM ConturiAdministratori")
                row = cursor.fetchone()
                if self.username_id.get() != row[0]:
                    messagebox.showerror("Error", "Please enter a valid username to reset the password.", parent=self.root)
                else:
                    cursor.execute("UPDATE ConturiAdministratori SET Parola = ?", self.new_password.get())
                    cursor.commit()
                    conectare.close()
                    messagebox.showinfo("Success", "Your password has been reset.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error Due to: {str(e)}", parent=self.root)
                self.root.destroy()

    def forgot_password_window(self):

        conectare = pyodbc.connect(string_de_conectare)
        cursor = conectare.cursor()
        cursor.execute("SELECT NumeUtilizator FROM ConturiAdministratori")
        row = cursor.fetchone()
        forgot_root = Toplevel()
        self.forgot_root = forgot_root
        self.forgot_root.title("Forgot password")
        self.forgot_root.geometry("400x400+600+100")
        self.forgot_root.resizable(False, False)
        self.forgot_root.config(bg="#ccc0a6")
        self.photo = PhotoImage(file="motorbike.png")
        self.forgot_root.iconphoto(False, self.photo)

        self.canvas = Canvas(self.forgot_root, bg="#ccc0a6", bd=0, width=500, height=500)
        self.canvas.place(x=0, y=0)


        # username in forgot password window
        self.username_id_label = Label(self.forgot_root, text="Username", bg="#ccc0a6",
                                       fg="#09324f", font=("Goudy old style", 13, "bold"))
        self.username_id_label.place(x=100, y=125)
        self.username_id = Entry(self.canvas, font=("times new roman", 15), bg="lightgray")
        self.username_id.place(x=100, y=150)

        # new password in forgot password window
        self.new_password_label = Label(self.canvas, text="New password", bg="#ccc0a6",
                                        fg="#09324f", font=("Goudy old style", 13, "bold"))
        self.new_password_label.place(x=100, y=185)
        self.new_password = Entry(self.canvas, font=("times new roman", 15), bg="lightgray")
        self.new_password.place(x=100, y=210)

        # confirm new password in forgot password window
        self.confirm_new_password_label = Label(self.canvas, text="Confirm password", bg="#ccc0a6",
                                                fg="#09324f", font=("Goudy old style", 13, "bold"))
        self.confirm_new_password_label.place(x=100, y=245)
        self.confirm_new_password = Entry(self.canvas, font=("times new roman", 15), bg="lightgray")
        self.confirm_new_password.place(x=100, y=270)

        # change password button
        self.change_button = Button(self.canvas, command=self.change_password, text="Change password",
                                    font=("times new roman", 15))
        self.change_button.place(x=110, y=320, height=40, width=180)

        # label for description
        description = Label(self.canvas, text="Change Password",
                            bg="#ccc0a6", fg="black", font=("Goudy old style", 18, "bold"))
        description.place(x=90, y=85)

        # change icons
        self.change_img = ImageTk.PhotoImage(file="gear.png")
        self .change_icon= Label(self.forgot_root, image=self.change_img, bg="#ccc0a6").place(x=168, y=15)

        # courier icon
        self.courier_img = ImageTk.PhotoImage(file="deliver_icon.png")
        self.courier_icon = Label(self.forgot_root, image=self.courier_img, bg="#ccc0a6").place(x=10, y=168)

        # box icon
        self.box_img = ImageTk.PhotoImage(file="box.png")
        self.box_icon = Label(self.forgot_root, image=self.box_img, bg="#ccc0a6").place(x=320, y=168)

