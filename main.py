import random as randd

cevaplar = ["Taş","Kağıt","Makas"]

yzCevap = cevaplar[randd.randint(0,2)]

print("""
#########################
#                       #
# Taş Kağıt Makas Oyunu #
#                       #
#########################
#                       #
# Made by s0ulfly;      #
#                       #
#########################
#                       #
# {} [1]               #
# {} [2]             #
# {} [3]             #
#                       #
#########################
""".format(cevaplar[0],cevaplar[1],cevaplar[2]))
def tasKagitMakas():
    print("Seçim yapınız: [1][2][3]")

    oyuncu = False
    while oyuncu == False:
        oyuncuCevap = int(input())
        if oyuncuCevap == 1:
            oyuncuCevap = cevaplar[0]
            oyuncu=True
        elif oyuncuCevap == 2:
            oyuncuCevap = cevaplar[1]
            oyuncu = True
        elif oyuncuCevap == 3:
            oyuncuCevap = cevaplar[2]
            oyuncu = True
        else:
            print("Hatalı giriş! Lütfen 1, 2 veya 3 rakamlarından birini giriniz: ")
            oyuncu = False



    if oyuncuCevap == yzCevap:
        print("Berabere! Yapayzekanın cevabı:",yzCevap,"Oyuncunun cevabı:",oyuncuCevap)
    elif oyuncuCevap == cevaplar[0]:
        if yzCevap == cevaplar[1]:
            print("Yapayzeka kazandı! Yapayzekanın cevabı:",yzCevap,"Oyuncunun cevabı:",oyuncuCevap)        
        else:
            print("Oyuncu kazandı! Yapayzekanın cevabı:",yzCevap,"Oyuncunun cevabı:",oyuncuCevap)         
    elif oyuncuCevap == cevaplar[1]:
        if yzCevap == cevaplar[0]:
            print("Oyuncu kazandı! Yapayzekanın cevabı:",yzCevap,"Oyuncunun cevabı:",oyuncuCevap)       
        else:
            print("Yapayzeka kazandı! Yapayzekanın cevabı:",yzCevap,"Oyuncunun cevabı:",oyuncuCevap)       
    elif oyuncuCevap == cevaplar[2]:
        if yzCevap == cevaplar[1]:
            print("Oyuncu kazandı! Yapayzekanın cevabı:",yzCevap,"Oyuncunun cevabı:",oyuncuCevap)       
        else:
            print("Yapayzeka kazandı! Yapayzekanın cevabı:",yzCevap,"Oyuncunun cevabı:",oyuncuCevap)
tasKagitMakas()   
while True:
    print("Tekrar oynamak ister misiniz?")
    yndn = str(input("Y/N: "))
    if yndn == "Y" or yndn == "y":
        yzCevap = cevaplar[randd.randint(0,2)]
        tasKagitMakas()
    elif yndn == "N" or yndn == "n":
        print("Görüşürüz!")
        break
    else:
        print("Hatalı giriş tekrar deneyiniz!")
