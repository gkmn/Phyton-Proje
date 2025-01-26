
def duzlestir(liste):
    duz_liste = []
    for eleman in liste:
        if isinstance(eleman, list):  
            duz_liste.extend(duzlestir(eleman)) 
        else:
            duz_liste.append(eleman)  
    return duz_liste

# Örnek kullanım:
    
input = [
    [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    ]

for girdi in input:
    cikti = duzlestir(girdi)    
    print(f"Girdi: {girdi}")
    print(f"Çıktı: {cikti}")
    print("-" * 20) 