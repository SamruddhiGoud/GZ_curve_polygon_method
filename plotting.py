import matplotlib.pyplot as plt

def plot_GZ(df, save_path=None):
    plt.figure()
    plt.plot(df["Heel (deg)"], df["GZ (m)"], marker="o")
    plt.axhline(0, color="black")
    plt.xlabel("Heel angle (deg)")
    plt.ylabel("GZ (m)")
    plt.title("GZ Curve (Polygon Method)")
    plt.grid()

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()
