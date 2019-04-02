#Claire Rhoda
#1068768
#Program 1
#This program calculates the Profit or Loss of inputed stock
#information using functions


def load()->(str,float,float,float,float):
    """stock info is inputed here"""
    sName = input("Enter a stock name or -1 to quit")
    if sName == "-1":
        return (None,None,None,None,None)
    shares = float(input("Enter number of shares bought"))
    stockPP = float(input("Enter stock purchase price"))
    stockSP = float(input("Enter stock selling price"))
    brokercomm = float(input("Enter broker commission"))
    return (sName,shares,stockPP,stockSP,brokercomm)

def calc(s:float,stockPP:float,stockSP:float,bcomm:float)->(float,float,float,float,float):
    """Profit/Loss info and commission infor is calculated"""
    tPrice = s * stockPP
    commPriceBought = tPrice * bcomm
    soldStock = s * stockSP
    commPriceSold = soldStock * bcomm
    ProfitLoss = (soldStock - commPriceSold) - (tPrice + commPriceBought)
    return(tPrice,commPriceBought,soldStock,commPriceSold,ProfitLoss)

def display(sName:str,tPrice:float,commPB:float,sStock:float,commPS:float,PL:float)->None:
    print("Stock Name:",sName)
    print("\nAmount paid for the stock:       $",format(tPrice,"12,.2f"))
    print("Commission paid on the purchase: $",format(commPB,"12,.2f"))
    print("Amount the stock sold for:       $",format(sStock,"12,.2f"))
    print("Commission paid on the sale:     $",format(commPS,"12,.2f"))
    print("Profit(or loss if negative):     $",format(PL,"12,.2f"))

def main():
    a = True
    while a == True:
        sName,shares,stockPP,stockSP,bcomm = load()
        if sName == None:
            a = False
        else:
            tPrice,commPB,sStock,commPS,PL = calc(shares,stockPP,stockSP,bcomm)
            display(sName,tPrice,commPB,sStock,commPS,PL)

if __name__ == "__main__":
    main()
