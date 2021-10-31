def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstName": "Miguel", "lastName": "Aguilera"}

    super_list = [
        {
        "firstName": "Miguel", 
        "lastName": "Aguilera"
        },
        {
        "firstName": "Facundo", 
        "lastName": "Sanchez"
        },
        {
        "firstName": "Jessica", 
        "lastName": "Hernandez"
        },
        {
        "firstName": "Arleth", 
        "lastName": "Carrasco"
        },
        {
        "firstName": "Pedro", 
        "lastName": "Suarez"
        }
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    for key,value in super_dict.items():
        print(f"{key}-{value}")

    for i in super_list:
        print(f"{i['firstName']} - {i['lastName']}")


if __name__ == '__main__':
    run()