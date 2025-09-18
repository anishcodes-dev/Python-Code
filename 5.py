#swap two variable
def swap_two_variable(a,b):
    c=a
    a=b
    b=c
    return a , b
    #in single in use a,b=b,a

if __name__=='__main__':
    a,b=map(int,input("Enter two number").split(','))
    print(swap_two_variable(a,b))