import random
from random import choice
import pyperclip

low_harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
high_harfler = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
numbers = ["1","2","3","4","5","6","7","8","9","0"]
password = []

def lowHarfEkle():
    password.append(choice(low_harfler))
def highHarfEkle():
    password.append(choice(high_harfler))
def symbolEkle():
    password.append(choice(symbols))
def numbersEkle():
    password.append(choice(numbers))

def_list = [lowHarfEkle,highHarfEkle,symbolEkle,numbersEkle]
high_low_list = [lowHarfEkle,highHarfEkle]
list2 = [numbersEkle,lowHarfEkle,highHarfEkle]
list3 = [lowHarfEkle,highHarfEkle,symbolEkle]

basamak = int(input("Kaç Basamaklı Olsun?: "))
symbols_sor = str(input("Özel Semboller Olsun Mu? (y/n): "))
rakam_sor = str(input("Rakamlar Olsun mu? (y/n): "))

while not (symbols_sor == "y" or symbols_sor == "n"):
    print("Cevap yes veya no olmalı! (y/n)")
    symbols_sor = input("Özel Semboller Olsun Mu? (y/n): ")

while not(rakam_sor == "y" or rakam_sor == "n"):
    print("Cevap yes veya no olmalı! (y/n)")
    rakam_sor = input("Rakamlar Olsun mu? (y/n): ")

if symbols_sor == "y" and rakam_sor == "y":
    for _ in range(basamak):
        random.choice(def_list)()
        
if symbols_sor == "n" and rakam_sor == "n":
    for _ in range(basamak):
        random.choice(high_low_list)()

if symbols_sor == "y" and rakam_sor == "n":
    for _ in range(basamak):
        random.choice(list3)()
if symbols_sor == "n" and rakam_sor == "y":
    for _ in range(basamak):
        random.choice(list2)()

mypass ="".join(map(str,password))
print(mypass)
pyperclip.copy(mypass)

