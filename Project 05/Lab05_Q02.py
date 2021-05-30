import numpy as np

N = 1000000; # Bearings
mean = 100;
sigma = 12;
M = 10000;

# Generating population
bearings = np.random.normal(mean, sigma, N);

def ConfidenceInterval(bearings, mean, sigma, M, n):
    successes_n95 = 0;
    successes_n99 = 0;
    successes_t95 = 0;
    successes_t99 = 0;

    # Giving z value
    z_95 = 1.96;
    z_99 = 2.58;

    # Giving t value
    if (n == 5):
        t_95 = 2.78;
        t_99 = 4.6;
    if (n == 40):
        t_95 = 2.02;
        t_99 = 2.7;
    if (n == 120):
        t_95 = 1.98;
        t_99 = 2.62;

    for i in range(M):
        # Generating sample of size n from population
        sample = np.random.choice(bearings, n);
        mean_s = sum(sample) / n;
        sigma_s = 0;
        for j in range(len(sample)):
            sigma_s = sigma_s + ((sample[j] - mean_s)**2);
        sigma_s = (sigma_s / (n - 1))**(1/2);

        # Finding upper and lower limits for Normal Distribution
        lowerLimit_n95 = mean_s - z_95 * sigma_s / (n**(1/2));
        upperLimit_n95 = mean_s + z_95 * sigma_s / (n**(1/2));

        lowerLimit_n99 = mean_s - z_99 * sigma_s / (n**(1/2));
        upperLimit_n99 = mean_s + z_99 * sigma_s / (n**(1/2));

        if (lowerLimit_n95 <= mean and mean <= upperLimit_n95):
            successes_n95 += 1;
        if (lowerLimit_n99 <= mean and mean <= upperLimit_n99):
            successes_n99 += 1;

        # Finding upper and lower limits for T-SDistribution
        lowerLimit_t95 = mean_s - t_95 * sigma_s / (n**(1/2));
        upperLimit_t95 = mean_s + t_95 * sigma_s / (n**(1/2));

        lowerLimit_t99 = mean_s - t_99 * sigma_s / (n**(1/2));
        upperLimit_t99 = mean_s + t_99 * sigma_s / (n**(1/2));

        if (lowerLimit_t95 <= mean and mean <= upperLimit_t95):
            successes_t95 += 1;
        if (lowerLimit_t99 <= mean and mean <= upperLimit_t99):
            successes_t99 += 1;

    # Calculating the success for 95 and 99 confidence level
    successes_n95 = successes_n95 / M * 100;
    successes_n99 = successes_n99 / M * 100;
    successes_t95 = successes_t95 / M * 100;
    successes_t99 = successes_t99 / M * 100;

    # Print results
    print("Normal Distribution with n = ", n, "\n");
    print("At 95% confidence level: ", successes_n95, "\n");
    print("At 99% confidence level: ", successes_n99, "\n");

    print("Student-T's Distribution with n = ", n, "\n");
    print("At 95% confidence level: ", successes_t95, "\n");
    print("At 99% confidence level: ", successes_t99, "\n");

ConfidenceInterval(bearings, mean, sigma, M, 5);
ConfidenceInterval(bearings, mean, sigma, M, 40);
ConfidenceInterval(bearings, mean, sigma, M, 120);
