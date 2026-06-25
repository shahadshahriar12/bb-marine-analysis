import xarray as xr

# Load dataset
ds = xr.open_dataset(
    "data/biogeochemistry/bay_of_bengal_biogeochemistry_2020_2026.nc"
)

# Surface layer (already 2D variables at surface)
surface = ds

# Swatch of No Ground region
region = surface.sel(
    latitude=slice(21.00, 21.21),
    longitude=slice(89.00, 90.00)
)

print("\n=== REGION DATA ===\n")
print(region)

# -------------------------
# Compute means safely
# -------------------------

def safe_mean(var):
    if var in region.data_vars:
        return region[var].mean().item()
    return None

results = {
    "chl_mean": safe_mean("chl"),
    "o2_mean": safe_mean("o2"),
    "no3_mean": safe_mean("no3"),
    "po4_mean": safe_mean("po4"),
    "si_mean": safe_mean("si"),
    "ph_mean": safe_mean("ph"),
    "fe_mean": safe_mean("fe"),
    "nppv_mean": safe_mean("nppv"),
    "phyc_mean": safe_mean("phyc"),
    "spco2_mean": safe_mean("spco2"),
}

print("\n=== REGION MEAN VALUES ===\n")
for k, v in results.items():
    print(f"{k}: {v}")