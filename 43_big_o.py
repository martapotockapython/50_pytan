# Pytanie 43 - uszereguj podane złożoności obliczeniowe algorytmów od
# najlepszej do najgorszej:

# O(1) -          sprawdzenie czy element jest w słowniku (tablicy hashującej)
# O(log(n)) -     wyszukiwanie binarne
# O(n) -          jednokrotne przejrzenie listy o długości n
# O(n * log(n)) - (wydajne) sortowanie (timsort, quicksort)
# O(n**2) -       mnożenie każdego z każdym z elementów na liście
# O(2**n) -       Fibonacci rekurencyjnie

import math       # poniższy kod wyświetla wykres przedstawiający porównanie różnych złożoności obliczeniowych
                  # przy użyciu popularnej bibliteki matplotlib
import matplotlib.pyplot as plt

seria0 = [1] * 10
seria1 = list(range(1,11))
seria2 = [math.log(x) for x in seria1]
seria3 = [math.log(x) * x for x in seria1]
seria4 = [x**2 for x in seria1]
seria5 = [2**x for x in seria1]

plt.plot(seria0, label="O(1)")
plt.plot(seria2, label="O(log(n))")
plt.plot(seria1, label="O(n)")
plt.plot(seria3, label="O(n * log(n))")
plt.plot(seria4, label="O(n**2)")
plt.plot(seria5, label="O(2**n)")

plt.legend()
plt.show()
