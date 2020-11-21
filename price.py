#def discounted(price, discount):
#    price = abs(float(price))
#    discount = abs(float(discount))
#    if discount >= 100:
#        price_with_discount = price
#    else:
#        price_with_discount = price - (price * discount / 100)
#    print(price_with_discount)
#
#
#price1 = 100
#discounted1 = 10
#print(discounted(price1, discounted1))



#def get_sum(one, two, delimiter='&'):
#    one = str(one).upper()
#    two = str(two).upper()
#    one_and_two = f'{one}{delimiter}{two}'
#    print(one_and_two)
#
#
#one1 = input('певрое значение')
#two1 = input('втооре значение')
#print(get_sum(one1, two1))

def format_price(price):
    price = int(price)
    price_str = f'Цена: {price} рублей'
    return price_str
    returned_price = price_str


price1 = input('Цена')
print(returned_price)