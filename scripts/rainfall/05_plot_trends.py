import os
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------
# Create output folder
# ------------------------------------

os.makedirs("outputs/rainfall/plots", exist_ok=True)

# ------------------------------------
# Read CSV
# ------------------------------------

df = pd.read_csv("outputs/rainfall/monthly_rainfall.csv")

df["month"] = pd.to_datetime(df["month"])

regions = df["region"].unique()

# ------------------------------------
# Individual plots
# ------------------------------------

for r in regions:

    temp = df[df["region"] == r]

    plt.figure(figsize=(8,4))

    plt.plot(
        temp["month"],
        temp["average_rainfall_mm_per_hour"],
        marker="o"
    )

    plt.title(f"Monthly Rainfall Trend - {r}")
    plt.xlabel("Time")
    plt.ylabel("Rainfall (mm/hr)")
    plt.grid(True)
    plt.tight_layout()

    safe_name = r.replace(" ", "_")

    plt.savefig(
        f"outputs/rainfall/plots/{safe_name}_rainfall.png",
        dpi=300
    )

    plt.close()

# ------------------------------------
# Combined plot
# ------------------------------------

plt.figure(figsize=(10,5))

for r in regions:

    temp = df[df["region"] == r]

    plt.plot(
        temp["month"],
        temp["average_rainfall_mm_per_hour"],
        label=r
    )

plt.title("Monthly Rainfall Trends")
plt.xlabel("Time")
plt.ylabel("Rainfall (mm/hr)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "outputs/rainfall/plots/all_regions_rainfall.png",
    dpi=300
)

plt.close()

print("All rainfall plots saved.")