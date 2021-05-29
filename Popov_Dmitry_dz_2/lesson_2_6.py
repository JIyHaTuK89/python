products = []
product_analytics = {"наименования" : [], "стоимости" : [], "количество" : [], "единицы исчисления" : [],}

new_products_amount = int(input("Введите количество товаров, которые необходимо добавить\nВнимание, рекомендуемое количество - 2: "))
counter = 1

# формируем список товаров и их описания
while new_products_amount:
    product_discription = {}
    product = input("Формат добавления: через пробел введите\nназвание, цена, количество, единицы исчисления: ").split()
    product_discription["название"] = product[0]
    product_discription["цена"] = int(product[1])
    product_discription["количество"] = int(product[2])
    product_discription["ед"] = product[3]
    new_block = (counter, product_discription)
    products.append(new_block)
    counter += 1
    new_products_amount -= 1

print("-" * 50)
print(products)

# формируем анализ товаров
for el in products:
    if not el[1]["название"] in product_analytics["наименования"]:
        product_analytics["наименования"].append(el[1]["название"])
    if not el[1]["цена"] in product_analytics["стоимости"]:
        product_analytics["стоимости"].append(el[1]["цена"])
    if not el[1]["количество"] in product_analytics["количество"]:
        product_analytics["количество"].append(el[1]["количество"])
    if not el[1]["ед"] in product_analytics["единицы исчисления"]:
        product_analytics["единицы исчисления"].append(el[1]["ед"])

print(product_analytics)



