# Compound rule of three

# 10 cranes can carry 200 boxes on a ship in 18 days of 8 working hours.
# How many boxes will be carried in 15 days by 6 cranes working 6 hours
# per day?

'''
    author: Vanderlei
    inspired in Ferretto's method on youtube:
    https://www.youtube.com/watch?v=NVLx8lWGeDE

    Python version: python 3.6
    
'''

from functools import reduce


def boxes_qty(values, product):    

    new_values = invert_products(values, product)    
    
    value = [reduce(lambda x, y: x*y, new_values[0]),
             reduce(lambda x, y: x*y, new_values[1])]        
    
    return max(value) / min(value)


def invert_products(lists, product):

    product_0 = 1
    product_1 = 1
    new_lists = [[],[]]
    
    if lists[1][product] is 'x':
        product_1 = lists[0][product]        
    else:
        product_0 = lists[1][product]
        product_1 = lists[0][product]

    for x, y in lists[1].items():
        if y == 'x':
            lists[1][x] = 1
    
    new_lists[0] = [y for x, y in lists[0].items() if x is not product]
    new_lists[1] = [y for x, y in lists[1].items() if x is not product]
    new_lists[0].append(product_0)
    new_lists[1].append(product_1)
    
    return new_lists
    



values = [{'cranes': 10, 'boxes': 200, 'days': 18, 'hours': 8},
          {'cranes': 6, 'boxes': 'x', 'days': 15, 'hours': 6}]

product = 'boxes'

print(boxes_qty(values, product))
