from numpy import loadtxt
from matplotlib.pylab import plot, show

data = loadtxt("sunspots.txt", float)

x = data[:,0] # months
y = data[:,1] # number of sunspots per month

plot(x, y)
show()

# Now only show first 1000 months with running average

x_thousand = x[0:1001]
y_thousand = y[0:1001]

def Y_k_average(y):
    r = 5
    for m in range(-r, r + 1):
        Yk_sum = y + m
    return (1/(2*r + 1)) * Yk_sum

plot(x_thousand, y_thousand)
plot(x_thousand, Y_k_average(y_thousand))
show()
