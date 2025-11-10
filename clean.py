import pandas as pd
 
# Đọc file Excel
df = pd.read_excel("thu thập data(4).xlsx")

# Chuyển cột Date sang datetime
df["Date"] = pd.to_datetime(df["Date"])

print(df)
