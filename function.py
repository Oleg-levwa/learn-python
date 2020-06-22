one = 'Learn '
two = ' python'
def get_summ (one, two, delimiter = '&'):
    result = str(one + delimiter + two)
    return result.upper()
summ = get_summ (one, two, delimiter = '&')
print (summ)

price = 56.24
def format_price (price):
    price = int(price)
    return f'Цена: {price} руб.'
result_price = format_price (price)
print (result_price)

