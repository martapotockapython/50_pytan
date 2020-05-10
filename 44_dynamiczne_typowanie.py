# Pytanie 45 - co to znaczy, że Python językiem dynamicznie typowanym?

a = 5            # tu zmienna a jest typu int
print(type(a))
a = "pięć"       # tu zmienna a jest typu str
print(type(a))
a = [1,2,3]      # a tu zmienna a jest typu List
print(type(a))

from typing import List   # aby używać type hints należy zainstalować i zaimportować bibliotekę typing

def przeliteruj(word: str) -> List[str]:  # definicja funkcji, która pobiera argument typu string i zwraca listę stringów
    return 5

print(przeliteruj(1))

# mypy - program, który pozwala analizować kod Pythona pod kątem poprawności przy założeniu statycznego typowania
# aby go użyć należy w konsoli wpisać: mypy nazwa_pliku_ktory_chcemy_przeanalizoac.pys
