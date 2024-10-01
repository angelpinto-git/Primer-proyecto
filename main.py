# Ejemplo con diccionarios
person = {
    'name': 'John Doe',
    'age': 30,
    'emails': ['john.doe@gmail.com'],
    'profession': 'Fullstack Developer',
}

for key, value in person.items():
    print(f'{key} -> {value}')