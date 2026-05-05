Program: Write a program to use the matplotlib and plot various graph like line plot, scatter plot, Box plots, bar charts, pie charts etc.

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 1. Line Plot
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2. Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 3. Bar Chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 4. Pie Chart
plt.figure()
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(y, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# 5. Box Plot
plt.figure()
data = [y, [5, 15, 20, 35, 50]]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()