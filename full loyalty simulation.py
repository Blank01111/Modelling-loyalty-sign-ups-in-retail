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

number_loyalty_sign_ups = [] # list for amount of loyalty sign ups each day

def poisson(mean):
    loyalty_sign_ups = np.random.poisson(mean) # The poisson distribution
    number_loyalty_sign_ups.append(loyalty_sign_ups) 

def random_walk(number_of_customers):
    for month in days: # Going through each month
        for day in range(month[0]): # Going through each day
            new_number_of_customers = -1
            while new_number_of_customers <= 0: # Runs untill simulated number of customers is greater than 0
                unrounded_value_added = np.random.normal(month[1], month[2]) # The normal distribution
                value_added = np.round(unrounded_value_added) # Making sure number simulated is a whole number
                new_number_of_customers = number_of_customers + value_added # New number of customers
            poisson((177/1480)*(number_of_customers + value_added)) # running the poisson distribution with the mean
random_walk(30) # Calling the random walk with starting number of customers
for sign_up in number_loyalty_sign_ups:
    print(sign_up) # Outputting amount of each loyalty sign ups for each day
print("Total number of sign ups this year: " + str(np.sum(number_loyalty_sign_ups))) # Outputting total number of sign ups in the simulated year
