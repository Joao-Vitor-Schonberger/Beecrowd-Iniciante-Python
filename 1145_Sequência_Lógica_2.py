import sys

input_data = sys.stdin.read().split()
if input_data:
    X = int(input_data[0])
    Y = int(input_data[1])

    for i in range(1, Y + 1):
        if i % X == 0:
            print(i)
        else:
            if i == Y:
                print(i)
            else:
                print(i, end=" ")