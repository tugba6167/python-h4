sayilar = []
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

print(f"Sayılar: {sayilar}")
print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")
kelimeler = []
while True:
    kelime = input("Bir kelime girin (çıkmak için 'q'): ")
    if kelime.lower() == 'q':
        break
    kelimeler.append(kelime)

kelimeler.reverse()
print(f"Ters sıralanmış kelimeler: {kelimeler}")
liste = [1, 2, 2, 3, 4, 4, 5]
yeni_liste = []

for eleman in liste:
    if eleman not in yeni_liste:
        yeni_liste.append(eleman)

print(f"Tekrarsız liste: {yeni_liste}")
liste = [1, 2, 2, 3, 4, 4, 5]
yeni_liste = list(set(liste))
print(f"Tekrarsız liste: {yeni_liste}")

