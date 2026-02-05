# Strings

my_new_string = "Hello, World!"
print(my_new_string)

# Formateo

name, surname, age = "Gael", "Flores", 22
print("Mi nombre es {} {} y mi edad {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad %d" % (name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad {age}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)

# División
language_slice = language[0:6:2]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)
print("EJERCICIO")
print("Hola Python"[0:4])

# Funciones
print("FUNCIONES")
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print("language".isnumeric())
print("124".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.upper().startswith("PY"))