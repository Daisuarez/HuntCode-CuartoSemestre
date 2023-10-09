# Bool contiene los números de True False
#Los tips numericos, es falso para el 0(cero), true para los demás valores

valor = 0.0
resultado = bool(valor)
print(f'valor: {valor}, resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}, resultado: {resultado}')


#Tipo string -> False '', True para lo dems valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor: {valor}, resultado: {resultado}')

# Tipo  colecciones -> false para coleccciones vacia
# TIpo colecciones -> True para todas las demás

# Lista
valor = []
resultado = bool(valor)
print(f'valor de una lista vacia: {valor}, resultado: {resultado}')

valor = [2,3,4]
resultado = bool(valor)
print(f'valor una lista con elementoos: {valor}, resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'valor de una tupla vacia: {valor}, resultado: {resultado}')

valor = (5,)
resultado = bool(valor)
print(f'valor de una tupla con elementos: {valor}, resultado: {resultado}')

#Diccionario
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio: {valor}, resultado: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado = bool(valor)
print(f'valor de un diccionario con elementos: {valor}, resultado: {resultado}')

# Sentencia de control con bool
if bool ('hola'): # cómo se puede usar el factor bool o sólo strg
    print('Regresa verdadero')
else:
    print('Regresa falso')

# Ciclos
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')