# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que determine cual sería el apellido de una persona
si se ingresaran los dos nombres completos de sus padres.
Dicha persona deberá tener los apellidos de ambos padres

- Primero el programa debe consultar el nombre completo del padre_1
- Luego el programa debe consultar el nombre completo del padre_2
- Luego debe consultar el nombre del hijo/a
- Debe extraer los apellidos de los padres
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres
  y el nombre ingresado de dicha persona
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejo por su cuenta a que busquen un poco más acerca de este método
que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

Cualquier duda con el método split pueden consultarla por el campus
'''
'''
print('Jugando con texto')
# Empezar aquí la resolución del ejercicio
print("Ingrese el nombre  de tu madre")
madre= str(input())
print("Ingrese el apellido  de tu madre")
madre_apellido= str(input())
print("Ingrese el nombre  de tu padre")
padre= str(input())
print("Ingrese el apellido  de tu padre")
padre_apellido= str(input())
print("Ingrese tu nombre")
hijo= str(input())


print("el hombre completo es", hijo,"" + madre_apellido, padre_apellido )'''


#usando split
print('usando split')

print("Ingrese el nombre completo de tu madre")
madre= str(input())

print("Ingrese el nombre completo  de tu padre")
padre= str(input())

print("Ingresa tu nombre completo")
hijo= str(input())


nombre, apellido=madre.split()
nombre1, apellido2=padre.split()
nombre2, apellido3 = hijo.split()

print( nombre2, apellido, apellido2)
