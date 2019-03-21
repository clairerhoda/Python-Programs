#Claire Rhoda
#1068768
#Program 4
#This program lets the user input their monthly sales and
#advanced pay (if any) to show the user their calculated pay.

def get_sales()->float:
    monlthy_sales = float(input("Enter the monthly sales:"))
    return monlthy_sales
                          
def get_advanced_pay()->float:
    print("Enter the amount of advanced pay, or")
    print("enter 0 if no advanced pay was given.")
    advanced_pay = float(input("Advanced pay:"))
    return advanced_pay
    
def determine_comm_rate(sales:float)->float:
    if sales < 10000.00:
        rate = .10
    elif sales >= 10000.00 and sales <= 14999.99:
        rate = .12
    elif sales >= 15000.00 and sales <= 17999.99:
        rate = .14
    elif sales >= 18000.00 and sales <= 21999.99:
        rate = .16
    else:
        rate = .18
    return rate

def main():
    #get the amount of sales from user
    sales = get_sales()

    #get the amount of advanced pay from the user
    advanced_pay = get_advanced_pay()

    #determine the commision rate
    comm_rate = determine_comm_rate(sales)

    #calculate the pay
    pay = sales * comm_rate - advanced_pay

    #Display the amount of pay.
    print('The pay is $',format(pay,',.2f'),sep='')

    #determine whether the pay is negative
    if pay < 0:
        print("The salesperson must reimburse")
        print("the company.")
        
if __name__ == "__main__":
    main()

