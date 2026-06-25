import copernicusmarine

copernicusmarine.subset(
    dataset_id="cmems_mod_glo_bgc_my_0.25deg_P1M-m",

    variables=[
        "chl",
        "fe",
        "no3",
        "nppv",
        "o2",
        "ph",
        "phyc",
        "po4",
        "si",
        "spco2"
    ],

    minimum_longitude=88,
    maximum_longitude=93,
    minimum_latitude=20,
    maximum_latitude=23,

    start_datetime="2020-01-01T00:00:00",
    end_datetime="2026-04-30T23:59:59",

    output_filename="data/biogeochemistry/bay_of_bengal_biogeochemistry_2020_2026.nc"
)