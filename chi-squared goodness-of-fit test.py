import pandas as pd
import numpy as np
import scipy.stats as stats

# Reading loyalty card sign-ups data set
sign_ups = pd.read_csv("Spreadsheet of loyalty signups.csv")
# Reading waiting times of loyalty card sign-ups data set
waiting_times = pd.read_csv("waiting times for loyalty.csv")
# Function to perform ChiSq test
def perform_chi_square(data_set, observations, max_obs, n, prob_function_pmf, prob_function_cdf, hyperparam, title):
    # Empty lists for observed and expected values
    observed = []
    expected = []
    # Setting iterator to 0
    i = 0
    # Running while iterator is less than one plus maximum observed value
    while i < max_obs:
        # Append observed count from data set
        observed.append(len(data_set[data_set[observations] == i]))
        # Append expected count using sample size (n) and given probability pmf
        expected.append(n * prob_function_pmf(i, hyperparam))
        # Run while expected value is less than 5 and iterator is less than one plus maximum observed value
        while expected[-1] < 5 and i < max_obs:
            # Increment iterator
            i += 1
            # Cumulatively add previous expected and observed value to next counts
            expected[-1] += n * prob_function_pmf(i, hyperparam)
            observed[-1] += len(data_set[data_set[observations] == i])
        # Increment iterator
        i +=1
    # Check if last expected value is less than 5
    if expected[-1] < 5:
        # Add last value to second last for both observed and expected values and remove last value from lists
        expected[-1] += n*(1- prob_function_cdf(i - 1, hyperparam))
        expected[-2] += expected[-1]
        expected = expected[:-1]
        observed[-2] += observed[-1]
        observed= observed[:-1]
    else:
        # If last expected value is not less than 5, add remaining probability of distribution to the last value
        expected[-1] += n*(1- prob_function_cdf(i - 1, hyperparam))
    # Perform the Chisq test
    test_statistic, pval = stats.chisquare(observed, expected, 1)
    # Output the results
    print(title)
    print(test_statistic)
    print(pval)
    print("")

# Perform Chisq test on Poisson model for number of loyalty card sign-ups per day
perform_chi_square(sign_ups, "Number_of_loyalty_card_sign_ups", 9, 50, stats.poisson.pmf, stats.poisson.cdf, 3.54, "Chisq test for Poisson(3.54):")
# Perform Chisq test on Geometric model for waiting times for loyalty card sign-ups
perform_chi_square(waiting_times, "waiting_time", 38, 177, stats.geom.pmf, stats.geom.cdf, 177/1480, "Chisq test for Geometric(177/1480):")
