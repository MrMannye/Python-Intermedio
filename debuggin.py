def divisors(numero):
    divisions = [i for i in range(1,numero+1) if numero % i == 0]
    return divisions

def run():
    pass


if __name__ == '__main__':
    run()
    numero = int(input("INGRESE UN NUMERO: "))
    print(divisors(numero))

# PARA CORRER EL DEBUGGER EN VSCODE, EN LA BARRA IZQUIERDA APARECE UN ELEMENTO DE RUN AN DEBUG
# DONDE PODEMOS IR EJECUTANDO PASO A PASO EL CODIGO DE PYTHON Y CHECAR LAS VARIABLES COMO ASI 
# EL FUNCIONAMIENTO CORRECTO DEL MISMO 

# PARA ELLO, AL MOMENTO DE EJECUTAR EL DEBUG NECESITAMOS DAR PAUSE E IR CON LA FUNCION PASO A PASO