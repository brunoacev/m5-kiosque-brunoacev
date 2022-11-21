from menu import products
from managments.products_handle import get_product_by_id, get_products_by_type, menu_report, add_product, calculate_tab


if __name__ == "__main__":
    # Seus prints de teste aqui
    ...
    # res_product_by_id = get_product_by_id(32)
    # print(res_product_by_id)

    # res_products_by_type = get_products_by_type("fruit")
    # print(res_products_by_type)

    # res_menu_report = menu_report()
    # print(res_menu_report)

    # product = {
    #   "title": "Suco de Limão",
    #   "price": 3.0,
    #   "rating": 5,
    #   "description": "Suco de limão",
    #   "type": "drink"
    # }
    # res_add_product = add_product(products, product)
    # print(res_add_product)

    table_1 = [{"_id": 7, "amount": 5}, {"_id": 2, "amount": 5}]
    res_calculate_tab = calculate_tab(table_1)
    print(res_calculate_tab)
