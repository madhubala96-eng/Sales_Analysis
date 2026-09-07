import pandas as pd 
data = pd.read_csv(.."/data/sales/.csv")
data["sales"]= data["quantity]*data["price"]
print("total sales:",data["sales"].sum())
