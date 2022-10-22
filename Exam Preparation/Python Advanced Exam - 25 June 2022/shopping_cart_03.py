def shopping_cart(*args):
    shopping_cart = ''
    meals_and_products = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }

    max_products_per_meal = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    empty_cart = True

    for pair in args:
        if pair == "Stop":
            break

        meal = pair[0]
        product = pair[1]

        if meal not in meals_and_products:
            meals_and_products[meal] = [product]
        else:
            if product not in meals_and_products[meal]:
                if len(meals_and_products[meal]) < max_products_per_meal[meal]:
                    meals_and_products[meal].append(product)

    for meal in meals_and_products.items():
        if len(meal[1]) > 0:
            empty_cart = False

    if empty_cart:
        return "No products in the cart!"

    sorted_meals_with_products = sorted(meals_and_products.items(), key=lambda x: (-len(x[1]), x[0]))

    for meals_with_products in sorted_meals_with_products:
        meal = meals_with_products[0]
        products = sorted(meals_with_products[1])

        shopping_cart += f"{meal}:\n"

        for product in products:
            shopping_cart += f" - {product}\n"


    return shopping_cart


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))








