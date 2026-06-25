import xarray as xr

ds = xr.open_dataset("data/sst_salinity/bay_of_bengal_2020_2026.nc")

# Surface layer
surface = ds.isel(depth=0)

# Swatch of No Ground
region = surface.sel(
    latitude=slice(21.00, 21.21),
    longitude=slice(89.00, 90.00)
)

print(region)

sst_mean = region.thetao.mean().item()
sal_mean = region.so.mean().item()

print("SST Mean:", sst_mean)
print("Salinity Mean:", sal_mean)