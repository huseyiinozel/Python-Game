from cgi import print_form
import msvcrt as m
import time
import os

def wait():
    m.getch()

def sayi (b):
    
    c = list(range(b+1))
    return c

print("Oyunumuza hosgeldiniz\nHazirsaniz kurallarımizi okumak icin lutfen bir tusa basiniz.")
wait()
while True:
    print("""Kurallar
    1: Önce oyunun hangi sayiya kadar oynanacaği belirlenir
    2: Daha sonra her oyuncu kendi tutuğu sayiyi yazar
    3: Oyun basladiği zaman sira ile herkes birer tahminde bulunur
    4: Kendi sayisi söylenen oyuncu oyundan cikar ve sona kalan oyuncu kaybeder""")
    print("""Kurallari anladiysaniz oyuna geçmek için 1 e basiniz.Kuralalri tekrar okumak için
    başka herhangi bir tusa basabilirsiniz""")
    a=input("Yapmak istediğiniz islem :")
    if a == "1":
        os.system("cls")
        break

    

print("Hangi sayiya kadar oynamak istiyorsunuz ? (Minimum 21)")
sayi2 = int(input("Sayi :"))
liste = list(range(1,sayi2+1))
print("Oyun hazirlaniyor ")
#time.sleep(1)
print("Oyunu kac oyuncu oynamak istiyorsunuz ?")
oyuncu=int(input("Oyuncu sayisi:"))
oyuncular=list(range(1,oyuncu+1))

#time.sleep(1)
print("Oyun hazirlaniyor...")
#time.sleep(1)
print("Oyunumuz hazir.Baslamak icin herhangi bir tusa basiniz...")
wait()
os.system('cls')
oyuncusayisi=list()
oyuncuad=list()
y=0
while True:
    while y<oyuncu:
        print("{}. oyuncu ismini girsin :".format(y+1))
        isim =input("isminiz:")
        oyuncuad.append(isim)
        y+=1
        os.system("cls")



    z = 0
    
    while z<oyuncu:
        print("Secebileceginiz sayilar :")
        print(liste)
        print("{}. oyuncu tuttugu sayiyi girsin.".format(oyuncuad[z]))
        a = int(input("Sayi:"))
        os.system("cls")
        oyuncusayisi.append(a)
        z+=1
        #time.sleep(1)
        
    break
#time.sleep(1)
v = 0
while len(oyuncusayisi)!=1:

    print("{}. oyuncu tahminini girsin:" .format(oyuncuad[v]))
    print("Soyleyebilecegi sayilar :")
    print(liste)
    gir =int(input("sayi:"))
    index =liste.index(gir)
    liste.pop(index)
    os.system("cls")

    
    for i in oyuncusayisi:
        if i == gir:
            h= oyuncusayisi.index(gir)


            print("{} sayisini {}. oyuncu tutmustu. {}. oyuncu oyundan cikabilirsiniz".format(gir,oyuncuad[h],oyuncuad[h]))

            oyuncusayisi.pop(h)
            print("devam etmek icin bir tusa basiniz")

            wait()
            
            os.system("cls")

            break
            

    v+=1

    if v == len(oyuncusayisi):
        v = 0
    
   print("try")
