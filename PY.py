import pandas as pd
import matplotlib as plt

data = {
    "SSH": [123,445,511,872],
    "name": ["harsh","bob","john","mike"],
    "age":[29,14,64,32],
    "height":[176,165,187,182],
    "gender": ["m","f","m","m"]
}

df = pd.DataFrame(data)

df.set_index("SSH")
# or 
df.set_index("SSH",implace=True)
print(df)
print(df.head())    # first 5
print(df.head(2))   # first 2 rows
print(df.tail(2))   # last 2 rows

print(df.ndim)  # give us dimensions of our df
print(df.size)  
# give us total number of element in df including rows and columns
print(df.dtypes)# gives datatype of each col 
print(df.T)     # gives transpose of df

print(df["name"])   # get name col
print(df["name"].iloc[1]) # get 2nd name

df["age"].plot  #simply plot it in line graph 
df.show()
df.plot