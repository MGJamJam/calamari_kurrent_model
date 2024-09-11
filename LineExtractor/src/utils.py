def parse_points(points_str):
    """Parse the 'points' attribute from PAGE XML to a list of (x, y) tuples."""
    return [tuple(map(int, point.split(','))) for point in points_str.split()]

def get_new_coords(points, bbox):
    """Update coordinates relative to the bounding box."""
    return ' '.join([f"{x - bbox[0]},{y - bbox[1]}" for x, y in points])
