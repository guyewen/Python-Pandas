import pandas as pd

pd.set_option('display.max.columns', 6)
data_csv = pd.read_csv(r"C:\PythonProject\PandasProject\Data\world_population.csv")
# print(data_csv)

# top 10 rank country
top_10_country = data_csv[data_csv['Rank'] <= 10]
# print(top_10_country)

# find a specific group of countries
countries_list = ['China', 'Russia', 'United States']
specific_countries = data_csv[data_csv['Country'].isin(countries_list)]
# print(specific_countries)

# search by a str.contains()
countries_united = data_csv[data_csv['Country'].str.contains('United')]
# print(countries_united)

# set index for a column, e.g. country
data_csv_country = data_csv.set_index('Country')
# print(data_csv_country)

# filter to show only wanted columns
data_csv_country_filtered_1 = data_csv_country.filter(
    items=['CCA3', 'Continent', 'Capital', '2022 Population', 'World Population Percentage'])
# print(data_csv_country_filtered_1)

# filter based on the indexed column, e.g. country, set axis = 0
# you may also set axis = 1, then you are filtering only on the header row
data_csv_country_filtered_2 = data_csv_country.filter(items=['Yemen'], axis=0)
# print(data_csv_country_filtered_2)

# filter with 'like'
data_csv_country_filtered_3 = data_csv_country.filter(like='United', axis=0)
# print(data_csv_country_filtered_3)

# use loc[], to find the specific row based on the key in index
data_csv_country_filtered_4 = data_csv_country.loc['Norway']
# print(data_csv_country_filtered_4)

# use iloc[], integer location
data_csv_country_filtered_5 = data_csv_country.iloc[88]
# print(data_csv_country_filtered_5)

# Sort top 10 countries
# sort_values(by='Key', ascending=Bool), by default ascending=True
top_10_country_sorted = data_csv[data_csv['Rank'] <= 10].sort_values(by='Rank')
# print(top_10_country_sorted)

# Sort continent first, then country
top_10_country_sorted_1 = data_csv[data_csv['Rank'] <= 10].sort_values(by=['Continent', 'Country'],
                                                                       ascending=[False, True])
print(top_10_country_sorted_1.filter(items=['Continent', 'Country', 'Rank']))
