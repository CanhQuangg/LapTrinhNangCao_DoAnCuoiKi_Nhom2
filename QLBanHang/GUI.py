from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, END, filedialog, ttk, LabelFrame, \
    Scrollbar, Toplevel

from openpyxl import *
import pandas as pd
from Class import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

#open database
global wb
wb = load_workbook("Database.xlsx")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class GUI_Login(Tk):
    def __init__(self, window):
        self.window = window
        self.window.title("Moring Coffee")
        self.window.geometry("1250x800")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 800,
            width = 1250,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0, y=0)

        #Background
        self.image_LoginBG = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.Login_Background = self.canvas.create_image(
            625.0,
            400.0,
            image = self.image_LoginBG
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            625.0,
            361.0,
            image=self.image_image_2
        )

        #Button
        ##Button login with staff account
        self.button_Login_Staff_Image = PhotoImage(
            file=relative_to_assets("Login_Staff.png"))
        self.button_login_staff = Button(
            image=self.button_Login_Staff_Image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonLoginStaff,
            relief="flat"
        )
        self.button_login_staff.place(
            x=625.0,
            y=609.0,
            width=265.0,
            height=77.0
        )

        ##Button login with manager account
        self.button_login_manager_image_2 = PhotoImage(
            file=relative_to_assets("Login_Manager.png"))
        self.button_login_manager = Button(
            image=self.button_login_manager_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonLoginManager,
            relief="flat"
        )
        self.button_login_manager.place(
            x=360.0,
            y=609.0,
            width=265.0,
            height=77.0
        )

        #Entry
        ##Entry username
        ###Underline entry box
        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            633.0,
            422.0,
            image=self.image_image_4
        )
        ###entry box
        self.entry_username_image = PhotoImage(
            file=relative_to_assets("entry_username.png"))
        self.entry_bg_2 = self.canvas.create_image(
            633,
            377,
            image=self.entry_username_image
        )

        self.entry_username = Entry(
            bd=0,
            bg="#BFBFBF",
            font=("Helvetica", 15),
            highlightthickness=0
        )
        self.entry_username.place(
            x=430.0,
            y=355,
            width=395.0,
            height=61
        )

        ##Entry password
        ### Underline entry password
        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            633.0,
            541.0,
            image=self.image_image_3
        )

        ###Entry box
        self.entry_password_image = PhotoImage(
            file=relative_to_assets("entry_password.png"))
        self.entry_bg_1 = self.canvas.create_image(
            633.5,
            495.5,
            image=self.entry_password_image
        )
        self.entry_password = Entry(
            bd=0,
            bg="#BFBFBF",
            show="*",
            width=30,
            highlightthickness=0
        )
        self.entry_password.place(
            x=430.0,
            y=475,
            width=395.0,
            height=61
        )

        #Label "Login"
        self.image_image_5 = PhotoImage(
            file=relative_to_assets("label_login.png"))
        self.image_5 = self.canvas.create_image(
            625.0,
            297.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("label_brand.png"))
        self.image_6 = self.canvas.create_image(
            625.0,
            210.0,
            image=self.image_image_6
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    #message
    def message_wrong(self):
        messagebox.showerror("Cannot Login", "Username or Password is incorrect")

    def message_wrong_role(self):
        messagebox.showerror("Cannot Login", "Canot login with that role")

    #Login
    def check_Account(self):
        wb = load_workbook("Database.xlsx")
        ws_Login = wb['LoginAccount']

        if self.entry_username.get() == '':
            messagebox.showwarning("Cannot Login", "Enter your Username")
            return False
        if self.entry_password.get() == '':
            messagebox.showwarning("Cannot Login", "Enter your Password")
            return False

        for row in ws_Login.values:
            if self.entry_username.get() == str(row[0]):
                if self.entry_password.get() == str(row[1]):
                    if self.role == row[2]:
                        wb.close()
                        return True
                    else:
                        self.message_wrong_role()
                        return False
                else:
                    self.message_wrong()
                    self.entry_password.delete(0, END)
                    return False
            else:
                continue

        #
        self.message_wrong()
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        return False

    #run button
    def buttonLoginManager(self):
        self.role = "Manager"

        check = self.check_Account()
        if check == True:
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)

            self.canvas.destroy()
            self.entry_password.destroy()
            self.entry_username.destroy()
            self.button_login_manager.destroy()
            self.button_login_staff.destroy()

            #self.window.destroy()
            GUI_Manager(self.window)

    def buttonLoginStaff(self):
        self.role = "Staff"

        check = self.check_Account()
        if check == True:
            self.entry_username.delete(0, END)
            self.entry_password.delete(0, END)


class GUI_Manager(Tk):
    def __init__(self,window):
        self.window = window
        self.status = "Overview"
        self.canvas = Canvas(
            #self.manager_window,
            self.window,
            bg="#FFFFFF",
            height=800,
            width=1250,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        # Navigation bar
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1250.0,
            65.0,
            fill="#85603F",
            outline="")

        # Logout button
        self.button_logout_image = PhotoImage(
            file=relative_to_assets("button_logout.png"))
        self.button_logout = Button(
            image=self.button_logout_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonLogout,
            relief="flat"
        )
        self.button_logout.place(
            x=1049.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # Report button
        self.button_report_image = PhotoImage(
            file=relative_to_assets("button_report.png"))
        self.button_report = Button(
            image=self.button_report_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonReport,
            relief="flat"
        )
        self.button_report.place(
            x=883.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        #button_customers
        self.button_customers_image = PhotoImage(
            file=relative_to_assets("button_customers.png"))
        self.button_customers = Button(
            image=self.button_customers_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCustomers,
            relief="flat"
        )
        self.button_customers.place(
            x=718.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        #button_cashBook
        self.button_cashBook_image = PhotoImage(
            file=relative_to_assets("button_cashBook.png"))
        self.button_cashBook = Button(
            image=self.button_cashBook_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCashBook,
            relief="flat"
        )
        self.button_cashBook.place(
            x=552.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        #button_staffs
        self.button_staffs_image = PhotoImage(
            file=relative_to_assets("button_staffs.png"))
        self.button_staffs = Button(
            image=self.button_staffs_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonStaffs,
            relief="flat"
        )
        self.button_staffs.place(
            x=387.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        #button_warehouse
        self.button_warehouse_image = PhotoImage(
            file=relative_to_assets("button_warehouse.png"))
        self.button_warehouse = Button(
            image=self.button_warehouse_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonWarehouse,
            relief="flat"
        )
        self.button_warehouse.place(
            x=221.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        #button_overview
        self.button_overview_image = PhotoImage(
            file=relative_to_assets("button_overview_show.png"))
        self.button_overview = Button(
            image=self.button_overview_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonOverview,
            relief="flat"
        )
        self.button_overview.place(
            x=55.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        self.frame_overview()

        self.window.mainloop()

    #----------------------------

    #searchBar event
    def search_material(self):
        check = self.entry_searchBar.get()
        list = []
        if check == "":
            self.frame_treeview_data("Warehouse", self.tv3)
        else:
            for row in self.ws_warehouse.values:
                for value in row:
                    value = str(value)
                    if check.lower() in value.lower():
                        list.append(row)

            self.clean_data(self.tv3)
            for row in list: self.tv3.insert("", "end", values=row)

    #frame
    def frame_overview(self):
        #Pie chart showing
        self.image_image_pieChart = PhotoImage(
            file=relative_to_assets("PieChart.png"))
        self.image_pieChart = self.canvas.create_image(
            221.0,
            309.0,
            image=self.image_image_pieChart
        )

        self.pieChartBox = self.canvas.create_rectangle(
            442.0,
            144.0,
            1195.0,
            636.0,
            fill="#FFFFFF",
            outline="")

        # buttun_options
        ##show_data_warehouse
        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.frame_treeview_data("Warehouse",self.tv1),
            relief="flat"
        )
        self.button_8.place(
            x=939.0,
            y=678.0,
            width=146.0,
            height=40.0
        )

        ##show_data_bill
        self.button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.frame_treeview_data("Bill",self.tv1),
            relief="flat"
        )
        self.button_9.place(
            x=1105.0,
            y=678.0,
            width=90.0,
            height=40.0
        )

        ##show_data_customers
        self.button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda : self.frame_treeview_data("CustomerList",self.tv1),
            relief="flat"
        )
        self.button_10.place(
            x=774.0,
            y=678.0,
            width=145.0,
            height=40.0
        )

        ##show_data_menu
        self.button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.frame_treeview_data("Menu",self.tv1),
            relief="flat"
        )
        self.button_11.place(
            x=608.0,
            y=678.0,
            width=145.0,
            height=40.0
        )

        ##show_data_staffs
        self.button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda : self.frame_treeview_data("StaffList",self.tv1),
            relief="flat"
        )
        self.button_12.place(
            x=442.0,
            y=678.0,
            width=146.0,
            height=40.0
        )

        # frame_showData
        self.frame_showData = LabelFrame(
            self.window,
            background="white",
        )
        self.frame_showData.place(
            x=442,
            y=137,
            width=753,
            height=449
        )

        ## Treeview Widget revenue
        self.tv1 = ttk.Treeview(self.frame_showData)
        self.tv1.place(relheight=1,
                       relwidth=1)

        self.treescrolly = Scrollbar(
            self.frame_showData, orient="vertical",
            command=self.tv1.yview)
        self.treescrollx = Scrollbar(
            self.frame_showData, orient="horizontal",
            command=self.tv1.xview)
        self.tv1.configure(xscrollcommand=self.treescrollx.set,
                           yscrollcommand=self.treescrolly.set)
        self.treescrollx.pack(side="bottom", fill="x")
        self.treescrolly.pack(side="right", fill="y")

        #show data in treeview
        self.frame_treeview_data("StaffList",self.tv1)

        ##Statistical_data
        ### frame_show_statistical_data
        self.frame_statistical_data = LabelFrame(
            self.window,
            background="white",
        )
        self.frame_statistical_data.place(
            x=55,
            y=535,
            width=312,
            height=182
        )

        self.tv2 = ttk.Treeview(self.frame_statistical_data)
        self.tv2.place(relheight=1,
                       relwidth=1)

        self.treescrolly2 = Scrollbar(
            self.frame_statistical_data, orient="vertical",
            command=self.tv2.yview)
        self.treescrollx2 = Scrollbar(
            self.frame_statistical_data, orient="horizontal",
            command=self.tv2.xview)
        self.tv2.configure(xscrollcommand=self.treescrollx2.set,yscrollcommand=self.treescrolly2.set)
        self.treescrollx2.pack(side="bottom", fill="x")
        self.treescrolly2.pack(side="right", fill="y")

        self.clean_data(self.tv2)
        self.df2 = pd.read_excel("Database.xlsx", sheet_name="Statistical")
        self.tv2["column"] = list(self.df2.columns)
        self.tv2.column("#0", width=120, minwidth=20)
        self.tv2.column("Revenue", width=70, minwidth=60)
        self.tv2.column("Cost", width=70, minwidth=60)
        self.tv2.column("Profit", width=70, minwidth=60)
        self.tv2["show"] = "headings"
        for column in self.tv2["columns"]:
            self.tv2.heading(column, text=column)

        self.df2_rows = self.df2.to_numpy().tolist()
        for row in self.df2_rows:
            self.tv2.insert("", "end", values=row)

    def frame_warehouse(self):
        self.ws_warehouse = wb["Warehouse"]

        # warehouse_showData
        self.warehouse_frame_showData = LabelFrame(
            self.window,
            background="white",
        )
        self.warehouse_frame_showData.place(
            x=55,
            y=246,
            width=1140,
            height=472
        )

        ## Treeview Widget
        self.tv3 = ttk.Treeview(self.warehouse_frame_showData)
        self.tv3.place(relheight=1,
                       relwidth=1)

        self.treescrolly3 = Scrollbar(
            self.warehouse_frame_showData, orient="vertical",
            command=self.tv3.yview)
        self.treescrollx3 = Scrollbar(
            self.warehouse_frame_showData, orient="horizontal",
            command=self.tv3.xview)
        self.tv3.configure(xscrollcommand=self.treescrollx3.set,
                           yscrollcommand=self.treescrolly3.set)
        self.treescrollx3.pack(side="bottom", fill="x")
        self.treescrolly3.pack(side="right", fill="y")

        # show data in treeview
        self.frame_treeview_data("Warehouse",self.tv3)

        #entry_searchBar
        self.entry_image_searchBar = PhotoImage(
            file=relative_to_assets("searchBar.png"))
        self.entry_bg_searchBar = self.canvas.create_image(
            359.0,
            195.0,
            image=self.entry_image_searchBar
        )
        self.entry_searchBar = Entry(
            bd=0,
            bg="#C4C4C4",
            font=("Helvetica", 12),
            highlightthickness=0
        )
        self.entry_searchBar.place(
            x=130.0,
            y=164.0,
            width=608.0,
            height=60.0
        )

        #button
        ##button_insert
        self.button_image_insert = PhotoImage(
            file=relative_to_assets("button_insert.png"))
        self.button_insert = Button(
            image=self.button_image_insert,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: InsertMaterial(),
            relief="flat"
        )
        self.button_insert.place(
            x=1134.0,
            y=164.0,
            width=61.0,
            height=62.0
        )

        ##button_save
        self.button_image_save = PhotoImage(
            file=relative_to_assets("button_save.png"))
        self.button_save = Button(
            image=self.button_image_save,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.button_save.place(
            x=1043.0,
            y=164.0,
            width=61.0,
            height=62.0
        )

        ##button_delete
        self.button_image_delete = PhotoImage(
            file=relative_to_assets("button_delete.png"))
        self.button_delete = Button(
            image=self.button_image_delete,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_delete.place(
            x=952.0,
            y=164.0,
            width=61.0,
            height=62.0
        )

        ##button_edit
        self.button_image_edit = PhotoImage(
            file=relative_to_assets("button_edit.png"))
        self.button_edit = Button(
            image=self.button_image_edit,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self.button_edit.place(
            x=861.0,
            y=164.0,
            width=61.0,
            height=62.0
        )

        ##button_search
        self.button_image_search = PhotoImage(
            file=relative_to_assets("button_search.png"))
        self.button_search = Button(
            image=self.button_image_search,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_material,
            relief="flat"
        )
        self.button_search.place(
            x=663.0,
            y=164.0,
            width=90.0,
            height=62.0
        )


    def frame_staffs(self):
        # entry_searchBar
        self.staff_entry_image_searchBar = PhotoImage(
            file=relative_to_assets("searchBar.png"))
        self.staff_entry_bg_searchBar = self.canvas.create_image(
            359.0,
            195.0,
            image=self.staff_entry_image_searchBar
        )
        self.staff_entry_searchBar = Entry(
            bd=0,
            bg="#C4C4C4",
            font=("Helvetica", 12),
            highlightthickness=0
        )
        self.staff_entry_searchBar.place(
            x=130.0,
            y=164.0,
            width=608.0,
            height=60.0
        )

        # button
        ##button_insert
        self.staff_button_image_insert = PhotoImage(
            file=relative_to_assets("button_insert.png"))
        self.staff_button_insert = Button(
            image=self.staff_button_image_insert,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("staff"),
            relief="flat"
        )
        self.staff_button_insert.place(
            x=1134.0,
            y=164.0,
            width=61.0,
            height=62.0
        )

        ##button_save
        self.staff_button_image_save = PhotoImage(
            file=relative_to_assets("button_save.png"))
        self.staff_button_save = Button(
            image=self.staff_button_image_save,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.staff_button_save.place(
            x=1043.0,
            y=164.0,
            width=61.0,
            height=62.0
        )

        ##button_delete
        self.staff_button_image_delete = PhotoImage(
            file=relative_to_assets("button_delete.png"))
        self.staff_button_delete = Button(
            image=self.staff_button_image_delete,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.staff_button_delete.place(
            x=952.0,
            y=164.0,
            width=61.0,
            height=62.0
        )

        ##button_edit
        self.staff_button_image_edit = PhotoImage(
            file=relative_to_assets("button_edit.png"))
        self.staff_button_edit = Button(
            image=self.staff_button_image_edit,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self.staff_button_edit.place(
            x=861.0,
            y=164.0,
            width=61.0,
            height=62.0
        )

        ##button_search
        self.staff_button_image_search = PhotoImage(
            file=relative_to_assets("button_search.png"))
        self.staff_button_search = Button(
            image=self.staff_button_image_search,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self.staff_button_search.place(
            x=663.0,
            y=164.0,
            width=90.0,
            height=62.0
        )

        # staff_showData
        self.staff_frame_showData = LabelFrame(
            self.window,
            background="white",
        )
        self.staff_frame_showData.place(
            x=55,
            y=246,
            width=1140,
            height=472
        )

        ## Treeview Widget
        self.tv4 = ttk.Treeview(self.staff_frame_showData)
        self.tv4.place(relheight=1,
                       relwidth=1)

        self.treescrolly4 = Scrollbar(
            self.staff_frame_showData, orient="vertical",
            command=self.tv4.yview)
        self.treescrollx4 = Scrollbar(
            self.staff_frame_showData, orient="horizontal",
            command=self.tv4.xview)
        self.tv4.configure(xscrollcommand=self.treescrollx4.set,
                           yscrollcommand=self.treescrolly4.set)
        self.treescrollx4.pack(side="bottom", fill="x")
        self.treescrolly4.pack(side="right", fill="y")

        # show data in treeview
        self.frame_treeview_data("StaffList", self.tv4)

    def frame_cashBook(self):
        pass

    def frame_customers(self):
        pass

    # def frame_report(self):
    #     pass


    def clean_data(self,treeview):
        treeview.delete(*treeview.get_children())

    def clean_window(self):
        if self.status == "Overview":
            self.canvas.delete(self.image_pieChart)
            self.frame_showData.destroy()
            self.frame_statistical_data.destroy()
            self.button_8.destroy()
            self.button_9.destroy()
            self.button_10.destroy()
            self.button_11.destroy()
            self.button_12.destroy()

        if self.status == "Warehouse":
            self.canvas.delete(self.entry_bg_searchBar)

            self.entry_searchBar.destroy()

            self.warehouse_frame_showData.destroy()

            self.button_insert.destroy()
            self.button_save.destroy()
            self.button_edit.destroy()
            self.button_delete.destroy()
            self.button_search.destroy()

        if self.status == "Staffs":
            self.canvas.delete(self.staff_entry_bg_searchBar)

            self.staff_entry_searchBar.destroy()

            self.staff_frame_showData.destroy()

            self.staff_button_insert.destroy()
            self.staff_button_save.destroy()
            self.staff_button_edit.destroy()
            self.staff_button_delete.destroy()
            self.staff_button_search.destroy()


    #change color navbar button
    def change_color_button_overview(self):
        # Change color of navbar
        ## Report button
        self.clean_window()
        self.button_report.destroy()
        self.button_report_image = PhotoImage(
            file=relative_to_assets("button_report.png"))
        self.button_report = Button(
            image=self.button_report_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonReport,
            relief="flat"
        )
        self.button_report.place(
            x=883.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        ## button_staffs
        self.button_staffs.destroy()
        self.button_staffs_image = PhotoImage(
            file=relative_to_assets("button_staffs.png"))
        self.button_staffs = Button(
            image=self.button_staffs_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonStaffs,
            relief="flat"
        )
        self.button_staffs.place(
            x=387.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        ##button_cashBook
        self.button_cashBook.destroy()
        self.button_cashBook_image = PhotoImage(
            file=relative_to_assets("button_cashBook.png"))
        self.button_cashBook = Button(
            image=self.button_cashBook_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCashBook,
            relief="flat"
        )
        self.button_cashBook.place(
            x=552.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        ##button_customers
        self.button_customers.destroy()
        self.button_customers_image = PhotoImage(
            file=relative_to_assets("button_customers.png"))
        self.button_customers = Button(
            image=self.button_customers_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCustomers,
            relief="flat"
        )
        self.button_customers.place(
            x=718.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        ##button_warehouse
        self.button_warehouse.destroy()
        self.button_warehouse_image = PhotoImage(
            file=relative_to_assets("button_warehouse.png"))
        self.button_warehouse = Button(
            image=self.button_warehouse_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonWarehouse,
            relief="flat"
        )
        self.button_warehouse.place(
            x=221.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        ## button_overview
        self.button_overview.destroy()
        self.button_overview_image = PhotoImage(
            file=relative_to_assets("button_overview_show.png"))
        self.button_overview = Button(
            image=self.button_overview_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonOverview,
            relief="flat"
        )
        self.button_overview.place(
            x=55.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

    def change_color_button_warehouse(self):
        self.clean_window()
        # Report button
        self.button_report.destroy()
        self.button_report_image = PhotoImage(
            file=relative_to_assets("button_report.png"))
        self.button_report = Button(
            image=self.button_report_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonReport,
            relief="flat"
        )
        self.button_report.place(
            x=883.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_overview
        self.button_overview.destroy()
        self.button_overview_image = PhotoImage(
            file=relative_to_assets("button_overview.png"))
        self.button_overview = Button(
            image=self.button_overview_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonOverview,
            relief="flat"
        )
        self.button_overview.place(
            x=55.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_staffs
        self.button_staffs.destroy()
        self.button_staffs_image = PhotoImage(
            file=relative_to_assets("button_staffs.png"))
        self.button_staffs = Button(
            image=self.button_staffs_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonStaffs,
            relief="flat"
        )
        self.button_staffs.place(
            x=387.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        # button_cashBook
        self.button_cashBook.destroy()
        self.button_cashBook_image = PhotoImage(
            file=relative_to_assets("button_cashBook.png"))
        self.button_cashBook = Button(
            image=self.button_cashBook_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCashBook,
            relief="flat"
        )
        self.button_cashBook.place(
            x=552.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_customers
        self.button_customers.destroy()
        self.button_customers_image = PhotoImage(
            file=relative_to_assets("button_customers.png"))
        self.button_customers = Button(
            image=self.button_customers_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCustomers,
            relief="flat"
        )
        self.button_customers.place(
            x=718.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        # button_warehouse
        self.button_warehouse.destroy()
        self.button_warehouse_image = PhotoImage(
            file=relative_to_assets("button_warehouse_show.png"))
        self.button_warehouse = Button(
            image=self.button_warehouse_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonWarehouse,
            relief="flat"
        )
        self.button_warehouse.place(
            x=221.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

    def change_color_button_staff(self):

        self.clean_window()

        # Change color of navbar
        # Report button
        self.button_report.destroy()
        self.button_report_image = PhotoImage(
            file=relative_to_assets("button_report.png"))
        self.button_report = Button(
            image=self.button_report_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonReport,
            relief="flat"
        )
        self.button_report.place(
            x=883.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_cashBook
        self.button_cashBook.destroy()
        self.button_cashBook_image = PhotoImage(
            file=relative_to_assets("button_cashBook.png"))
        self.button_cashBook = Button(
            image=self.button_cashBook_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCashBook,
            relief="flat"
        )
        self.button_cashBook.place(
            x=552.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_customers
        self.button_customers.destroy()
        self.button_customers_image = PhotoImage(
            file=relative_to_assets("button_customers.png"))
        self.button_customers = Button(
            image=self.button_customers_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCustomers,
            relief="flat"
        )
        self.button_customers.place(
            x=718.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        # button_warehouse
        self.button_warehouse.destroy()
        self.button_warehouse_image = PhotoImage(
            file=relative_to_assets("button_warehouse.png"))
        self.button_warehouse = Button(
            image=self.button_warehouse_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonWarehouse,
            relief="flat"
        )
        self.button_warehouse.place(
            x=221.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_overview
        self.button_overview.destroy()
        self.button_overview_image = PhotoImage(
            file=relative_to_assets("button_overview.png"))
        self.button_overview = Button(
            image=self.button_overview_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonOverview,
            relief="flat"
        )
        self.button_overview.place(
            x=55.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_staffs
        self.button_staffs.destroy()
        self.button_staffs_image = PhotoImage(
            file=relative_to_assets("button_staffs_show.png"))
        self.button_staffs = Button(
            image=self.button_staffs_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonStaffs,
            relief="flat"
        )
        self.button_staffs.place(
            x=387.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

    def change_color_button_cashbook(self):

        self.clean_window()

        # Change color of navbar
        # Report button
        self.button_report.destroy()
        self.button_report_image = PhotoImage(
            file=relative_to_assets("button_report.png"))
        self.button_report = Button(
            image=self.button_report_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonReport,
            relief="flat"
        )
        self.button_report.place(
            x=883.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_staffs
        self.button_staffs.destroy()
        self.button_staffs_image = PhotoImage(
            file=relative_to_assets("button_staffs.png"))
        self.button_staffs = Button(
            image=self.button_staffs_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonStaffs,
            relief="flat"
        )
        self.button_staffs.place(
            x=387.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        # button_customers
        self.button_customers.destroy()
        self.button_customers_image = PhotoImage(
            file=relative_to_assets("button_customers.png"))
        self.button_customers = Button(
            image=self.button_customers_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCustomers,
            relief="flat"
        )
        self.button_customers.place(
            x=718.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        # button_warehouse
        self.button_warehouse.destroy()
        self.button_warehouse_image = PhotoImage(
            file=relative_to_assets("button_warehouse.png"))
        self.button_warehouse = Button(
            image=self.button_warehouse_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonWarehouse,
            relief="flat"
        )
        self.button_warehouse.place(
            x=221.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_overview
        self.button_overview.destroy()
        self.button_overview_image = PhotoImage(
            file=relative_to_assets("button_overview.png"))
        self.button_overview = Button(
            image=self.button_overview_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonOverview,
            relief="flat"
        )
        self.button_overview.place(
            x=55.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_cashBook
        self.button_cashBook.destroy()
        self.button_cashBook_image = PhotoImage(
            file=relative_to_assets("button_cashBook_show.png"))
        self.button_cashBook = Button(
            image=self.button_cashBook_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCashBook,
            relief="flat"
        )
        self.button_cashBook.place(
            x=552.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

    def change_color_button_customers(self):
        self.clean_window()

        # Change color of navbar
        # Report button
        self.button_report.destroy()
        self.button_report_image = PhotoImage(
            file=relative_to_assets("button_report.png"))
        self.button_report = Button(
            image=self.button_report_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonReport,
            relief="flat"
        )
        self.button_report.place(
            x=883.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_staffs
        self.button_staffs.destroy()
        self.button_staffs_image = PhotoImage(
            file=relative_to_assets("button_staffs.png"))
        self.button_staffs = Button(
            image=self.button_staffs_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonStaffs,
            relief="flat"
        )
        self.button_staffs.place(
            x=387.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        # button_warehouse
        self.button_warehouse.destroy()
        self.button_warehouse_image = PhotoImage(
            file=relative_to_assets("button_warehouse.png"))
        self.button_warehouse = Button(
            image=self.button_warehouse_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonWarehouse,
            relief="flat"
        )
        self.button_warehouse.place(
            x=221.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_overview
        self.button_overview.destroy()
        self.button_overview_image = PhotoImage(
            file=relative_to_assets("button_overview.png"))
        self.button_overview = Button(
            image=self.button_overview_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonOverview,
            relief="flat"
        )
        self.button_overview.place(
            x=55.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_cashBook
        self.button_cashBook.destroy()
        self.button_cashBook_image = PhotoImage(
            file=relative_to_assets("button_cashBook.png"))
        self.button_cashBook = Button(
            image=self.button_cashBook_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCashBook,
            relief="flat"
        )
        self.button_cashBook.place(
            x=552.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_customers
        self.button_customers.destroy()
        self.button_customers_image = PhotoImage(
            file=relative_to_assets("button_customers_show.png"))
        self.button_customers = Button(
            image=self.button_customers_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCustomers,
            relief="flat"
        )
        self.button_customers.place(
            x=718.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

    def change_color_button_report(self):
        self.clean_window()
        # button_staffs
        self.button_staffs.destroy()
        self.button_staffs_image = PhotoImage(
            file=relative_to_assets("button_staffs.png"))
        self.button_staffs = Button(
            image=self.button_staffs_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonStaffs,
            relief="flat"
        )
        self.button_staffs.place(
            x=387.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        # button_warehouse
        self.button_warehouse.destroy()
        self.button_warehouse_image = PhotoImage(
            file=relative_to_assets("button_warehouse.png"))
        self.button_warehouse = Button(
            image=self.button_warehouse_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonWarehouse,
            relief="flat"
        )
        self.button_warehouse.place(
            x=221.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_overview
        self.button_overview.destroy()
        self.button_overview_image = PhotoImage(
            file=relative_to_assets("button_overview.png"))
        self.button_overview = Button(
            image=self.button_overview_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonOverview,
            relief="flat"
        )
        self.button_overview.place(
            x=55.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_cashBook
        self.button_cashBook.destroy()
        self.button_cashBook_image = PhotoImage(
            file=relative_to_assets("button_cashBook.png"))
        self.button_cashBook = Button(
            image=self.button_cashBook_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCashBook,
            relief="flat"
        )
        self.button_cashBook.place(
            x=552.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

        # button_customers
        self.button_customers.destroy()
        self.button_customers_image = PhotoImage(
            file=relative_to_assets("button_customers.png"))
        self.button_customers = Button(
            image=self.button_customers_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonCustomers,
            relief="flat"
        )
        self.button_customers.place(
            x=718.0,
            y=0.0,
            width=145.0,
            height=65.0
        )

        # Report button
        self.button_report.destroy()
        self.button_report_image = PhotoImage(
            file=relative_to_assets("button_report_show.png"))
        self.button_report = Button(
            image=self.button_report_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.buttonReport,
            relief="flat"
        )
        self.button_report.place(
            x=883.0,
            y=0.0,
            width=146.0,
            height=65.0
        )

    #file
    def frame_treeview_data(self, sheet_name,treeview):
        self.clean_data(treeview)
        self.df = pd.read_excel("Database.xlsx", sheet_name=sheet_name)
        treeview["column"] = list(self.df.columns)
        treeview["show"] = "headings"
        for column in treeview["columns"]:
            treeview.heading(column, text=column)

        self.df_rows = self.df.to_numpy().tolist()
        for row in self.df_rows:
            treeview.insert("", "end", values=row)


    #run_button
    def buttonOverview(self):
        self.change_color_button_overview()
        #frame_overview
        self.frame_overview()

        self.status = "Overview"

    def buttonWarehouse(self):
        self.change_color_button_warehouse()
        self.frame_warehouse()

        self.status = "Warehouse"

    def buttonStaffs(self):
        self.change_color_button_staff()
        self.frame_staffs()
        self.status = "Staffs"

    def buttonCashBook(self):

        self.change_color_button_cashbook()
        self.status = "Cashbook"

    def buttonCustomers(self):

        self.change_color_button_customers()
        self.status = "Customers"

    def buttonReport(self):

        self.change_color_button_report()
        self.status = "Report"


    def buttonLogout(self):
        self.canvas.destroy()
        GUI_Login(self.window)

class InsertMaterial():
    def __init__(self):
        self.window_insert = Toplevel()
        self.window_insert.title("Insert Material in Warehouse")
        self.window_insert.geometry("502x461")
        self.window_insert.configure(bg="#FFFFFF")

        self.canvas_insert = Canvas(
            self.window_insert,
            bg="#FFFFFF",
            height=461,
            width=502,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas_insert.place(x=0, y=0)

        #button insert
        self.button_image_insertMaterial = PhotoImage(
            file=relative_to_assets("button_insertData.png"))
        self.button_insertMaterial = Button(
            self.window_insert,
            image=self.button_image_insertMaterial,
            borderwidth=0,
            highlightthickness=0,
            command=self.closeInsertWindow,
            relief="flat"
        )
        self.button_insertMaterial.place(
            x=203.99999999999997,
            y=381.0,
            width=94.0,
            height=40.0
        )

        #entry
        self.entry_image_shortData = PhotoImage(
            file=relative_to_assets("entry_insertShortData.png"))


        self.entry_bg_insertType = self.canvas_insert.create_image(
            362.5,
            80.0,
            image=self.entry_image_shortData
        )
        self.entry_insertType = Entry(
            self.window_insert,
            bd=0,
            bg="#DFDFDF",
            font=("Helvetica", 12),
            highlightthickness=0
        )
        self.entry_insertType.place(
            x=308.0,
            y=59.99999999999999,
            width=109.0,
            height=38.0
        )

        self.entry_bg_id = self.canvas_insert.create_image(
            362.5,
            140.0,
            image=self.entry_image_shortData
        )
        self.entry_insertId = Entry(
            self.window_insert,
            bd=0,
            bg="#DFDFDF",
            font=("Helvetica", 12),
            highlightthickness=0
        )
        self.entry_insertId.place(
            x=308.0,
            y=120.0,
            width=109.0,
            height=38.0
        )

        self.entry_image_insertLongData = PhotoImage(
            file=relative_to_assets("entry_insertLongData.png"))

        self.entry_bg_insertName = self.canvas_insert.create_image(
            325.5,
            200.5,
            image=self.entry_image_insertLongData
        )
        self.entry_bg_insertName = Entry(
            self.window_insert,
            bd=0,
            bg="#DFDFDF",
            font=("Helvetica", 12),
            highlightthickness=0
        )
        self.entry_bg_insertName.place(
            x=233.99999999999997,
            y=180.0,
            width=183.0,
            height=39.0
        )

        self.entry_bg_quantity = self.canvas_insert.create_image(
            362.5,
            261.0,
            image=self.entry_image_shortData
        )
        self.entry_insertQuantity = Entry(
            self.window_insert,
            bd=0,
            bg="#DFDFDF",
            font=("Helvetica", 12),
            highlightthickness=0
        )
        self.entry_insertQuantity.place(
            x=308.0,
            y=241.0,
            width=109.0,
            height=38.0
        )

        self.entry_bg_unit = self.canvas_insert.create_image(
            362.5,
            321.0,
            image=self.entry_image_shortData
        )
        self.entry_insertUnit = Entry(
            self.window_insert,
            bd=0,
            bg="#DFDFDF",
            font=("Helvetica", 12),
            highlightthickness=0
        )
        self.entry_insertUnit.place(
            x=308.0,
            y=301.0,
            width=109.0,
            height=38.0
        )

        self.image_image_type = PhotoImage(
            file=relative_to_assets("image_type.png"))
        self.image_1 = self.canvas_insert.create_image(
            94.99999999999997,
            80.0,
            image=self.image_image_type
        )

        self.image_image_id = PhotoImage(
            file=relative_to_assets("image_id.png"))
        self.image_2 = self.canvas_insert.create_image(
            83.99999999999997,
            141.0,
            image=self.image_image_id
        )

        self.image_image_name = PhotoImage(
            file=relative_to_assets("image_name.png"))
        self.image_3 = self.canvas_insert.create_image(
            94.99999999999997,
            201.0,
            image=self.image_image_name
        )

        self.image_image_quantity = PhotoImage(
            file=relative_to_assets("image_quantity.png"))
        self.image_4 = self.canvas_insert.create_image(
            105.99999999999997,
            262.0,
            image=self.image_image_quantity
        )

        self.image_image_unit = PhotoImage(
            file=relative_to_assets("image_unit.png"))
        self.image_5 = self.canvas_insert.create_image(
            91.99999999999997,
            323.0,
            image=self.image_image_unit
        )
        self.window_insert.resizable(False, False)
        self.window_insert.mainloop()

    def closeInsertWindow(self):
        print(self.entry_insertType.get())
        print(self.entry_insertId.get())
        print(self.entry_bg_insertName.get())
        print(self.entry_insertQuantity.get())
        print(self.entry_insertUnit.get())
        # self.canvas_insert.destroy()
        # self.window_insert.destroy()

class DeleteMaterial():
    pass

class EditMaterial():
    pass

class Save():
    pass