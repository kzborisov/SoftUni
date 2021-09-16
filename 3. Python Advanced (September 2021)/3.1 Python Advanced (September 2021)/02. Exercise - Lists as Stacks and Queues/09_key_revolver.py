from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
bullets_in_barrel = barrel_size
bullets_shot = 0

while True:
    if not bullets or not locks:
        break

    bullets_in_barrel -= 1
    bullets_shot += 1
    curr_bullet = bullets.pop()
    curr_lock = locks[0]

    if curr_lock >= curr_bullet:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if bullets_in_barrel == 0:
        if bullets:
            print('Reloading!')
            bullets_in_barrel = barrel_size

if not locks:
    bullets_cost = bullets_shot * bullet_price
    money_earned = intelligence - bullets_cost
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
