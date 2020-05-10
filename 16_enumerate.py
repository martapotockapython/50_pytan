# Pytanie 16 - wypisz podaną listę imion przed każdym dodając kolejny numer.
# Zacznij numerowanie od 1.

imiona = ['Adam', 'Stanisław', 'Maria', 'Zofia', 'Mikołaj']

num = 1                  # zmienna przechowująca wartość licznika
for imie in imiona:      # dla kolejnego imienia w liście imiona
    print(num, imie)     # wydrkuj licznik i imię
    num += 1             # zwiększ wartość licznika o 1


for num, imie in enumerate(imiona,1):
    print(num, imie)

# enumerate powoduje automatyczną aktualizację licznika dla kolejnego imienia w liście imiona
# parametr 1 informuje enumerate, aby zaczęła numerować od liczby 1
