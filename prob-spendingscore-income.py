import pandas as pd

data = pd.read_csv('Mall_Customers2.csv')

high_income_customers = data[data['Annual Income (k$)'] > 60000]

total_high_income_customers = len(high_income_customers)

if total_high_income_customers > 0:
   
    high_spending_customers = high_income_customers[high_income_customers['Spending Score (1-100)'] > 50]

    total_high_income_high_spending_customers = len(high_spending_customers)

   
    probability = total_high_income_high_spending_customers / total_high_income_customers
    print("Probability of customer spending score > 50 given income > $60,000:", probability)
else:
    print("No customers found with income > $60,000.")
