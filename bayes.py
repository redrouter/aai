import pandas as pd

data = pd.read_csv('Mall_Customers2.csv')

total_customers = len(data)
prior_age_30_40 = len(data[(data['Age'] >= 30) & (data['Age'] <= 40)]) / total_customers
prior_spending_score_40_50 = len(data[(data['Spending Score (1-100)'] >= 40) & (data['Spending Score (1-100)'] <= 50)]) / total_customers

likelihood_age_30_40 = len(data[(data['Age'] >= 30) & (data['Age'] <= 40) & (data['Spending Score (1-100)'] >= 40) & (data['Spending Score (1-100)'] <= 50)]) / len(data[(data['Spending Score (1-100)'] >= 40) & (data['Spending Score (1-100)'] <= 50)])
likelihood_spending_score_40_50 = len(data[(data['Age'] >= 30) & (data['Age'] <= 40) & (data['Spending Score (1-100)'] >= 40) & (data['Spending Score (1-100)'] <= 50)]) / len(data[(data['Age'] >= 30) & (data['Age'] <= 40)])

marginal_likelihood = likelihood_age_30_40 * prior_age_30_40 + likelihood_spending_score_40_50 * prior_spending_score_40_50

posterior_age_30_40 = (likelihood_age_30_40 * prior_age_30_40) / marginal_likelihood
posterior_spending_score_40_50 = (likelihood_spending_score_40_50 * prior_spending_score_40_50) / marginal_likelihood

print("Posterior probability of age between 30-40:", posterior_age_30_40)
print("Posterior probability of spending score between 40-50:", posterior_spending_score_40_50)
