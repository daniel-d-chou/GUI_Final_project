import Next_Page_class
import GUI_Class_file

proj = Next_Page_class.Our_project()
proj2 = GUI_Class_file.MyGui2()
root = proj.root_lvl1_(800, 600)
root.geometry("600x900+1200+50")
x = 0
num = 0
# ______________________________FUNCTIONS____________________________________
def station_selected_and_fare(event):
    global num
    x = 0
    for i in options:
        x+=1
        if i == station_option.get():
            num = abs(x-5) * 13
            to_station.configure(text=f"To: {station_option.get()}")
    fare.configure(state= 'normal')
    fare.delete(0, 'end')
    fare.insert(0, "$ %.2f" % num)
    fare.configure(state= 'readonly')
    total_amount_indicator.configure(text=f"$ {num * int(no_of_tix.get())}")


def update_amount():
    total_amount_indicator.configure(text= f"$ {num * int(no_of_tix.get())}")


def update_change(another_event):
    print(currency_entry.get())
    change_indicator.configure(text= "$ %.2f" % (float(currency_entry.get()) - float(num * int(no_of_tix.get()))))
    if float(currency_entry.get()) - float(num * int(no_of_tix.get())) < 0:
        message_status.configure(text= "* Insufficient balance", fg= 'red')
    else:
        message_status.configure(text= "* The required balance is met", fg= 'green')


def clear():
    station_option.current(4)
    fare.configure(state= 'normal')
    fare.delete(0, 'end')
    fare.insert(0, "%.2f" % 0.00)
    fare.configure(state= 'readonly')
    no_of_tix.delete(0, 'end')
    no_of_tix.insert(0, 1)
    total_amount_indicator.configure(text= "$ 0")
    currency_entry.delete(0, 'end')
    change_indicator.configure(text= "$ %.2f" % 0.00)
    message_status.configure(text= '*')
    station_selected_and_fare(1)


def return_():
    station_option.current(4)
    fare.configure(state= 'normal')
    fare.delete(0, 'end')
    fare.insert(0, "%.2f" % 0.00)
    fare.configure(state= 'readonly')
    no_of_tix.delete(0, 'end')
    no_of_tix.insert(0, 1)
    total_amount_indicator.configure(text= "$ 0")
    currency_entry.delete(0, 'end')
    change_indicator.configure(text= "$ %.2f" % 0.00)
    message_status.configure(text= '*')
    station_selected_and_fare(1)
    proj.other_page(home_page_frame)


def confirm():
    if currency_entry.get() == '' or float(currency_entry.get()) - float(num * int(no_of_tix.get())) < 0:
        message_status.configure(text="* Insufficient balance, cannot proceed", fg='red')
    else:
        proj2.create_messagebox("Update", "Ticket Purchased Successfully")
        message_status.configure(text="*")
        clear()
        proj.other_page(home_page_frame)
# ______________________________FUNCTIONS____________________________________


# ____________________________________________________FRAMES___________________________________________________________
# _______________LVL 1:_____________________
main_frame = proj2.create_labelframe(root, '', None, 0, 0, 20, 0, 20, 0, 'w')
# _______________LVL 1:_____________________

# _______________LVL 2: _____________________
home_page_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')
home_page_frame.configure(width= 400, height= 200)

buy_ticket_onetime_frame = proj.frame_lvl_(main_frame, None, 0, 0, 'news')
buy_ticket_onetime_frame.configure(width= 400, height= 200)

buy_ticket_as_user_frame = proj.frame_lvl_(main_frame, 'yellow', 0, 0, 'news')
buy_ticket_as_user_frame.configure()

create_account_frame = proj.frame_lvl_(main_frame, 'yellow', 0, 0, 'news')
buy_ticket_as_user_frame.configure()
# _______________LVL 2:_____________________

# _______________________________________LVL 3:_______________________________________________________
# ______________LVL 3: home_page_frame ________________
frame_holder = proj2.create_frame(home_page_frame, None, 0, 0,
                                  100, 0, 15, 15, 'news')
frame_holder.pack()
# ______________LVL 3: home_page_frame ________________

# _______________________________________LVL 3:_______________________________________________________


# _______________________________________LVL 4:_______________________________________________________
# _______________LVL 4: Homepage frames_____________________
purchase_ticket_frame = proj2.create_labelframe(frame_holder, 'Purchase Ticket', None,
                                                0, 0, 0, 0, 10, 10, 'w')
create_user_frame = proj2.create_labelframe(frame_holder, 'Create Account', None,
                                                1, 0, 0, 0, 10, 10, 'w')
# _______________LVL 4: Homepage frames_____________________

# _______________LVL 4: Buy ticket onetime frames_____________________
one_time_ticket_purchase = proj2.create_labelframe(buy_ticket_onetime_frame, ' One-time Ticket Purchase', None,
                                                0, 0, 30, 30, 30, 30, 'w')
one_time_ticket_purchase.configure(font= ('Times New Roman', 25, 'bold'))
# _______________LVL 4: Buy ticket onetime frames_____________________
# _______________________________________LVL 4:_______________________________________________________

# _______________LVL 5: One-time Ticket Purchase frames_____________________
mini_frames = []
for i in range(9):
    frame = proj2.create_frame(one_time_ticket_purchase, None,
                               x, 0, 15, 15, 10, 10, 'n')
    x += 1
    mini_frames.append(frame)
    if len(mini_frames) == 9:
        x = 0
        # _______________LVL 6: mini_frame[2] frames_____________________
        frame = proj2.create_frame(mini_frames[2], None,
                                   1, 0, 0, 0, 0, 0, 'w')
        # _______________LVL 6: mini_frame[2] frames_____________________
        mini_frames.append(frame)
# _______________LVL 5: One-time Ticket Purchase frames_____________________

# ____________________________________________________FRAMES___________________________________________________________



# ____________________________________________________FRAMES___________________________________________________________

# ___________________________________LVL 2:_________________________________________________
# _______________________LVL 2: Homepage content________________________________
purchase_button1 = proj.button(purchase_ticket_frame, 'Purchase Ticket (One Time)', 25, 1,
                               0, 0, 10, 10, 20, 0)
purchase_button1.configure(command= lambda :proj.other_page(buy_ticket_onetime_frame))
purchase_button2 = proj.button(purchase_ticket_frame, 'Purchase Ticket (As a user)', 25, 1,
                               1, 0, 10, 10, 20, 20)
buy_ticket_button = proj.button(create_user_frame, 'Create an Account', 25, 1,
                                1, 0, 10, 10, 20, 20)

# _______________________LVL 2: Homepage content________________________________


# ___________________LVL 2: Buy ticket one time content_________________________
# ___________LVL 5: One-time Ticket Purchase contents___________
options = ["Station -4","Station -3",
           "Station -2","Station -1",
           "Station 0","Station 1",
           "Station 2", "Station 3",
           "Station 4"]
current_station_label = proj2.create_label(mini_frames[0], "You're in: Station 0",
                                           0, 0, 1, 0, 0, 0, 0,'w')
current_station_label.configure(font= ('Times New Roman', 15))
station_option = proj2.create_combobox_with_label(mini_frames[1], 'Your Destination: ', 'Times New Roman',
                                                  15, '', options, None, 15,0, 0, 1, 0,
                                                  10, 10, 0, 0, 'n')
station_option.configure(font=('Times New Roman', 15))
station_option.current(4)
station_option.bind("<<ComboboxSelected>>", station_selected_and_fare)

journey = proj2.create_label(mini_frames[2], "Journey: ",
                                           0, 0, 1, 0, 0, 0, 0,'news')
journey.configure(font= ('Times New Roman', 15))
from_station = proj2.create_label(mini_frames[9], "From: Station 0",
                                           0, 0, 1, 0, 0, 0, 0,'news')
from_station.configure(font= ('Times New Roman', 12))
to_station = proj2.create_label(mini_frames[9], "To: Station 0",
                                           1, 0, 1, 0, 0, 0, 0,'news')
to_station.configure(font= ('Times New Roman', 12))

fare = proj2.create_entry_with_label(mini_frames[3], 'Fare: ', 'Times New Roman', 15, '', None, 10,
                                           0, 0, 1, 0, 20, 20, 0, 0, 'n')
fare.insert(0, "$ 0")
fare.configure(font= ('Times New Roman', 15), state= 'readonly')

no_of_tix = proj2.create_spinbox_with_label(mini_frames[4], 'Number of Tickets: ', 'Times New Roman', 15, '', None, 1, 10, 10,
                                           0, 0, 1, 0, 0, 0, 0, 0, 'n')
no_of_tix.configure(font=('Times New Roman', 15), command= update_amount)
total_amount_label = proj2.create_label(mini_frames[5], "Total Amount: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
total_amount_label.configure(font=('Times New Roman', 15))
total_amount_indicator = proj2.create_label(mini_frames[5], "$ 0",
                                           0, 1, 1, 0, 0, 0, 0,'w')
total_amount_indicator.configure(font=('Times New Roman', 15))
currency_entry = proj2.create_entry_with_label(mini_frames[6], "Enter Currency Amount: ", 'Times New Roman', 15, '', None, 10,
                                           0, 0, 1, 0, 0, 0, 0, 0, 'n')
currency_entry.configure(font=('Times New Roman', 15))
currency_entry.bind('<KeyRelease>', update_change)
change_label = proj2.create_label(mini_frames[7], "Change: ",
                                           0, 0, 1, 0, 0, 0, 0,'w')
change_label.configure(font=('Times New Roman', 15))
change_indicator = proj2.create_label(mini_frames[7], "$ 0",
                                           0, 1, 1, 0, 0, 0, 0,'w')
message_status = proj2.create_label(mini_frames[7], '*', 1, 0, 2, 0, 0, 0, 0, 'w')
change_indicator.configure(font=('Times New Roman', 15))

return_button = proj.button(mini_frames[8], 'Return', 15, 1,
                            0, 0, 0, 0, 0, 0)
return_button.configure(command= return_)
clear_button = proj.button(mini_frames[8], 'Clear', 15, 1,
                            0, 1, 10, 10, 0, 0)
clear_button.configure(command= clear)
confirm_button = proj.button(mini_frames[8], 'Confirm', 15, 1,
                            0, 2, 0, 0, 0, 0)
confirm_button.configure(command=confirm)
# ___________LVL 5: One-time Ticket Purchase contents___________
# ___________________LVL 2: Buy ticket one time content_________________________
# ___________________________________LVL 2:_________________________________________________

# ______________________________CONTENT_______________________________________
home_page_frame.tkraise()
root.mainloop()
