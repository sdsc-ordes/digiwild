import geopandas as gpd
from shapely.geometry import box

bounding_boxes = [
    # 'Head incl. eyes',
    box(250, 375, 350, 500),
    # 'Beak and mouth region',
    box(200, 450, 250, 500),
    # 'Feathers/Wings', 
    box(10, 10, 50, 50), 
    # 'Legs', 
    box(325, 575, 450, 675),
    # 'Body'
    box(500, 500, 500, 500)
]

# Create a GeoDataFrame from these boxes
gdf = gpd.GeoDataFrame({'geometry': bounding_boxes, 
                        'name': ['Head incl. eyes',
                                 'Beak and mouth region',
                                 'Feathers/Wings', 
                                 'Legs', 
                                 'Body']})
