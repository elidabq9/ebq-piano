print("Hello world")

import pandas as pd
fileA = pd.read_csv("fileA.csv")
fileB = pd.read_csv("fileB.csv")

fileA.head()
fileB.head()

print(fileA.head())

inner_merged = pd.merge(fileA, fileB)
print(inner_merged)