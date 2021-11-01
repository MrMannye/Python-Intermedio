from functools import reduce

# FUNCION PARA FILTRAR SOLO LOS NUMERO IMPARES DE UNA LISTA
def function_filter():
    my_list = [1,2,3,4,5,6,8,15,21]
    new_list = list(filter(lambda x: x%2 != 0,my_list))
    print(new_list)

# FUNCION PARA RECORRER TODA LA LISTA Y ELEVAR AL CUADRADO CADA ELEMENTO
def function_map():
    my_list = [1,2,3,4,5]
    new_list = list(map(lambda x: x**2,my_list))
    print(new_list)

def function_reduce():
    my_list = [2,2,2,2,2]
    all_multiplied = reduce(lambda a,b: a*b, my_list)
    print(all_multiplied)


if __name__ == "__main__":
    function_map()
    function_filter()
    function_reduce()