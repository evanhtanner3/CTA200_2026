import numpy as np
import matplotlib.pyplot as plt

z = 0

x = np.linspace(-2,2, 1000)
y = np.linspace(-2,2, 1000)



re, im = np.meshgrid(x,y)


c = re + 1j*im

for k in x:
    z = z**2 + c

boundary = np.abs(z) < 2
