# przypomnienie podstaw f-stringów
name = "Marta"
role = "developer"

# Stary sposób — .format()
print("Cześć, {}! Jesteś {}.".format(name, role))

# F-string (od Python 3.6)
print(f"Cześć, {name}! Jesteś {role}.")


# te same cudzysłowy (Python 3.12+)
user = {"name": "Marta", "role": "developer"}

# Przed Python 3.12 — trzeba było używać INNYCH cudzysłowów:
print(f"Użytkownik: {user['name']}")

# Od Python 3.12 — te same cudzysłowy działają:
print(f"Użytkownik: {user["name"]}")


# backslashe wewnątrz f-stringów (Python 3.12+)
owoce = ["jabłko", "gruszka", "śliwka"]

# Przed Python 3.12 — obejście z dodatkową zmienną:
separator = '\n'
print(f"Lista:\n{separator.join(owoce)}")

# Od Python 3.12 — backslash działa bezpośrednio:
print(f"Lista:\n{'\n'.join(owoce)}")


# zagnieżdżone f-stringi (Python 3.12+)
user_name = "Marta"
message = f"Witaj, {f'{user_name}' if user_name else 'nieznajomy'}!"
print(message)
# Witaj, Marta!

user_name = ""
message = f"Witaj, {f'{user_name}' if user_name else 'nieznajomy'}!"
print(message)
# Witaj, nieznajomy!
