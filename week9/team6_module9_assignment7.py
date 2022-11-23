import heapq


class StockExchange():
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []


    # adds order to heap if order is a buy order or a sell order
    def add_order(self, buy_or_sell, price, shares):
        if buy_or_sell == "buy":
            heapq.heappush(self.buy_orders, (shares, price))
        elif buy_or_sell == "sell":
            heapq.heappush(self.sell_orders, (shares, price))
        self.process_orders()

    # processes orders by matching buy orders with sell orders
    def process_orders(self):
        while self.buy_orders and self.sell_orders:
            buy_order = self.buy_orders[0]
            sell_order = self.sell_orders[0]
            if buy_order[0] >= sell_order[0]:
                if buy_order[1] == sell_order[1]:
                    heapq.heappop(self.buy_orders)
                    heapq.heappop(self.sell_orders)
                elif buy_order[1] > sell_order[1]:
                    heapq.heappop(self.buy_orders)
                    heapq.heappush(self.buy_orders, (buy_order[0], buy_order[1] - sell_order[1]))
                    heapq.heappop(self.sell_orders)
                    print("Processing order: Sell " + str(sell_order[1]) + " shares at $" + str(sell_order[0]) + " each")
                else:
                    heapq.heappop(self.sell_orders)
                    heapq.heappush(self.sell_orders, (sell_order[0], sell_order[1] - buy_order[1]))
                    heapq.heappop(self.buy_orders)
                    print("Processing order: Buy " + str(buy_order[1]) + " shares at $" + str(buy_order[0]) + " each")
            else:
                break

        


# Driver Code:
print("TEST RUN.1")
# Test RUN.1
stock_exchange = StockExchange()
stock_exchange.add_order("buy", 100, 10)
stock_exchange.add_order("sell", 40, 9)
stock_exchange.process_orders()  # This will return: Processing order: Sell 40 shares at $9 each.
print(stock_exchange.buy_orders)  # This will return: [(1, 60, 10)]. Because we sold 40 of them and 60 left with price $10.
print(stock_exchange.sell_orders)  # This will return an empty list because all 40 is sold and popped from the list.


print("TEST RUN.2")
# TEST RUN.2
stock_exchange.add_order("buy", 50, 8)
stock_exchange.process_orders()  # This will return nothing because a sell is required as well to process order.
print(stock_exchange.buy_orders)  # This will return: [(1, 50, 8), (1, 60, 10)]
print(stock_exchange.sell_orders)  # This will return an empty list.


print("TEST RUN.3")
# TEST RUN.3
stock_exchange.add_order("sell", 30, 7)
stock_exchange.process_orders()  # This will return: Processing order: Sell 30 shares at $7 each. - Explanation: It will sell from the first item of [(1, 50, 8), (1, 60, 10)], which is (1, 50, 8) and also because 8>7..
print(stock_exchange.buy_orders)  # [(1, 20, 8), (1, 60, 10)]
print(stock_exchange.sell_orders)  # []


print("TEST RUN.4")
# TEST RUN.4
stock_exchange.add_order("sell", 150, 7)
stock_exchange.add_order("buy", 100, 14)
stock_exchange.process_orders()
# This will return:
# Processing order: Sell 20 shares at $7 each
# Processing order: Sell 60 shares at $7 each
# Processing order: Sell 70 shares at $7 each
print(stock_exchange.buy_orders)  # [(1, 30, 14)]
print(stock_exchange.sell_orders)  # []