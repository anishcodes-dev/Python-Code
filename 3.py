#even and odd
def check_even_odd(n):
    if n % 2==0:
        return "Even"
    else:
        return "Old"

if __name__ == '__main__':
    n =int(input("enter the number : "))
    print(check_even_odd(n))