from menu import products

__name__ == "tab_handler"


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

    subtotal = sum([a*b for a, b in zip(values_list, amount_list)])
    subsubtt = round(subtotal, 2)

    return {"subtotal": f'${subsubtt}'}
