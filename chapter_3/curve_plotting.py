from matplotlib.pylab import plot, show
from numpy import sin, cos, pi, linspace, exp

#deltoid curve
theta_values = linspace(0, 2*pi)

def deltoid_curve(theta_values):
    x = x_curve(theta_values)
    y = y_curve(theta_values)
    
    return x, y

def x_curve(theta):
    x = 2*cos(theta) + cos(2*theta)
    return x
def y_curve(theta):
    y = 2*sin(theta) - sin(2*theta)
    return y

def galilean_spiral(theta_limit, theta_steps):
    theta = linspace(0, theta_limit, theta_steps)
    r = theta**2
    
    return r, theta

def polar_converter(r, theta_array):
    x = r * cos(theta_array)
    y = r * sin(theta_array)
    return x, y

def feys_function(theta_limit, theta_steps):
    theta = linspace(0, theta_limit, theta_steps)
    r = exp(cos(theta)) - 2*cos(4*theta) + sin(theta/12)**5
    return r, theta

x, y = deltoid_curve(theta_values)
plot(x,y)
show()

#galilean spiral in polar plot
r, theta = galilean_spiral(10*pi, 100)
x, y = polar_converter(r, theta)
plot(x,y)
show()

#feys function
r, theta = feys_function(24*pi, 10000)
x, y = polar_converter(r, theta)
plot(x,y)
show()