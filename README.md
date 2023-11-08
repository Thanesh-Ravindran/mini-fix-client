# mini-fix-client

## Description
FIX Client: A Python-based Financial Information Exchange (FIX) Protocol Client.

##### 1. FixClient Class:

 - The FixClient class is the central component responsible for simulating a FIX protocol client.
 - It initiates a connection to the trading server, sends orders, and processes server responses.
 - The class includes methods for creating logon messages, new order messages, and generating random orders for simulation.
 - It maintains a sequence number for order identification during simulation.
 - The client operates based on a configuration specified in a config file.

##### 2. OrderManager:
 - The OrderManager class is responsible for managing and tracking orders.
 - It allows the addition, retrieval, and status updates of orders.
 - The class is initialized within the FixClient and used to track the status of orders sent to the server.

##### 3. MessageHandler:
 - The MessageHandler class handles incoming server responses.
 - It interprets response messages, updates the order status, and processes different types of messages.
 - The class is also initialized within the FixClient.
Stats:

The Stats class is designed to calculate trading statistics.
It tracks trading volume, profit and loss (PNL), and the volume-weighted average price (VWAP) of the fills for each instrument.
The statistics are continuously updated during the simulation.

## Usage
To use this application, you can run it in a Docker container. Ensure you have Docker installed on your system.
Test session configs available in config/config.json.

```bash
python version: 3.10
```

##### 1. Navigate into project directory
```bash
cd mini-fix-client

```

##### 2. Build docker image
```bash
docker build -t mini-fix-client .
```

##### 3. Run the Docker Container
```bash
docker run mini-fix-client
```