#While loop to print variable "s", "n" amount of times.

def print_n():
    s = input("Enter a statement here: ")
    n = int(input("Now enter how many times you want it repeated: "))
    a = 0
    while a < n:
        print(s)
        a += 1

print_n()
