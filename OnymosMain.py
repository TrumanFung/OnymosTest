NUM_TICKERS = 1024
MAX_ORDERS = 10000

class Order:
    def __init__(self, orderType, ticker, quantity, price):
        self.orderType = orderType
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

orderBook = [None] * MAX_ORDERS
orderCount = 0

def generateRandomNumber():
    seed = 12345
    seed = (seed * 1103515245 + 12345) & 0x7fffffff
    return seed

def getRandomInRange(start, end):
    return start + (generateRandomNumber() % (end - start + 1))

def pickRandomOption(options):
    index = getRandomInRange(0, len(options) - 1)
    return options[index]

def addOrder(orderType, ticker, quantity, price):
    global orderCount
    if orderCount >= MAX_ORDERS:
        print("Order book is full. Cannot add more orders.")
        return

    newOrder = Order(orderType, ticker, quantity, price)
    orderBook[orderCount] = newOrder
    orderCount += 1
    print(f"Added Order: {orderType} {ticker} {quantity} @ {price}")

def matchOrders():
    global orderBook, orderCount

    for i in range(orderCount):
        if orderBook[i] is None:
            continue

        for j in range(i + 1, orderCount):
            if orderBook[j] is None:
                continue

            order1 = orderBook[i]
            order2 = orderBook[j]

            if order1.ticker != order2.ticker:
                continue

            isBuySellMatch = (
                order1.orderType == 'Buy' and
                order2.orderType == 'Sell' and
                order1.price >= order2.price
            )

            isSellBuyMatch = (
                order1.orderType == 'Sell' and
                order2.orderType == 'Buy' and
                order2.price >= order1.price
            )

            if isBuySellMatch or isSellBuyMatch:
                tradeQuantity = min(order1.quantity, order2.quantity)
                print(f"Matched Order: {order1.orderType} {order1.ticker} {tradeQuantity} @ {order1.price} with {order2.orderType} {order2.ticker} {tradeQuantity} @ {order2.price}")

                order1.quantity -= tradeQuantity
                order2.quantity -= tradeQuantity

                if order1.quantity == 0:
                    orderBook[i] = None
                if order2.quantity == 0:
                    orderBook[j] = None

def simulateTransactions():
    tickers = [f"TICKER_{i}" for i in range(NUM_TICKERS)]
    while True:
        orderType = pickRandomOption(['Buy', 'Sell'])
        ticker = pickRandomOption(tickers)
        quantity = getRandomInRange(1, 100)
        price = getRandomInRange(10, 1000)
        addOrder(orderType, ticker, quantity, price)
        matchOrders()

simulateTransactions()