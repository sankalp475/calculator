#!/usr/bin/python3
# Calcutator TR Sürümü LinuxUsersLinuxMint tarafından Çevirisi yapılmıştır.
from inputdtr import *
while True:
    print("Çıkış yapmak için n tuşuna tıklayınız.s") # LinuxUsersLinuxMint tarafından düzeltilmiştir.
    op = input("Operator seçiniz?'(+ , - , * , /, %)'\n")
    # input operator from user
    if op == 'n':
        break  
    if op == '+':
        top()
    elif op == '-':
        cık()
    elif op == '*':
        carp() 
    elif op == '/':
        bol()
    elif op == '%': # LinuxUsersLinuxMint tarafından düzenlenmiştir.
        yuzde()
    else:
        print("Geçersiz Numara")
    print("Python calcutator'u kullandığınız için teşekkür ederim\n")
    print("Çevirisi LinuxUsersLinuxMint tarafından yapılmıştır.")
    print("\n")