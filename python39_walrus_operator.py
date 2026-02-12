# Do czego służy i jak działa walrus operator
# :=

# text = "przykładowy tekst"
# if (length := len(text)) > 10:
#     print(f"Długość tekstu to {length}")


# while (line := input("Podaj komendę (q dla wyjścia): ")) != 'q':
#     print(f"Wykonuję: {line}")

def process(x):
    # czasochłonna funkcja
    return x ** 2 + x

numbers = range(11)

results = [processed for n in numbers if (processed := process(n)) > 20]
print(results)
