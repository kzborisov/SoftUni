from collections import deque


def stock_availability(flavors, order_type: str, *args):
    flavors = deque(flavors)
    if order_type == "delivery":
        for arg in args:
            flavors.append(arg)
        return list(flavors)
    else:
        if not args:
            flavors.popleft()
            return list(flavors)
        if len(args) == 1 and str(args[0]).isdigit():
            for _ in range(int(args[0])):
                flavors.popleft()
            return list(flavors)
        else:
            for arg in args:
                while arg in flavors:
                    flavors.remove(arg)
            return list(flavors)



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
