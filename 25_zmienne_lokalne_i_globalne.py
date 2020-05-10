# Pytanie 25 - co zostanie wypisane w wyniku wykonania poniższego kodu?

x = 10             # zmienna globalna

def f():
    global x       # słowo global informuje Pythona, że poprzez zmienną x będziemy odnosić się do zmiennej globalnej
    x = 111        # zmiana wartości przypisanej do zmiennej globalnej
    y = 12         # zmienna lokalna (przestaje istnieć po zakończeniu wykonywania funkcji)
    print(x, y)

f()                # uruchomienie funkcji wydrukuje zmienną globalną x i zmienna lokalną y
print(x)           # drukuje zmienną globalną x
