# Pytanie 34 - napisz fragment kodu, w którym zobrazujesz użycie słowa kluczowego assert.
# Wyjaśnij jaka jest rola testów jednostkowych i czym charakteryzuje się dobry test jednostkowy.

def dodawanie(a,b):                       # definicja funkcji dodającej dwie wartości
    return a + b

def test_dodawanie_intow():               # funkcja testująca funkcję dodawanie
    assert dodawanie(2,3) == 5            # sprawdzenie czy funkcja dodawanie dla wartości 2 i 3 zwróci 5

def test_dodawanie_stringow():            # inna funkcja testująca funkcję dodawanie
    assert dodawanie('a', 'b') == 'abc'   # sprawdzenie czy funkcja dodawanie dla wartości 'a' i 'b' zwróci 'ab'

# pytest    - framework do uruchamiania testów, którego używaliśmy w tym filmie.
# aby o zainstalowac nalezy w linii komend wpisać "pip install pytest"
# aby uruchomić testy wpisujemy: pytest nazwa_pliku.py

# unittest - moduł biblioteki standardowej służący do uruchamiania testów, działa podobnie jak pytest
