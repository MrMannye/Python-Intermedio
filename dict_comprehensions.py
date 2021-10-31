# FUNCION PARA CREAR UNA DICCIONARIO CON LOS PRIMEROS 100 NUMEROS 
# AL CUADRADO Y SOLO SI NO DIVISIBLES ENTRE 3
def run(): 
    my_dict = {}
    for i in range(1,101):
        if i % 3 != 0:
            my_dict[i] = i**3

    print(my_dict)

# MISMA FUNCIONALIDAD DE LA FUNCION RUN() PERO CON DICT COMPREHENSIONS
# ES DECIR, CREAR EL MISMO ARREGLO PERO CON EL FOR Y LA CONDICION DENTRO
# DEL DICCIONARIO
def run2():
    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dict)


if __name__ == '__main__':
    run()
    run2()