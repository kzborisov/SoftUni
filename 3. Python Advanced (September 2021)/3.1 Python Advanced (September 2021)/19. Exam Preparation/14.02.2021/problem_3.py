from collections import deque


def deliver(stock: list, boxes):
    for box in boxes:
        stock.append(box)
    return stock


def sell(stock: deque, sold=None):
    if sold:
        if str(sold[0]).isdigit():
            for _ in range(int(sold[0])):
                stock.popleft()
        elif any(str(x).isalpha() for x in sold):
            for flavor in sold:
                while flavor in stock:
                    stock.remove(flavor)
        return list(stock)
    stock.popleft()
    return list(stock)


def stock_availability(stock, action, *args):
    if action == "delivery":
        stock = deliver(stock, args)
    elif action == "sell":
        if args:
            stock = sell(deque(stock), args)
        else:
            stock = sell(deque(stock))
    return stock


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
