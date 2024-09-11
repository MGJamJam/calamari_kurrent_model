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

        # Create a black and white mask (mode 'L') of the same size as the original image
        mask = Image.new('L', self.image.size, 0)
        # Draw the polygon on the mask, filling the polygon area with 1 (white)
        ImageDraw.Draw(mask).polygon(points, outline=1, fill=1)
        # Convert the mask and original image to a NumPy array for easier manipulation
        mask = np.array(mask)
        image_array = np.array(self.image)

        new_image_array = image_array.copy()
        # Set the alpha channel of the image based on the mask. The masked areas (polygon) will become opaque (255)
        new_image_array[:, :, 3] = mask * 255

        # Convert the modified NumPy array back to an RGBA image
        cropped_image = Image.fromarray(new_image_array, 'RGBA')
        # Get the bounding box (bbox) of the opaque region in the image (the polygon)
        bbox = cropped_image.getbbox()
        if bbox:
            return cropped_image.crop(bbox), bbox
        else:
            raise Exception("No bounding box for cropped image")

    def save_image(self, output_path):
        """Save the processed image to the given path."""
        self.image.save(output_path)
