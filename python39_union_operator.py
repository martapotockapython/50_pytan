# W jaki sposób połączysz dwa słowniki w jeden nowy,
# tak aby oryginalne wersje słowników pozostały niezmienione?

# === Przykład 1: łączenie słowników przez unpacking (stara metoda) ===
user_defaults = {"theme": "light", "language": "pl", "font_size": 14}
user_settings = {"theme": "dark", "font_size": 18}

merged = {**user_defaults, **user_settings}
print(merged)
# {'theme': 'dark', 'language': 'pl', 'font_size': 18}

print(user_defaults)
# {'theme': 'light', 'language': 'pl', 'font_size': 14}
print(user_settings)
# {'theme': 'dark', 'font_size': 18}


# === Przykład 2: update() modyfikuje oryginał ===
user_defaults = {"theme": "light", "language": "pl", "font_size": 14}
user_settings = {"theme": "dark", "font_size": 18}

user_defaults.update(user_settings)
print(user_defaults)
# {'theme': 'dark', 'language': 'pl', 'font_size': 18}


# === Przykład 3: operator | dla słowników (Python 3.9+) ===
user_defaults = {"theme": "light", "language": "pl", "font_size": 14}
user_settings = {"theme": "dark", "font_size": 18}

merged = user_defaults | user_settings
print(merged)
# {'theme': 'dark', 'language': 'pl', 'font_size': 18}

print(user_defaults)
# {'theme': 'light', 'language': 'pl', 'font_size': 14}
print(user_settings)
# {'theme': 'dark', 'font_size': 18}


# === Przykład 4: operator |= (in-place) ===
user_defaults = {"theme": "light", "language": "pl", "font_size": 14}
user_settings = {"theme": "dark", "font_size": 18}

user_defaults |= user_settings
print(user_defaults)
# {'theme': 'dark', 'language': 'pl', 'font_size': 18}


# === Przykład 5: zestawienie starych i nowych metod ===
# TWORZENIE NOWEGO SŁOWNIKA (oryginały bez zmian):
# Stare: merged = {**d1, **d2}
# Nowe:  merged = d1 | d2

# MODYFIKACJA W MIEJSCU (oryginał zmieniony):
# Stare: d1.update(d2)
# Nowe:  d1 |= d2


# === Przykład 6: operator | dla setów ===
backend = {"Python", "Java", "Go"}
frontend = {"JavaScript", "TypeScript", "Python"}

all_languages = backend | frontend
print(all_languages)
# {'Python', 'Java', 'Go', 'JavaScript', 'TypeScript'}

backend |= frontend
print(backend)
# {'Python', 'Java', 'Go', 'JavaScript', 'TypeScript'}
