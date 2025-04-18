# coding=utf-8
"""
Last Edited: 04/09/2025
@author: John Mark Mayhall
"""
import os

import netCDF4
import numpy as np
from mayavi import mlab

# Define paths
nc_path = "C:/Users/jmayhall/Downloads/aes740_project/no_tke/cm1out_liqhurr.nc"
output_dir = "C:/Users/jmayhall/Downloads/aes740_project/no_tke/liq_photos"

# Variables to process
variables_to_plot = ["qv", "ql", "th", "rho", "xh", "yh", "zh"]
units_out = {'qv': 'kg/kg', 'ql': 'kg/kg', 'th': 'K', 'rho': 'kg/m^3'}

# Ensure output directories exist
for var in variables_to_plot[: -3]:
    os.makedirs(os.path.join(output_dir, var), exist_ok=True)

# Load dataset once
dataset = netCDF4.Dataset(nc_path)

# Extract variables into a dictionary
variables = {var: np.asarray(dataset.variables.get(var)) for var in variables_to_plot}
tke_data = np.asarray(dataset.variables.get("tke"))  # TKE is used in all plots


# Function to process and swap axes
def process_data(data: np.array) -> np.array:
    """
    Function for converting data to x, y, z format.
    :param data: Data array in the format z, y, x.
    :return: Data array in the format of x, y, z.
    """
    return data.swapaxes(0, 2)


# Function to plot and save figures
def plot_contour3d(base_data: np.array, overlay_data: np.array, var_name: str, timestep: int,
                   extent: list, units: dict) -> None:
    """
    Function for plotting array data.
    :param units: Colorbar Units.
    :param extent: List of the maximum and minimum extent for the plot.
    :param base_data: The data being plotted.
    :param overlay_data: Data being plotted over the TKE data.
    :param var_name: The variable being plotted.
    :param timestep: The timestep being plotted.
    :return:
    """
    fig = mlab.figure(size=(1500, 1000))
    v = mlab.contour3d(overlay_data, contours=50, colormap="jet", extent=extent)
    mlab.colorbar(object=v, title=f'{units.get(var_name)}', label_fmt='%.5f', nb_labels=4)
    mlab.axes(xlabel="x (km)", ylabel="y (km)", zlabel="z (km)")
    mlab.outline(v)

    save_path = os.path.join(output_dir, var_name, f"{var_name}_tke_timestep{timestep}.png")
    mlab.savefig(save_path)

    # Clean up
    mlab.close(all=True)
    mlab.clf()


# Iterate over time steps
num_timesteps = tke_data.shape[0]
for i in range(num_timesteps):
    tke_frame = process_data(tke_data[i])

    for var in variables_to_plot[: -3]:
        var_frame = process_data(variables[var][i])
        extent_out = [np.min(variables['xh']), np.max(variables['xh']), np.min(variables['yh']),
                      np.max(variables['yh']), 0, 25]
        plot_contour3d(tke_frame, var_frame, var, i, extent_out, units_out)
