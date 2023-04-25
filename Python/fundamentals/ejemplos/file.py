# print(type(2))	

# decimal = 2.1

# tupla = ()

# nombre="SEBASTIAN"

# print(type(tupla))
# print(type(nombre))
# print(type(decimal))

# # new_person = "TAPIA"
# # print(type(new_person))


#dic_vacío = {}
#new_person = {'name': 'John', 'edad': 38, 'peso': 160.2, 'usa_lentes': False}
#new_person['name'] = 'Jack'	# actualiza si la llave existe, agrega un par clave-valor si no
#new_person['hobbies'] = ['escalada', 'programación']
#print(new_person)	
# salida: {'name': 'Jack', 'edad': 38, 'peso: 160.2, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}
# w = new_person.pop('peso')	# remueve la llave indicada y devuelve el valor
# print(w)		# salida: 160.2
# print(new_person)	
# # salida: {'name': 'Jack', 'edad': 38, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}        

#int_to_float = float(35)
#float_to_int = int(44.2)
#int_to_complex = complex(35)
#print(int_to_float)
#print(float_to_int)
#print(int_to_complex)
#print(type(int_to_float))
#print(type(float_to_int))
#print(type(int_to_complex))


#print(100 + 42)			# salida: TypeError
#print("Hola " + str(42))		# salida: Hola 42


#total = 35
#user_val = "26"
#total = total + user_val		# salida: TypeError
#total = total + int(user_val)		# el total será 61


#first_name = "Zen"
#last_name = "Coder"
#age = 27
#print(f"Mi nombre is {first_name} {last_name} and tengo {age} años de edad.")


frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
ensalada = 3 * vegetales
print(ensalada)
