#!/usr/bin/python3
# Calcutator TR Sürümü LinuxUsersLinuxMint tarafından Çevirisi yapılmıştır.

while True:
    print("Çıkış yapmak için n tuşuna tıklayınız.s") # LinuxUsersLinuxMint tarafından düzeltilmiştir.
    op = input("Operator seçiniz?'(+ , - , * , /, %)'\n")
    # input operator from user
    if op == 'n':
        break
    num1 = float(input("1. sayiyi giriniz:\n"))
    # input number 1 from user
    num2 = float(input("2. sayiyi giriniz:\n"))
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
            print("0 sayısına bölünemez")
        else:
            result = num1 / num2
            print("{0} / {1} = {2}".format(num1,num2,result))
    def percentage(num1,num2): # LİnuxUsersLinuxMint taradından düzenlenmiştir.
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
    elif op == '%': # LinuxUsersLinuxMint tarafından düzenlenmiştir.
        percentage(num1,num2)
    else:
        print("Geçersiz Numara")
    print("Python calcutator'u kullandığınız için teşekkür ederim\n")
    print("Çevirisi LinuxUsersLinuxMint tarafından yapılmıştır.")
    print("\n")
