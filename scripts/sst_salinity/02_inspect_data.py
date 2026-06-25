import xarray as xr

ds = xr.open_dataset("data/sst_salinity/bay_of_bengal_2020_2026.nc")

print(ds)