def bmi(paino,pituus):
    painoindeksi = paino / (pituus * pituus)
    return painoindeksi

#Testataan toiminta
oma_bmi = bmi(73,1.71)

print ("Hoh-hoijaa taas on lihottu , painoindeksi on ", oma_bmi)

try:
    print(x)
except:
    print ("Something went wrong")
finally:
    print("")