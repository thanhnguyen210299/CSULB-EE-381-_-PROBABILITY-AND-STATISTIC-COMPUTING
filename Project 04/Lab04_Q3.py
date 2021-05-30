import numpy as np
import math
import matplotlib.pyplot as plt
# Generate the values of the RV X
N = 10000;
beta = 45;
n = 24;
# Part a, b and c -
# Create a vector of 24 elements
# Calculate the sum of the elements in this vector
# Repeat this experiment for a total 10000 times
mu_T = beta;
sigma_T = beta;
X = np.zeros((N,1));
for i in range(0,N):
    x = np.random.exponential(beta, n);
    w = np.sum(x);
    X[i] = w;

# Part d and e
# Calculate the average and standard deviation
mu_c = 24 * beta;
sigma_c = beta * np.sqrt(24);
# Create bins and histogram
nbins = 50; # Number of bins
edgecolor = 'w'; # Color separating bars in the bargraph
bins = [float(x) for x in np.linspace(0, 2000, nbins)];
h1, bin_edges = np.histogram(X, bins, density = True);
# Define points on the horizontal axis
be1 = bin_edges[0 : np.size(bin_edges) - 1];
be2 = bin_edges[1 : np.size(bin_edges)];
b1 = (be1 + be2) / 2;
barwidth = b1[1] - b1[0]; # Width of bars in the bargraph
plt.close('all');

# PLOT THE BAR GRAPH
fig1 = plt.figure(1);
plt.bar(b1, h1, width = barwidth, edgecolor = edgecolor);

# Part d
def NormPDF(mu, sigma, x):
    f = ((1 / (sigma * np.sqrt(2 * math.pi)) * np.exp((-1 * ((x-mu)**2)) / (2 * (sigma**2))) * np.ones(np.size(x))));
    return f;

# Plot PDF
f = NormPDF(mu_c, sigma_c, b1);
plt.plot(b1, f, 'r');
plt.title('PDF of lifetime of a 24 batteries carton & comparison w/ Gaussian');
plt.xlabel('Lifetime of a 24 batteries carton - Days');
plt.ylabel('PDF');
fig1.show();

# Plot bar graph
fig2 = plt.figure(2);

# Part e
F = np.cumsum(h1) * barwidth;
#plt.plot(b1, F, 'r');
plt.bar(b1, F, width = barwidth, edgecolor = edgecolor);
plt.title('CDF of lifetime of a 24 batteries carton');
plt.xlabel('Lifetime of a 24 batteries carton - Days');
plt.ylabel('CDF');
fig2.show();

def question01(b1, F):
    day = 0;
    for i, days in enumerate(b1):
        if (days <= 1095):
            day = i;
    # Calculate 1 - F(1095)
    p = 1 - F[day];
    print("Question 1 - P(S > 3 years) = ", p);

def question02(b1, F):
    day1 = 0;
    day2 = 0;
    for i, days in enumerate(b1):
        if (days > 730):
            day1 = i;
            break;
    for i, days in enumerate(b1):
        if (days < 912):
            day2 = i;
    #Calculate F(912) - F(730)
    p = F[day2] - F[day1];
    print("Question 2 - P(730 < S < 912) = ", p);

question01(b1, F);
question02(b1, F);

