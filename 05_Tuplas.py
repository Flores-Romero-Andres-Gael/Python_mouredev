# TUPLAS

my_other_tuple = (1, 2, 3, 4, 5)
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
print(type(my_tuple))