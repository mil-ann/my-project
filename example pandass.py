import pandas as pd
data = {
    'name' : ('saroj','asish','samrat','dipson'),
    'age' : (20 ,21 ,22 ,23),
    'city': ('bkt','ktm','kalanki','radhe')
}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv(r'C:\Users\Hp\Desktop\csv.csv')
print(df)
df.head(12)
df = df.dropna()
#df.isnull()
print(df)

