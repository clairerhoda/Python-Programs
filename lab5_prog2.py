#Claire Rhoda
#1068768
#Program 2
#This program determines the admission fee of the ageGroup that user inputs

def determineRank(years)->str:
    record = {1:'Freshman',2:'Sophomore',3:'Junior',4:'Senior'}
    return record[years]


def main():
    print("Enter the year")
    years = int(input("(1 for Freshman, 2 for Sophomore, 3 Junior, 4 is Senior"))
    print("The rank is",determineRank(years),"year.")

if __name__ == "__main__":
    main()