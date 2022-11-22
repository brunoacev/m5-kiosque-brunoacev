import statistics
from collections import Counter
from menu import products

__name__ == "product_handler"


def get_product_by_id(id: int):

    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if (id == product['_id']):
            return product
    return dict()


def get_products_by_type(productType: str):

    if (type(productType) != str):
        raise TypeError("product type must be a str")
    result = list()
    for product in products:
        if (productType == product['type']):
            result.append(product)
    return result


def menu_report():
    contagem_de_produtos = len(products)

    prices_list = []
    types_list = [str]
    all_types = []

    for product in products:
        prices_list.append(product["price"])

        if types_list.count(product["type"]) == 0:
            types_list.append(product["type"])
            all_types.append(product["type"])

        tipo_mais_comum = [str]
        qtd_tipo_mais_comum = 0
        preco_medio = statistics.mean(prices_list)

    for type in types_list:
        if all_types.count(type) > qtd_tipo_mais_comum:
            qtd_tipo_mais_comum = all_types.count(type)
            tipo_mais_comum.clear()
            tipo_mais_comum.append(type)

    return f'Products Count: {contagem_de_produtos} - Average Price: {f"${round(preco_medio, 2)}"} - Most Common Type: {tipo_mais_comum[0]}'


def add_product(menu: list, **args):

    new_id = 0
    for product in menu:
        if product["_id"] > new_id:
            new_id = product["_id"]
    new_id = new_id + 1
    new_product = {"_id": new_id, **args}
    menu.append(new_product)

    return new_product
