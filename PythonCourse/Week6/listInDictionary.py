# list in a dictionary
# store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
for topping in pizza['toppings']:
    print("\t" + topping)