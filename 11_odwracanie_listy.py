# Pytanie 11 - na podstawie listy jezyki stworz listę jezyki_odwrocone
# zawierającą elementy listy jezyki w odwroconej kolejnosci

jezyki = ['Python', 'Java', 'C#', 'Ruby']

# 1
# jezyki.reverse()             # odwróć listę języki (nastąpi nadpisanie wcześniejszej listy)
# jezyki_odwrocone = jezyki    # przypisz wartość listy języki do nowej zmiennej jezyki_odwrocone
# print(jezyki_odwrocone)      # wydrukuj liste jezyki_odwrocone

# 2
# jezyki_odwrocone = list(reversed(jezyki))  # stwórz listę na podstawie obiektu zawierającego odwrócone elementy listy języki i przypisz do języki_odwrócone
# print(jezyki_odwrocone)
# print(jezyki)

# 3
# jezyki_odwrocone = jezyki[::-1]            # do zmiennej jezyki_odwrocone przypisz wartosci listy jezyki odczytane od tyłu
# print(jezyki_odwrocone)

# 4
jezyki_odwrocone = []                  # stworz pusta liste jezyki_odwrocone
for jezyk in jezyki:                   # dla kolejnego jezyka w liscie jezyki
    jezyki_odwrocone.insert(0,jezyk)   # umiesc ten jezyk na indeksie zerowym listy jezyki_odwrocone
print(jezyki_odwrocone)
