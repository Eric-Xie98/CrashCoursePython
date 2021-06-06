

def make_pizza(size, *toppings):
    print("Making a " + str(size) + " inch large pizza with these toppings:")

    for topping in toppings:
        print(topping.title())

