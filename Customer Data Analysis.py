import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and clean missing values
file_path = "Online Retail.csv"
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Convert Invoice Date to datetime format (fixes inconsistencies)
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], dayfirst=True, errors='coerce')

# Remove rows where 'CustomerID' is missing
data = data.dropna(subset=['CustomerID'])

# Calculate Total Sales per Transaction
data['TotalSales'] = data['Quantity'] * data['UnitPrice']


# Total Sales Analysis
total_sales = data['TotalSales'].sum()
print(f"Total Sales: ${total_sales:.2f}")

# Most Frequent Buyers (Top 5 customers by number of purchases)
most_frequent_buyers = data['CustomerID'].value_counts().head(5)
print("\nTop 5 Frequent Buyers:")
print(most_frequent_buyers)

# Top 5 Customers by Total Spending
top_spenders = data.groupby('CustomerID')['TotalSales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Customers by Total Spending:")
print(top_spenders)

# Top 5 Most Popular Products
popular_products = data['Description'].value_counts().head(5)
print("\nTop 5 Most Popular Products:")
print(popular_products)

# Top 5 Products by Revenue Generated
top_revenue_products = data.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products by Revenue:")
print(top_revenue_products)

# Total Sales by Top 5 Countries
sales_by_country = data.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Countries by Total Sales:")
print(sales_by_country)

# Bar Chart: Top 5 Customers by Total Spending
plt.figure(figsize=(8,5))
top_spenders.plot(kind='bar', color='blue')
plt.title("Top 5 Customers by Total Spending")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')  # Avoid scientific notation
plt.tight_layout()
plt.show()

# Bar Chart: Top 5 Most Sold Products
plt.figure(figsize=(8,5))
popular_products = data['Description'].value_counts().head(5)
popular_products.plot(kind='bar', color='skyblue')
plt.title("Top 5 Most Sold Products")
plt.xlabel("Product Name")
plt.ylabel("Units Sold")
plt.xticks(rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# Bar Chart: Top 5 Revenue-Generating Products
plt.figure(figsize=(8,5))
top_revenue_products.plot(kind='bar', color='orange')
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product Name")
plt.ylabel("Total Revenue ($)")
plt.xticks(rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# Bar Chart: Top 5 Countries by Total Sales
plt.figure(figsize=(8,5))
sales_by_country.plot(kind='bar', color='green')
plt.title("Top 5 Countries by Total Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()
