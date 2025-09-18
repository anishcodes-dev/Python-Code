#calculating area of traingle
def area_of_traingle(a,b,c):
    #perimeter
    s=(a+b+c)/2
    area =(s+(s-a)+(s-b)+(s-c))**0.5
    return area

if __name__=='__main__':
    print(area_of_traingle(2,3,4))
