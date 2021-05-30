import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import math

def erf_normal(x):
    t = 1.0 / (1.0 + 0.5 * abs(x))
    ans = 1 - t * math.exp(-x * x - 1.26551223 + t * (1.00002368 + t * (0.37409196 + t * (0.09678418 + t * (-0.18628806 + t * (0.27886807 + t * (-1.13520398 + t * (1.48851587 + t * (-0.82215223 + t * (0.17087277))))))))))
    if x >= 0.0:
        return ans
    else:
        return -ans

# Create cdf of a normal random variable
def norm_cdf(x, mu, var):
    return 0.5 * (1 + math.erf((x - mu)/math.sqrt(2*var)))

# Create pdf of a uniform random variable
def norm_pdf(x, mu, sigma_2):
    f = np.exp(- (x - mu)**2 / (2 * sigma_2)) / (math.sqrt(2 * np.pi * sigma_2))
    return f

# Genrating the list of x
x = np.linspace(-6, 6, 100000)

mean = [0, 0, 0, -3, -3, -3]
variance = [1, 0.1, 0.01, 1, 0.1, 0.01]

# Plotting
# divide the frame into 4 part: part a is in row 1, and part b is in row 2
fig, (ax1, ax2) = plt.subplots(1, 2)
# Set title and label for graphs
plt.suptitle("Normal distribution for random variable")
ax1.set_title("pdf function")
ax2.set_title("cdf function")
ax1.set_xlabel('x')
ax2.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax2.set_ylabel('F(x)')

# Plotting pdf
for i in range(6):
    ax1.plot(x, [norm_pdf(x_i, mean[i], variance[i]) for x_i in x], label = 'mean=%.d var=%.2f' %(mean[i], variance[i]))

# Plotting cdf
for i in range(6):
    ax2.plot(x, [norm_cdf(x_i, mean[i], variance[i]) for x_i in x], label = 'mean=%.d var=%.2f' %(mean[i], variance[i]))

ax1.legend()
ax2.legend()
plt.show()
