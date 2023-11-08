# src/message_handler.py
# handle FIX messages and updating order status and statistics

import logging

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class MessageHandler:
    def handle_message(self, response, order_manager, stats):
        if response.startswith("35=8"):
            logging.info(f"Response (35=8): {response}")
            order_id = self.extract_field_value(response, "11")
            instrument = self.extract_field_value(response, "55")
            side = self.extract_field_value(response, "54")
            fill_price = float(self.extract_field_value(response, "44"))
            fill_quantity = int(self.extract_field_value(response, "38"))

            order = order_manager.find_order_by_id(order_id)
            if order:
                if fill_quantity > 0:
                    logging.info(f"Response (35=8), fill quantity: {fill_quantity}")
                    order_manager.update_order_status(order_id, "FILLED")
                    logging.info(
                        f"Order Status: {order_manager.update_order_status(order_id, 'FILLED')}"
                    )
                    stats.update_stats(
                        order, instrument, side, fill_price, fill_quantity
                    )
                    logging.info(
                        f"Stats: {stats.update_stats(order, instrument, side, fill_price, fill_quantity)}"
                    )

                    logging.info(f"Response (35=8), fill quantity: {fill_quantity}")
                elif fill_quantity == 0:
                    logging.info(f"Response (35=8), fill quantity: {fill_quantity}")
                    order_manager.update_order_status(order_id, "CANCELED")
                    logging.info(
                        f"Order Status: {order_manager.update_order_status(order_id, 'CANCELED')}"
                    )
                else:
                    logging.info(
                        f"Response (35=8), invalid fill quantity: {fill_quantity}"
                    )
                    order_manager.update_order_status(order_id, "REJECTED")
                    logging.error(
                        f"Order Status: {order_manager.update_order_status(order_id, 'REJECTED')}"
                    )

        elif response.startswith("35=3"):
            logging.info(f"Response (35=3): {response}")
            order_id = self.extract_field_value(response, "11")
            order_manager.update_order_status(order_id, "REJECTED")
            logging.info(
                f"Order Status: {order_manager.update_order_status(order_id, 'REJECTED')}"
            )
        elif response.startswith("35=9"):
            logging.info(f"Response (35=9): {response}")
            order_id = self.extract_field_value(response, "11")
            order_manager.update_order_status(order_id, "CANCEL REJECTED")
            logging.info(
                f"Order Status: {order_manager.update_order_status(order_id, 'CANCEL REJECTED')}"
            )
        else:
            logging.error(f"Unknown Response: {response}")

    def extract_field_value(self, response, field_tag):
        field_tag = field_tag + "="
        start_index = response.find(field_tag)
        if start_index != -1:
            start_index += len(field_tag)
            end_index = response.find("|", start_index)
            if end_index != -1:
                return response[start_index:end_index]
        return ""
