import pandas as pd
import numpy as np

def read_offsets(filepath):
    df = pd.read_excel(filepath, sheet_name="Sheet1", index_col=0)

    # Handle any remaining dash symbols safely
    df = df.replace("-", 0)

    z_vals = df.index.to_numpy(dtype=float)      # waterlines (m)
    x_vals = df.columns.to_numpy(dtype=float)    # stations (m or nondim)
    offsets = df.to_numpy(dtype=float)           # half-breadths (m)

    return x_vals, z_vals, offsets


def save_results(df, filepath):
    df.to_excel(filepath, index=False)
