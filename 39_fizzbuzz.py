# Pytanie 39 - napisz program, który dla kolejnych liczb z zakresu od 1 do n:
# wypisze: "Fizz" - jeśli liczba będzie podzielna przez 3
# wypisze: "Buzz" - jeśli liczba będzie podzielna przez 5
# wypisze: "FizzBuzz" - jeśli liczba będzie podzielna przez 3 i 5
# jeśli nie zajdzie żaden z tych przypadków, to wypisz po prostu liczbę.
# Zadanie to znane jest pod nazwą: FizzBuzz.

def fizzbuzz(n):
    for num in range(1, n+1):   # range do n+1 bo chcemy wypisać liczby do n włącznie
        if num % 15 == 0:       # w tej wersji zadania ważna jest kolejność bloków if, elif, else
            print("FizzBuzz")   # gdybyśmy jako pierwsze sprawdzili podzielność przez 3 lub 5
        elif num % 3 == 0:      # to program nigdy nie sprawdziłby podzielności przez 3 ORAZ 5
            print("Fizz")       # a więc nigdy nie wydrukowałby FizzBuzz
        elif num % 5 == 0:      # zatem warunek podzielności przez 3 ORAZ 5 musi być sprawdzony jako pierwszy
            print("Buzz")
        else:
            print(num)

fizzbuzz(30)

def fizzbuzz(n):
    for num in range(1, n+1):
        wynik = ''              # w każdym obiegu pętli tworzymy pusty string do przechowywania wyniku
        if num % 3 == 0:
            wynik += "Fizz"     # wynik = wynik + "Fizz"
        if num % 5 == 0:
            wynik += "Buzz"
        if num % 3 != 0 and num % 5 != 0:
            wynik = str(num)    # jeśli liczba nie jest podzielna ani przez 3 ani przez 5
        print(wynik)            # to do zmiennej wynik dodajemy stringa utworzonego z tej liczby

fizzbuzz(30)
