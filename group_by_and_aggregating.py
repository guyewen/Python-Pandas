import pandas as pd

df = pd.read_csv(r"C:\PythonProject\PandasProject\Data\Flavors.csv")

# Group by certain column
df_grouped = df.groupby('Base Flavor')

# Find the mean for each group
df_grouped_mean = df_grouped.mean(True)

# count each group
df_grouped_count = df_grouped.count()

# min & max, if only want number, put True as parameter
df_grouped_min = df_grouped.min()
df_grouped_max = df_grouped.max(True)

# sum
df_grouped_sum = df_grouped.sum(True)

# describe, the distribution of the data
df_grouped_describe = df_grouped.describe()

# aggregate on columns
df_grouped_agg = df_grouped.agg({'Flavor Rating': ['mean', 'sum'], 'Texture Rating': ['min', 'max']})

# Group by multiple columns
df_grouped_multi = df.groupby(['Base Flavor', 'Liked'])
df_grouped_multi_mean = df_grouped_multi.mean(True)

# aggregate on multi-group-by
df_grouped_multi_agg = df_grouped_multi.agg({'Flavor Rating': ['mean', 'sum'], 'Texture Rating': ['min', 'max']})

print(df_grouped_describe)
