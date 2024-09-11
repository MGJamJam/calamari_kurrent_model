import os
from image_processing import ImageProcessor
from page_xml_processing import PageXMLProcessor
from utils import parse_points


def line_extractor_draw_polygons(xml_path, output_dir):
    # Initialize XML and Image Processor
    xml_processor = PageXMLProcessor(xml_path)
    image_filename = xml_processor.get_page_image_filename()
    image_processor = ImageProcessor(os.path.join(os.path.dirname(xml_path), image_filename))

    # draw polygons for every textline
    for textline in xml_processor.get_textlines():
        coords = parse_points(textline.find('.//ns:Coords', namespaces=xml_processor.namespace).attrib['points'])
        image_processor.draw_polygon(coords)

    # Save the annotated image
    output_image_path = os.path.join(output_dir, f"annotated_{os.path.basename(image_filename)}")
    image_processor.save_image(output_image_path)
    print(f"Annotated image saved as: {output_image_path}")


def line_extractor_crop_polygons(xml_path, output_dir):
    # Initialize XML and Image Processor
    xml_processor = PageXMLProcessor(xml_path)

    image_filename = xml_processor.get_page_image_filename()
    image_processor = ImageProcessor(os.path.join(os.path.dirname(xml_path), image_filename))

    # loop through all textlines of all textregions and extract the textlines into own files
    for text_region in xml_processor.get_textregions():
        for text_line in text_region.findall('.//ns:TextLine', namespaces=xml_processor.namespace):
            cropped_xml_processor = PageXMLProcessor(xml_path)
            text_line_id = text_line.attrib.get('id', None)

            coords_points = parse_points(
                text_line.find('.//ns:Coords', namespaces=xml_processor.namespace).attrib['points'])
            baseline_points = parse_points(
                text_line.find('.//ns:Baseline', namespaces=xml_processor.namespace).attrib['points'])

            cropped_image, bbox = image_processor.crop_polygon(coords_points)

            if bbox:
                cropped_image_base_name = f"{image_filename.strip('.png')}_{text_line_id}"
                cropped_xml_processor.update_xml(text_region.attrib.get('id', None), bbox, text_line, coords_points, baseline_points, f"{cropped_image_base_name}.png")

                # Save cropped image and corresponding XML
                cropped_image.save(os.path.join(output_dir, f"{cropped_image_base_name}.png"))
                cropped_xml_processor.save_xml(os.path.join(output_dir, f"{cropped_image_base_name}.xml"))
                print(f"Saved: {cropped_image_base_name}.png and XML")



# TODO loop through an input folder
xml_path = "bayerische-gesandtschaft-paepstlicher-stuhl-180-1824.xml"
output_dir = "../output"

os.makedirs(output_dir, exist_ok=True)

# Process XML and draw polygons
line_extractor_draw_polygons(xml_path, output_dir)

# Process XML and crop polygons (if needed)
line_extractor_crop_polygons(xml_path, output_dir)

