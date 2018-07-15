#Program to test if word is a palindrome.


def palindrome():
    n = input("Type a word to see if it's a palindrome.\n")

    if n[::-1] == n[:]:
        print("Success!")
    else:
        print("This word isn't a palindrome.")

palindrome()
