# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load dataset
file_path = r"C:\Users\ASUS\Downloads\Air_Quality (2).csv"  # Updated dataset file path
df = pd.read_csv(file_path)

# Display basic info and check for missing values
print("Dataset Info:\n")
print(df.info())
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill numeric missing values with the mean (if any)
df = df.fillna(df.mean(numeric_only=True))

# ---------------------------
# 1. Trend of Air Quality Over Time
# ---------------------------
if "Time Period" in df.columns and "Data Value" in df.columns:
    print("\n=== 1. Trend of Air Quality Over Time ===")
    df["Time Period"] = pd.to_datetime(df["Time Period"], errors="coerce")
    air_quality_trend = df.groupby("Time Period")["Data Value"].mean()
    print(air_quality_trend)

    plt.figure()
    air_quality_trend.plot(marker="o", color="blue")
    plt.title("Trend of Air Quality Over Time")
    plt.xlabel("Time Period")
    plt.ylabel("Average Data Value")
    plt.tight_layout()
    plt.show()

# ---------------------------
# 2. Locations with Highest Pollution Levels
# ---------------------------
if "Geo Place Name" in df.columns and "Data Value" in df.columns:
    print("\n=== 2. Locations with Highest Pollution Levels ===")
    top_polluted_locations = df.groupby("Geo Place Name")["Data Value"].mean().sort_values(ascending=False).head(10)
    print(top_polluted_locations)

    plt.figure()
    sns.barplot(x=top_polluted_locations.values, y=top_polluted_locations.index, palette="Reds")
    plt.title("Top 10 Locations with Highest Pollution Levels")
    plt.xlabel("Average Data Value")
    plt.ylabel("Locations")
    plt.tight_layout()
    plt.show()

# ---------------------------
# 3. Air Quality Comparison Between Urban and Rural Areas
# ---------------------------
if "Geo Type Name" in df.columns and "Data Value" in df.columns:
    print("\n=== 3. Air Quality Comparison Between Urban and Rural Areas ===")
    urban_rural_comparison = df.groupby("Geo Type Name")["Data Value"].mean()
    print(urban_rural_comparison)

    plt.figure()
    sns.barplot(x=urban_rural_comparison.index, y=urban_rural_comparison.values, palette="coolwarm")
    plt.title("Air Quality: Urban vs Rural Areas")
    plt.xlabel("Geo Type")
    plt.ylabel("Average Data Value")
    plt.tight_layout()
    plt.show()

# ---------------------------
# 4. Pollutant with the Most Significant Impact
# ---------------------------
if "Name" in df.columns and "Data Value" in df.columns:
    print("\n=== 4. Pollutant with the Most Significant Impact ===")
    pollutant_impact = df.groupby("Name")["Data Value"].mean().sort_values(ascending=False).head(10)
    print(pollutant_impact)

    plt.figure()
    sns.barplot(x=pollutant_impact.values, y=pollutant_impact.index, palette="viridis")
    plt.title("Top 10 Pollutants by Impact")
    plt.xlabel("Average Data Value")
    plt.ylabel("Pollutants")
    plt.tight_layout()
    plt.show()

# ---------------------------
# 5. Most and Least Polluted Locations Over Time
# ---------------------------
if "Geo Place Name" in df.columns and "Time Period" in df.columns and "Data Value" in df.columns:
    print("\n=== 5. Most and Least Polluted Locations Over Time ===")
    most_polluted = df.groupby(["Time Period", "Geo Place Name"])["Data Value"].mean().reset_index()
    most_polluted = most_polluted.sort_values(by="Data Value", ascending=False).head(10)
    least_polluted = df.groupby(["Time Period", "Geo Place Name"])["Data Value"].mean().reset_index()
    least_polluted = least_polluted.sort_values(by="Data Value", ascending=True).head(10)

    print("Most Polluted Locations Over Time:\n", most_polluted)
    print("\nLeast Polluted Locations Over Time:\n", least_polluted)

    plt.figure()
    sns.lineplot(data=most_polluted, x="Time Period", y="Data Value", hue="Geo Place Name", marker="o")
    plt.title("Most Polluted Locations Over Time")
    plt.xlabel("Time Period")
    plt.ylabel("Data Value")
    plt.legend(title="Locations")
    plt.tight_layout()
    plt.show()

    plt.figure()
    sns.lineplot(data=least_polluted, x="Time Period", y="Data Value", hue="Geo Place Name", marker="o")
    plt.title("Least Polluted Locations Over Time")
    plt.xlabel("Time Period")
    plt.ylabel("Data Value")
    plt.legend(title="Locations")
    plt.tight_layout()
    plt.show()
