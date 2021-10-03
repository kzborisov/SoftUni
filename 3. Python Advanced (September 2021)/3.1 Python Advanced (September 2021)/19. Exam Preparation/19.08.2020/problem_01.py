from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]

    # The taxi cannot drive the customer
    if customer > taxi:
        taxis.pop()
        continue

    # The taxi can drive
    total_time += customer
    customers.popleft()
    taxis.pop()

if not customers:
    print("All customers were driven to their destinations\n"
          f"Total time: {total_time} minutes")
elif not taxis and customers:
    print("Not all customers were driven to their destinations\n"
          f"Customers left: {', '.join(str(x) for x in customers)}")
