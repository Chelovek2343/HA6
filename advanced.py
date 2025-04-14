import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

# Load sales data
df = pd.read_csv('sales_data.csv')

# We'll use only the first 10 rows for these visualizations
subset = df.head(10)

# ----- Box Plot: show distribution of Units_Sold, Unit_Price, Total_Sales
data = [subset['Units_Sold'], subset['Unit_Price'], subset['Total_Sales']]
plt.boxplot(data, labels=['Units Sold', 'Unit Price', 'Total Sales'])
plt.title('Box Plot of Sales Data')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()

# ----- 2D Heatmap: correlation heatmap of numeric columns
correlation = df[['Units_Sold', 'Unit_Price', 'Total_Sales']].corr()
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlation)), correlation.columns)
plt.yticks(range(len(correlation)), correlation.columns)
plt.title('2D Heatmap - Correlation')
plt.show()

# ----- Stacked Bar: show stacked bar of Units_Sold for top 4 Products over 3 years
grouped = df.groupby(['Product_ID', 'Year'])['Units_Sold'].sum().unstack(fill_value=0)
grouped = grouped.head(4)  # Take first 4 products

labels = grouped.index
year_1, year_2, year_3 = grouped.columns

plt.bar(labels, grouped[year_1], label=str(year_1))
plt.bar(labels, grouped[year_2], bottom=grouped[year_1], label=str(year_2))
plt.bar(labels, grouped[year_3], bottom=grouped[year_1] + grouped[year_2], label=str(year_3))
plt.xlabel('Product ID')
plt.ylabel('Units Sold')
plt.title('Stacked Bar - Units Sold Over Years')
plt.legend()
plt.show()

# ----- Gantt Chart: simulate tasks using rows (each task is a product sale)
tasks = subset['Product_ID']
start_times = subset['Day']
durations = np.random.randint(1, 5, size=len(subset))  # Simulated durations
plt.barh(tasks, durations, left=start_times, color='skyblue')
plt.xlabel('Day')
plt.ylabel('Product ID')
plt.title('Gantt Chart - Simulated Sales Activity')
plt.show()

# ----- Polar Plot: show total sales in polar form by angle (10 items)
angles = np.linspace(0, 2 * np.pi, len(subset), endpoint=False)
radii = subset['Total_Sales'].values

plt.subplot(111, projection='polar')
plt.plot(angles, radii, marker='o')
plt.title('Polar Plot - Total Sales Distribution')
plt.show()
