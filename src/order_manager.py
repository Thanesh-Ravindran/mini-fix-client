# src/order_manager.py
# manage and track orders with methods to add, retrieve, find by ID,
# update status, and cancel orders in a list


class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order_id, instrument, side, order_type, price, quantity):
        order = {
            "order_id": order_id,
            "instrument": instrument,
            "side": side,
            "order_type": order_type,
            "price": price,
            "quantity": quantity,
            "status": "NEW",  # initial order status
        }
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def find_order_by_id(self, order_id):
        for order in self.orders:
            if order["order_id"] == order_id:
                return order
        return None

    def update_order_status(self, order_id, new_status):
        order = self.find_order_by_id(order_id)
        if order:
            order["status"] = new_status

    def cancel_order(self, order_id):
        order = self.find_order_by_id(order_id)
        if order:
            order["status"] = "CANCELLED"
