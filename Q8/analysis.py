import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("quarterly_patient_satisfaction.csv")

avg = df["PatientSatisfaction"].mean()
avg_rounded = round(avg, 2)
print("Average Patient Satisfaction:", avg_rounded)

# Requirement check
assert avg_rounded == 4.79, f"Average must be 4.79, got {avg_rounded}"

# Trend vs Benchmark
plt.figure(figsize=(9, 5))
plt.plot(df["Quarter"], df["PatientSatisfaction"], marker="o", label="Patient Satisfaction")
plt.plot(df["Quarter"], df["Benchmark"], marker="o", linestyle="--", label="Industry Target (4.5)")
plt.title("2024 Quarterly Patient Satisfaction vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("trend_vs_benchmark.png", dpi=150)
plt.close()

# Gap to target
df["GapToTarget"] = df["PatientSatisfaction"] - df["Benchmark"]
plt.figure(figsize=(9, 5))
plt.bar(df["Quarter"], df["GapToTarget"])
plt.axhline(0, linestyle=":")
plt.title("Gap to Target (Positive = Above 4.5)")
plt.xlabel("Quarter")
plt.ylabel("Patient Satisfaction - Target")
plt.tight_layout()
plt.savefig("gap_to_target.png", dpi=150)
plt.close()
