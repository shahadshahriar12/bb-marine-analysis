import xarray as xr
import pandas as pd

from regions import regions

ds = xr.open_dataset("data/sst_salinity/bay_of_bengal_2020_2026.nc")

# surface layer (~0.5 m)
surface = ds.isel(depth=0)

records = []

for region_name, bounds in regions.items():

    region_ds = surface.sel(
        latitude=slice(bounds["lat_min"], bounds["lat_max"]),
        longitude=slice(bounds["lon_min"], bounds["lon_max"])
    )

    for t in range(len(region_ds.time)):

        monthly_sst = (
            region_ds.thetao
            .isel(time=t)
            .mean()
            .item()
        )

        monthly_sal = (
            region_ds.so
            .isel(time=t)
            .mean()
            .item()
        )

        records.append({
            "month": str(region_ds.time.values[t])[:7],
            "region": region_name,
            "sst_mean": monthly_sst,
            "salinity_mean": monthly_sal
        })

df = pd.DataFrame(records)

df.to_csv(
    "outputs/sst_salinity/monthly_sst_salinity.csv",
    index=False
)

print(df.head())
print()
print("Rows:", len(df))
print("Saved to outputs/sst_salinity/monthly_sst_salinity.csv")