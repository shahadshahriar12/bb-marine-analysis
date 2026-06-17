import copernicusmarine

copernicusmarine.subset(
    dataset_id="cmems_mod_glo_phy_my_0.083deg_P1M-m",
    
    variables=[
        "thetao",   # Sea Temperature
        "so"        # Salinity
    ],

    minimum_longitude=88,
    maximum_longitude=93,
    minimum_latitude=20,
    maximum_latitude=23,

    start_datetime="2020-01-01T00:00:00",
    end_datetime="2026-12-31T23:59:59",

    output_filename="data/bay_of_bengal_2020_2026.nc"
)