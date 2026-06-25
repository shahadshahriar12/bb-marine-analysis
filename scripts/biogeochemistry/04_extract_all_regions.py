import xarray as xr
import pandas as pd
from regions import regions

# Load dataset
ds = xr.open_dataset(
    "data/biogeochemistry/bay_of_bengal_biogeochemistry_2020_2026.nc"
)

surface = ds  # already surface-based

records = []

for region_name, bounds in regions.items():

    region_ds = surface.sel(
        latitude=slice(bounds["lat_min"], bounds["lat_max"]),
        longitude=slice(bounds["lon_min"], bounds["lon_max"])
    )

    for t in range(len(region_ds.time)):

        # Helper for safe mean
        def mean(var):
            return region_ds[var].isel(time=t).mean().item()

        records.append({
            "month": str(region_ds.time.values[t])[:7],
            "region": region_name,

            # 🌊 Biology
            "chlorophyll_a": mean("chl"),
            "phytoplankton_carbon": mean("phyc"),
            "primary_productivity": mean("nppv"),

            # 🧪 Chemistry
            "dissolved_oxygen": mean("o2"),
            "ph": mean("ph"),
            "pco2_surface": mean("spco2"),

            # 🌱 Nutrients
            "nitrate": mean("no3"),
            "phosphate": mean("po4"),
            "silicate": mean("si"),
            "iron": mean("fe"),
        })

# Convert to DataFrame
df = pd.DataFrame(records)

# Save output
output_path = "outputs/biogeochemistry/monthly_biogeochemistry.csv"
df.to_csv(output_path, index=False)

print(df.head())
print()
print("Rows:", len(df))
print("Saved to:", output_path)