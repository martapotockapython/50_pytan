# Pytanie 27
# Objętość graniastosłupa oblicza się na podstawie wzoru: V = a * b * h
# a i b to długości boków jego podstawy, a h to wysokość.
# Poniższy kod znajduje największy graniastosłup jaki możemy utworzyć
# z elementów list A, B i H.
# Ile operacji zostane wykonane w wyniku uruchomienia tego kodu?
# W jaki sposób można by to zadanie rozwiązać bardziej efektywnie?

import random                                     # biblioteka random służy do generowania liczb losowych

A = [random.randint(0,100) for i in range(5)]     # tworzenie pięcioelementowej listy losowych integerów z zakresu od 0 do 100
B = [random.randint(0,100) for i in range(5)]
H = [random.randint(0,100) for i in range(5)]

max_v = 0                                         # zmienna do przechowywania maksymalnej znalezionej objętości graniastosłupa
for a in A:                                       # dla każdego elementu w liście A
    for b in B:                                   # dla każdego elementu w liście B
        for h in H:                               # dla każdego elementu w liście H
            if a * b * h > max_v: # 125 operacji  # jeśli a*b*h jest większe niż maksymalna znaleziona objętość
                max_v = a * b * h                 # do zmiennej max_v przypisz wynik mnożenia a*b*h
print(max_v)


print(max(A) * max(B) * max(H)) # 15 operacji     # pomnóż przez siebie największe elementy list A, B i H

# uproszczenie zagnieżdzonych pętli for możliwe przy użyciu biblioteki itertools
# więcej w materiałach dodatkowych
