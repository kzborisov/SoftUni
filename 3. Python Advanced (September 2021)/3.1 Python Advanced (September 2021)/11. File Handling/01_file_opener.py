# try:
#     file = open("./text.txt", 'r')
#     print('File found')
#     file.close()
# except FileNotFoundError:
#     print('File not found')
import time

for i in range(10):
    time.sleep(.3)
    print("\r", end="")
    print(i, end="")

