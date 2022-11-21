import statistics
from collections import Counter
from menu import products

__name__ == "product_handler"


def get_product_by_id(id: int):

    try:
        if type(id) == int:
            for product in products:
                if (id == product['_id']):
                    return product
            return dict()
        raise TypeError

    except TypeError:
        return TypeError("product id must be an int")


def get_products_by_type(productType: str):

    try:
        if (type(productType) == str):
            result = list()
            for product in products:
                if (productType == product['type']):
                    result.append(product)
            return result
        raise TypeError

    except TypeError:
        return TypeError("product type must be a str")


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

    return f'Products Count: {contagem_de_produtos} - Average Price: {preco_medio} - Most Common Type: {tipo_mais_comum[0]}'


def add_product(menu: list, args):

    new_id = 0
    for product in menu:
        if product["_id"] > new_id:
            new_id = product["_id"]
    new_id = new_id + 1
    new_product = {"_id": new_id, **args}
    menu.append(new_product)

    return  new_product


def calculate_tab(table: list):
    id_list = []
    amount_list = []

    for row in table:
        id_list.append(row["_id"])
        amount_list.append(row["amount"])

    values_list = []

    for id in id_list:
        for product in products:
            if product["_id"] == id:
                values_list.append(product["price"])

    subtotal = f'$%.2f' % sum([a*b for a, b in zip(values_list, amount_list)])

    return {"subtotal": subtotal}
