import os
import xarray as xr

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

print("\n=== VARIABLES ===\n")
print(list(ds.data_vars))

print("\n=== DATASET ===\n")
print(ds)

print("\n=== PRECIPITATION ATTRIBUTES ===\n")
print(ds["precipitation"].attrs)