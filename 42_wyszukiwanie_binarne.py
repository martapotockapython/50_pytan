# Pytanie 42 - przy użyciu wyszukiwania binarnego sprawdź
# czy liczba 341 znajduje się w posortowanej liście P

P = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]


szukana = 100        # zmienna przechowująca szukaną wartość
lewy = 0             # indeks lewy określający początek przeszukiwanego zakresu listy
prawy = len(P) - 1   # indeks prawy określający koniec przeszukiwanego zakresu listy
while lewy <= prawy: # dopóki indeks lewy jest mniejszy lub równy prawemu
    srodkowy = (lewy + prawy) // 2  # wyliczamy indeks srodkowy, jako średnią indeksów lewy i prawy (// - zwraca część całkowitą z dzielenia)
    if P[srodkowy] == szukana:  # jeśli lista od inseksu srodkowy zawiera szukaną wartość
        print(f"Liczba {szukana} znajduje się na liście.") # wypisz informację, że wartość znaleziono
        break        # i przerwij działanie pętli while
    elif P[srodkowy] < szukana:  # jeśli lista od indeksu srodkowy zawiera wartość mniejszą niż szukana
        lewy = srodkowy + 1      # przesuń indeks lewy na pozycję o jeden większą niz srodkowy
    else:                        # w przeciwnym wypadku (czyli jeśli lista od indeku srodkowy zawiera wartość większa niż szukana)
        prawy = srodkowy - 1     # przesuń indeks prawy na pozycję o jeden mniejszą niż srodkowy
else:                 # jeśli pętla while skończy się wykonywać, bo warunek w niej zawarty zwróci False, to wtedy uruchomi się ten else
    print(f"Liczby {szukana} nie ma na liście.")
