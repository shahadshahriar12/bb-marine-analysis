import os
import xarray as xr

# Find the first monthly rainfall file
folder = "data/rainfall"

files = sorted(
    f for f in os.listdir(folder)
    if f.endswith(".HDF5")
)

filename = os.path.join(folder, files[0])

# Open the Grid group
ds = xr.open_dataset(
    filename,
    group="Grid",
    engine="netcdf4"
)

# -----------------------------
# Swatch of No Ground
# -----------------------------

region = ds.sel(
    lon=slice(89.00, 90.00),
    lat=slice(21.00, 21.21)
)

print(region)

rainfall_mean = region["precipitation"].mean().item()

print()
print("Mean Rainfall:", rainfall_mean, "mm/hr")