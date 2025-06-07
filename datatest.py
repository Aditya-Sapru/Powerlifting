import pandas as pd
import matplotlib.pyplot as plt 
import math 

# Load dataset
df = pd.read_csv("debloated_powerlifting.csv")
df = df[df["Equipment"] == "Raw"]
# Only males
men_df = df[df["Sex"] == "M"]

# Only females
women_df = df[df["Sex"] == "F"]

# Print original DataFrame head
print("📄 Full Dataset:")
print(df.head())

# Print male dataset head
print("\n👨 Male Lifters:")
print(men_df.head())

# Print female dataset head
print("\n👩 Female Lifters:")
print(women_df.head())
