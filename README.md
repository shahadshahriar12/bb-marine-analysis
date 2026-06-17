# 🌊 Bay of Bengal Oceanographic Data Pipeline (2020–2026)

This project implements a reproducible Python-based workflow to extract, process, and analyze monthly sea surface temperature (SST) and sea surface salinity (SSS) from Copernicus Marine reanalysis data for selected coastal and offshore regions of the Bay of Bengal.

The final output is a structured dataset of polygon-averaged oceanographic variables suitable for climate analysis, fisheries research, and environmental studies.

---

# 📌 Study Objective

To compute monthly spatial averages of:
- Sea Surface Temperature (SST)
- Sea Surface Salinity (SSS)

across six predefined marine and coastal regions in the northern Bay of Bengal from January 2020 to April 2026.

---

# 🌍 Study Regions

The following regions were analyzed using rectangular polygon approximations:

- Swatch of No Ground  
- Middle Ground  
- South Patches  
- South of South Patches  
- Kuakata Beach (coastal buffer zone)  
- Patenga Beach (coastal buffer zone)

Each region is defined using latitude–longitude bounding boxes.

---

# 🧾 Data Source

Ocean reanalysis data was obtained from:

- Copernicus Marine Service  
  https://marine.copernicus.eu  

Dataset:
- GLOBAL_MULTIYEAR_PHY_001_030 (monthly mean product)

Variables used:
- `thetao` → Sea Water Temperature (°C)
- `so` → Sea Water Salinity (PSU)

Spatial resolution:
- ~0.083° global grid

Temporal coverage:
- January 2020 – April 2026

---

# ⚙️ Methodology

## 1. Environment Setup

A Python virtual environment (`venv`) was used with the following dependencies:

- xarray
- netCDF4
- numpy
- pandas
- copernicusmarine

---

## 2. Data Download

A subset of global reanalysis data was downloaded using the Copernicus Marine Python API:

- Region: Bay of Bengal (88°E–93°E, 20°N–23°N)
- Variables: SST (`thetao`), Salinity (`so`)
- Time range: 2020–2026

Output format:
- NetCDF (`.nc`)

---

## 3. Data Structure

The downloaded dataset contains:

- Dimensions:
  - time (monthly, 76 steps)
  - depth (50 levels)
  - latitude
  - longitude

- Variables:
  - `thetao(time, depth, lat, lon)`
  - `so(time, depth, lat, lon)`

Surface values were extracted using:
- depth level = 0 (≈ 0.5 m)

---

## 4. Region Definition

Each study region was defined using bounding boxes:

[lat_min, lat_max, lon_min, lon_max]

# 📊 Output

The pipeline generates: outputs/monthly_sst_salinity.csv


Format:

| Month   | Region                | SST_mean | Salinity_mean |
|----------|----------------------|----------|----------------|
| 2020-01  | Swatch_of_No_Ground  | ...      | ...            |

Total records:
- 76 months × 6 regions = **456 rows**

---

# 🧪 Setup

## 1. Clone repo

```bash
git clone <your-repo-url>
cd bb-ocean-analysis
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run analysis

```bash
python scripts/01_download.py
python scripts/04_extract_all.py
```

---

# 📂 File Structure

bb-ocean-analysis/
│
├── data/
├── outputs/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore

```