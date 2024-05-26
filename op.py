class EmployeePayroll:
    def __init__(self):
        self.company_name = ''
        self.department_name = ''
        self.employee_code = ''
        self.employee_name = ''
        self.salary_date_cutoff = ''
        self.basic_pay = 0
        self.overtime_pay = 0
        self.absence_pay = 0
        self.honorarium = 0
        self.tardiness_pay = 0
        self.gross_earnings = 0
        self.sss = 0
        self.philhealth_contribution = 0
        self.withholding_tax = 0
        self.hdmf_contribution = 0
        self.deductions = 0
        self.net_pay = 0

    def input_basic_pay_info(self):
        self.rate_per_hour = float(input("Enter rate per hour: "))
        self.hours_per_payday = float(input("Enter no. of hours per payday: "))
        self.basic_pay = self.rate_per_hour * self.hours_per_payday

    def input_overtime_pay_info(self):
        self.overtime_hours_per_payday = float(input("Enter Number of overtime hours per payday: "))
        self.overtime_pay = self.overtime_hours_per_payday * self.rate_per_hour

    def input_absence_pay_info(self):
        self.num_of_absences = float(input("Enter number of absences: "))
        self.absence_pay = self.num_of_absences * self.rate_per_hour

    def input_honorarium(self):
        self.honorarium = float(input("Enter honorarium: "))

    def input_tardiness_pay_info(self):
        self.tardiness_hours = float(input("Enter number of hours in tardiness: "))
        self.tardiness_pay = self.rate_per_hour * self.tardiness_hours

    def calculate_gross_earnings(self):
        self.gross_earnings = self.basic_pay + self.overtime_pay + self.honorarium

    def calculate_sss_contribution(self, gross_earnings):
        if gross_earnings < 4250.00:
            self.sss = 180.00
        else:
            for i in range(69):
                if gross_earnings > 19749.99:
                    self.sss = 900.00
                    break
                elif 4250.00 + (500 * (i - 1)) <= gross_earnings <= (4749.99 + (500 * (i - 1))):
                    self.sss = 180.00 + (22.50 * i)
        return "%.2f" % round(self.sss, 2)


    def calculate_philhealth_contribution(self, gross_earnings):
        if gross_earnings < 10000.00:
            self.philhealth_contribution = 0.00
        elif 10000.00 <= gross_earnings < 90000.00:
            self.philhealth_contribution = float(0.045 * gross_earnings)
        else:
            self.philhealth_contribution = 4050.00
        return "%.2f" % round(self.philhealth_contribution, 2)

    def calculate_withholding_tax(self, gross_earnings):
        if 0.00 <= gross_earnings <= 10417.00:
            self.withholding_tax = 0
        elif 10417 < gross_earnings <= 16666.00:
            self.withholding_tax = 0 + ((gross_earnings - 10417.00) * 0.15)
        elif 16666.00 < gross_earnings <= 33332.00:
            self.withholding_tax = 937.50 + ((gross_earnings - 16667.00) * .20)
        elif 33333.00 < gross_earnings <= 83332.00:
            self.withholding_tax = 4270.00 + ((gross_earnings - 33333.00) * 0.25)
        elif 83332.00 < gross_earnings <= 333332.00:
            self.withholding_tax = 16770.70 + ((gross_earnings - 83333.00) * 0.30)
        else:
            self.withholding_tax = 91770.70 + ((gross_earnings - 333333.00) * 0.35)
        return "%.2f" % round(self.withholding_tax, 2)

    def calculate_hdmf_contribution(self):
        self.hdmf_contribution = 100.00

    def calculate_deductions(self):
        self.deductions = self.absence_pay + self.tardiness_pay + self.withholding_tax + \
                          self.sss + self.philhealth_contribution + self.hdmf_contribution

    def calculate_net_pay(self):
        self.net_pay = self.gross_earnings - self.deductions

    def display_payroll(self):
        print("Company Name: ", self.company_name)
        print("Department: ", self.department_name)
        print("Employee code: ", self.employee_code)
        print("Employee name: ", self.employee_name)
        print("Salary Cut-Off Date: ", self.salary_date_cutoff)
        print("Basic Pay: %.2f" % self.basic_pay)
        print("Overtime pay: %.2f" % self.overtime_pay)
        print("Absences pay: %.2f" % self.absence_pay)
        print("Honorarium: %.2f" % self.honorarium)
        print("Tardiness pay: %.2f" % self.tardiness_pay)
        print("Withholding Tax: %.2f" % self.withholding_tax)
        print("SSS Contribution: %.2f" % self.sss)
        print("HDMF Contribution: %.2f" % self.hdmf_contribution)
        print("PhilHealth Contribution: %.2f" % self.philhealth_contribution)
        print("Deductions: %.2f" % self.deductions)
        print("Gross Earnings: %.2f" % self.gross_earnings)
        print("Net Pay: %.2f" % self.net_pay)



