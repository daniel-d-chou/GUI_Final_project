import New_bullshit2
import Next_Page_class
import GUI_Class_file
import op
from PIL import ImageTk

obj1 = Next_Page_class.Our_project()
obj2 = New_bullshit2.MyGui2()
obj3 = GUI_Class_file.MyGui2()
obj4 = op.EmployeePayroll()

root = obj2.root_lvl1_()
canvas = obj2.canvas_lvl2_(root)
# _________________________________ BUTTON FUNCTIONS ____________________________________________
img = []


def retrieve_data():  # SEARCH BUTTON
    global img
    x = 0
    l1 = ("First_name, Middle_name, Last_name, Civil_status, Qualified_dept_stat, Paydate, Employee_stat, Designation,Department, Employee_pic")
    command = (f"SELECT {l1} "
               f"FROM personal_infotbl "
               f"WHERE Employee_no == {float(A1.get())}")
    ok = obj3.cursor_database("AssessmentApplicationDB",command)
    for i in range(8):
        personal_info[x].configure(state= 'normal')
        personal_info[x].delete(0, 'end')
        personal_info[x].insert(0, ok[i])
        personal_info[x].configure(state='readonly')
        x += 1
        if x == len(ok):
            x = 0

    A2.configure(state='normal')
    A2.delete(0, 'end')
    A2.insert(0, str(ok[8]))
    A2.configure(state='readonly')

    img = ImageTk.PhotoImage(data = ok[9], size=(150,150))
    pic.configure(image= img)


def compute_data():  # GROSS INCOME BUTTON
    x = 0
    income_cutoff_basic_income = float(basic_income[0].get()) * float(basic_income[1].get())
    income_cutoff_honorarium_income = float(honorarium_income[0].get()) * float(honorarium_income[1].get())
    income_cutoff_other_income = float(other_income[0].get()) * float(other_income[1].get())
    gross_income = income_cutoff_basic_income + income_cutoff_honorarium_income + income_cutoff_other_income

    basic_income[2].configure(state= 'normal')
    basic_income[2].delete(0, 'end')
    basic_income[2].insert(0, income_cutoff_basic_income)
    basic_income[2].configure(state='readonly')

    honorarium_income[2].configure(state='normal')
    honorarium_income[2].delete(0, 'end')
    honorarium_income[2].insert(0, income_cutoff_honorarium_income)
    honorarium_income[2].configure(state='readonly')

    other_income[2].configure(state='normal')
    other_income[2].delete(0, 'end')
    other_income[2].insert(0, income_cutoff_other_income)
    other_income[2].configure(state='readonly')

    summary_income[0].configure(state= 'normal')
    summary_income[0].delete(0, 'end')
    summary_income[0].insert(0, gross_income)
    summary_income[0].configure(state='readonly')




def compute_net_income():  # NET INCOME BUTTON
    x = 0
    sss_contribution = float(obj4.calculate_sss_contribution(float(summary_income[0].get())))
    philhealth_contribution = float(obj4.calculate_philhealth_contribution(float(summary_income[0].get())))
    pagibig_contribution = 100.00
    withholded_tax = float(obj4.calculate_withholding_tax(float(summary_income[0].get())))
    unpackening = [sss_contribution, philhealth_contribution, pagibig_contribution, withholded_tax]

    for i in unpackening:
        regular_deductions[x].configure(state='normal')
        regular_deductions[x].delete(0, 'end')
        regular_deductions[x].insert(0, i)
        regular_deductions[x].configure(state='readonly')
        x += 1
        if x == len(unpackening):
            x = 0

    computed_other_deduction = 0
    for i in other_deductions:
        computed_other_deduction += float(other_deductions[x].get())
        x += 1
        if x == len(other_deductions):
            x = 0
    total_deduction = sss_contribution + philhealth_contribution + pagibig_contribution + withholded_tax + computed_other_deduction
    net_income = float(summary_income[0].get()) - total_deduction

    A3.configure(state='normal')
    A3.delete(0, 'end')
    A3.insert(0, total_deduction)
    A3.configure(state='readonly')

    summary_income[1].configure(state='normal')
    summary_income[1].delete(0, 'end')
    summary_income[1].insert(0, net_income)
    summary_income[1].configure(state='readonly')
    print(A3.get())


def save_to_database():  # SAVE BUTTON
    fields = ["Employee_no, Basic_income, Honorarium_income, Other_income, Gross_income, SSS_contribution, Philhealth_contribution,"
              " Pagibig_contribution, Income_tax_contribution, SSS_loan, Pagibig_loan, Faculty_savings_deposit,"
              " Faculty_savings_loan, Salary_loan, Other_loan, Total_deduction, Net_income"]
    values = ("'"+str(A1.get())+"','"+str(basic_income[2].get())+"','"+str(honorarium_income[2].get())+"','"+str(other_income[2].get())+"',"
              "'"+str(summary_income[0].get())+"','"+str(regular_deductions[0].get())+"','"+str(regular_deductions[1].get())+"',"
              "'"+str(regular_deductions[2].get())+"','"+str(regular_deductions[3].get())+"','"+str(other_deductions[0].get())+"',"
              "'"+str(other_deductions[1].get())+"','"+str(other_deductions[2].get())+"','"+str(other_deductions[3].get())+"',"
              "'"+str(other_deductions[4].get())+"','"+str(other_deductions[5].get())+"','"+str(summary_income[0].get())+"',"
              "'"+str(summary_income[1].get())+"'")
    obj3.create_table("AssessmentApplicationDB", "Payroll_table", fields[0])
    obj3.save_data_into_database("AssessmentApplicationDB", "Payroll_table", fields[0], values)


def clear():  # NEW BUTTON
    sep_entry = [A1,A2,A3]
    x = 0
    for i in range(len(basic_income)):
        if i <= len(basic_income):
            basic_income[x].configure(state= 'normal')
            basic_income[x].delete(0, 'end')
            basic_income[x].insert(0, "%.2f" % 0)
            honorarium_income[x].configure(state='normal')
            honorarium_income[x].delete(0, 'end')
            honorarium_income[x].insert(0, "%.2f" % 0)
            other_income[x].configure(state='normal')
            other_income[x].delete(0, 'end')
            other_income[x].insert(0, "%.2f" % 0)
            sep_entry[x].configure(state='normal')
            sep_entry[x].delete(0, 'end')
            sep_entry[2].insert(0, "%.2f" % 0)
            x += 1
            if x == len(basic_income):
                x = 0
    for i in range(len(personal_info)):
        if i < len(summary_income):
            summary_income[x].configure(state='normal')
            summary_income[x].delete(0, 'end')
            regular_deductions[x].configure(state='normal')
            regular_deductions[x].delete(0, 'end')
            other_deductions[x].configure(state='normal')
            other_deductions[x].delete(0, 'end')
            other_deductions[x].insert(0, "%.2f" % 0)
            personal_info[x].configure(state='normal')
            personal_info[x].delete(0, 'end')
            x += 1
        elif len(regular_deductions) > i >= len(summary_income):
            regular_deductions[x].configure(state='normal')
            regular_deductions[x].delete(0, 'end')
            other_deductions[x].configure(state='normal')
            other_deductions[x].delete(0, 'end')
            other_deductions[x].insert(0, "%.2f" % 0)
            personal_info[x].configure(state='normal')
            personal_info[x].delete(0, 'end')
            x += 1
        elif len(other_deductions) > i >= len(regular_deductions):
            other_deductions[x].configure(state='normal')
            other_deductions[x].delete(0, 'end')
            other_deductions[x].insert(0, "%.2f" % 0)
            personal_info[x].configure(state='normal')
            personal_info[x].delete(0, 'end')
            x += 1
        else:
            personal_info[x].configure(state='normal')
            personal_info[x].delete(0, 'end')
            x += 1
            if x == len(personal_info):
                x = 0


def update():
    command2 = ("""UPDATE Payroll_table SET Basic_income = ?, Honorarium_income = ?, Other_income = ?, Gross_income = ?, SSS_contribution = ?, Philhealth_contribution = ?,
              Pagibig_contribution = ?, Income_tax_contribution = ?, SSS_loan = ?, Pagibig_loan = ?, Faculty_savings_deposit = ?, Faculty_savings_loan = ?, 
              Salary_loan = ?, Other_loan = ?, Total_deduction = ?, Net_income = ? WHERE Employee_no = ?""", (basic_income[2].get(), honorarium_income[2].get(), other_income[2].get(), summary_income[0].get(), regular_deductions[0].get(),
                  regular_deductions[1].get(), regular_deductions[2].get(), regular_deductions[3].get(), other_deductions[0].get(), other_deductions[1].get(),
                  other_deductions[2].get(), other_deductions[3].get(), other_deductions[4].get(), other_deductions[5].get(), A3.get(), summary_income[1].get(),
                A1.get()))
    obj3.cursor_database2("AssessmentApplicationDB", command2)


x = 0
# _____________________________________________________ -Frames- ______________________________________________________
# _____________________________ LVL 1 ______________________________________

main_frame = obj2.frame_lvl_(canvas, 'floral white', 700, 1000,
                             0, 0, 10, 10, 10, 10, 'n')
# _____________________________ LVL 1 ______________________________________

# _____________________________ LVL 2 ______________________________________
lvl2_top_frame = obj2.frame_lvl_(main_frame, 'floral white', 50, 50,
                                 0, 0, 10, 10, 10, 10, 'n')
lvl2_bot_frame = obj2.frame_lvl_(main_frame, 'floral white', 50, 50,
                                 1, 0, 10, 10, 10, 10, 'n')
# _____________________________ LVL 2 ______________________________________

# _____________________________ LVL 3 ______________________________________
lvl3_left_frame = obj2.frame_lvl_(lvl2_bot_frame, 'floral white', 50, 50,
                                  0, 0, 70, 0, 10, 10, 'w')
lvl3_right_frame = obj2.frame_lvl_(lvl2_bot_frame, 'floral white', 50, 50,
                                  0, 1, 10, 10, 10, 10, 'e')
# _____________________________ LVL 3 ______________________________________

# _____________________________ LVL 4 ______________________________________
lvl4_left_frame = []
Label_frame_names = ["Employee  Basic Info", "Basic Income", "Honorarium Income", "Other Income", "Summary Income"]
for i in Label_frame_names:
    frame = obj2.label_frame_lvl_(lvl3_left_frame, Label_frame_names[x], 'Times New Roman', 20, '', 'floral white',
                                              x, 0, 0, 0, 0, 10,'n')
    lvl4_left_frame.append(frame)
    x += 1
    if x == len(Label_frame_names):
        x = 0

lvl4_1_right_frame = obj2.frame_lvl_(lvl3_right_frame, 'floral white', 50, 50,
                                          0, 0, 0, 0, 0, 10, 'n')
lvl4_2_right_frame = obj2.label_frame_lvl_(lvl3_right_frame, "Regular Deductions", 'Times New Roman', 20, '', 'floral white',
                                          1, 0, 0, 0, 25, 25,'n')
lvl4_3_right_frame = obj2.label_frame_lvl_(lvl3_right_frame, "Other Deductions", 'Times New Roman', 20, '', 'floral white',
                                          2, 0, 0, 0, 0, 25,'n')
lvl4_4_right_frame = obj2.label_frame_lvl_(lvl3_right_frame, "Deduction Summary", 'Times New Roman', 20, '', 'floral white',
                                          3, 0, 0, 0, 0, 25,'n')
lvl4_5_right_frame = obj2.frame_lvl_(lvl3_right_frame, 'floral white', 50, 50,
                                          4, 0, 50, 0, 0, 0, 'n')
# _____________________________ LVL 4 ______________________________________

# _____________________________ LVL 5 ______________________________________
lvl5_1_in_4_1_left_frame = obj2.frame_lvl_(lvl4_left_frame[0], 'floral white', 50, 50,
                                      1, 0, 20, 20, 30, 20, 'nw')
lvl5_1_in_4_2_left_frame = obj2.frame_lvl_(lvl4_left_frame[1], 'floral white', 50, 50,
                                      0, 0, 15, 15, 10, 0, 'nw')
lvl5_1_in_4_3_left_frame = obj2.frame_lvl_(lvl4_left_frame[2], 'floral white', 50, 50,
                                      0, 0, 15, 15, 10, 0, 'nw')
lvl5_1_in_4_4_left_frame = obj2.frame_lvl_(lvl4_left_frame[3], 'floral white', 50, 50,
                                      0, 0, 15, 15, 10, 0, 'nw')
lvl5_1_in_4_5_left_frame = obj2.frame_lvl_(lvl4_left_frame[4], 'floral white', 50, 50,
                                      0, 0, 15, 15, 10, 0, 'nw')

lvl5_1_in_4_1_right_frame = obj2.frame_lvl_(lvl4_1_right_frame, 'floral white', 50, 50,
                                      0, 0, 20, 20, 30, 25, 'nw')
lvl5_1_in_4_2_right_frame = obj2.frame_lvl_(lvl4_2_right_frame, 'floral white', 50, 50,
                                      0, 0, 20, 20, 10, 0, 'nw')
lvl5_1_in_4_3_right_frame = obj2.frame_lvl_(lvl4_3_right_frame, 'floral white', 50, 50,
                                      0, 0, 20, 20, 10, 0, 'nw')
lvl5_1_in_4_4_right_frame = obj2.frame_lvl_(lvl4_4_right_frame, 'floral white', 50, 50,
                                      0, 0, 20, 20, 10, 0, 'nw')
lvl5_1_in_4_5_right_frame = obj2.frame_lvl_(lvl4_5_right_frame, 'floral white', 50, 50,
                                      0, 0, 20, 20, 10, 0, 'nw')
# _____________________________ LVL 5 ______________________________________
# _____________________________________________________ -Frames- ______________________________________________________


# _____________________________________________________ -Contents- ______________________________________________________
# _____________________________ LVL 1 ______________________________________
# NONE
# _____________________________ LVL 1 ______________________________________

# _____________________________ LVL 2 ______________________________________
obj2.label(lvl2_top_frame, "SERI'S CHOICE PAYROLL", 'Algerian', 30, '', 'floral white',
           'black', 0, 0, 1, 2, 0, 0, 0, 0, 'n')
# _____________________________ LVL 2 ______________________________________

# _____________________________ LVL 3 ______________________________________
# NONE
# _____________________________ LVL 3 ______________________________________

# _____________________________ LVL 4 ______________________________________
framek = obj3.create_frame(lvl4_left_frame[0], None,  0, 0, 20, 0, 0, 0, 'w')
framek.configure(width= 150, height= 150)
framek.grid_propagate(False)
pic = obj3.create_label(framek, '', 0, 0, 1, 0, 0, 0, 0, 'w')
pic.configure(image= obj3.insert_image('C:\\Users\\JASMIN R. DY\\PycharmProjects\\OOP_Payroll\\images\\image6.jpg', 150, 150))
# _____________________________ LVL 4 ______________________________________

# _____________________________ LVL 5 ______________________________________
unpack1 = [("Rate/Hour:     ", '', 9, '', 'floral white', 'black',30, 0, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w'),
           ("No. of Hours / Cut-off:     ", '', 9, '', 'floral white', 'black',30, 2, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w'),
           ("Income / Cut-off:     ", '', 9, '', 'floral white', 'black',30, 4, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w')]
unpack2 = [("Gross Income:     ", '', 9, '', 'floral white', 'black',30, 0, 0, 0, 1, 1, 1, 0, 20, 0, 10, 'w'),
           ("Net Income:     ", '', 9, '', 'floral white', 'black',30, 2, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w')]
unpack4 = ["First Name:     ","Middle Name:     ","Surname:     ","Civil Status:     ","Qual Dependent stat:     ",
           "Paydate:     ","Employee Status:     ","Designation:     ",]
unpack5 = ["SSS Contribution:     ","Philhealth Contribution:     ","Pag-ibig Contribution:     ",
           "Income Tax Contribution:     "]
unpack6 = ["SSS Loan:     ","Pag-ibig Loan:     ","Faculty Savings Deposit:     ","Faculty Savings Loan:     ",
           "Salary Loan:     ","Other Loans:     "]

A1 = obj2.entry_and_label(lvl5_1_in_4_1_left_frame, "Employee Number:     ", '', 9, '', 'floral white', 'black',30,
                     0, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w')
obj2.label(lvl5_1_in_4_1_left_frame, "Search Employee: ", 'TIMES NEW ROMAN', 10, '', 'FLORAL WHITE', 'black',
                     1, 0, 1, 1, 0 ,0 ,0, 0, 'w')
btn = obj2.button(lvl5_1_in_4_1_left_frame, "SEARCH", 'Times New Roman', 10, '', 'red', 'white',10, 1,
                     1, 1, 1, 1, 0, 0, 0, 10, 'w')
btn.configure(command=retrieve_data)
A2 = obj2.entry_and_label(lvl5_1_in_4_1_left_frame, "Department:     ", '', 9, '', 'floral white', 'black',30,
                     2, 0, 0, 1, 1, 1, 0, 0, 0, 0, 'w')

basic_income = []
for data in unpack1:
    entry = obj2.entry_and_label(lvl5_1_in_4_2_left_frame, *data)
    basic_income.append(entry)
    entry.insert(0, "%.2f" % 0)

honorarium_income = []
for data in unpack1:
    entry = obj2.entry_and_label(lvl5_1_in_4_3_left_frame, *data)
    honorarium_income.append(entry)
    entry.insert(0, "%.2f" % 0)

other_income = []
for data in unpack1:
    entry = obj2.entry_and_label(lvl5_1_in_4_4_left_frame, *data)
    other_income.append(entry)
    entry.insert(0, "%.2f" % 0)

summary_income = []
for data in unpack2:
    entry = obj2.entry_and_label(lvl5_1_in_4_5_left_frame, *data)
    summary_income.append(entry)

personal_info = []
for i in range(8):
    entry = obj2.entry_and_label(lvl5_1_in_4_1_right_frame, unpack4[i], '', 9, '', 'floral white', 'black', 30,
                         i, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w')
    personal_info.append(entry)

regular_deductions = []
for i in unpack5:
    entry = obj2.entry_and_label(lvl5_1_in_4_2_right_frame, unpack5[x], '', 9, '', 'floral white', 'black', 30,
                         x, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w')
    regular_deductions.append(entry)
    x += 1
    if x == len(unpack6):
        x = 0

other_deductions = []
for i in unpack6:
    entry = obj2.entry_and_label(lvl5_1_in_4_3_right_frame, unpack6[x], '', 9, '', 'floral white', 'black', 30,
                         x, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w')
    other_deductions.append(entry)
    entry.insert(0, "%.2f" % 0)
    x += 1
    if x == len(unpack6):
        x = 0

A3 = obj2.entry_and_label(lvl5_1_in_4_4_right_frame, "Total Deductions:                  ", '', 9, '', 'floral white', 'black',30,
                     5, 0, 0, 1, 1, 1, 0, 0, 0, 10, 'w')

btn1 = obj2.button(lvl5_1_in_4_5_right_frame, "GROSS INCOME", 'TIMES NEW ROMAN', 10, '', '#0047AC', 'WHITE',
15, 1, 0, 0, 1, 1, 0, 5, 0, 0, 'w')
btn1.configure(command= compute_data)
btn2 = obj2.button(lvl5_1_in_4_5_right_frame, "NET INCOME", 'TIMES NEW ROMAN', 10, '', '#0047AC', 'WHITE',
12, 1, 0, 1, 1, 1, 0, 5, 0, 0, 'w')
btn2.configure(command= compute_net_income)
btn3 = obj2.button(lvl5_1_in_4_5_right_frame, "SAVE", 'TIMES NEW ROMAN', 10, '', '#1497D4', 'WHITE',
9, 1, 0, 2, 1, 1, 0, 5, 0, 0, 'w')
btn3.configure(command= save_to_database)
btn4 = obj2.button(lvl5_1_in_4_5_right_frame, "UPDATE", 'TIMES NEW ROMAN', 10, '', '#1497D4', 'WHITE',
9, 1, 0, 3, 1, 1, 0, 5, 0, 0, 'w')
btn4.configure(command=update)
btn5 = obj2.button(lvl5_1_in_4_5_right_frame, "NEW", 'TIMES NEW ROMAN', 10, '', '#FFB921', 'WHITE',
7, 1, 0, 4, 1, 1, 0, 0, 0, 0, 'w')
btn5.configure(command=clear)
# _____________________________ LVL 5 ______________________________________
# _____________________________________________________ -Contents- ______________________________________________________

root.mainloop()
