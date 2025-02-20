import geopandas as gpd
from shapely.geometry import box

bounding_boxes = [
    # 'Head incl. eyes',
    box(250, 375, 350, 485),
    # 'Beak and mouth region',
    box(200, 450, 250, 485),
    # 'Feathers/Wings/Tail',
    box(50, 100, 725, 355),
    # 'Legs',
    box(325, 585, 450, 675),
    # 'Body'
    box(275, 510, 500, 565),
]

# Create a GeoDataFrame from these boxes
gdf = gpd.GeoDataFrame(
    {
        "geometry": bounding_boxes,
        "name": ["Head incl. eyes", "Beak", "Feathers/Wings/Tail", "Legs", "Body"],
    }
)
