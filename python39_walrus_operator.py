# Do czego służy i jak działa walrus operator
# :=

# if bez walrusa 
text = "To jest jakiś przykładowy tekst"
length = len(text)
if length > 10:
    print(f"Tekst ma {length} znaków")


# if z walrusem 
text = "To jest jakiś przykładowy tekst"
if (length := len(text)) > 10:
    print(f"Tekst ma {length} znaków")


# błąd bez nawiasów 
text = "To jest jakiś przykładowy tekst"
if length := len(text) > 10:
    print(f"Wartość length: {length}")
    # length = True (!)


# pętla while bez walrusa 
line = input("Podaj komendę (quit aby zakończyć): ")
while line != "quit":
    print(f"Wykonuję: {line}")
    line = input("Podaj komendę (quit aby zakończyć): ")


# pętla while z walrusem
while (line := input("Podaj komendę (quit aby zakończyć): ")) != "quit":
    print(f"Wykonuję: {line}")


# list comprehension bez walrusa
def process(x):
    """Symulacja kosztownej operacji."""
    print(f"  Przetwarzam {x}...")
    return x ** 2 + x

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Funkcja wywołana DWA RAZY na element!
results = [process(n) for n in numbers if process(n) > 20]
print(f"Wyniki: {results}")


# list comprehension z walrusem
results = [value for n in numbers if (value := process(n)) > 20]
print(f"Wyniki: {results}")
