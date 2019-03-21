#Claire Rhoda
#1068768
#Program 3
#This program calculates the area of a triangle with
#user inputed length and height

def getData()->(float,float):
    l = float(input("Enter length of triangle"))
    h = float(input("Enter height of triangle"))
    return(l,h)

def trigArea(length:float,height:float)->float:
    a = (length * height) / 2
    return a

def displayData(length:float,height:float,area:float)->None:
    print("The length of the trianlge is",length)
    print("The height of the triangle is",height)
    print("The area of the triangle is",area)
    
def main():
    length,height = getData()
    area = trigArea(length,height)
    displayData(length,height,area)
    
if __name__ == "__main__":
    main()
