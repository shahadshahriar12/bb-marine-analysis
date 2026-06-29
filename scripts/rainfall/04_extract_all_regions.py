import os
import xarray as xr
import pandas as pd

from regions import regions

# -----------------------------
# Input / Output
# -----------------------------

folder = "data/rainfall"
output_csv = "outputs/rainfall/monthly_rainfall.csv"

files = sorted(
    f for f in os.listdir(folder)
    if f.endswith(".HDF5")
)

records = []

# -----------------------------
# Process every monthly file
# -----------------------------

for file in files:

    filename = os.path.join(folder, file)

    ds = xr.open_dataset(
        filename,
        group="Grid",
        engine="netcdf4"
    )

    # Extract month (YYYY-MM)
    month = str(ds.time.values[0])[:7]

    # Loop through all regions
    for region_name, bounds in regions.items():

        region_ds = ds.sel(
            lon=slice(bounds["lon_min"], bounds["lon_max"]),
            lat=slice(bounds["lat_min"], bounds["lat_max"])
        )

        rainfall = (
            region_ds["precipitation"]
            .mean()
            .item()
        )

        records.append({
            "month": month,
            "region": region_name,
            "average_rainfall_mm_per_hour": rainfall
        })

# -----------------------------
# Save CSV
# -----------------------------

df = pd.DataFrame(records)

df.to_csv(
    output_csv,
    index=False
)

print(df.head())
print()
print("Rows:", len(df))
print(f"Saved to {output_csv}")