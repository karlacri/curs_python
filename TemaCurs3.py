# Suma parametrilor dintr-o functie nedefinita

def my_function(list_param):
    list_param.append(1)
my_list = [3, 8, 'xyz', ['test', 99, 100], -3, 2]
my_function(my_list)
print("Suma numerelor intregi si reale din lista: ", sum([i for i in my_list if isinstance(i, int) or isinstance(i, float)]))

# Verificare numar intreg

my_var = input("Introduceti un numar: "):
