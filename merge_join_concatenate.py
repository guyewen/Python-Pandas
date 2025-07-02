import pandas as pd

df1 = pd.read_csv(r"C:\PythonProject\PandasProject\Data\LOTR.csv")
df2 = pd.read_csv(r"C:\PythonProject\PandasProject\Data\LOTR 2.csv")

# merge function
# by default inner join
default_join = df1.merge(df2)

# same inner join, you can specify based on which columns to merge
inner_join = df1.merge(df2, how='inner', on=['FellowshipID', 'FirstName'])

# outer join
outer_join = df1.merge(df2, how='outer')

# left join
left_join = df1.merge(df2, how='left')

# right join
right_join = df1.merge(df2, how='right')

# cross join
cross_join = df1.merge(df2, how='cross')
# merge function

# join function
join1 = df1.join(df2, on='FellowshipID', how='outer', lsuffix='_Left', rsuffix='_Right')

# join function with index
join1_index = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix='_Left', rsuffix='_Right')

# concatenate, put everything together in 1 table
concat1 = pd.concat([df1, df2])

# only put shared columns together
concat2 = pd.concat([df1, df2], join='inner')

print(concat2)
