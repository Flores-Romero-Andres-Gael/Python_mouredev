# TUPLAS

"""my_other_tuple = (1, 2, 3, 4, 5)
my_tuple = tuple()

print(my_other_tuple)

my_tuple = (1, "Hello", 3.4, True, "World")

my_sum_tuple= my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[2:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Changed value"
my_tuple.insert(1, "New value")
print(my_tuple)
my_tuple = tuple(my_tuple)
print(type(my_tuple))"""

my_tuple = (10, 20, 30 ,40 ,50)
print(my_tuple)
my_tuple2 = (100, 200, 300, 400, 500)
print(my_tuple2[2])
my_tuple3 = (1, 2, 3, 3, 4, 3, 5, 8, 3, 3, 3, 1 ,2 ,3, 9, 3)
print(my_tuple3.count(3))

my_tuple4 = ("Java", "C++", "JavaScript", "Python", "Java", "C#", "Python")
print(my_tuple4.index("Python"))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)   

sub_tuple = my_tuple[2:4]
print(sub_tuple)

tuple4 = ("Rojo", "Verde", "Azul")
print(type(tuple4), tuple4)
tuple4 = list(tuple4)
print(type(tuple4), tuple4)
tuple4[2] = "Amarillo"
tuple4 = tuple(tuple4)
print(type(tuple4), tuple4)

only = (100, )
print(only)