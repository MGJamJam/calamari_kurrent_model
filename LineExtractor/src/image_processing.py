from PIL import Image, ImageDraw
import numpy as np

class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path).convert("RGBA")

    def draw_polygon(self, points, rectangle=False):
        """Draws a polygon or rectangle on the image."""
        draw = ImageDraw.Draw(self.image)
        x_coords, y_coords = zip(*points)
        if rectangle:
            draw.rectangle([min(x_coords), min(y_coords), max(x_coords), max(y_coords)], outline="red", width=2)
        else:
            draw.polygon(points, outline='red', width=2)

    def crop_polygon(self, points):
        """Crop the polygon area from the image."""
        mask = Image.new('L', self.image.size, 0)
        ImageDraw.Draw(mask).polygon(points, outline=1, fill=1)
        mask = np.array(mask)

        image_array = np.array(self.image)
        new_image_array = image_array.copy()
        new_image_array[:, :, 3] = mask * 255

        cropped_image = Image.fromarray(new_image_array, 'RGBA')
        bbox = cropped_image.getbbox()
        if bbox:
            return cropped_image.crop(bbox), bbox
        return cropped_image, None

    def save_image(self, output_path):
        """Save the processed image to the given path."""
        self.image.save(output_path)
