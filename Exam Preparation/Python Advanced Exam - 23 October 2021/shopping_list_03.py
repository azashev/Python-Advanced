def shopping_list(leva, **keywords):
    if leva < 100:
        return "You do not have enough budget."
    basket = set()
    result = ''
    for product, value in keywords.items():
        product_price = value[0] * value[1]
        if product_price <= leva:
            if product not in basket and len(basket) == 5:
                break
            leva -= product_price
            basket.add(product)
            result += f"You bought {product} for {product_price:.2f} leva.\n"

    return result
