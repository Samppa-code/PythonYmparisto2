# Otetaan käyttöön modulin saniteetti.py toiminnot
import saniteetti

# Funktio bmi laskemiseksi
def bmi(paino, pituus):
    painoindeksi = paino / (pituus * pituus)
    return painoindeksi

# Funkitio rasvaprosentin laskemiseksi
def rasvaprosentti(bmi, ika, sukupuoli):

    rprosentti = (1.2 * bmi) + (0.23 * ika) - (10.8 * sukupuoli) - 5.4
    return rprosentti


# Kysytään käyttäjältä tarvittavat tiedod
# Huom. Näppäimmistöltä saadaan aina merkkijono (string)
paino_str = input("Anna painosi kilogrammoina: ")
paino = saniteetti.on_jarkeva(paino_str, 20, 200)
pituus_str = input("Anna pituutesi metreinä: ")
ika_str = input("Kuinka vanha olet: ")
sukupuoli_str = input("Paina 1 jos olet mies, 0 jos olet nainen: ")

# Muutetaan merkkijonot liukuluvuiksi

tapahtui_virhe = False

try:
    if paino_str.isalpha():
        raise TypeError("Vain numerot ja desimaalipilkku on sallittu")
    paino = float(paino_str)

except Exception as virhe:
    print(virhe)
    tapahtui_virhe = True

try:
    pituus = float(pituus_str)
except:
    print("Pituus virheellinen")
    tapahtui_virhe = True

try:
    ika = float(ika_str)
except:
    print("Ikä virheellinen")
    tapahtui_virhe = True

try:
    sukupuoli = float(sukupuoli_str)
except:
    print("Sukupuoli virheellinen, syötä vain 1 tai 0")
    tapahtui_virhe = True

if tapahtui_virhe == False:
    painoindeksi = bmi(paino, pituus)
    print("Painoindeksi on: ", painoindeksi)
    rprosentti = rasvaprosentti(painoindeksi, ika, sukupuoli)
    print("Rasvaprosentti on: ", rprosentti)
else:
    print("Ei voitu laskea, jokin tieto virheellinen")
