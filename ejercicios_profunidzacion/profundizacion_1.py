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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''


# Empezar aquí la resolución del ejercicio
print("bienvenido/a a la calculadora")
print("Ingrese un numero")
valor1 = int(input())
print("Ingrese un segundo numero")
valor2 = int(input())
# Suma
Suma= valor1 + valor1
print("La suma de", valor1, "y", valor2, "es",Suma)
# Resta
Resta= valor1- valor2
print("La resta de", valor1, "y", valor2, "es",Resta)
#Multiplicación
Multiplicacion= valor1 * valor2
print("La multiplicación de", valor1, "y", valor2, "es",Multiplicacion)
#Division
Division= valor1 / valor2
print("La división de", valor1, "y", valor2, "es",Division)
#Potencia
Potencia= valor1 ** valor2
print("La potencia de", valor1, "y", valor2, "es",Potencia)