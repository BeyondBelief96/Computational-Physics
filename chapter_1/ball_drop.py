h = float(input("Enter the height of the tower: "))
t = float(input("Enter the time interval: "))
g = 9.81

s = g*t**2/2

dist = 0;
if(h - s < 0):
    dist = 0
else:
    dist = h - s;
print("The height of the ball is", dist, "meters")