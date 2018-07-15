
def right_justify(s):
    print(" " * 65 + s)

right_justify('monty')

def print_spam():
    print('spam')

def do_twice(f, g):
    f(g)
    f(g)

def print_twice(yo):
    print(yo)
    print(yo)

do_twice(print_twice, 'spam')

def do_four(a, b):
    do_twice(a, b)
    do_twice(a, b)

do_four(print_twice, 'easy')

def quad(a):
    print_twice(a)
    print_twice(a)

sub = " -" * 4

def frame():
    print("+" + sub + "+" + sub + "+")


body = "/" + " " * 8 + "/" + " " * 8 + "/"

def grid1(a, b):
    a()
    quad(b)
    a()
    quad(b)
    a()

grid1(frame, body)
