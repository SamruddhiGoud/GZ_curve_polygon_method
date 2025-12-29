import os
import numpy as np
import pandas as pd

from io_utils import read_offsets, save_results
from hydrostatics import compute_KN
from plotting import plot_GZ

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

OFFSET_FILE = "offsets_clean.xlsx"
DRAFT = 11.6        # m
KG = 7.5            # m
HEEL_ANGLES = np.arange(0, 91, 5)

def main():
    x, z, offsets = read_offsets(OFFSET_FILE)

    data = []
    for heel in HEEL_ANGLES:
        KN = compute_KN(x, z, offsets, heel, DRAFT)
        GZ = KN - KG * np.sin(np.radians(heel))
        data.append([heel, KN, GZ])

    df = pd.DataFrame(data, columns=["Heel (deg)", "KN (m)", "GZ (m)"])

    save_results(df, "output/GZ_table.xlsx")
    plot_GZ(df, "output/GZ_curve.png")

if __name__ == "__main__":
    main()
