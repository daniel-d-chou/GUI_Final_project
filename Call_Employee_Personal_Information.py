import New_bullshit
import Next_Page_class
import GUI_Class_file

obj = New_bullshit.MyGui2()
obj2 = Next_Page_class.Our_project()
obj3 = GUI_Class_file.MyGui2()

# _________________________ Combo_box Values_________________________________________
combo_box_values = [['Jr','ll','lll','Sr.','None'],
                    ['Male', 'Female'],
                    ['Japanese','Canadian','Filipino','Norwegian','Irish'],
                    ['Single','Married','Widowed'],
                    ['None'],
                    ['Japan','Canada','Philippines','Norway','Ireland']]


# __________________________BUTTON FUNCTIONS_______________________________
def get_entry():
    path = a25.get()
    open_file = open(path, 'rb')
    data = open_file.read()
    command2 = ("""UPDATE personal_infotbl SET Employee_pic = ? WHERE Employee_no = ?""", (data, a14.get()))
    nms = ["First_name","Middle_name","Last_name","Suffix",
           "Date_of_birth","Gender","Nationality","Civil_status",
           "Department","Designation","Qualified_dept_stat",
           "Employee_stat","Paydate","Employee_no",
           "Contact_Number","Email",
           "Other_Social_Media","Social_Media_Account_ID_No",
           "Address_line_1","Address_line_2","City_Municipality","State_Province","Country","Zipcode","Picture_path"]
    ls = [ a1.get(), a2.get(), a3.get(),a4.get(),
           a5.get(), a6.get(), a7.get(),a8.get(),
           a9.get(),a10.get(),a11.get(),
          a12.get(),a13.get(),a14.get(),
          a15.get(),a16.get(),
          a17.get(),a18.get(),
          a19.get(),a20.get(),a21.get(),a22.get(),a23.get(),a24.get(),a25.get()]
    query = ("INSERT INTO personal_infotbl"
             f"({nms[0]}, {nms[1]}, {nms[2]},{nms[3]},"
             f" {nms[4]}, {nms[5]}, {nms[6]},{nms[7]},"
             f" {nms[8]}, {nms[9]}, {nms[10]},"
             f" {nms[11]},{nms[12]},{nms[13]},"
             f" {nms[14]},{nms[15]},"
             f" {nms[16]},{nms[17]},"
             f" {nms[18]},{nms[19]},{nms[20]},{nms[21]},{nms[22]},{nms[23]},{nms[24]})"
             "VALUES"
             f"('"+str(ls[0])+"','"+ str(ls[1])+"','"+ str(ls[2])+"','"+str(ls[3])+"',"
             "'"+  str(ls[4])+"','"+ str(ls[5])+"','"+ str(ls[6])+"','"+str(ls[7])+"',"
             "'"+  str(ls[8])+"','"+ str(ls[9])+"','"+ str(ls[10])+"',"
             "'"+  str(ls[11])+"','"+str(ls[12])+"','"+str(ls[13])+"',"
             "'"+  str(ls[14])+"','"+str(ls[15])+"',"
             "'"+  str(ls[16])+"','"+str(ls[17])+"',"
             "'"+  str(ls[18])+"','"+str(ls[19])+"','"+str(ls[20])+"','"+str(ls[21])+"','"+str(ls[22])+"','"+str(ls[23])+"','"+str(ls[24])+"')"
            )
    obj2.new_user("AssessmentApplicationDB", query)
    obj3.cursor_database2("AssessmentApplicationDB", command2)


def delete_entry_content():
    ls = [a1, a2, a3, a4,
          a5, a6, a7, a8,
          a9, a10, a11,
          a12, a13, a14,
          a15, a16,
          a17, a18,
          a19, a20, a21, a22, a23, a24, a25]
    for i in range(25):
        ls[i].delete(0, 'end')


def insert_picture():
    path = obj3.select_path()
    picture = obj3.insert_image(path, 150, 150)
    insert_pic.configure(image= picture)
    a25.insert(0, path)


# __________________________________________________-Frames-___________________________________________________________

# _____________________________ -LVL 1- The entire window (Start)_____________________________
root = obj.root_lvl1_()
# _____________________________ -LVL 1- The entire window (End)_______________________________


# _____________________________ -LVL 2- The canvas (Start)____________________________________
content_frame = obj.canvas_lvl2_(root)
# _____________________________ -LVL 2- The canvas (End)______________________________________


# _____________________________ -LVL 3- The Frame which holds all contents (Start)____________
lvl3_mainframe = obj.frame_lvl_(content_frame, 0, 0, 50, 0, 0, 0, 'n', 0, 'floral white')
# _____________________________ -LVL 3- The Frame which holds all contents (End)____________


# _____________________________ -LVL 4- Frames which holds parts of all contents (Start)______
lvl4_1stframe = obj.frame_lvl_(lvl3_mainframe, 0, 0, 10, 10, 10, 10, 'n', 0, 'yellow')
lvl4_2ndframe = obj.frame_lvl_(lvl3_mainframe, 1, 0, 10, 10, 0, 10, 'n', 0, 'floral white')
lvl4_3rdframe = obj.frame_lvl_(lvl3_mainframe, 2, 0, 10, 10, 0, 10, 'n', 0, 'light grey')
lvl4_4thframe = obj.label_frame_lvl_(lvl3_mainframe, "Contact Info", 'Times New Roman', 20, 'bold', 'floral white',
                                               3, 0, 10, 10, 0, 10, 'n')
lvl4_5thframe = obj.label_frame_lvl_(lvl3_mainframe, "Address", 'Times New Roman', 20, 'bold', 'floral white',
                                               4, 0, 10, 10, 0, 10, 'n')
lvl4_6thframe = obj.frame_lvl_(lvl3_mainframe, 5, 0, 10, 10, 0, 10, 'w', 0, 'floral white')
# _____________________________ -LVL 4- Frames which holds parts of all contents (End)______


# _____________________________ -LVL 5- Frames inside LVL 4 frames (Start)____________________
lvl5_in_2ndframe = obj.frame_lvl_(lvl4_2ndframe, 0, 0, 0, 0, 150, 0, 'w', 0, 'light grey')
lvl5_in_3rdframe = obj.frame_lvl_(lvl4_3rdframe, 0, 0, 10, 10, 10, 10, 'w', 0, 'floral white')
lvl5_in_4thframe = obj.frame_lvl_(lvl4_4thframe, 0, 0, 10, 10, 10, 10, 'w', 0, 'floral white')
lvl5_in_5thframe = obj.frame_lvl_(lvl4_5thframe, 0, 0, 10, 10, 10, 10, 'w', 0, 'floral white')
lvl5_in_6thframe = obj.frame_lvl_(lvl4_6thframe, 0, 0, 50, 0, 10, 50, 'w', 0, 'floral white')
# _____________________________ -LVL 5- Frames inside LVL 4 frames (End)______________________


# _____________________________ -LVL 6- Frames inside LVL 5 frames (Start)____________________
lvl6_in_2ndframe = obj.frame_lvl_(lvl5_in_2ndframe,0,0,200,20,50,15,'w','n','light grey')
pic_frame        = obj.frame_lvl_(lvl4_2ndframe,   0,0,15,0,0,0,'w',0,'light grey')

lvl6_1_in_3rdframe = obj.frame_lvl_(lvl5_in_3rdframe, 0, 0, 0, 0, 0, 0, 'w',0, 'light grey')
lvl6_2_in_3rdframe = obj.frame_lvl_(lvl5_in_3rdframe, 1, 0, 0, 0, 0, 0, 'w',0, 'light grey')

lvl6_1_in_4thframe = obj.frame_lvl_(lvl5_in_4thframe, 0, 0, 0, 0, 0, 0, 'w',0, 'floral white')
lvl6_2_in_4thframe = obj.frame_lvl_(lvl5_in_4thframe, 1, 0, 0, 0, 0, 0, 'w',0, 'floral white')

lvl6_1_in_5thframe = obj.frame_lvl_(lvl5_in_5thframe, 4, 0, 0, 0, 0, 0, 'w',0, 'floral white')
lvl6_2_in_5thframe = obj.frame_lvl_(lvl5_in_5thframe, 5, 0, 0, 0, 10, 0, 'w',0, 'floral white')
# _____________________________ -LVL 6- Frames inside LVL 5 frames (End)______________________


# _____________________________ -LVL 7- Frames inside LVL 6 frames (Start)____________________
lvl7_1_in_2ndframe = obj.frame_lvl_(lvl6_in_2ndframe, 0, 0, 0, 0, 0, 0, 'w', 0, 'light grey')
lvl7_2_in_2ndframe = obj.frame_lvl_(lvl6_in_2ndframe, 1, 0, 0, 0, 0, 10, 'w', 0, 'light grey')
# _____________________________ -LVL 7- Frames inside LVL 6 frames (End)______________________
# __________________________________________________-Frames-___________________________________________________________


# ________________________________________-Contents (widgets, buttons, etc.)-__________________________________________
# __________________ -LVL 1- _______________________
# NONE
# __________________ -LVL 1- _______________________

# __________________ -LVL 2- _______________________
# NONE
# __________________ -LVL 2- _______________________

# __________________ -LVL 3- _______________________
# NONE
# __________________ -LVL 3- _______________________

# __________________ -LVL 4- _______________________
obj.create_label(lvl4_1stframe, "SERI'S EMPLOYEE PERSONAL INFORMATION", 'Algerian', 35, 'bold', 'floral white', 0, 0, 0, 0, 0, 0, 'n')
# __________________ -LVL 4- _______________________

# __________________ -LVL 5- _______________________
a19 = obj.create_entry_with_label(lvl5_in_5thframe, "Address Line 1", 'floral white',
                            134, 0, 0, 10, 10, 10, 0, 'w')
a20 = obj.create_entry_with_label(lvl5_in_5thframe, "Address Line 2", 'floral white',
                            120, 2, 0, 10, 10, 10, 0, 'w')
a25 = obj.create_entry_with_label(lvl5_in_5thframe, "Picture Path", 'floral white',
                            134, 6, 0, 10, 10, 10, 0, 'w')
btn1 = obj.create_button(lvl5_in_6thframe, "Save", 15, 1, 'light blue', 'black',
                  0, 0, 10, 5, 0, 0, 'w')
btn1.configure(command= get_entry)
btn2 = obj.create_button(lvl5_in_6thframe, "Cancel", 15, 1, 'white', 'black',
                  0, 1, 10, 5, 0, 0, 'w')
btn2.configure(command= delete_entry_content)
# __________________ -LVL 5- _______________________

# __________________ -LVL 6- _______________________
a9 = obj.create_entry_with_label(lvl6_1_in_3rdframe, "Department", 'light grey',
                            72, 0, 0, 10, 10, 0, 10, 'w')
a10 = obj.create_entry_with_label(lvl6_1_in_3rdframe, "Designation", 'light grey',
                            30, 0, 1, 0, 10, 0, 10, 'w')
a11 = obj.create_combobox_with_label(lvl6_1_in_3rdframe, "Qualified Dept. Status", combo_box_values[4], 'light grey',
                            25, 0, 2, 0, 10, 0, 10, 'w')

a12 = obj.create_entry_with_label(lvl6_2_in_3rdframe, "Employee Status", 'light grey',
                            82, 0, 0, 10, 10, 0, 10, 'w')
a13 = obj.create_dateentry_with_label(lvl6_2_in_3rdframe, "Paydate", 'light grey',
                            13, 0, 1, 0, 10, 0, 10, 'w')
a14 = obj.create_entry_with_label(lvl6_2_in_3rdframe, "Employee Number", 'light grey',
                            32, 0, 2, 0, 10, 0, 10, 'w')

a15 = obj.create_entry_with_label(lvl6_1_in_4thframe, "Contact Number", 'floral white',
                            50, 0, 0, 10, 10, 0, 10, 'w')
a16 = obj.create_entry_with_label(lvl6_1_in_4thframe, "Email", 'floral white',
                            82, 0, 1, 0, 10, 0, 10, 'w')

a17 = obj.create_entry_with_label(lvl6_2_in_4thframe, "Other (Social Media)", 'floral white',
                            50, 0, 0, 10, 10, 0, 10, 'w')
a18 = obj.create_entry_with_label(lvl6_2_in_4thframe, "Social Media Account ID/No.", 'floral white',
                            82, 0, 1, 0, 10, 0, 10, 'w')

a21 = obj.create_entry_with_label(lvl6_1_in_5thframe, "City/Municipality", 'floral white',
                            65, 0, 0, 10, 10, 10, 0, 'w')
a22 = obj.create_entry_with_label(lvl6_1_in_5thframe, "State/Province", 'floral white',
                            65, 0, 1, 10, 10, 10, 0, 'w')

a23 = obj.create_combobox_with_label(lvl6_2_in_5thframe, "Country", combo_box_values[5], 'floral white',
                            62, 0, 0, 10, 10, 0, 10, 'w')
a24 = obj.create_entry_with_label(lvl6_2_in_5thframe, "Zipcode", 'floral white',
                            30, 0, 1, 10, 10, 0, 10, 'w')
# __________________ -LVL 6- _______________________

# __________________ -LVL 7- _______________________
a1 = obj.create_entry_with_label(lvl7_1_in_2ndframe, "First Name", 'light grey',
                            25, 0, 0, 10, 10, 5, 0, 'w')
a2 = obj.create_entry_with_label(lvl7_1_in_2ndframe, "Middle Name", 'light grey',
                            25, 0, 1, 0, 10, 5, 0, 'w')
a3 = obj.create_entry_with_label(lvl7_1_in_2ndframe, "Last Name", 'light grey',
                            25, 0, 2, 0, 10, 5, 0, 'w')
a4 = obj.create_combobox_with_label(lvl7_1_in_2ndframe, "Suffix", combo_box_values[0], 'light grey',
                            15, 0, 3, 0, 10, 5, 0, 'w')
a4.configure(validatecommand =  insert_picture)

a5 = obj.create_dateentry_with_label(lvl7_2_in_2ndframe, "Date of Birth", 'light grey',
                            28, 0, 0, 10, 10, 5, 0, 'w')
a6 = obj.create_combobox_with_label(lvl7_2_in_2ndframe, "Gender", combo_box_values[1], 'light grey',
                            20, 0, 1, 0, 10, 5, 0, 'w')
a7 = obj.create_combobox_with_label(lvl7_2_in_2ndframe, "Nationality", combo_box_values[2], 'light grey',
                            14, 0, 2, 0, 10, 5, 0, 'w')
a8 = obj.create_combobox_with_label(lvl7_2_in_2ndframe, "Civil Status", combo_box_values[3], 'light grey',
                            19, 0, 3, 0, 10, 5, 0, 'w')

obj.create_frame(pic_frame, 'floral white', 0, 0, 0, 0, 0, 0, 0, 0, 'w')
a26 = insert_pic = obj3.create_label(pic_frame, '', 0, 0, 2, 0, 0, 0, 0,'w')
insert_pic.configure(image= obj3.insert_image('C:\\Users\\JASMIN R. DY\\PycharmProjects\\OOP_Payroll\\images\\image6.jpg', 150, 150))
pic_btn = obj.create_button(pic_frame, "choose file", 0, 0, 'floral white',
                  'black', 1, 0, 0, 0, 0, 0, 'w')
pic_btn.configure(command= insert_picture)
obj.create_label(pic_frame, "no file chosen", 'Times New Roman',
                  10, '', 'light grey', 1, 1, 0, 0, 0, 0, 'w')
# __________________ -LVL 7- _______________________
# ________________________________________-Contents (widgets, buttons, etc.)-__________________________________________


root.mainloop()