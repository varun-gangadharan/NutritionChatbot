import os
import pandas as pd

food_path = os.path.join("data", "food.csv")
food_df = pd.read_csv(food_path)
print(food_df.head())
df = food_df
print(df[df['Description'].str.lower().replace('[^a-zA-Z\s]', '', regex=True).str.contains('chicken thighs')].head(1)['Data.Protein'])

df['processed_description'] = df['Description'].str.lower().str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

# Define the condition using all necessary keywords
condition = (
    df['processed_description'].str.contains('fat') &
    df['processed_description'].str.contains('free') &
    df['processed_description'].str.contains('half') &
    df['processed_description'].str.contains('and') &
    df['processed_description'].str.contains('half')
)

# Filter the DataFrame based on the condition and get the first row
#print(df[condition].head(1))