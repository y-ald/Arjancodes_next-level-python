# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Calculate total prices and filter orders
# Use generator expressions to calculate the total prices for each sales order and filter
# orders with a total price greater than $100.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from dataclasses import dataclass
from decimal import Decimal

from typing import Generator


@dataclass
class Order:
    product: str
    quantity: int
    price: Decimal


def calculate_total_price(quantity: int, price: Decimal) -> Decimal:
    return quantity * price


def main() -> None:
    # List of sales orders
    sales_orders = [
        Order(product="A", quantity=5, price=Decimal("60.00")),
        Order(product="B", quantity=3, price=Decimal("15.00")),
        Order(product="C", quantity=2, price=Decimal("20.00")),
        Order(product="D", quantity=4, price=Decimal("45.00")),
    ]

    def price_generators(orders: list[Order]) -> Generator[Decimal, list[Order], None]:
        for order in orders:
            yield calculate_total_price(order.quantity, order.price)

    def price_generators_with_filter(orders: list[Order]) ->  Generator[Decimal, list[Order], None]:
        for price in price_generators(orders):
            if(price >= 100):
                yield price

    print([price for price in price_generators_with_filter(sales_orders)])

if __name__ == "__main__":
    main()
