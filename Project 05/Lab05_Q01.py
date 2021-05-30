import numpy as np
import matplotlib.pyplot as plt
import random

N = 1000000; # Bearings
mean = 100;
sigma = 12;
M = 10000;
nSample = 200;

# Generating population
bearings = np.random.normal(mean, sigma, N);

# Z value for confidence interval
z_95 = 1.96;
z_99 = 2.58;

result = [];
for i in range(0, nSample):
    n = i + 1;
    sample = np.random.choice(bearings, i + 1);
    result.append(sum(sample) / n);

x = np.linspace(1, nSample);

# Plotting Figure a
fig1 = plt.figure(1);
plt.title("Sample Means and 95% confidence Intervals");
plt.xlabel("Sample Size");
plt.ylabel("x_bar");
plt.axhline(y = mean, color = "black");
plt.plot(x, mean + z_95 * sigma / (x**(1/2)), 'r--');
plt.plot(x, mean - z_95 * sigma / (x**(1/2)), 'r--');
plt.scatter(range(nSample), result, marker = 'x', color = "blue");
fig1.show();

#Plotting Figure b
fig2 = plt.figure(2);
plt.title("Sample Means and 99% confidence Intervals");
plt.xlabel("Sample Size");
plt.ylabel("x_bar");
plt.axhline(y = mean, color = "black");
plt.plot(x, mean + z_99 * sigma / (x**(1/2)), 'g--');
plt.plot(x, mean - z_99 * sigma / (x**(1/2)), 'g--');
plt.scatter(range(nSample), result, marker = 'x', color = "blue");
fig2.show();
