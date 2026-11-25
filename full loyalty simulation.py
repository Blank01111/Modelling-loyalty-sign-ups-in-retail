import scipy.stats as stats
import numpy as np

days = [[31, 0, 4], #January
        [28, 0, 6], #February
        [31, 0, 6], #March
        [30, 0, 4], #April
        [31, 0, 4], #May
        [30, 0, 4], #June
        [31,0, 8], #July
        [31, 0, 8], #August
        [30, 0, 4], #September
        [31, 0, 6], #October
        [30, 0, 9], #November
        [30, 5, 10]] #December

# list for amount of loyalty sign ups each day
number_loyalty_sign_ups = []

def poisson(mean):
    # The poisson distribution
    loyalty_sign_ups = np.random.poisson(mean)
    number_loyalty_sign_ups.append(loyalty_sign_ups) 

def random_walk(number_of_customers):
    # Going through each month
    for month in days:
        # Going through each day
        for day in range(month[0]):
            new_number_of_customers = -1
            # Runs until simulated number of customers is greater than 0
            while new_number_of_customers <= 0:
                # The normal distribution
                unrounded_value_added = np.random.normal(month[1], month[2])
                # Making sure number simulated is a whole number
                value_added = np.round(unrounded_value_added)
                # New number of customers
                new_number_of_customers = number_of_customers + value_added
            # running the poisson distribution with the mean
            poisson((177/1480)*(number_of_customers + value_added))

# Calling the random walk with starting number of customers
random_walk(30)
for sign_up in number_loyalty_sign_ups:
    # Outputting amount of each loyalty sign-ups for each day
    print(sign_up)
# Outputting total number of sign-ups in the simulated year
print("Total number of sign ups this year: " + str(np.sum(number_loyalty_sign_ups)))
