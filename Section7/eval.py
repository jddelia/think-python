#A program to test the eval function.

def eval_loop():
    try:
        while True:
            a = input('''Enter something here, or type "done"
to stop evaluating: ''')
            if a == "done":
                break
            print(eval(a))
    except NameError:
        print(str(a))
eval_loop()
