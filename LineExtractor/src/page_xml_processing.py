import xml.etree.ElementTree as ET
import copy

from utils import get_new_coords


class PageXMLProcessor:
    def __init__(self, xml_path):
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()
        ET.register_namespace('', self.root.tag.split('}')[0].strip('{'))
        self.namespace = {'ns': self.root.tag.split('}')[0].strip('{')}

    def get_page_image_filename(self):
        page_elem = self.root.find('.//ns:Page', namespaces=self.namespace)
        return page_elem.attrib['imageFilename']

    def get_textlines(self):
        return self.root.findall('.//ns:TextLine', namespaces=self.namespace)

    def get_textregions(self):
        return self.root.findall('.//ns:TextRegion', namespaces=self.namespace)

    def get_page(self):
        return self.root.find('.//ns:Page', namespaces=self.namespace)

    def update_xml(self, text_region_id, bbox, text_line, text_line_coords_points, base_line_coords_points, image_file_name):
        """Updates the PAGE XML file by stripping irrelevant information for the specified text line,
        and adjusting the coordinates and file information to match the cropped image."""

        # Remove all other text regions and text lines of given text region
        self.delete_text_regions_and_text_lines(text_region_id)

        # Update coordinates to be relative to the bounding box of the cropped image
        new_text_line_coords = get_new_coords(text_line_coords_points, bbox)
        new_base_line_coords = get_new_coords(base_line_coords_points, bbox)
        new_text_region_coords = f"0,0 0,{bbox[3] - bbox[1]} {bbox[2] - bbox[0]},{bbox[3] - bbox[1]} {bbox[2] - bbox[0]},0"

        # Update the filename, image width, and image height
        page = self.get_page()
        page.set('imageWidth', str(bbox[2] - bbox[0]))
        page.set('imageHeight', str(bbox[3] - bbox[1]))
        page.set('imageFilename', image_file_name)

        # Update the text line with the new coordinates
        new_text_line = copy.deepcopy(text_line)
        new_text_line.find('.//ns:Coords', namespaces=self.namespace).set('points', new_text_line_coords)
        new_text_line.find('.//ns:Baseline', namespaces=self.namespace).set('points', new_base_line_coords)

        # Update the text region's coordinates and append the updated text line
        text_region = self.get_textregions()[0]
        text_region.find('.//ns:Coords', namespaces=self.namespace).set('points', new_text_region_coords)
        text_region.append(new_text_line)

    def save_xml(self, output_path):
        """Save the XML to a given path."""
        new_tree = ET.ElementTree(self.root)
        new_tree.write(output_path, encoding='utf-8', xml_declaration=True)

    def delete_text_regions_and_text_lines(self, text_region_id):
        """Delete all the text lines of a given text region and all other text regions."""
        for region in self.get_textregions():
            if region.attrib.get('id') == text_region_id:
                for text_line in region.findall('.//ns:TextLine', namespaces=self.namespace):
                    region.remove(text_line)

                text_equiv = region.find('.//ns:TextEquiv', namespaces=self.namespace)
                if text_equiv is not None:
                    region.remove(text_equiv)
            else:
                self.get_page().remove(region)
