name_1 = input("Введите наименование первого товара: ")
price_1 = input("Введите цену первого товара: ")
value_1 = input("Введите количество первого товара: ")
um_1 = input("Введите единицы измерения первого товара: ")
product_1 = {"название": name_1, "цена": price_1, "количество": value_1, "eд": um_1}
name_2 = input("Введите наименование первого товара: ")
price_2 = input("Введите цену первого товара: ")
value_2 = input("Введите количество первого товара: ")
um_2 = input("Введите единицы измерения первого товара: ")
product_2 = {"название": name_2, "цена": price_2, "количество": value_2, "eд": um_2}
name_3 = input("Введите наименование первого товара: ")
price_3 = input("Введите цену первого товара: ")
value_3 = input("Введите количество первого товара: ")
um_3 = input("Введите единицы измерения первого товара: ")
product_3 = {"название": name_3, "цена": price_3, "количество": value_3, "eд": um_3}
tuple_of_products_1 = (1, product_1)
tuple_of_products_2 = (2, product_2)
tuple_of_products_3 = (3, product_3)
print(tuple_of_products_1)
print(tuple_of_products_2)
print(tuple_of_products_3)
products = {"название": name_1, "цена": price_1, "количество": value_1, "eд": um_1,
            "название": name_2, "цена": price_2, "количество": value_2, "eд": um_2
            "название": name_3, "цена": price_3, "количество": value_3, "eд": um_3}