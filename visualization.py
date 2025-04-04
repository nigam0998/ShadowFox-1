import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# Create a Line Plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line Graph')

# Labels and Title
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Line Plot Example")

# Show Plot
plt.legend()
plt.show()
# Create a DataFrame
data = pd.DataFrame({
    "X": [1, 2, 3, 4, 5, 6],
    "Y": [5, 15, 25, 30, 10, 50]
})

# Seaborn Scatter Plot
sns.scatterplot(x="X", y="Y", data=data)

# Show Plot
plt.title("Scatter Plot Example")
plt.show()
# Sample Data
x = ["A", "B", "C", "D"]
y = [20, 34, 30, 35]

# Bar Chart
plt.bar(x, y, color=['red', 'blue', 'green', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")

# Show Plot
plt.show()
# Generate random data
data = np.random.randn(100)

# Box Plot
sns.boxplot(data=data)
plt.title("Box Plot Example")
plt.show()
# Generate sample correlation data
corr_data = np.random.rand(5, 5)
df_corr = pd.DataFrame(corr_data, columns=['A', 'B', 'C', 'D', 'E'])

# Heatmap
sns.heatmap(df_corr, annot=True, cmap="coolwarm")
plt.title("Heatmap Example")
plt.show()
