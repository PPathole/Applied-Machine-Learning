import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming you have your data stored in a pandas DataFrame called 'df'
# If not, you can create one from your existing data

# Calculate average internal offer price and KBB listing price for each car model and trim level
average_prices = df.groupby(['model', 'trim']).agg({'internal_offer': 'mean', 'kbb_listing price': 'mean'}).reset_index()

# Plotting the comparison of average prices
plt.figure(figsize=(12, 8))
sns.barplot(data=average_prices, x='model', y='internal_offer', hue='trim', palette='coolwarm', ci=None)
plt.title('Comparison of Average Internal Offer Price by Model and Trim')
plt.xlabel('Car Model')
plt.ylabel('Average Internal Offer Price')
plt.legend(title='Trim')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(data=average_prices, x='model', y='kbb_listing price', hue='trim', palette='coolwarm', ci=None)
plt.title('Comparison of Average KBB Listing Price by Model and Trim')
plt.xlabel('Car Model')
plt.ylabel('Average KBB Listing Price')
plt.legend(title='Trim')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
