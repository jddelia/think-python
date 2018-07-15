#Conditionals Exercises

import time

int(time.time() % 60)
int(time.time() % 3600 // 60)
int(time.time() % 86400 // 3600 - 4)
int(time.time() // 86400)

def clock():
    print("\tThe time is", str(int(time.time() % 86400 // 3600 - 4)) + ":" + str(int(time.time() % 3600 // 60)) + ":" + str(int(time.time() % 60)) + " EST")
    print()
    print("\t", "It has been", int(time.time() // 86400), "days since the begining of epoch time.")

clock()
