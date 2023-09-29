#!/usr/bin/python3
from inputd import *
while True:
    print("use n for exit") # Fixed by LinuxUsersLinuxMint
    op = input("choose the operator?'(+ , - , * , /, %)'\n") # Edited by LinuxUsersLinuxMint
    # input operator from user
    if op == 'n':
        break
    if op == '+':
        addition()
    elif op == '-':
        subraction()
    elif op == '*':
        multiplication()   
    elif op == '/':
        division()
    elif op == '%': # Edited by LinuxUsersLinuxMint
        Percentage()
    else:
        print("invalid number")
    print("thanks for using python calculator")
    print("\n")