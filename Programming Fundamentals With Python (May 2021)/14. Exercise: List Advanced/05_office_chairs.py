# Task 05. Office Chairs

rooms_cnt = int(input())
chairs_left = 0
game_on = True


for room in range(1, rooms_cnt+1):
    room_info = input().split()
    chairs = room_info[0]
    visitors = int(room_info[1])

    if len(chairs) < visitors:
        print(f"{visitors-len(chairs)} more chairs needed in room {room}")
        game_on = False
    else:
        chairs_left += len(chairs) - visitors

if game_on:
    print(f"Game On, {chairs_left} free chairs left")
