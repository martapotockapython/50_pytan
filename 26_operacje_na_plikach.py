# Pytanie 26
# - stwórz plik o nazwie "moj_plik.txt"
# - wpisz do niego liczb od 1 do 100, każdą w nowej linijce
# - otwórz plik i zapisz jego zawartosc do listy z_pliku

with open('moj_plik.txt', 'w') as f:    # otwórz plik 'mój_plik.txt' w wersji do zapisu ('w' od write), nadaj mu alias f
    for n in range(1, 101):             # dla kolejnych liczb z zakresu od 1 do 100
        f.write(str(n) + '\n')          # wpisz do pliku stringa utworzonego na podstawie liczby oraz znak nowej linii '\n'

with open('moj_plik.txt', 'r') as f:    # otwórz plik 'mój_plik.txt' w wersji do odczytu ('r' od read), nadaj mu alias f
    z_pliku = f.readlines()             # do listy z_pliku wpisz kolejne linijki przeczytane z pliku 'moj_plik.txt'
                                        # każda linijka będzie osobnym elementem listy
print(z_pliku)
