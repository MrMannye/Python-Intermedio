
from dict_comprehensions import run


def run():
    string = input("INGRESE SU PALABRA: ")
    palindromo = lambda string : string == string[::-1]
    if palindromo(string) == True: 
        print("SU PALABRA ES UN PALINDROMO")
    else: 
        print("SU PALABRA NO ES UN PALINDROMO")




if __name__ == "__main__":
    run()
