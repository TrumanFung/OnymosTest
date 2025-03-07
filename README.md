# Stock Trading Engine

## Overview

This project implements a simple real-time stock trading engine that matches Buy and Sell orders based on defined rules. It simulates a stock exchange where orders for various ticker symbols (stocks) can be placed and matched if the conditions are met. The system supports up to 1,024 unique tickers and a maximum of 10,000 total orders in the order book.

## Features

- **Add Order**: Place a Buy or Sell order for a specific stock ticker with defined quantity and price.
- **Order Matching**: Match Buy orders with Sell orders based on price and availability.
- **Simulated Transactions**: A simulation of random stock trades using a random number generator to continuously add new orders and match them if possible.
- **Concurrency Support**: Code is designed to handle race conditions and use lock-free data structures (though simplified for this simulation).

## Class & Functions

### `Order` Class

The `Order` class is a blueprint for each stock order placed, containing:

- **orderType**: Either 'Buy' or 'Sell'.
- **ticker**: The stock's ticker symbol (e.g., TICKER_1).
- **quantity**: The number of shares being traded.
- **price**: The price per share.

### `addOrder(orderType, ticker, quantity, price)`

Adds an order to the global order book if there's room. The parameters are:

- **orderType**: 'Buy' or 'Sell'.
- **ticker**: The ticker symbol of the stock.
- **quantity**: The number of shares.
- **price**: The price per share.

If the order book is full, a message will be printed, and no new order will be added.

### `matchOrders()`

This function iterates through the order book and attempts to match Buy and Sell orders for the same stock ticker symbol based on the following rules:

- A Buy order can be matched with a Sell order if the Buy price is greater than or equal to the Sell price.
- A Sell order can be matched with a Buy order if the Sell price is less than or equal to the Buy price.

It calculates the trade quantity based on the smaller order's quantity, performs the trade, and adjusts the remaining quantities accordingly. If an order's quantity is reduced to zero, it is removed from the order book.

### `simulateTransactions()`

This function simulates random stock transactions in an infinite loop. It randomly selects order types, stock ticker symbols, quantities, and prices to generate Buy and Sell orders. It continuously adds these orders to the order book and tries to match them.

### Random Functions

- **`generateRandomNumber()`**: Generates a pseudo-random number based on a seed.
- **`getRandomInRange(start, end)`**: Returns a random number between start and end.
- **`pickRandomOption(options)`**: Picks a random element from the provided list of options.

## How It Works

1. **Order Addition**: The `simulateTransactions` function continuously generates random Buy and Sell orders for up to 1,024 tickers.
2. **Order Matching**: After adding each order, the system checks if any Buy and Sell orders can be matched. If a match is found, a trade occurs, and the quantities are adjusted.
3. **Continuous Simulation**: The engine runs indefinitely, simulating ongoing stock market activity.

## Constraints & Requirements

- **No Dictionaries/Maps**: The implementation avoids using dictionaries, maps, or similar data structures, as required. Instead, a fixed-size list (`orderBook`) is used to store orders.
- **Concurrency**: In a real-world scenario, multiple stockbrokers would submit orders simultaneously. This solution is designed to handle concurrent order modifications, although actual thread synchronization mechanisms are omitted in this simplified simulation.
- **Performance**: The `matchOrders` function works in O(n) time, where `n` is the number of active orders in the order book.

## Future Improvements

- Add thread safety to handle real-world concurrent access.
- Implement persistence for the order book, so it is not memory-bound.
- Enhance the order matching algorithm to improve performance for large-scale trading operations.

## How to Run

To execute the stock trading simulation:

1. Clone the repository.
2. Run the Python script. It will simulate random stock transactions indefinitely.

```bash
python stock_trading_engine.py
