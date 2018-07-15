#This program traverses a series of prefixes
#And adds a suffix to them.

def abecadarian():
    index = 0
    prefix = "JKLMNOPQ"
    suffix = "ack"
    letters = prefix[0]

    for letters in prefix:
        if letters == "O" or letters == "Q":
            print(letters + "u" + suffix)
        else:
            print(letters + suffix)

abecadarian()
