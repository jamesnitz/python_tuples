# #tuples are immutable, may be nested, 
# and can contain mutable objects. IE:
# t = 12345, 54321, 'hello!'
# print(t[0])
# u = t, (1, 2, 3, 4, 5)
# empty = ()
# print(type(empty))

zoo = ("monkey", "pig", "chicken", "dog", "bigger dog")
(first_animal, second_animal, third_animal, fourth_animal, _fifth_animal) = zoo
# print(zoo.index("monkey"))
animal_to_find = "pig"
# search the tuple to see if it contains a particular value
if animal_to_find in zoo:
    print(f"{animal_to_find} is in the zoo")
else:
  print("nope not in this zoo!")


# convert the tuple into a list, add items to the list 
# then convert back to a tuple
zoo_list = list(zoo)
zoo_list.extend(["puppy", "horse", "penguin"])
zoo = tuple(zoo_list)
for animal in zoo:
  print(f"{animal} loves the zoo!")
