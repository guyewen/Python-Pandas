import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# can print out and check all available style
# print(plt.style.available)
# plt.style.use('classic')  # set style

df = pd.read_csv(r"C:\PythonProject\PandasProject\Data\Ice Cream Ratings.csv").set_index('Date')
df.plot()
plt.close()  # close current active figure

# subplots separate each column into a single graph
df.plot(kind='line', subplots=True, title='Ice Cream Ratings', ylabel='Rating')
plt.close()

# bar chart
df.plot(kind='bar', stacked=True)
plt.close()

# only visualize part of the table
df['Flavor Rating'].plot(kind='bar')
plt.close()

# horizontal bar chart
df.plot.barh()
plt.close()

# scatter chart, need to give x-axis and y-axis
# optional: s is the size of the dot, c is color
df.plot.scatter(x='Texture Rating', y='Overall Rating', s=100, c='red')
plt.close()

# histogram
df.plot.hist(bins=20)
plt.close()

# boxplot
df.boxplot()
plt.close()

# area, figsize() to set the size
df.plot.area(figsize=(10, 5))
plt.close()

# pie chart
df.plot.pie(y='Flavor Rating', figsize=(10, 6))

plt.show()  # show the visualizations
