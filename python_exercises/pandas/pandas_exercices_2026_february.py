import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "A", "C", "B"],
    "price": [10, 15, 10, 20, 15],
    "quantity": [2, 1, 3, 5, 2]
})

print("----Exercice1----")
print(df.head())
print(df.shape)
df.info()
print(df.dtypes)