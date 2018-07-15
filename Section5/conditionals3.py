#Conditionals Exercise 3

def is_triangle():
    a = int(input("Select first number: "))
    b = int(input("Select second number: "))
    c = int(input("Select third number: "))
    if (a > b + c) or (b > c + a) or (c > a + b):
        print("No")
    else:
        print("Yes")

is_triangle()
