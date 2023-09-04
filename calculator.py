#!/usr/bin/python3
# from functions import*

while True:
    print("use n for exit")
    op = input("choose the operator?'(+ , - , * , /, %)'\n")
    # input operator from user
    if op == 'n':
        break
    num1 = float(input("enter 1st number\n"))
    # input number 1 from user
    num2 = float(input("enter 2nd number\n"))
    # input number 2 from user
    
    def addition(num1,num2):
        result = num1 + num2
        print("{0} + {1} = {2}".format(num1,num2,result))
    def substraction(num1,num2):
        result = num1 - num2
        print("{0} - {1} = {2}".format(num1,num2,result))
    def multiplication(num1,num2):
        result = num1 * num2
        print("{0} * {1} = {2}".format(num1,num2,result))
    def division(num1,num2):
        if num2 == 0:
            print("cant divide by zero")
        else:
            result = num1 / num2
            print("{0} / {1} = {2}".format(num1,num2,result))
    def percentage(num1,num2):
        result = num1 % num2
        print("{0} % {1} = {2}". format(num1,num2,result))
            
    if op == '+':
        addition(num1,num2)
    elif op == '-':
        substraction(num1,num2)
    elif op == '*':
        multiplication(num1,num2)   
    elif op == '/':
        division(num1,num2)
    elif op == '%':
        percentage(num1,num2)
    else:
        print("invalid number")
    print("thanks for using python calculator")
    print("\n")
