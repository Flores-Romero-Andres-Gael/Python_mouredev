# Listas

"""my_list = [10, 20, 30, 40, 50]
my_other_list = list()

print(len(my_list))

my_other_list = [10, 20, 30, 40, 50]
print(my_other_list)
print(len(my_other_list))

my_new_list = ["Start", 10, 20.5, "Hello", True, 30, 30, "Python", "Pepe", "Hello", 15, 24.358, "End"]
print(my_new_list)
print(type(my_new_list))

print(my_new_list[0])
print(my_new_list[1])
print(my_new_list[-1])
print(my_new_list[-5])
print (my_new_list.count("Hello"))  

my_datos_list = ["Gael", 22, 1.75, "Mexico", "Spanish"]

name, age, height, country, language = my_datos_list
print(name)

print(my_datos_list + my_new_list)

my_datos_list.append("Romero")
print(my_datos_list)

my_datos_list.insert(5, "Flores")
print(my_datos_list)

my_datos_list.remove("Spanish")
print(my_datos_list)

my_new_list.remove(30)
print(my_new_list)

print(my_new_list.pop(2))
print(my_new_list)

my_pop_list = my_new_list.pop(0)
print(my_pop_list)
print(my_new_list)  

print(my_datos_list)
my_datos_list[5] = "Gonzalez"
print(my_datos_list)

my_data = ['Andres', 'Gael', 'Flores', 'Romero', 22, 1.75, 'Mexico', 'Spanish']
my_datos_list = my_data.copy()
print(my_datos_list)

my_datos_list.reverse()
print(my_datos_list)

print(my_list)
print(my_list[1:4])
my_list_ejemplo = [3,1,2]
my_list_ejemplo.sort()
print(my_list_ejemplo)"""

"""my_list = "Hola Python"
print(my_list)"""

_list = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print(list2[2])

_list.append(6)
print(_list)

list2.insert(2, 15)
print(list2)

list2.insert(3, 30)
print(list2)
list2.remove(30)
print(list2)

delete = _list.pop(5)
print(_list)
a = delete
print(a)

list3 = [100, 200, 300, 400, 500]
print(list3)
list3.reverse()
print(list3)

list4 = [3, 4, 6, 8, 1, 0, 2, 5, 9, 7]
print(list4)
list4.sort()
print(list4)

list5 = [1, 2, 3, 4, 5]
list6 = [6, 7, 8, 9, 10]

list_new = list5 + list6
print(list_new)

my_sublist = list2[0:4]
print(list2)
print(my_sublist)