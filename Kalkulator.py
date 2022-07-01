#!/bin/user/python

# module
import os,sys,time,subprocess

# menu
def perkalian(a,b):
    return a*b
def pembagian(a,b):
    return a/b
def pertambahan(a,b):
    return a+b
def pengurangan(a,b):
    return a-b

# daftar
os.system("clear")
os.system("figlet Kalkulator")
print("      By: MasLucknut_2")
print("————————————————————————————————")
print("1). Perkalian")
print("2). Pembagian")
print("3). Pertambaha")
print("4). Pengurangan")
print("————————————————————————————————")
mull=input("masukin pilihannya banh ~>> ")

gas1 = int(input("angka pertama ~>> "))
gas2 = int(input("angka kedua ~>> "))

# masukin data
if mull =="1":
   print(gas1,"*",gas2,"=",perkalian(gas1,gas2))
if mull =="2":
   print(gas1,"/",gas2,"=",pembagian(gas1,gas2))
if mull =="3":
   print(gas1,"+",gas2,"=",pertambahan(gas1,gas2))
if mull =="4":
   print(gas1,"-",gas2,"=",pengurangan(gas1,gas2))