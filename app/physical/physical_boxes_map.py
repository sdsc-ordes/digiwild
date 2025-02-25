from PIL import Image, ImageDraw, ImageFont

from physical_boxes_define import gdf

from dotenv import load_dotenv
import os

load_dotenv()
PATH_ASSETS = os.getenv("PATH_ASSETS")


# Function to draw the bounding boxes on the image
def draw_bounding_boxes(image_path, gdf):
    image = Image.open(image_path + "bird.png").convert("RGB")
    # Convert the image to an editable format
    draw = ImageDraw.Draw(image)

    # Optional: Load a font (requires a TTF file)
    # try:
    font = ImageFont.truetype(PATH_ASSETS + "fonts/LiberationSans-Regular.ttf", 20)

    # Draw each bounding box on the image
    for _, row in gdf.iterrows():
        xmin, ymin, xmax, ymax = row["geometry"].bounds
        draw.rectangle([xmin, ymin, xmax, ymax], outline="purple", width=2)
        draw.text((xmin, ymin - 22), row["name"], fill="black", font=font)

    image.save(image_path + "bird_boxed.png", "PNG")


if __name__ == "__main__":
    draw_bounding_boxes(PATH_ASSETS + "images/", gdf)
