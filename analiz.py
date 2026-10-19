import csv

toplam = {}
with open("satis.csv", encoding="utf-8") as f:
    for satir in csv.DictReader(f):
        tutar = int(satir["adet"]) * int(satir["fiyat"])
        toplam[satir["urun"]] = toplam.get(satir["urun"], 0) + tutar

for urun, tutar in toplam.items():
    print(urun, tutar, "TL")
