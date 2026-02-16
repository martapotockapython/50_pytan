# podstawowa składnia match-case
def handle_command(command):
    match command:
        case "start":
            return "Uruchamiam serwer"
        case "stop":
            return "Zatrzymuję serwer"
        case "restart":
            return "Restartuję serwer"
        case _:
            return f"Nieznana komenda: {command}"

print(handle_command("start"))
print(handle_command("stop"))
print(handle_command("halo"))


# to samo z if/elif 
def handle_command(command):
    if command == "start":
        return "Uruchamiam serwer"
    elif command == "stop":
        return "Zatrzymuję serwer"
    elif command == "restart":
        return "Restartuję serwer"
    else:
        return f"Nieznana komenda: {command}"


# === Przykład 3: operator OR we wzorcach ===
def check_status(code):
    match code:
        case 200 | 201:
            return "Sukces"
        case 301 | 302:
            return "Przekierowanie"
        case 404:
            return "Nie znaleziono"
        case 500 | 502 | 503:
            return "Błąd serwera"
        case _:
            return f"Inny kod: {code}"

print(check_status(200))
print(check_status(404))
print(check_status(999))


# dopasowywanie tupli
def describe_point(point):
    match point:
        case (0, 0):
            return "Początek układu współrzędnych"
        case (0, y):
            return f"Na osi Y: y={y}"
        case (x, 0):
            return f"Na osi X: x={x}"
        case (x, y):
            return f"Punkt: x={x}, y={y}"

print(describe_point((0, 0)))
print(describe_point((0, 5)))
print(describe_point((3, 7)))


# guard clause
def classify_number(number):
    match number:
        case n if n < 0:
            return f"{n} jest ujemna"
        case 0:
            return "Zero"
        case n if n % 2 == 0:
            return f"{n} jest parzysta"
        case n:
            return f"{n} jest nieparzysta"

print(classify_number(-5))
print(classify_number(4))
print(classify_number(7))
