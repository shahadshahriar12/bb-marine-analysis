import xarray as xr

ds = xr.open_dataset("data/bay_of_bengal_2020_2026.nc")

print(ds)