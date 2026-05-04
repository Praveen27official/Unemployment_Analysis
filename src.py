import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/Unemployment_in_India.csv")

# Rename columns
df.columns = ['Region', 'Date', 'Frequency', 'Unemployment Rate',
              'Employed', 'Labour Participation Rate', 'Area']

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

# Drop missing values
df = df.dropna()

print("Dataset Loaded Successfully!")
print(df.head())

# ===============================
# 📊 1. Unemployment Trend
# ===============================
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date', y='Unemployment Rate')
plt.title("Unemployment Rate Over Time")
plt.xticks(rotation=45)
plt.savefig("outputs/plots/unemployment_trend.png")
plt.show()

# ===============================
# 📊 2. State-wise Analysis
# ===============================
plt.figure(figsize=(12,6))
sns.barplot(data=df, x='Region', y='Unemployment Rate')
plt.xticks(rotation=90)
plt.title("State-wise Unemployment")
plt.savefig("outputs/plots/statewise.png")
plt.show()

# ===============================
# 📊 3. COVID Analysis
# ===============================
covid_df = df[df['Date'].dt.year == 2020]

plt.figure(figsize=(12,6))
sns.lineplot(data=covid_df, x='Date', y='Unemployment Rate', hue='Region')
plt.title("Unemployment During COVID-19")
plt.savefig("outputs/plots/covid.png")
plt.show()

# ===============================
# 📊 4. Urban vs Rural
# ===============================
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='Area', y='Unemployment Rate')
plt.title("Urban vs Rural Unemployment")
plt.savefig("outputs/plots/urban_rural.png")
plt.show()
