requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers")
    else:
        print(f"adding {requested_topping}")
print("\nYour Pizza is Done!")