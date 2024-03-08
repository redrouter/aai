import pandas as pd
data = pd.read_csv('Mall_Customers2.csv')
age_greater_than_40 = data[data['Age'] > 40]
total_age_greater_than_40 = len(age_greater_than_40)
high_spending_customers = age_greater_than_40[age_greater_than_40['Spending Score (1-100)'] > 50]
total_age_greater_than_40_high_spending = len(high_spending_customers)
probability = total_age_greater_than_40_high_spending / total_age_greater_than_40
print("Probability of customer spending score > 50 given age > 40:", probability)
