import pandas as pd

# Load the dataset
data = pd.read_csv('Mall_Customers2.csv')

# Filter the dataset to include only customers with income > $60,000
high_income_customers = data[data['Annual Income (k$)'] > 60000]

# Calculate the total number of customers with income > $60,000
total_high_income_customers = len(high_income_customers)

if total_high_income_customers > 0:
    # Filter the dataset to include only customers with spending score > 50
    high_spending_customers = high_income_customers[high_income_customers['Spending Score (1-100)'] > 50]

    # Calculate the number of customers with income > $60,000 and spending score > 50
    total_high_income_high_spending_customers = len(high_spending_customers)

    # Calculate the probability
    probability = total_high_income_high_spending_customers / total_high_income_customers
    print("Probability of customer spending score > 50 given income > $60,000:", probability)
else:
    print("No customers found with income > $60,000.")
