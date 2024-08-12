from PIL import Image, ImageDraw, ImageFont

from boxes_define import gdf

# Function to draw the bounding boxes on the image
def draw_bounding_boxes(image_path, gdf):
    image = Image.open(image_path+'bird.png').convert("RGB")
    # Convert the image to an editable format
    draw = ImageDraw.Draw(image)

    # Optional: Load a font (requires a TTF file)
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    # Draw each bounding box on the image
    for _, row in gdf.iterrows():
        xmin, ymin, xmax, ymax = row['geometry'].bounds
        draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)
        draw.text((xmin, ymin-10), row['name'], fill="red", font=font)

    image.save(image_path+'bird_boxed.png', "PNG")

if __name__ == "__main__":
    draw_bounding_boxes('assets/images/', gdf)