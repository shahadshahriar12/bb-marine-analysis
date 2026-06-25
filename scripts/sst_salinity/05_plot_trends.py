import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output folders
os.makedirs("outputs/sst_salinity/plots/sst", exist_ok=True)
os.makedirs("outputs/sst_salinity/plots/salinity", exist_ok=True)

df = pd.read_csv("outputs/sst_salinity/monthly_sst_salinity.csv")

# Convert month column to datetime
df["month"] = pd.to_datetime(df["month"])

regions = df["region"].unique()

# ==================================================
# SST: Individual region plots
# ==================================================

for r in regions:
    temp = df[df["region"] == r]

    plt.figure(figsize=(8, 4))
    plt.plot(temp["month"], temp["sst_mean"], marker="o")
    plt.title(f"SST Trend - {r}")
    plt.xlabel("Time")
    plt.ylabel("SST (°C)")
    plt.grid(True)
    plt.tight_layout()

    safe_name = r.replace(" ", "_")
    plt.savefig(
        f"outputs/sst_salinity/plots/sst/{safe_name}_sst.png",
        dpi=300
    )
    plt.close()

# ==================================================
# SST: Combined plot
# ==================================================

plt.figure(figsize=(10, 5))

for r in regions:
    temp = df[df["region"] == r]
    plt.plot(temp["month"], temp["sst_mean"], label=r)

plt.title("Monthly Sea Surface Temperature (SST) Trends")
plt.xlabel("Time")
plt.ylabel("SST (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    f"outputs/sst_salinity/plots/sst/all_regions_sst.png",
    dpi=300
)
plt.close()

# ==================================================
# Salinity: Individual region plots
# ==================================================

for r in regions:
    temp = df[df["region"] == r]

    plt.figure(figsize=(8, 4))
    plt.plot(temp["month"], temp["salinity_mean"], marker="o")
    plt.title(f"Salinity Trend - {r}")
    plt.xlabel("Time")
    plt.ylabel("Salinity (PSU)")
    plt.grid(True)
    plt.tight_layout()

    safe_name = r.replace(" ", "_")
    plt.savefig(
        f"outputs/sst_salinity/plots/salinity/{safe_name}_salinity.png",
        dpi=300
    )
    plt.close()

# ==================================================
# Salinity: Combined plot
# ==================================================

plt.figure(figsize=(10, 5))

for r in regions:
    temp = df[df["region"] == r]
    plt.plot(temp["month"], temp["salinity_mean"], label=r)

plt.title("Monthly Sea Surface Salinity Trends")
plt.xlabel("Time")
plt.ylabel("Salinity (PSU)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    f"outputs/sst_salinity/plots/salinity/all_regions_salinity.png",
    dpi=300
)
plt.close()

print("All plots saved.")