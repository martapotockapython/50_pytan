# Pytanie 17 - znajdź różnicę między największą a najmniejszą wartością
# na poniższej liście.
# Zadbaj o to aby rozwiązanie było efektywne.

A = [4, 5, 7, -3, 2, 8, -10, 15]

# 1
A = sorted(A)            # O(N*log_N) # sorted(A) sortuje w miejscu listę A
print(A[-1] - A[0])                   # drukowanie różnicy między ostatnim, a pierwszym elementem posortowanej listy A

# 2
najmniejsza = A[0]                    # zmiennej najmniejsza przypisujemy wartość listy A od indeksu 0
najwieksza = A[0]                     # zmiennej największa przypisujemy wartość listy A od indeksu 0

for liczba in A:               # O(N) # dla liczby w liście A
    if liczba < najmniejsza:          # jeśli liczba jest mniejsza niż zmienna najmniejsza
        najmniejsza = liczba          # zmiennej najmniejsza przypisz wartość liczby
    elif liczba > najwieksza:         # jeśli liczba jest większa niż zmienna największa
        najwieksza = liczba           # zmiennej największa przypisz wartość liczby
print(najwieksza - najmniejsza)       # wydrukuj różnicę między zmienną największa a najmniejsza

# 3
print(max(A) - min(B))         # O(N) # max(A) - funkcja znajdująca największą wartość listy A
                                      # min(A) - funkcja znajdująca najmniejszą wartość listy A
