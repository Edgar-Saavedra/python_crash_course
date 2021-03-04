# pseudo code:
# 3 strings x
# put strings in list, use for loop to print names
# lists = ARRAYS
# array is a collection of same DATA TYPE
# you cant have strings number etc
fave_pizzas = [
  'pepperoni',
  'cheese',
  'hot-wing-sauce'
]

# for current_item in fave_pizzas:
#   print(current_item)
  # print(f"----- {current_item}")
  # print("End of ITEM IN LOOP")

# fave_pizza_lists = [
#   [
#     'pepperoni',
#     'cheese'
#   ],
#   [
#     'emilianos fave',
#     'charlies fave'
#   ],
#   [
#     'anchovies'
#   ]
# ]

# for characters in 'my string':
#   print(f"current char - {characters}")

# for list_item in fave_pizzas:
#   print("Printing out the list")
#   for item in list_item:
#     print(f"list item -- {item}")
    


# 4-1. Pizzas: Think of at least three kinds of your favorite pizza . 
#   Store these pizza names in a list, and then use a for loop to print the name of each pizza .

# • Modify your for loop to print a sentence using the name of the 
#   pizza instead of printing just the name of the pizza . 
#   For each pizza you should have 
#   one line of output containing a simple statement like I like pepperoni pizza .

# make list
favePizzas = ['cheese', 'peperoni','sausage']
# loop over list and add in sentence
for pizza in favePizzas: 
  print(f"{pizza.title()}, is my favorite pizza!")

# • Add a line at the end of your program, outside the for loop, 
#   that states how much you like pizza .
#   The output should consist of three or more lines about the kinds of 
#   pizza you like and then an additional sentence, such as I really love pizza!
print("This pizza was delicious!")


# 4-2. Animals: Think of at least three different animals that have a common 
#   char- acteristic . Store the names of these animals in a list, and then use 
#   a for loop to print out the name of each animal .
# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in common . You could print a sentence such as Any of these animals would make a great pet!
felines = ['cat', 'lion', 'tiger']
for cats in felines:
  print(cats)

