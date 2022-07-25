from math import sqrt

hbar = 1.05457182 * 10**-34
m = 9.11 * 10**-31 #kg
E = 30 #eV
V = 9 #eV

k1 = sqrt(2*m*E)/ hbar
k2 = sqrt(2*m*(E - V)) / hbar

def CalculateTransmissionCoefficient(k1, k2):
    T = (4*k1*k2) / (k1 + k2)**2
    print("Transmission Coefficient: ", T)
    
def CalculateReflectionCoefficient(k1, k2):
    R = ((k1 - k2) / (k1 + k2))**2
    print("Reflection Coefficient: ", R)
    
CalculateTransmissionCoefficient(k1, k2)
CalculateReflectionCoefficient(k1, k2)