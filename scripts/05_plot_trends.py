import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/monthly_sst_salinity.csv")

# Convert month to datetime for proper plotting
df["month"] = pd.to_datetime(df["month"])

regions = df["region"].unique()

# ---------------------------
# SST Plot
# ---------------------------
plt.figure()

for r in regions:
    temp = df[df["region"] == r]
    plt.plot(temp["month"], temp["sst_mean"], label=r)

plt.title("Monthly Sea Surface Temperature (SST) Trends")
plt.xlabel("Time")
plt.ylabel("SST (°C)")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/sst_trends.png", dpi=300)
plt.close()


# ---------------------------
# Salinity Plot
# ---------------------------
plt.figure()

for r in regions:
    temp = df[df["region"] == r]
    plt.plot(temp["month"], temp["salinity_mean"], label=r)

plt.title("Monthly Sea Surface Salinity Trends")
plt.xlabel("Time")
plt.ylabel("Salinity (PSU)")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/salinity_trends.png", dpi=300)
plt.close()

print("Plots saved in outputs/")