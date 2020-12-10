import pandas as pd

# Note Examples
df = pd.read_csv("cellphone.csv")

print(df.head())
print(df.columns)
print(df.shape)

print(df.iloc[0,1])
print(df.loc[:,['Provider','Price']].head())

print(df.loc[:1,:])

new_row = ['C',8,2,100,100,1]
df.loc[8,:] = new_row
print(df,'\n')

df.drop(8,inplace=True)
print(df,'\n')

new_column = df.loc[:,'Price']/df.loc[:,'Data']
name_new_column = "£/GB"
position_new_column = 6
df.insert(position_new_column, name_new_column, new_column)
print(df,'\n')

df.drop('£/GB',axis=1,inplace=True)
print(df,'\n')

filtered_rows = df.loc[:,'Price']<10
print(filtered_rows,'\n')

print(df[filtered_rows],'\n')

max_data = df.loc[:,'Data'].max()
mean_data = df.loc[:,'Data'].mean()
print(max_data)
print(mean_data,'\n')

grouped = df.groupby(['Provider'])
print(grouped.size())

grouped = df.groupby(['Provider','Voice'])
print(grouped.size())

print(df.groupby(['Provider']).mean()["Price"])







