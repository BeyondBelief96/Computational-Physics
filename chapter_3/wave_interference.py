from math import sqrt, sin, pi
from numpy import empty
from matplotlib.pylab import imshow, gray, show

wavelength = 5.0 # wavelength
k = 2*pi/wavelength # wavevector
amplitude = 1.0 # wave amplitude
separation = 20 # 20 cm separation between centers of waves
side = 100 #size of side of square on grid
points = 500
spacing = side/points

#calculate the positions of the centers of each wave
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

#make an array to store the heights
xi = empty([points, points], float)

#calculate values in array
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = sqrt((x - x1)**2 + (y- y2)**2)
        r2 = sqrt((x - x2)**2 + (y - y2)**2)
        xi[i,j] = amplitude*sin(k*r1) + amplitude*sin(k*r2)
        
#make plot
imshow(xi, origin="lower", extent=[0, side, 0, side])
gray()
show()