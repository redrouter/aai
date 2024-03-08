import pandas as pd

# Load the dataset
data = pd.read_csv('Mall_Customers2.csv')

# Filter the dataset to include only customers with age > 40
age_greater_than_40 = data[data['Age'] > 40]

# Calculate the total number of customers with age > 40
total_age_greater_than_40 = len(age_greater_than_40)

# Filter the dataset to include only customers with spending score > 50
high_spending_customers = age_greater_than_40[age_greater_than_40['Spending Score (1-100)'] > 50]

# Calculate the number of customers with age > 40 and spending score > 50
total_age_greater_than_40_high_spending = len(high_spending_customers)

# Calculate the probability
probability = total_age_greater_than_40_high_spending / total_age_greater_than_40
print("Probability of customer spending score > 50 given age > 40:", probability)
