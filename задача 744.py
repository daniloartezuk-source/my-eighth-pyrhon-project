import math

def custom_round(x):
    if x - math.floor(x) >= 0.5:
        return math.ceil(x)
    return math.floor(x)

for _ in range(2):
    x = float(input())
    print(custom_round(x))