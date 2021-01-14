from numpy import random
import time

left_value = 10
right_value = 10



running = True
while running:
    left_chance = left_value/(right_value+left_value)
    right_chance = right_value/(right_value+left_value)

    a = random.choice(["left","right"],p=[left_chance,right_chance])
    
    if a == "right":
        right_value = right_value * 1.01
    elif a == "left":
        left_value = left_value * .99

    print(a)
    print(f"({left_chance},{right_chance})")

    time.sleep(.1)