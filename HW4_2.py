from scipy.stats import binom
import numpy as np

def verify_binomial_distribution_parameters(p, n):
    # Generate a random sample from the binomial distribution
    sample = np.random.binomial(n, p, size=10000)

    # Calculate the mean and standard deviation of the sample
    sample_mean = np.mean(sample)
    sample_std_dev = np.std(sample, ddof=1)  # ddof=1 for sample standard deviation

    # Calculate the theoretical mean and standard deviation
    theoretical_mean = n * p
    theoretical_std_dev = np.sqrt(n * p * (1 - p))

    # Print the results
    print(f"Sample Mean: {sample_mean:.4f}")
    print(f"Theoretical Mean: {theoretical_mean:.4f}")
    print(f"Sample Standard Deviation: {sample_std_dev:.4f}")
    print(f"Theoretical Standard Deviation: {theoretical_std_dev:.4f}")

# Parameters
p = 0.05
n = 60  # You can choose any value greater than 50

# Verify the binomial distribution parameters
verify_binomial_distribution_parameters(p, n)
