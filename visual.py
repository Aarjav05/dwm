import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "F1Drivers_Dataset.csv"  # Adjust this path if needed
df = pd.read_csv(file_path)

# Clean and preprocess data
df['Race_Wins'] = pd.to_numeric(df['Race_Wins'], errors='coerce')
df['Points'] = pd.to_numeric(df['Points'], errors='coerce')
df['Nationality'] = df['Nationality'].fillna('Unknown')
df['Decade'] = pd.to_numeric(df['Decade'], errors='coerce')
df['Champion'] = df['Champion'].fillna(False)

# 1. Top 10 Drivers by Race Wins
top_winners = df[['Driver', 'Race_Wins']].sort_values(by='Race_Wins', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top_winners['Driver'][::-1], top_winners['Race_Wins'][::-1])
plt.title('Top 10 F1 Drivers by Race Wins')
plt.xlabel('Race Wins')
plt.ylabel('Driver')
plt.tight_layout()
plt.show()

# 2. Average Points per Driver by Decade
points_by_decade = df.groupby('Decade')['Points'].mean().dropna()

plt.figure(figsize=(8,5))
plt.plot(points_by_decade.index, points_by_decade.values, marker='o')
plt.title('Average Points per Driver by Decade')
plt.xlabel('Decade')
plt.ylabel('Average Points')
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Distribution of Drivers by Nationality (Top 10)
top_nationalities = df['Nationality'].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.bar(top_nationalities.index, top_nationalities.values)
plt.title('Top 10 Nationalities of F1 Drivers')
plt.xlabel('Nationality')
plt.ylabel('Number of Drivers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Champion vs Non-Champion Count
champion_counts = df['Champion'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(champion_counts, labels=['Non-Champions', 'Champions'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Champion vs Non-Champion Drivers')
plt.tight_layout()
plt.show()
