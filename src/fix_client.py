# src/fix_client.py
# FixClient class for simulating a FIX protocol client to interact with a trading server
# run: establishes a connection to the server, sends orders, and handles responses
# create_logon_message: creates a FIX logon message for session initiation
# create_new_order_message: creates a FIX new order message
# generate_random_order: generates random order details for simulation
# inits OrderManager and MessageHandler for order tracking and processing


import socket
import time
import random
import logging

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

from src.order_manager import OrderManager
from src.message_handler import MessageHandler
from src.stats import Stats


class FixClient:
    def __init__(self, config):
        self.config = config
        self.sequence_number = 1
        self.order_manager = OrderManager()
        self.message_handler = MessageHandler()
        self.stats = Stats()

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                logging.info(
                    f"Connecting to server: {self.config['server_ip']} at port: {self.config['server_port']}"
                )
                s.connect((self.config["server_ip"], self.config["server_port"]))
                if s:
                    logging.info(
                        f"Connection to server: {self.config['server_ip']} at port: {self.config['server_port']} successful"
                    )

                logon_message = self.create_logon_message()
                s.send(logon_message.encode())
                response = s.recv(1024).decode()
                logging.info(f"Response: {response}")
                if "35=A" in response:
                    self.sequence_number = 1

                start_time = time.time()
                while time.time() - start_time < 300:  # within 5mins
                    if random.random() < 0.5:
                        (
                            order_id,
                            instrument,
                            side,
                            order_type,
                            price,
                            quantity,
                        ) = self.generate_random_order()
                        new_order_message = self.create_new_order_message(
                            order_id, instrument, side, order_type, price, quantity
                        )
                        s.send(new_order_message.encode())
                        self.order_manager.add_order(
                            order_id, instrument, side, order_type, price, quantity
                        )
                    else:
                        response = s.recv(1024).decode()
                        self.message_handler.handle_message(
                            response, self.order_manager, self.stats
                        )
        except Exception as e:
            logging.error(f"An error occurred while connecting to the server: {str(e)}")

    def create_logon_message(self):
        return f"8=FIX.4.2|35=A|49={self.config['sender_comp_id']}|56={self.config['target_comp_id']}|34=1|"

    def create_new_order_message(
        self, order_id, instrument, side, order_type, price, quantity
    ):
        return f"8=FIX.4.2|35=D|49={self.config['sender_comp_id']}|56={self.config['target_comp_id']}|11={order_id}|55={instrument}|54={side}|40={order_type}|44={price}|38={quantity}|"

    def generate_random_order(self):
        order_id = self.sequence_number
        self.sequence_number += 1
        instruments = ["MSFT", "AAPL", "BAC"]
        instrument = random.choice(instruments)
        side = random.choice(["BUY", "SELL", "SHORT"])
        order_type = random.choice(["LIMIT", "MARKET"])
        price = round(random.uniform(100, 200), 2)
        quantity = round(random.randint(10, 100), 0)
        return order_id, instrument, side, order_type, price, quantity
