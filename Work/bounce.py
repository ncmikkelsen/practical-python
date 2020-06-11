# bounce.py
#
# Exercise 1.5

ball_height = 60;

for bounce in range(10):
    print(bounce, round(ball_height, 4))
    ball_height *= 0.6
