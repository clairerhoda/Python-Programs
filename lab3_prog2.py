#Claire Rhoda
#1068768
#Program 2
#This program calculates simple interest of a given rate, period, and principal

def show_interest(rate:float,periods:int,principal:float)->float:
    interest = principal * rate * periods
    return interest

def main():
    rate = 0.01
    periods = 10
    principal = 10000.00
    answer = show_interest(rate,periods,principal)
    print("The simple interest will be $",answer)
    
if __name__ == "__main__":
    main()
    
