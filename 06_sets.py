# Sets
# No es ordenado y no acepta repetidos
my_set = set()
my_other_set = {}
print(type(my_set)) 
print(type(my_other_set)) 

my_other_set = {"Gael", "Flores", 22}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Mexico")
print(my_other_set)

print("Gael" in my_other_set)
print("Argentina" in my_other_set)
print("Flores" not in my_other_set)

my_other_set.remove("Flores")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

my_set = {"Gael", "Flores", 22}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Mexico", "Argentina", "Colombia"}
union = my_set.union(my_other_set)
nuevo_set = {"Peru", "Chile"}
print(union.union(nuevo_set))

print(union.difference(my_set))

print(len({1, 2, 3, 4}))