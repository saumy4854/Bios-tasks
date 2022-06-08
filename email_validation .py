import re

regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    email = input("Enter your email: ")
    check(email)