from pprint import pprint

def make_dict(file: str) -> dict:
    result: dict = dict()

    with open(file, encoding = 'cp1251') as file:
        for line in file:
            dish = line.strip()
            dish_quantity = int(file.readline())
            ingredients_list = []
            for ingredients in range(dish_quantity):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredients_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
                )
            result[dish] = ingredients_list
            file.readline()
    return result

def get_shop_list_by_dishes(dishes, person_count):
    item_list = {}
    for dish in dishes:
        ingredients = cook_book.get(dish)
        for ingredient in ingredients:
            ingredient_name = ingredient.get('ingredient_name')
            measure = ingredient.get('measure')
            if ingredient_name not in item_list:
                quantity = ingredient.get('quantity')
                item_list[ingredient_name] = {'measure': measure, 'quantity': int(quantity) * person_count}
            else:
                quantity = int(ingredient.get('quantity')) * person_count + int(item_list.get(ingredient_name).get('quantity'))
                item_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return item_list

cook_book = make_dict('recipes.txt')

shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)

print(cook_book)
pprint(shop_list)






