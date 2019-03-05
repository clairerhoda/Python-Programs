#Claire Rhoda
#1068768
#Program 4
#This program

#user inputs their income

user_income = int(input("Enter a negative to quit or a new tax income to continue"))

while user_income >= 0:
    #calculations for 2017
    if user_income <= 9325:
        tax17 =  (user_income * .10)
    elif user_income >= 9326 and user_income <= 37950:
        tax17 = ((user_income - 9325) * .15) + 932.5      
    elif user_income >= 37951 and user_income <= 91900:
        tax17 = ((user_income - 9325 - 28625) * .25) + 932.5 + 4293.75
    elif user_income >= 91901 and user_income <= 191650:
        tax17 = ((user_income - 9325 - 28625 - 53950) * .28) + 932.5 + 4293.75 + 13487.5
    elif user_income >= 191651 and user_income <= 416700:
        tax17 = ((user_income - 9325 - 28625 - 53950 - 99750) * .33) + 932.5 + 4293.75 + 13487.5 + 27930
    elif user_income >= 416701 and user_income <= 418400:
        tax17 = ((user_income - 9325 - 28625 - 53950 - 99750 -225050) * .35) + 932.5 + 4293.75 + 13487.5 + 27930 + 74266.5
    elif user_income > 418401:
        tax17 = ((user_income - 9325 - 28625 - 53950 - 99750 -225050 - 1700) * .396) + 932.5 + 4293.75 + 13487.5 + 27930 + 74266.5 + 595

    #calculations for 2018
    if user_income <= 9525:
        tax18 = (user_income * .10)
    elif user_income >= 9526 and user_income <= 38700:
        tax18 = ((user_income - 9525) * .12) + 952.5   
    elif user_income >= 38701 and user_income <= 82500:
        tax18 = ((user_income - 9525 - 29175) * .22) + 952.5 + 3501
    elif user_income >= 82501 and user_income <= 157500:
        tax18 = ((user_income - 9525 - 29175 - 43800) * .24) + 952.5 + 3501 + 9636
    elif user_income >= 157501 and user_income <= 200000:
        tax18 = ((user_income - 9525 - 29175 - 43800 -75000) * .32) + 952.5 + 3501 + 9636 + 18000      
    elif user_income >= 200001 and user_income <= 500000:
        tax18 = ((user_income - 9525 - 29175 - 43800 -75000 - 42500) * .35) + 952.5 + 3501 + 9636 + 18000 + 13600   
    elif user_income > 500000:
        tax18 = ((user_income - 9525 - 29175 - 43800 -75000 - 42500 - 300000) * .37) + 952.5 + 3501 + 9636 + 18000 + 13600 + 105000 
    print("Income:",user_income)
    print("2017 tax:",tax17)
    print("2018 tax:",tax18)
    print("Differnce:",tax18 - tax17)
    print("Difference (percent) :",((tax17 - tax18)/ tax17 * 100))
    user_income = int(input("Enter a negative to quit or a new tax income to continue"))

