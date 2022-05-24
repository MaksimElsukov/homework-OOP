
from ast import If
from os import rename

cook_book = {}

def function_cooking_book(cook_book = {}):
    # cook_book = {}
    with open('recipes.txt', encoding='utf-8') as file_r:
        for line in file_r:     
            dish = line.strip()     
            if dish != "":
                number_of_ingredients = int(file_r.readline())  
            else: 
                continue    
            ingredients = []    
            for ingredient in range(number_of_ingredients): 
                ingredients.append(file_r.readline().strip().split('|'))    
            dictionary_of_ingredients = [] 
            for ingredient in ingredients:  
                d_of_ingr = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}  
                dictionary_of_ingredients.append(d_of_ingr)
                cook_book.update({dish: dictionary_of_ingredients}) 
    # print(cook_book)   

function_cooking_book(cook_book)

print(cook_book)

def function_shop_list_by_dishes(dishes =[], person = 1):
    shop_list = {} # Список покупок
    dishes_in = [] # Список ингр для блюд
    if len(dishes) == 0 : 
        print("Список блюд пуст!")
        return
    else:
        for dish in dishes:
            ingredients = cook_book.get(dish)
            if ingredients == None:
                print(f'Блюдо [{dish}] не найдено в кулинарной книге! q(0_0)p')
                return
            else:

                dishes_in.append(ingredients)
                for current_dish in dishes_in:
                    for ingridient in current_dish:
                        ingridient_name = ingridient['ingredient_name']
                        if shop_list.get(ingridient_name) == None:
                            shop_list[ingridient_name] = {'measure': ingridient['measure'],'quantity': ingridient['quantity']*person}
                        else:
                            change_ingr = shop_list[ingridient_name]
                            change_ingr.update({'quantity' : change_ingr['quantity'] + ingridient['quantity']})
                dishes_in.clear()
   
    print(shop_list)


function_shop_list_by_dishes(["Омлет", "Фахитос"], 2)    
    
    
    