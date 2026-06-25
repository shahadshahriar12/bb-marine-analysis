import os
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv("outputs/biogeochemistry/monthly_biogeochemistry.csv")

df["month"] = pd.to_datetime(df["month"])
regions = df["region"].unique()

# ----------------------------
# Create folders
# ----------------------------
base = "outputs/biogeochemistry/plots"

for var in [
    "chlorophyll_a",
    "dissolved_oxygen",
    "nitrate",
    "phosphate",
    "silicate",
    "ph",
    "iron",
    "primary_productivity",
    "phytoplankton_carbon",
    "pco2_surface"
]:
    os.makedirs(f"{base}/{var}", exist_ok=True)

# ----------------------------
# Helper function
# ----------------------------
def plot_variable(var, ylabel):
    # Individual region plots
    for r in regions:
        temp = df[df["region"] == r]

        plt.figure(figsize=(8, 4))
        plt.plot(temp["month"], temp[var], marker="o")

        plt.title(f"{ylabel} Trend - {r}")
        plt.xlabel("Time")
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.tight_layout()

        safe_name = r.replace(" ", "_")

        plt.savefig(
            f"{base}/{var}/{safe_name}_{var}.png",
            dpi=300
        )
        plt.close()

    # Combined plot
    plt.figure(figsize=(10, 5))

    for r in regions:
        temp = df[df["region"] == r]
        plt.plot(temp["month"], temp[var], label=r)

    plt.title(f"Monthly {ylabel} Trends")
    plt.xlabel("Time")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        f"{base}/{var}/all_regions_{var}.png",
        dpi=300
    )
    plt.close()


# ----------------------------
# Generate plots
# ----------------------------

plot_variable("chlorophyll_a", "Chlorophyll-a (mg/m³)")
plot_variable("dissolved_oxygen", "Dissolved Oxygen (mmol/m³)")
plot_variable("nitrate", "Nitrate (mmol/m³)")
plot_variable("phosphate", "Phosphate (mmol/m³)")
plot_variable("silicate", "Silicate (mmol/m³)")
plot_variable("ph", "pH")
plot_variable("iron", "Iron (mmol/m³)")
plot_variable("primary_productivity", "Primary Productivity")
plot_variable("phytoplankton_carbon", "Phytoplankton Carbon")
plot_variable("pco2_surface", "Surface pCO₂")

print("All biogeochemistry plots saved successfully.")