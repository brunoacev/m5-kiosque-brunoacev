from menu import products
from management.product_handler import get_product_by_id, get_products_by_type, menu_report, add_product
from management.tab_handler import calculate_tab


if __name__ == "__main__":
    # Seus prints de teste aqui
    ...
    get_product_by_id()
    get_products_by_type()
    menu_report()

    new_product = {

        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    add_product()
    calculate_tab()
