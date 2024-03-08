import pandas as pd


data = pd.read_csv('Mall_Customers2.csv')


total_customers = len(data)

female_customers = data[data['Gender'] == 'Female']

total_female_customers = len(female_customers)


high_spending_customers = data[data['Spending Score (1-100)'] > 40]

total_high_spending_customers = len(high_spending_customers)

female_high_spending_customers = female_customers[female_customers['Spending Score (1-100)'] > 40]

total_female_high_spending_customers = len(female_high_spending_customers)

joint_probability = total_female_high_spending_customers / total_customers

print("Joint probability of customer being female and spending score > 40:", joint_probability)
