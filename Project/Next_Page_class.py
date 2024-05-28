import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from PIL import ImageTk, Image


class Our_project:
    @staticmethod
    def root_lvl1_(width, height):
        root = tk.Tk()
        """root.state('zoomed')"""
        root.geometry(f"{width}x{height}")
        return root

    @staticmethod
    def canvas_lvl2_(root):
        #   Creating Main_Frame
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand=1)

        #   Creating a Canvas inside the Main_Frame
        canvas = Canvas(main_frame, bg="white")
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        #   Adding a Scrollbar to the Canvas
        v_scroll = Scrollbar(canvas, command=canvas.yview)
        v_scroll.pack(side=RIGHT, fill=Y)

        #   Configuring Canvas Commands
        canvas.configure(yscrollcommand=v_scroll.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        #   Creating Secondary Frame inside Canvas
        sub_frame = Frame(canvas, bg="light grey")

        #   Creating a Window inside Canvas, which contains the Secondary Frame
        canvas.create_window((0, 0), window=sub_frame, anchor='nw')

        return sub_frame

    @staticmethod
    def frame_lvl_(container_lvl, bg, i, j, sticky):
        frame = tk.Frame(container_lvl, bg=bg)
        frame.grid(row=i, column=j, sticky= sticky)
        return frame

    @staticmethod
    def label(container, label_name, i, j):
        label = tk.Label(container, text=label_name)
        label.grid(row=i, column=j)
        return label
    
    @staticmethod
    def entry(container, i, j, pad_right, pad_left, pad_top, pad_bot, sticky):
        entry = tk.Entry(container, width= 15)
        entry.grid(row= i, column= j, padx= (pad_right, pad_left), pady= (pad_top, pad_bot), sticky= sticky)
        return entry

    @staticmethod
    def label_frame_lvl_(container_lvl, label_name, i, j, w, h, sticky):
        frame = tk.LabelFrame(container_lvl, text=label_name, width=w, height=h)
        frame.grid(row=i, column=j, sticky= sticky)
        return frame

    @staticmethod
    def label_and_entry(container, label_name, font, size, style, bg, fg, w,
                        i, j, i_add, j_add, i_span, j_span, pad_left, pad_right, pad_top, pad_bot, sticky_side):
        label = tk.Label(container, text=label_name, font=(font, size, style), bg=bg, fg=fg)
        label.grid(row=i, column=j, rowspan=i_span, columnspan=j_span, padx=(pad_left, pad_right),
                   pady=(pad_top, pad_bot), sticky=sticky_side)
        entry = tk.Entry(container, width=w)
        entry.grid(row=i + i_add, column=j + j_add, rowspan=i_span, columnspan=j_span, padx=(pad_left, pad_right),
                   pady=(pad_top, pad_bot), sticky=sticky_side)
        return entry

    @staticmethod
    def date_and_label(container, label_name, font, size, style, bg, fg, w,
                       i, j, i_add, j_add, i_span, j_span, pad_left, pad_right, pad_top, pad_bot, sticky_side):
        label = tk.Label(container, text=label_name, font=(font, size, style), bg=bg, fg=fg)
        label.grid(row=i, column=j, rowspan=i_span, columnspan=j_span, padx=(pad_left, pad_right),
                   pady=(pad_top, pad_bot), sticky=sticky_side)
        date_entry = DateEntry(container, width=w, bg=bg)
        date_entry.grid(row=i + i_add, column=j + j_add, rowspan=i_span, columnspan=j_span, padx=(pad_left, pad_right),
                        pady=(pad_top, pad_bot), sticky=sticky_side)
        return date_entry

    @staticmethod
    def combo_box_and_label(container, label_name, font, size, style, bg, fg, w, values,
                            i, i_add, j, j_add, i_span, j_span, pad_left, pad_right, pad_top, pad_bot, sticky_side):
        label = tk.Label(container, text=label_name, font=(font, size, style), bg=bg, fg=fg)
        label.grid(row=i + i_add, column=j + j_add, rowspan=i_span, columnspan=j_span, padx=(pad_left, pad_right),
                   pady=(pad_top, pad_bot), sticky=sticky_side)
        combo_box = ttk.Combobox(container, width=w, values=values)
        combo_box.grid(row=i, column=j + 1, rowspan=i_span, columnspan=j_span, padx=(pad_left, pad_right),
                       pady=(pad_top, pad_bot), sticky=sticky_side)
        return combo_box

    @staticmethod
    def button(container, btn_text, w, h, i, j, pad_left, pad_right, pad_top, pad_bot, bg, fg):
        button = tk.Button(container, text=btn_text, width=w, height=h, bg=bg, fg=fg)
        button.grid(row=i, column=j, padx= (pad_left, pad_right), pady= (pad_top, pad_bot))
        return button

    @staticmethod
    def create_image(container, path, lenght, width, i, j, k, pad_left, pad_right, pad_top, pad_bot, stick_side):

        image = Image.open(path)
        image_picked = ImageTk.PhotoImage(image.resize((lenght, width)))
        image_label = tk.Label(container, image=image_picked)
        image_label.grid(row=i, column=j, columnspan=k, padx=(pad_left, pad_right), pady=(pad_top, pad_bot),
                         sticky=stick_side)
        return image_label

    @staticmethod
    def new_user(database, query):
        connection = sqlite3.connect(f"{database}")
        connection.execute(query)
        connection.commit()
        connection.close()
        return connection

    @staticmethod
    def other_page(page):
        page.tkraise()
