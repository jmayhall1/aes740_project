# coding=utf-8
"""
@author: John Mark Mayhall
"""
import os

import netCDF4
import numpy as np
from mayavi import mlab

# Define file paths
nc_path = "C:/Users/jmayhall/Downloads/aes740_project/cm1out_icehurr.nc"
output_dir = "C:/Users/jmayhall/Downloads/aes740_project/ice_photos"

# Ensure output directories exist
variables_to_plot = ["qv", "dbz", "qi", "th", "rho"]
for var in variables_to_plot:
    os.makedirs(os.path.join(output_dir, var), exist_ok=True)

# Load dataset once
dataset = netCDF4.Dataset(nc_path)

# Extract relevant variables
variables = {var: np.array(dataset.variables.get(var)) for var in variables_to_plot}
tke_data = np.array(dataset.variables.get("tke"))  # TKE is used in all plots


# Function to process and swap axes
def process_data(data: np.array) -> np.array:
    """
    Function for converting data to x, y, z format.
    :param data: Data array in the format z, y, x.
    :return: Data array in the format x, y, z.
    """
    return data.swapaxes(0, 2)


# Function to plot and save figures
def plot_contour3d(base_data: np.array, overlay_data: np.array, var_name: str, timestep: int) -> None:
    """
    Function for plotting array data.
    :param base_data: The data being plotted.
    :param overlay_data: Data being plotted over the TKE data.
    :param var_name: The variable being plotted.
    :param timestep: The timestep being plotted.
    :return:
    """
    fig = mlab.figure(size=(1024, 1024))
    s = mlab.contour3d(base_data, contours=10, colormap="Greys")
    v = mlab.contour3d(overlay_data, contours=25, colormap="jet", opacity=0.5)
    mlab.axes(xlabel="x", ylabel="y", zlabel="z")
    mlab.outline(s)

    save_path = os.path.join(output_dir, var_name, f"{var_name}_tke_timestep{timestep}.png")
    mlab.savefig(save_path)

    # Clean up
    mlab.close(all=True)
    mlab.clf()


# Iterate over time steps
num_timesteps = tke_data.shape[0]
for i in range(num_timesteps):
    tke_frame = process_data(tke_data[i])

    for var in variables_to_plot:
        var_frame = process_data(variables[var][i])
        plot_contour3d(tke_frame, var_frame, var, i)
