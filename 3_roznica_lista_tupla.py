# Pytanie 3 - napisz kod, który zaprezentuje najważniejsze różnice między listą a tuplą

L = [1, 2, 3, True, (1, 2)]          # lista zawierająca różne typy danych, w tym tuplę
T = (4, 5, 6, False, ['x', 'y'])     # tupla zawierająca różne typy danych, w tym listę
# listę zapisujemy w nawiasach kwadratowych [], a tuplę w nawiasach okrągłych ()

L[2] = 'trzy'                        # modyfikacja zawartości listy - operacja legalna
print(L)

T[2] = 'sześć'  # próba modyfikacji zawartości tupli - operacja zabroniona, skutkuje TypeError
