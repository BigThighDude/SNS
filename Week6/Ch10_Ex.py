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

# End of notes

# Exercise 1
df = pd.read_csv("ws.csv")

# Exercise 2
print(df.shape[0]) # 30,922 packets

# Exercise 3
print(df.columns)
print(len(df.columns))  # 7 columns

# Exercise 4
# df.drop(str(df.columns[-1]), axis = 1, inplace = True)
print(df.columns)

# Exercise 5
# df.insert(6, 'Time per Length', df.loc[:,'Time']/df.loc[:,'Length'])
print(df.columns)

# Exercise 6
print(df.loc[:,'Length'].max()) # Max Length is 1434

# Exercise 7
print(df.loc[:,'Length'].mean()) # Mean Length is 769

# Exercise 8
# Flow = IP src, IP dest, TCP src, TCP dest
print(df.shape[0])
df = df[df['Protocol'] != 'TCP']
print(df.shape)

x = df['Info']
print(x.str.split(r""))
















