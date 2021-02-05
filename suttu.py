def bmi(paino,pituus):
    painoindeksi = paino / (pituus * pituus)
    return painoindeksi

#Testataan toiminta
oma_bmi = bmi(73,1.71)