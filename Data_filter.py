import pandas as pd

data = pd.read_csv('ogalla_raw.csv')
df = data.drop_duplicates(subset='StateWellNumber',keep='last')

# Save the filtered DataFrame to a new CSV file named after aquifer
df.to_csv('ogalla2022_data.csv', index=False)

print("complete!!!")