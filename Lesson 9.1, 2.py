from pprint import pprint

cook_book = {}

with open('cook_book.txt', encoding='utf-8') as f:
    f.seek(0, 2)
    f_len = f.tell()
    f.seek(0)
    while f.tell() < f_len:
        dish = f.readline().strip()
        ingr_count = int(f.readline().strip())
        cook_book[dish] = []
        for counter in range(ingr_count):
            ingr_dict = {}
            ingr_list = f.readline().strip().split(sep=' | ')
            ingr_dict['ingredient_name'] = ingr_list[0]
            ingr_dict['quantity'] = int(ingr_list[1])
            ingr_dict['measure'] = ingr_list[2]
            cook_book[dish].append(ingr_dict)
        f.readline().strip()


def get_shop_list_by_dishes(dishes_list, person_count):
    ingredients_for_buy = {}
    for dish_name in dishes_list:
        if dish_name in cook_book:
            for ingr in cook_book[dish_name]:
                if not ingr['ingredient_name'] in ingredients_for_buy:
                    ingr['quantity'] *= person_count
                    ingredients_for_buy[ingr.pop('ingredient_name')] = ingr
                else:
                    ingr['quantity'] *= person_count
                    ingr['quantity'] += ingredients_for_buy[ingr['ingredient_name']]['quantity']
                    ingredients_for_buy[ingr.pop('ingredient_name')] = ingr
    return ingredients_for_buy


# pprint(cook_book, width=100)
# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
