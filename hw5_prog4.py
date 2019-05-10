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
        self.annualInterestRate_frame = tkinter.Frame(self.main_window)
        self.numberOfYears_frame = tkinter.Frame(self.main_window)
        self.loanAmount_frame = tkinter.Frame(self.main_window)
        self.monthlyPayment_frame = tkinter.Frame(self.main_window)
        self.totalPayment_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for Annual Interest Rate.
        self.annualInterestRate_label = tkinter.Label(self.annualInterestRate_frame, \
                        text='Annual Interest Rate')
        self.annualInterestRate_entry = tkinter.Entry(self.annualInterestRate_frame, \
                                         width=10)
        self.annualInterestRate_label.pack(side='left')
        self.annualInterestRate_entry.pack(side='left')

        # Create and pack the widgets for Number of Years.
        self.numberOfYears_label = tkinter.Label(self.numberOfYears_frame, \
                        text='Number of Years')
        self.numberOfYears_entry = tkinter.Entry(self.numberOfYears_frame, \
                                         width=10)
        self.numberOfYears_label.pack(side='left')
        self.numberOfYears_entry.pack(side='left')
        
        # Create and pack the widgets for Loan Amount.
        self.loanAmount_label = tkinter.Label(self.loanAmount_frame, \
                        text='Loan Amount')
        self.loanAmount_entry = tkinter.Entry(self.loanAmount_frame, \
                                         width=10)
        self.loanAmount_label.pack(side='left')
        self.loanAmount_entry.pack(side='left')

        # Create and pack the widgets for Monthly Payment.
        self.result_label = tkinter.Label(self.monthlyPayment_frame, \
                        text='Monthly Payment')
        self.monthlyPayment = tkinter.StringVar() # To update avg_label
        self.monthlyPayment_label = tkinter.Label(self.monthlyPayment_frame, \
                                    textvariable=self.monthlyPayment)
        self.result_label.pack(side='left')
        self.monthlyPayment_label.pack(side='left')

        # Create and pack the widgets for Total Payment.
        self.result_label = tkinter.Label(self.totalPayment_frame, \
                        text='Total Payment')
        self.totalPayment = tkinter.StringVar() # To update avg_label
        self.totalPayment_label = tkinter.Label(self.totalPayment_frame, \
                                    textvariable=self.totalPayment)
        self.result_label.pack(side='left')
        self.totalPayment_label.pack(side='left')

        # Create and pack the button widgets.
        self.compute_button = tkinter.Button(self.button_frame, \
                                     text='Compute Payment', \
                                     command=self.total_payment)
        self.compute_button.pack(side='right')
        

        # Pack the frames.
        self.annualInterestRate_frame.pack()
        self.numberOfYears_frame.pack()
        self.loanAmount_frame.pack()
        self.monthlyPayment_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The total_payment method is the callback function for
    # the compute_button widget.


    def total_payment(self):
        # Get the three test scores and store them
        # in variables.
        self.annualInterestRate = float(self.annualInterestRate_entry.get())
        self.numberOfYears = float(self.numberOfYears_entry.get())
        self.loanAmount = float(self.loanAmount_entry.get())

        # Calculate the average.
        self.totalPayment = (self.annualInterestRate + self.numberOfYears + \
                        self.loanAmount) / 3.0

        # Update the avg_label widget by storing
        # the value of self.average in the StringVar
        # object referenced by avg.
        self.totalPayment.set(self.totalPayment)

# Create an instance of the TestAvg class.
loan_program = LoanProgram()
