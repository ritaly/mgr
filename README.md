Mapa regionów podatnych na niealleliczną rekombinację alleliczną u Arabidopsis thaliana  
  
**Ustawienie parametrów**  
* odległości między regionami flankującymi
  * min: 10tys
  * max 30/40tys  
* długość fragmentów: 1000, przesunięcie: 500
* procent podobieństwa: > 95%
* odcinek o wysokiej homologii wewnętrznej?
* inicjowane przeskoki?

#### 1. Przygotowanie danych   
PrepareTestData.py
Wycięcie znanego CNV wraz z rejonem flankującym na podstawie Zmienko et al. BMC Genomics (2016) 17:893

![Region CNV](/notatki/region.jpg)


fragment - Chr3:6'300'000-6'400'000  
  
#### 2. Przygotowanie plików o długości 1000 z przesunięciem o 500  
Divide.py  
Pliki o sekwencjach długości po 1000nt --> do znalezienia % podobieństwa między nimi


