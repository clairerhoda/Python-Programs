#Claire Rhoda
#1068768
#Program 4
#This program uses a tkinter module for a Loan program

import tkinter

class LoanProgram:
    def __init__(self):
        # Create the main window.
        
        self.main_window = tkinter.Tk()
        self.main_window.title("Loan Calculator")

        # Create the six frames.
        self.annualInterest_frame = tkinter.Frame(self.main_window)
        self.numberOfYears_frame = tkinter.Frame(self.main_window)
        self.loanAmount_frame = tkinter.Frame(self.main_window)
        self.monthly_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets annual interest rate.
        self.annualInterest_label = tkinter.Label(self.annualInterest_frame, \
                        text='Annual Interest Rate')
        self.annualInterest_entry = tkinter.Entry(self.annualInterest_frame, \
                                         width=10)
        self.annualInterest_label.pack(side='left')
        self.annualInterest_entry.pack(side='left')

        # Create and pack the widgets for test 2.
        self.numberOfYears_label = tkinter.Label(self.numberOfYears_frame, \
                        text='Number of Years')
        self.numberOfYears_entry = tkinter.Entry(self.numberOfYears_frame, \
                                         width=10)
        self.numberOfYears_label.pack(side='left')
        self.numberOfYears_entry.pack(side='left')
        
        # Create and pack the widgets for test 3.
        self.loanAmount_label = tkinter.Label(self.loanAmount_frame, \
                        text='Loan Amount')
        self.loanAmount_entry = tkinter.Entry(self.loanAmount_frame, \
                                         width=10)
        self.loanAmount_label.pack(side='left')
        self.loanAmount_entry.pack(side='left')


        # Create and pack the widgets for the average.
        self.result_label = tkinter.Label(self.monthly_frame, \
                        text='Monthly Payment')
        self.monthly = tkinter.StringVar() # To update monthly_label
        self.monthly_label = tkinter.Label(self.monthly_frame, \
                                    textvariable=self.monthly)
        self.result_label.pack(side='left')
        self.monthly_label.pack(side='left')


        # Create and pack the widgets for the total payment.
        self.result_label = tkinter.Label(self.total_frame, \
                        text='Total Payment')
        self.total = tkinter.StringVar() # To update avg_label
        self.total_label = tkinter.Label(self.total_frame, \
                                    textvariable=self.total)
        self.result_label.pack(side='left')
        self.total_label.pack(side='left')
        

        # Create and pack the button widgets.
        
        self.calc_button = tkinter.Button(self.button_frame, \
                        text='Compute Payment', \
                                     command=self.calc_monthly_total)
        
        self.calc_button.pack(side='left')

        # Pack the frames.
        self.annualInterest_frame.pack()
        self.numberOfYears_frame.pack()
        self.loanAmount_frame.pack()
        self.monthly_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()
        

    def calc_monthly_total(self):
        # Get the annual interest rate, the number of years, and the
        #loan amount and store in variables.
        self.annualInterest = float(self.annualInterest_entry.get())
        self.numberOfYears = float(self.numberOfYears_entry.get())
        self.loanAmount = float(self.loanAmount_entry.get())

        # Calculate the monthly payment.
        self.monthlyInterestRate = self.annualInterest / 1200
        self.monthlyPayment = self.loanAmount * self.monthlyInterestRate / \
                         (1 - (1 / (1 + self.monthlyInterestRate) ** \
                               (self.numberOfYears * 12)))
        
        self.totalPayment = self.monthlyPayment * self.numberOfYears * 12

        # Update the monthly_label widget by storing
        # the value of self.monthlyPayment in the StringVar1
        # object referenced by monthly.
        self.monthly.set(format(self.monthlyPayment,'.2f'))

        # Update the total_label widget by storing
        # the value of self.totalPayment in the StringVar2
        # object referenced by total
        self.total.set(format(self.totalPayment,'.2f'))

# Create an instance of the TestAvg class.
test_loan = LoanProgram()

