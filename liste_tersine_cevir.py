def tersine_cevir(liste):
    ters_liste = []
    for eleman in liste[::-1]:  # Listeyi tersten geziyoruz
        if isinstance(eleman, list):  # Eleman bir liste mi?
            ters_liste.append(eleman[::-1])  # Evet ise, elemanı da tersine çevirip ekle
        else:
            ters_liste.append(eleman)  # Liste değilse doğrudan ekle
    return ters_liste

# Örnek kullanım:
girdi = [[1, 2], [3, 4], [5, 6, 7]]
cikti = tersine_cevir(girdi)
print(cikti)  