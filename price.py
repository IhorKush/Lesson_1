def discounted(price, discount, max_discounted=40):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discounted = abs(float(max_discounted))
    if max_discounted > 99:
        raise ValueError('The discount cannot be more than 99%')
    if discount >= max_discounted:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount


print(discounted(100, 20, 30))
