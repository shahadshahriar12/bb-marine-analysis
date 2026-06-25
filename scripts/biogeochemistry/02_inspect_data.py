import xarray as xr

ds = xr.open_dataset("data/biogeochemistry/bay_of_bengal_biogeochemistry_2020_2026.nc")

print(ds)