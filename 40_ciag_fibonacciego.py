# Pytanie 40 - ciąg Fibonacciego to ciąg liczb, którego:
# - zerowy element wynosi 0
# - pierwszy element wynosi 1
# - każdy kolejny element jest sumą dwóch poprzedzających go elementów.
# Napisz funkcję, która zwróci n-ty element ciągu Fibonacciego.

# kolejny element ciągu: 0   1   2   3   4   5   6    7   8   9  10
# wartość dla elementu:  0   1   1   2   3   5   8   13  21  34  55

def fibonacci_l(n): # O(n)
    p, d = 0, 1              # inicjalizacja zmiennych p-pierwsza, d-druga
    for _ in range(n):       # _ - oznacza, że nie potrzebujemy zmiennej do przechowywania kolejnej wartości z range, chcemy tylko aby pętla wykonała się n razy
        p, d = d, p + d      # jednoczesne aktualizowanie zawartości zmiennych p i d, aby przypisać do nich wartości z poprzedniego obiegu pętli
    return p

print(fibonacci_l(8))


def fibonacci_r(n): # O(2 ^ n)
    if n <= 1:               # każda funkcja rekurencyjna musi mieć warunek, który powoduje returna bez kolejnego wywołania rekurencji
        return n             # tu tym warunkiem jest sytuacja gdy szukamy wartości dla zerowego lub pierwszego elementu ciągu Fibonacciego
    return fibonacci_r(n - 1) + fibonacci_r(n - 2)  # dla każdego elementu innego niż zerowy lub pierwszy, funkcja wywołuje samą siebie
                             # aby policzyć dwa poprzednie wyrazy ciągu i dodać je do siebie
print(fibonacci_r(10))
