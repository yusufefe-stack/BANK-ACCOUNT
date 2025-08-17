# banka hesap uygulaması


def hesap_oluşturma(hesap_sahibi):
    return {"hesap_sahibi": hesap_sahibi, "bakiye": 0}

def para_yatırma(hesap, miktar):
    if miktar > 0:
        hesap["bakiye"] += miktar
        print(f"Hesabınıza {miktar} TL yatırıldı. Güncel bakiye: {hesap['bakiye']} TL")
    else:
        print("Para yatırma miktarı pozitif olmalıdır.")

def para_çekme(hesap, miktar):
    if miktar > 0:
        if hesap["bakiye"] >= miktar:
            hesap["bakiye"] -= miktar
            print(f"Hesabınızdan {miktar} TL çekildi. Güncel bakiye: {hesap['bakiye']} TL")
        else:
            print("Yetersiz bakiye.")
    else:
        print("Para miktarı pozitif olmalıdır.")

def bakiye_görüntüleme(hesap):
    print(f"{hesap['hesap_sahibi']} adlı hesabın bakiyesi: {hesap['bakiye']} TL")

print("Banka uygulamamıza hoşgeldiniz")
hesap_sahibi = input("Hesap sahibinin adı: ")
hesap = hesap_oluşturma(hesap_sahibi)

while True:
    print("\nSeçenekler:")
    print("1. Para Yatırma")
    print("2. Para Çekme")
    print("3. Bakiye Görüntüleme")
    print("4. Çıkış")

    seçiniz = int(input("1-4 arasında bir rakam seçiniz: "))

    if seçiniz == 1:
        miktar = float(input("Yatırmak istediğiniz tutarı giriniz: "))
        para_yatırma(hesap, miktar)
    elif seçiniz == 2:
        miktar = float(input("Çekmek istediğiniz tutarı giriniz: "))
        para_çekme(hesap, miktar)
    elif seçiniz == 3:
        bakiye_görüntüleme(hesap)
    elif seçiniz == 4:
        print("İyi günler dileriz!")
        break
    else:
        print("Yanlış seçim, tekrar deneyiniz.")
