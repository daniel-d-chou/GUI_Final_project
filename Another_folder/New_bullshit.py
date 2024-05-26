import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from PIL import ImageTk, Image


class MyGui2:
    def __init__(self):
        self.frame = ''
        self.labelframe = ''
        self.label = ''
        self.button = ''
        self.image = ''
        self.entry = ''
        self.combo_box = ''
        self.date_entry = ''


    def create_label(self,container, label_name, font, size, style, bg, i, j, padl, padr, padt, padb, stick_side):
        self.label = (tk.Label(container, text= label_name, font= (font, size, style), bg= bg)
                      .grid(row= i, column= j, padx= (padl, padr), pady= (padt, padb), sticky= stick_side))

    def create_frame(self, container, bg, w, h, i, j, padleft, padright, padtop, padbot, stick_side):
        self.frame = tk.Frame(container, bg=bg, width=w, height=h)
        self.frame.grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)

    def create_entry_with_label(self, container, label_name, bg, w, i, j, padleft, padright, padtop, padbot,
                                stick_side):
        self.label = (tk.Label(container, text=label_name, bg=bg)
                      .grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side))
        self.entry = tk.Entry(container, width=w)
        self.entry.grid(row=i + 1, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return self.entry

    def create_combobox_with_label(self, container, label_name, values, bg, w, i, j, padleft, padright, padtop, padbot,stick_side):
        self.label = (tk.Label(container, text=label_name, bg=bg)
                      .grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side))
        self.combo_box = ttk.Combobox(container, values=values, width=w)
        self.combo_box.grid(row=i + 1, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return self.combo_box

    def create_dateentry_with_label(self, container, label_name, bg, w, i, j, padleft, padright, padtop, padbot,stick_side):
        self.label = (tk.Label(container, text=label_name, bg=bg)
                      .grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side))
        self.date_entry = DateEntry(container, width= w, bg= bg)
        self.date_entry.grid(row=i+1, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return self.date_entry

    def create_button(self, container, button_text, w, h, bg, fg, i, j, padleft, padright, padtop, padbot,stick_side):
        self.button = tk.Button(container, text= button_text, width= w, height= h, bg = bg, fg= fg)
        self.button.grid(row= i, column= j, padx= (padleft, padright), pady= (padtop, padbot), sticky= stick_side)
        return self.button

    def create_image(self, container, path, lenght, width, i, j, k, stick_side):
        self.image = Image.open(path)
        self.image_picked = ImageTk.PhotoImage(self.image.resize((lenght, width)))
        self.image_label = tk.Label(container, image= self.image_picked).grid(row= i, column= j, columnspan= k, sticky= stick_side)

    @staticmethod
    def root_lvl1_():
        root = tk.Tk()
        """root.state('zoomed')"""
        root.geometry("1000x1200")
        root.state('zoomed')
        return root

    @staticmethod
    def canvas_lvl2_(root):
        #   Creating Main_Frame
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand= 1)

        #   Creating a Canvas inside the Main_Frame
        canvas = Canvas(main_frame, bg="GRAY")
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

    @staticmethod
    def frame_lvl_(container_lvl, i, j, padl, padr, padt, padb, stick_side, p, bg):
        frame = tk.Frame(container_lvl, bg= bg, width= 50, height= 50)
        frame.grid(row= i, column= j, padx= (padl, padr), pady= (padt, padb), sticky= stick_side)
        return frame

    @staticmethod
    def label_frame_lvl_(container_lvl, label_name, font, size, style, bg, i, j, padleft, padright, padtop, padbot,stick_side):
        frame = tk.LabelFrame(container_lvl, text= label_name, font= (font, size, style), bg=bg, width=50, height=50)
        frame.grid(row=i, column=j, padx=(padleft, padright), pady=(padtop, padbot), sticky=stick_side)
        return frame
