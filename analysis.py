import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

print("📊 Dataset:")
print(df)

# Basic statistics
avg_sleep = df["sleep_hours"].mean()
avg_energy = df["energy_level"].mean()

print("\n🧠 Insights:")
print(f"Average sleep: {avg_sleep}")
print(f"Average energy: {avg_energy}")

# Relationship
correlation = df["sleep_hours"].corr(df["energy_level"])
print(f"Correlation between sleep and energy: {correlation}")

# Plot
plt.plot(df["sleep_hours"], df["energy_level"])
plt.xlabel("Sleep Hours")
plt.ylabel("Energy Level")
plt.title("Sleep vs Energy")
plt.show()
if correlation > 0.7:
    print("👉 Strong positive relationship: more sleep = more energy")
elif correlation > 0.3:
    print("👉 Moderate relationship between sleep and energy")
else:
    print("👉 Weak or no clear relationship")
