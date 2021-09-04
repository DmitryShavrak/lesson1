def format_price(price):
    price = int(price)
    result = f"Цена: {price} руб."
    return result

res = format_price(56.24)
print(res)