import pandas as pd

# Set index when reading the file
df = pd.read_csv(r"C:\PythonProject\PandasProject\Data\world_population.csv", index_col="Country")

# reset index
df.reset_index(inplace=True)

# manually set index
df.set_index('Country', inplace=True)

# multiple index
df.reset_index(inplace=True)
df.set_index(['Continent', 'Country'], inplace=True)

# sort based on index
df.sort_index(inplace=True)
# pd.set_option('display.max.rows', None)

# after sorting, get all asia countries
asia_countries = df.loc['Asia']
# Can also get a specific country
specific_country = df.loc['Europe', 'Sweden']

print(specific_country)
