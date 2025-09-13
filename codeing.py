def fuc1(a):
    print("goodaday," + a)
    return "done"
a = fuc1("Rajnish")
print(a)
#Recursion
def factorial(a):
    if( a == 0 or a==1):
        return 1
    return a * factorial(a-1)
a =  int(input("Enter a number: "))
print("the factorial of :" ,factorial(a))
factorial(a)

