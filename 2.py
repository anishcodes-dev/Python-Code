#factorial using recurison
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)

if __name__=="__main__":
    num=int(input("Enter a number: "))
    result=factorial_recursive(num)
    print(f"The factorial of {num} is {result}")    