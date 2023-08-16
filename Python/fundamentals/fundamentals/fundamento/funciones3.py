# 1 Actualizar valores
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)  # [[5, 2, 3], [15, 8, 9]]

estudiantes = [{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}]
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)  # [{'first_name': 'Michael', 'last_name': 'Bryant'}, {'first_name': 'John', 'last_name': 'Rosales'}]

directorio_deportes = {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'fútbol': ['Messi', 'Ronaldo', 'Rooney']}
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)  # {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'fútbol': ['Andrés', 'Ronaldo', 'Rooney']}

z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)  # [{'x': 10, 'y': 30}]


# 2 iterar
def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"{key} - {value}")

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(estudiantes)
# Salida:
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3 valor de listas
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', estudiantes)
# Salida:
# Michael
# John
# Mark
# KB

iterateDictionary2('last_name', estudiantes)
# Salida:
# Jordan
# Rosales
# Guillen
# Tonel

# 4 iterar un diccionario
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{key}: {len(value)}")
        for item in value:
            print(item)

some_dict = {
    'clave1': [1, 2, 3],
    'clave2': ['a', 'b', 'c', 'd'],
    'clave3': [True, False]
}