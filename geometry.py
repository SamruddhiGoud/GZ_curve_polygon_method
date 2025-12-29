from shapely.geometry import Polygon, box
from shapely.affinity import rotate

def build_section_polygon(z_vals, y_vals):
    port = [(-y, z) for y, z in zip(y_vals, z_vals)]
    starboard = [(y, z) for y, z in zip(y_vals[::-1], z_vals[::-1])]
    return Polygon(port + starboard)

def rotate_section(section, heel_deg):
    # Rotate about keel + centreline
    return rotate(section, heel_deg, origin=(0, 0), use_radians=False)

def submerged_part(section, draft):
    water_plane = box(-1e4, -1e4, 1e4, draft)
    return section.intersection(water_plane)
