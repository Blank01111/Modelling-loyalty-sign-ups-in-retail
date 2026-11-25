import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading loyalty sign-up data set and viewing first few entries
sign_ups = pd.read_csv("Spreadsheet of loyalty signups.csv")
print(sign_ups.head())

# Outputting summary statistics for loyalty signups
print("Summary statistics for all loyalty sign-ups in a day")
print("")
print(sign_ups["Number_of_loyalty_card_sign_ups"].describe())

#Setting hours worked variable as a string
sign_ups["Hours_worked"] = sign_ups["Hours_worked"].astype("string")
# Boxplot for loyalty sign-ups by hours worked
sns.boxplot(data = sign_ups, x = "Hours_worked", y = "Number_of_loyalty_card_sign_ups")
plt.title("Boxplot of loyalty sign ups for both shifts")
plt.show()
plt.clf()

# Subset of loyalty data set of 4 hour shifts and viewing summary statistics
sign_ups_4h = sign_ups[sign_ups["Hours_worked"] == "4"]
print("Summary statistics for loyalty sign-ups in 4 hour shifts")
print("")
print(sign_ups_4h["Number_of_loyalty_card_sign_ups"].describe())

# Subset of loyalty data set of 5.5 hour shifts and viewing summary statistics
print("Summary statistics for loyalty sign-ups in 5.5 hour shifts")
print("")
sign_ups_5h = sign_ups[sign_ups["Hours_worked"] == "5.5"]
print(sign_ups_5h["Number_of_loyalty_card_sign_ups"].describe())

# Labels for loyalty card sign-ups
lst_full = ["1", "2", "3", "4", "5", "6", "7", "8"]
# Empty list to store the number of occurrences
num_sign_up_occurrence_4h = []
# Looping through number of sign-ups
for num_sign_ups in range(1, 9):
    # Counting occurrences of sign-ups in 4h dataset
    num_sign_up_occurrence_4h.append(len(sign_ups_4h[sign_ups_4h["Number_of_loyalty_card_sign_ups"] == num_sign_ups]))
# Plotting as a bar plot
plt.bar(lst_full, num_sign_up_occurrence_4h)
plt.title("Bar plot ofr loyalty card sign-ups for 4h shifts")
plt.xlabel("Number of loyalty signups")
plt.ylabel("Count")
plt.show()
plt.clf()

# Labels for loyalty sign-ups for 5.5 hour dataset
lst_part = ["1", "2", "3", "4", "5", "6"]
# Empty list to store the number of occurrences
num_sign_up_occurrence_5h = []
# Looping through number of sign-ups
for num_sign_ups in range(1, 7):
    # Counting occurrences of sign-ups in 5.5h dataset
    num_sign_up_occurrence_5h.append(len(sign_ups_5h[sign_ups_5h["Number_of_loyalty_card_sign_ups"] == num_sign_ups]))
# Plotting it as a bar plot
plt.bar(lst_part, num_sign_up_occurrence_5h)
plt.title("Bar plot of loyalty card sign-ups for 5h shifts")
plt.xlabel("Number of loyalty signups")
plt.ylabel("Count")
plt.show()
plt.clf()

# Empty list to store the number of occurrences
num_sign_up_occurrence = []
# Looping through number of sign-ups
for num_sign_ups in range(1, 9):
    # Counting occurrences of sign-up number
    num_sign_up_occurrence.append(len(sign_ups[sign_ups["Number_of_loyalty_card_sign_ups"] == num_sign_ups]))

# Plotting it as a bar plot
plt.bar(lst_full, num_sign_up_occurrence)
plt.title("Loyalty signups per day for both shifts")
plt.xlabel("Number of loyalty signups")
plt.ylabel("Count")
plt.show()
plt.clf()

# Loading the waiting times data set, viewing the head and getting summary statistics of waiting times
waiting = pd.read_csv("waiting times for loyalty.csv")
print(waiting.head())
print("Summary statistics for waiting times until loyalty sign-up")
print("")
print(waiting["waiting_time"].describe())

# Empty list to store occurrences of waiting times
num_waiting_occurrence = []
# Looping through each waiting time
for num_waiting in range(1, max(waiting["waiting_time"])+1):
    # Counting the occurrences of current waiting time
   num_waiting_occurrence.append(len(waiting[waiting["waiting_time"] == num_waiting]))

# Plotting it as a histogram
plt.hist(num_waiting_occurrence)
plt.title("Histogram of people asked for loyalty until sign-up")
plt.xlabel("Waiting time in people asked")
plt.ylabel("Frequency")
plt.xticks(range(0, max(num_waiting_occurrence)+1))
plt.show()