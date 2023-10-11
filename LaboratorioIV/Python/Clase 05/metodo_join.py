


#help(str.join)


tupla_str=('Hola ','alumnos', 'Tecnicatura', 'universitaria')
mensaje = ' '.join(tupla_str)
print(f'Mensaje : {mensaje}')


lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ' , '.join(lista_cursos)
print(f'Mensaje : {mensaje}')


cadena = 'HolaMundo'
mensaje ='.'.join(cadena)
print(f'Mensaje : {mensaje}')

diccionario= {'Nombre': 'Roberto', 'Apellido': 'Pasto', 'Edad': 20}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}, Type: {type(llaves)}')
print(f'valores: {valores}, Type: {type(valores)}')










