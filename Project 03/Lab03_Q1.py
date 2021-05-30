import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np

# Create cdf of a uniform random variable
def uniform_cdf(a, b, x):
    if (x > a and x < b):
        return (x-a)/(b-a)
    elif (x >= b):
        return 1
    else:
        return 0

# Create pdf of a uniform random variable
def uniform_pdf(a, b, x):
    if (x > a and x < b):
        return 1 / (b - a)
    else:
        return 0

# Genrating uniform distribution
a, b = 1, 10
size = 100000 #the number of points
x = np.linspace(-0.5, 11.5, size)

# Plotting
# divide the frame into 4 part: part a is in row 1, and part b is in row 2
fig, axes = plt.subplots(2, 2)
# Set title and label for graphs
plt.suptitle("Uniform distribution for continuos random variable")
axes[0][0].set_title("pdf using equations")
axes[1][0].set_title("pdf from Scipy package")
axes[0][1].set_title("cdf using equations")
axes[1][1].set_title("cdf from Scipy package")
for i in range(2):
    axes[1][i].set_xlabel('x')
    axes[i][0].set_ylabel('f(x)')
    axes[i][1].set_ylabel('F(x)')

# Plotting pdf
axes[0][0].plot(x, [uniform_pdf(a, b, x_i) for x_i in x], 'r-')
axes[1][0].plot(x, uniform.pdf(x, a, b - 1), 'r-')

# Plotting cdf
axes[0][1].plot(x, [uniform_cdf(a, b, x_i) for x_i in x], 'b-')
axes[1][1].plot(x, uniform.cdf(x, a, b - 1), 'b-')

plt.show()
