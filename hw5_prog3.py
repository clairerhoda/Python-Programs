#Claire Rhoda
#1068768
#Program 3
#This program calculates and displays the loan for buying a car.

class Loan:
    #initializer is created
    def __init__(self,annualInterest,numberOfYears,loanAmount,borrowersName):
        #all inputs are set 
        self.__annualInterest = annualInterest
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrowersName = borrowersName
        

    def setAnnualInterestRate(self, annualInterestRate):
        """mutates interest rate"""
        self.__annualInterestRate = annualInterestRate
        

    def setNumberOfYears(self, numberOfYears):
        """mutates number of years"""
        self.__numberOfYears = numberOfYears
        

    def setLoanAmount(self, loanAmount):
        """mutates loan amount"""
        self.__loanAmount = loanAmount
        

    def setBorrowerName(self, borrowersName):
        """mutates borrowers name"""
        self.__borrowersName = borrowerName
        

    def getAnnualInterestRate(self):
        """getter for annual interest rate"""
        return self.__annualInterest
    

    def getNumberOfYears(self):
        """getter for number of years"""
        return self.__numberOfYears
    

    def getLoanAmount(self):
        """getter for loan amount"""
        return self.__loanAmount
    

    def getBorrowersName(self):
        """getter for borrowers name"""
        return self.__borrowersName

    
    def getMonthlyPayment(self):
        """monthly interest rate and payment are mutated"""
        monthlyInterestRate = self.__annualInterest / 1200
        monthlyPayment = self.__loanAmount * monthlyInterestRate / \
                         (1 - (1 / (1 + monthlyInterestRate) ** \
                               (self.__numberOfYears * 12)))
        return monthlyPayment


    def getTotalPayment(self):
        """getter for total payment"""
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return totalPayment

        
def main():
    #user input loan information
    annualInterestRate = float(input("Enter yearly interest rate:"))
    numOfYearsLoan = float(input("Enter number of years as an interger:"))
    loanAmount = float(input("Enter loan amount:"))
    borrowersName = input("Enter a borrower's name:")
    #infomration is sent to class
    loan = Loan(annualInterestRate,numOfYearsLoan,loanAmount,\
                borrowersName)

    print("The loan is for",loan.getBorrowersName())
    print("The monthly payment is",format(loan.getMonthlyPayment(),'.2f'))
    print("The total payment is",format(loan.getTotalPayment(),'.2f'),"\n")
    answer = input("Do you want to change the loan amount? Y for yes or enter to quit")
    if answer.upper() == 'Y':
        loanAmount = float(input("Enter new loan amount"))
        print("The loan if for",loan.getBorrowersName())
        #new information is resent to class
        loan = Loan(annualInterestRate,numOfYearsLoan,loanAmount,\
                borrowersName)
        print("The monthly payment is",format(loan.getMonthlyPayment(),'.2f'))
        print("The total payment is",format(loan.getTotalPayment(),'.2f'))
        
main()


##Test Case 1
##>>> 
##======= RESTART: /Users/clairerhoda/workspace/comp_sci_10/hw5_prog3.py =======
##Enter yearly interest rate:2.5
##Enter number of years as an interger:5
##Enter loan amount:1000.00
##Enter a borrower's name:John Jones
##The loan is for John Jones
##The monthly payment is 17.75
##The total payment is 1064.84 
##
##Do you want to change the loan amount? Y for yes or enter to quity
##Enter new loan amount5000
##The loan if for John Jones
##The monthly payment is 88.74
##The total payment is 5324.21
##
##Test Case 2
##>>> 
##======= RESTART: /Users/clairerhoda/workspace/comp_sci_10/hw5_prog3.py =======
##Enter yearly interest rate:3
##Enter number of years as an interger:6
##Enter loan amount:50.00
##Enter a borrower's name:Jeff G
##The loan is for Jeff G
##The monthly payment is 0.76
##The total payment is 54.70 
##
##Do you want to change the loan amount? Y for yes or enter to quit
##
##Test Case 3
##>>> 
##======= RESTART: /Users/clairerhoda/workspace/comp_sci_10/hw5_prog3.py =======
##Enter yearly interest rate:15
##Enter number of years as an interger:20
##Enter loan amount:2500.00
##Enter a borrower's name:Fred K
##The loan is for Fred K
##The monthly payment is 32.92
##The total payment is 7900.74 
##
##Do you want to change the loan amount? Y for yes or enter to quity
##Enter new loan amount9000.00
##The loan if for Fred K
##The monthly payment is 118.51
##The total payment is 28442.65
##
##Test Case 4
##>>> 
##======= RESTART: /Users/clairerhoda/workspace/comp_sci_10/hw5_prog3.py =======
##Enter yearly interest rate:5.5
##Enter number of years as an interger:3
##Enter loan amount:6500.00
##Enter a borrower's name:Greg H
##The loan is for Greg H
##The monthly payment is 196.27
##The total payment is 7065.84 
##
##Do you want to change the loan amount? Y for yes or enter to quit
##
##Test Case 5
##>>> 
##======= RESTART: /Users/clairerhoda/workspace/comp_sci_10/hw5_prog3.py =======
##Enter yearly interest rate:90
##Enter number of years as an interger:1.5
##Enter loan amount:90
##Enter a borrower's name:Henry F
##The loan is for Henry F
##The monthly payment is 9.27
##The total payment is 166.91 
##
##Do you want to change the loan amount? Y for yes or enter to quit
##>>> 

    
