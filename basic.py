import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# Read CSV data
df = pd.read_csv('sales_data.csv')

# Extract relevant columns
units_sold = df['Units_Sold'].head(10)
product_ids = df['Product_ID'].head(10)
unit_price = df['Unit_Price'].head(10)
total_sales = df['Total_Sales'].head(10)

# Line Plot - Units Sold
plt.plot(units_sold)
plt.title('Line - Units Sold')
plt.xlabel('Index')
plt.ylabel('Units Sold')
plt.show()

# Bar Plot - Units Sold by Product
plt.bar(product_ids, units_sold)
plt.title('Bar - Units Sold by Product')
plt.xlabel('Product ID')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.show()

# Scatter Plot - Units Sold vs Unit Price
plt.scatter(units_sold, unit_price)
plt.title('Scatter - Units Sold vs Unit Price')
plt.xlabel('Units Sold')
plt.ylabel('Unit Price')
plt.show()

# Pie Chart - Proportion of Units Sold
plt.pie(units_sold, labels=product_ids, autopct='%1.1f%%')
plt.title('Pie - Units Sold Distribution')
plt.show()

# 3D Scatter Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(units_sold, unit_price, total_sales)
ax.set_xlabel('Units Sold')
ax.set_ylabel('Unit Price')
ax.set_zlabel('Total Sales')
plt.title('3D Scatter - Sales Overview')
plt.show()
