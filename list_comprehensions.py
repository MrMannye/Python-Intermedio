# FUNCION PARA CREAR UNA LISTA CON LOS PRIMEROS 100 NUMEROS 
# AL CUADRADO Y SOLO SI NO DIVISIBLES ENTRE 3
def run(): 
    squares = []
    for i in range(1,101):
        if i % 3 != 0:
            squares.append(i**2)

    print(squares)

# MISMA FUNCIONALIDAD DE LA FUNCION RUN() PERO CON LIST COMPREHENSIONS
# ES DECIR, CREAR EL MISMO ARREGLO PERO CON EL FOR Y LA CONDICION DENTRO
# DEL ARREGLO
def run2():
    arreglo = [i**2 for i in range(1,101) if i % 3 != 0]
    print(arreglo)


if __name__ == '__main__':
    run()
    run2()