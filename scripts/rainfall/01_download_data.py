import os
import earthaccess

# Login
earthaccess.login(persist=True)

# Search monthly rainfall data
results = earthaccess.search_data(
    short_name="GPM_3IMERGM",
    version="07",
    temporal=("2020-01-01", "2026-06-30"),
)

print(f"Found {len(results)} files.")

# Create output directory
os.makedirs("data/rainfall", exist_ok=True)

# Download all files
earthaccess.download(
    results,
    local_path="data/rainfall"
)

print("\nDownload completed successfully.")