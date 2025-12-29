import os
import numpy as np
import pandas as pd

from io_utils import read_offsets, save_results
from hydrostatics import compute_KN
from plotting import plot_GZ


# -------------------------------------------------------------------
# User-defined inputs
# -------------------------------------------------------------------

OFFSET_FILE = "offsets_clean.xlsx"   # Offset table input
DRAFT = 11.6                         # Ship draft (m)
KG = 7.5                             # Centre of gravity above keel (m)
HEEL_ANGLES = np.arange(0, 91, 5)    # Heel angles (degrees)


# -------------------------------------------------------------------
# Main execution
# -------------------------------------------------------------------

def main():
    """
    Computes the GZ curve of a ship using a polygon-based hydrostatic method.
    """

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    # Read offset data
    x_vals, z_vals, offsets = read_offsets(OFFSET_FILE)

    results = []

    # Loop over heel angles
    for heel in HEEL_ANGLES:
        KN = compute_KN(x_vals, z_vals, offsets, heel, DRAFT)
        GZ = KN - KG * np.sin(np.radians(heel))
        results.append([heel, KN, GZ])

    # Store results in a table
    df = pd.DataFrame(
        results,
        columns=["Heel (deg)", "KN (m)", "GZ (m)"]
    )

    # Save and plot results
    save_results(df, "output/GZ_table.xlsx")
    plot_GZ(df, "output/GZ_curve.png")


if __name__ == "__main__":
    main()
