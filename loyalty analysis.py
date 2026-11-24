import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

waiting = pd.read_csv("Spreadsheet of loyalty signups.csv")
print(waiting.head())
waiting.Hours_worked = waiting.Hours_worked.astype("string")
sns.boxplot(data = waiting, x = "Hours_worked", y = "Number_of_loyalty_card_sign_ups")
plt.title("Boxplot of loyalty sign ups for both shifts")
plt.show()
