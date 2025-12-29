import numpy as np
from geometry import build_section_polygon, rotate_section, submerged_part

def section_properties(section):
    if section.is_empty:
        return 0.0, 0.0
    return section.area, section.centroid.x

def integrate_trapezoidal(x, f):
    return np.trapz(f, x)

def compute_KN(x_vals, z_vals, offsets, heel_deg, draft):
    areas = []
    moments = []

    for i in range(len(x_vals)):
        section = build_section_polygon(z_vals, offsets[:, i])
        section = rotate_section(section, heel_deg)
        submerged = submerged_part(section, draft)

        A, y_bar = section_properties(submerged)

        areas.append(A)
        moments.append(A * abs(y_bar))  # <<< KEY PHYSICS FIX

    volume = integrate_trapezoidal(x_vals, areas)
    transverse_moment = integrate_trapezoidal(x_vals, moments)

    return transverse_moment / volume
