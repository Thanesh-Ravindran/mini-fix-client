# src/stats.py
# track and calculate trading statistics, including trading volume, PNL, and VWAP


class Stats:
    def __init__(self):
        self.trading_volume = 0.0
        self.pnl = 0.0
        self.vwap = {}  # dict to store VWAP/instrument

    def calculate_stats(self):
        return self.total_volume, self.pnl, self.vwap

    def update_stats(self, order, instrument, side, fill_price, fill_quantity):
        self.trading_volume += fill_price * fill_quantity

        if side == "BUY":
            self.pnl -= fill_price * fill_quantity
        elif side == "SELL":
            self.pnl += fill_price * fill_quantity

        if instrument not in self.vwap:
            self.vwap[instrument] = {"total_price": 0.0, "total_quantity": 0}
        self.vwap[instrument]["total_price"] += fill_price * fill_quantity
        self.vwap[instrument]["total_quantity"] += fill_quantity
