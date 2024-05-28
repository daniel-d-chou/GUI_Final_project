import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
from PIL import ImageTk, Image

# tibo si chanel
class MyGui2:
    def __init__(self):
        self.root = ''
        self.frame = ''
        self.labelframe = ''
        self.label = ''
        self.button = ''
        self.image = ''
        self.entry = ''
        self.combo_box = ''
        self.option_menu = ''
        self.spinbox = ''
        self.date_entry = ''
        self.connection = ''
        self.con = ''

    def deploy_root(self, width, height):
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        return self.root

    def create_frame(self, container, bg, i, j, padleft, padright, padtop, padbot, stick_side):
        self.frame = tk.Frame(container, bg=bg)
        self.frame.grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return self.frame

    def create_labelframe(self, container, text, bg, i, j, padleft, padright, padtop, padbot, stick_side):
        self.frame = tk.LabelFrame(container, text= text, bg=bg)
        self.frame.grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return self.frame


    def create_label(self,container, label_name, i, j, j_span, pad_left, pad_right, pad_top, pad_bot, stick_side):
        self.label = tk.Label(container, text= label_name)
        self.label.grid(row= i, column= j, padx= (pad_left, pad_right), pady= (pad_top, pad_bot), columnspan= j_span,
                        sticky= stick_side)
        return self.label


    def create_entry_with_label(self, container, label_name, font, size, style, bg, w, i, j, i2, j2,
                                padleft, padright, padtop, padbot, stick_side):
        self.label = tk.Label(container, text=label_name, font=(font, size, style), bg=bg)
        self.label.grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        self.entry = tk.Entry(container, width=w)
        self.entry.grid(row=i2, column=j2, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return self.entry

    def create_combobox_with_label(self, container, label_name, font, size, style, values, bg, w, i, j, i2, j2,
                                   padleft, padright, padtop, padbot,stick_side):
        self.label = tk.Label(container, text=label_name, font=(font, size, style), bg=bg)
        self.label.grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        self.combo_box = ttk.Combobox(container, values=values, width=w)
        self.combo_box.grid(row=i2, column=j2, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return self.combo_box

    def create_dateentry_with_label(self, container, label_name, bg, w, i, j, i2, j2, padleft, padright, padtop, padbot,stick_side):
        self.label = tk.Label(container, text=label_name, bg=bg)
        self.label.grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        self.date_entry = DateEntry(container, width= w, bg= bg)
        self.date_entry.grid(row=i2, column=j2, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return self.date_entry

    def create_option_menu(self, container, option_lists, i, j, padleft, padright, padtop, padbot,stick_side):
        self.option_menu = tk.OptionMenu(container, tk.StringVar(container), *option_lists)
        self.option_menu.grid(row= i, column= j, padx= (padleft, padright), pady= (padtop, padbot), sticky= stick_side)
        return self.option_menu

    def create_spinbox_with_label(self, container, label_name, font, size, style, bg, start, end, width,
                                  i, j, i2, j2, padleft, padright, padtop, padbot,stick_side):
        self.label = tk.Label(container, text=label_name, font=(font, size, style), bg=bg)
        self.label.grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        self.spinbox = tk.Spinbox(container, from_= start, to= end, width= width)
        self.spinbox.grid(row= i2, column= j2, padx= (padleft, padright), pady= (padtop, padbot), sticky= stick_side)
        return self.spinbox

    def create_button(self, container, button_text, w, h, bg, fg, i, j, padleft, padright, padtop, padbot,stick_side):
        self.button = tk.Button(container, text= button_text, width= w, height= h, bg = bg, fg= fg)
        self.button.grid(row= i, column= j, padx= (padleft, padright), pady= (padtop, padbot), sticky= stick_side)
        return self.button

    def create_messagebox(self, title, message):
        messagebox.showinfo(f"{title}", f"{message}")

    def select_path(self):
        self.filepath = filedialog.askopenfilename(initialdir= "C:\\Users\\JASMIN R. DY\\PycharmProjects\\OOP_Payroll\\images",
                                                   title= "Select Picture File",
                                                   filetypes= (("picture files", "*.jpg"),("all files", "*.*")))
        return self.filepath

    def insert_image(self, path, lenght, width):
        self.image = Image.open(path)
        self.image_picked = ImageTk.PhotoImage(self.image.resize((lenght, width)))

        return self.image_picked

    def create_table(self, database, table_title, fields):
        self.connection = sqlite3.connect(f"{database}")
        self.con = self.connection.cursor()
        create = f"CREATE TABLE IF NOT EXISTS {table_title} ({fields})"
        self.con.execute(create)
        self.connection.commit()
        self.connection.close()


    def save_data_into_database(self, database, table_name, fields, values):
        self.connection = sqlite3.connect(f"{database}")
        query = (f"INSERT INTO {table_name} ({fields}) " 
                 "VALUES " 
                 f"({values})")
        self.connection.execute(query)
        self.connection.commit()
        self.connection.close()

    def cursor_database(self, database, command):
        self.connection = sqlite3.connect(f"{database}")
        self.con = self.connection.cursor()
        self.con.execute(command)
        self.connection.commit()
        return self.con.execute(command).fetchone()

    def cursor_database2(self, database, command):
        self.connection = sqlite3.connect(f"{database}")
        self.con = self.connection.cursor()
        self.con.execute(*command)
        self.connection.commit()



    @staticmethod
    def canvas_lvl2_(root, bg):
        #   Creating Main_Frame
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand= 1)

        #   Creating a Canvas inside the Main_Frame
        canvas = Canvas(main_frame, bg=bg)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        #   Adding a Scrollbar to the Canvas
        v_scroll = Scrollbar(canvas, command=canvas.yview)
        v_scroll.pack(side=RIGHT, fill=Y)

        #   Configuring Canvas Commands
        canvas.configure(yscrollcommand=v_scroll.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        #   Creating Secondary Frame inside Canvas
        sub_frame = Frame(canvas, bg="GRAY")

        #   Creating a Window inside Canvas, which contains the Secondary Frame
        canvas.create_window((0, 0), window=sub_frame, anchor='nw')
        return sub_frame

