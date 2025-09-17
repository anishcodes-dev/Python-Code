#factorial code using for loop
def factorial_num(n):
    fact=1
    if n==0  or n==1 :
        return 1
    else:
        for i in range(1,n+1):
          fact*=i

    return fact
 

if __name__=="__main__":
    num=int(input("Enter a number: "))
    result=factorial_num(num)
    print(f"The factorial of {num} is {result}")