def palindrome():
    count = 999999
    count2 = 10000
    cstring = str(count)

    while count > 99999:
        count -= 1
        cstring = str(count)
        if cstring[2:] == cstring[5:1:-1]:
            if str(count + 1)[1:] == str(count + 1)[5:0:-1]:
                if str(count + 2)[1:5] == str(count + 2)[4:0:-1]:
                    if str(count + 3)[:] == str(count + 3)[::-1]:
                        print(cstring)


palindrome()
