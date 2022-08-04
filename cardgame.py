from cgi import print_form
import msvcrt as m
import time
import os
from turtle import goto

def wait():
    m.getch()

def sayi (b):   
    c = list(range(b+1))
    return c

print("Oyunumuza hosgeldiniz\nHazirsaniz kurallarımizi okumak icin lutfen bir tusa basiniz.")
wait()
os.system("cls")
while True:
    print("""Kurallar
    1: Önce oyunun hangi sayiya kadar oynanacaği belirlenir
    2: Daha sonra her oyuncu kendi tutuğu sayiyi yazar
    3: Oyun basladiği zaman sira ile herkes birer tahminde bulunur
    4:Eger kendi tuttugunuz sayiyi girerseniz otomatik olarak kaybeden siz olursunuz
    5: Kendi sayisi söylenen oyuncu oyundan cikar ve sona kalan oyuncu kaybeder""")
    print("""Kurallari anladiysaniz oyuna geçmek için 1 i seçiniz basiniz.Kurallari tekrar okumak için
    başka herhangi bir tusa basabilirsiniz""")
    a=input("Yapmak istediğiniz islem :")
    if a == "1":
        os.system("cls")
        break
print("Hangi sayiya kadar oynamak istiyorsunuz ? (Minimum 21)")
while True:
    sayi2 = int(input("Sayi :"))
    if sayi2<21:
        print('lütfen 21 veya 21 den büyük bir sayi giriniz')
        sayi3=int(input("sayi : "))
        liste = list(range(1,sayi3+1))
        break
    else:
        liste = list(range(1,sayi2+1))
        break
print("Oyun hazirlaniyor ")
time.sleep(1)
while True:
    print("Oyunu kac oyuncu oynamak istiyorsunuz ?")
    oyuncu=int(input("Oyuncu sayisi:"))
    if oyuncu <2:
        print("Bu oyun en az 2 kisi ile oynanabilir")
        continue
    else:    
        oyuncular=list(range(1,oyuncu+1))
        time.sleep(1)
        print("Oyun hazirlaniyor...")
        time.sleep(1)
        print("Oyunumuz hazir.Baslamak icin herhangi bir tusa basiniz...")
        wait()
        os.system('cls')
        oyuncusayisi=list()
        oyuncuad=list()
        y=0
        break
while True:
    while y<oyuncu:
        print("{}. oyuncu ismini girsin :".format(y+1))
        isim =input("isminiz:")
        oyuncuad.append(isim)
        y+=1
        os.system("cls")
        time.sleep(0.5)
    z = 0   
    while z<oyuncu:
        print("Secebileceginiz sayilar :")
        print(liste)
        print("{}. oyuncu tuttugu sayiyi girsin.".format(oyuncuad[z]))
        a = int(input("Sayi:"))
        os.system("cls")
        oyuncusayisi.append(a)
        z+=1
        time.sleep(0.5)               
    break
v = 0
while len(oyuncusayisi)!=1: 
    print("\n {}. oyuncu tahminini girsin:" .format(oyuncuad[v]))
    print("Soyleyebilecegi sayilar :")
    print(liste)
    gir =int(input("sayi:"))
    if gir not in liste:
        print("Lutfen yukarıda gösterilen secebileceginiz sayilardan birini seciniz")
        continue
    index =liste.index(gir)
    liste.pop(index)
    os.system("cls")
    time.sleep(0.5) 
    for i in oyuncusayisi:
        if i == gir:
            h= oyuncusayisi.index(gir)
            e = oyuncusayisi[v]
            if e== gir:
                print("kendi tuttugunuz sayiyi girdiniz")
                print("Kaybeden sizsiniz.Gecmis olsun")
                exit()
            print("{} sayisini {}. oyuncu tutmustu. {}. oyuncu oyundan cikabilirsiniz".format(gir,oyuncuad[h],oyuncuad[h]))
            oyuncusayisi.pop(h)
            oyuncuad.pop(h)
            print("devam etmek icin bir tusa basiniz")
            wait()
            os.system("cls")   
            break          
    if v+1 == len(oyuncusayisi)  :
        v = 0
    else:
        k = len(oyuncusayisi) 
        if k<oyuncu:
            v+=1
        else:    
            print("Bu sayiyi kimse tutmamiş.Tahmin etmeye devam edin")
            v+=1      
print("Oyun bitmiştir kaybeden {} olmustur".format(oyuncuad[0]))
